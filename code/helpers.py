"""Functions used in more than one stage (written with AI assistance, see the paper appendix)."""
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent  # repository root, whatever the working directory
DATA = ROOT / "data"
FIGURES = ROOT / "figures"

SEED = 42  # fixed random seed for every stage

# Fuel items in sheet INDEX_m of the UST (BFS) workbook, identified by their PosNo code:
# 7111 = Diesel, 7110 = Benzin, 7105 = all fuels, 100 = Total CPI (code 100_100).
UST_POSNO = {"diesel": 7111, "petrol": 7110, "fuels_total": 7105, "cpi_total": 100}


def load_ust_fuel(path):
    """Read the monthly index series (Dec 2020 = 100) from the UST consumer-price workbook."""
    raw = pd.read_excel(path, sheet_name="INDEX_m", header=None)
    header = raw.iloc[3]
    date_cols = [c for c in raw.columns if hasattr(header[c], "year")]
    dates = pd.to_datetime([header[c] for c in date_cols])
    out = {}
    for name, posno in UST_POSNO.items():
        row = raw[raw[0].astype(str) == f"100_{posno}"]  # code column, e.g. "100_7111"
        if len(row) == 0:
            raise ValueError(f"no row found for {name} (code 100_{posno})")
        vals = row[date_cols].apply(pd.to_numeric, errors="coerce")
        # the Total row also appears again in the special-groupings block: accept it only if identical
        if len(row) > 1 and not vals.nunique(dropna=False).eq(1).all():
            raise ValueError(f"rows for {name} differ")
        out[name] = vals.iloc[0].values
    df = pd.DataFrame(out, index=dates)
    df.index.name = "month"
    return df


def to_monthly_mean(s):
    """Average a daily series by calendar month, labelled by the first day of the month."""
    return s.resample("MS").mean()
