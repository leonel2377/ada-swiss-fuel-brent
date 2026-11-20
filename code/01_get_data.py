"""Stage 1: download the two public FRED series into data/.

Brent crude, USD per barrel, daily:  FRED series DCOILBRENTEU
Exchange rate, CHF per 1 USD, daily: FRED series DEXSZUS
(The Swiss fuel price indices come from the UST/BFS workbook already stored in data/.)
Run from the repository root:  python code/01_get_data.py
"""
from pathlib import Path
import pandas as pd

BASE = "https://fred.stlouisfed.org/graph/fredgraph.csv?id="
SERIES = {"brent_usd_daily.csv": "DCOILBRENTEU", "chf_per_usd_daily.csv": "DEXSZUS"}
DATA = Path(__file__).resolve().parent.parent / "data"

for filename, series_id in SERIES.items():
    df = pd.read_csv(BASE + series_id)
    df.to_csv(DATA / filename, index=False)
    print(f"{series_id}: {df.shape[0]} rows, {df.iloc[0, 0]} to {df.iloc[-1, 0]} -> data/{filename}")
