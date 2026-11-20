# Swiss fuel prices and Brent: pass-through and forecasting

Advanced Data Analytics, autumn 2026. How quickly do Swiss petrol and diesel prices follow Brent, does the
USD/CHF rate matter beyond converting Brent into francs, and does a non-linear model forecast better than a
linear distributed-lag regression?

## Install
    pip install -r requirements.txt

## Run, in this order (from the repository root)
1. `python code/01_get_data.py` downloads Brent and USD/CHF from FRED into `data/`.
2. `code/02_clean.ipynb` builds the monthly dataset `data/clean_monthly.csv`.
3. `code/03_model.ipynb` fits the models (to be written).
4. `code/04_figures.ipynb` produces every figure and table in the paper (to be written).

Every notebook runs top to bottom in a fresh kernel. Random seed: `helpers.SEED`.
Running time and hardware: TO FILL IN at the end.

## Data
- Swiss consumer price index (petrol, diesel, all fuels, total), monthly, December 2020 = 100:
  Swiss Federal Statistical Office (BFS/UST), file `su-d-05_02_67.xlsx` in `data/`. Licence: OPEN-BY (free use, cite the source).
- Brent (DCOILBRENTEU) and CHF per USD (DEXSZUS): FRED, Federal Reserve Bank of St. Louis. Check FRED's terms and
  the series' sources before publishing; TO CONFIRM.

## Tools used
Generative AI assistance (Claude) is declared in the appendix of the paper.
