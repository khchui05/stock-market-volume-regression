# Data

This project uses one dataset: **Smarket** from *An Introduction to Statistical Learning with Applications in Python* (ISLP).

| Column | Type | Description |
| --- | --- | --- |
| `Year` | quantitative | Year of the trading day (2001–2005) |
| `Lag1`–`Lag5` | quantitative | S&P 500 percentage return 1–5 trading days earlier |
| `Volume` | quantitative | Shares traded that day, in billions (**the outcome**) |
| `Today` | quantitative | S&P 500 percentage return that day |
| `Direction` | qualitative | `Up` or `Down`: whether the market rose or fell that day |

1,250 trading days, no missing values. Original source: Yahoo Finance, via the ISLP package.

## Getting the data

The CSV isn't committed to the repo. Download it with:

```bash
python modules/get_data.py
```

This saves `data/00-raw/Smarket.csv`. (The notebooks also read the same file straight from its URL, so they run without this step.)

## Folders

- `00-raw/`: the original download. Never edited by hand.
- `01-interim/`: intermediate outputs, if any.
- `02-processed/`: final cleaned data used for modeling, if saved.
