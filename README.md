# NYC Airbnb Data Cleaning Pipeline

## Project Overview

This project cleans and validates the NYC Airbnb Open Data dataset using Python and pandas. It identifies missing values, checks duplicate records, investigates suspicious values, and saves a cleaned dataset for further analysis.

## Dataset

* Dataset: NYC Airbnb Open Data
* Original rows: 48,895
* Original columns: 16

## Project Structure

```text
AgenticX_Data_Cleaning/
├── data/
│   ├── raw/
│   └── processed/
│       └── AB_NYC_2019_cleaned.csv
├── reports/
│   └── cleaning_report.md
├── src/
│   └── cleaning_pipeline.py
└── README.md
```

## Cleaning Operations

1. Inspected dataset columns, data types, missing values, and duplicates.
2. Replaced missing `name` and `host_name` values with `Unknown`.
3. Replaced missing `reviews_per_month` values with `0`.
4. Converted `last_review` to datetime format while retaining missing dates.
5. Removed 11 listings with a price of zero.
6. Removed 14 listings with `minimum_nights` greater than 365.
7. Validated the cleaned dataset.

## Results

* Final rows: 48,870
* Final columns: 16
* Rows removed: 25
* Duplicate rows: 0
* Minimum price after cleaning: 10
* Maximum price after cleaning: 10,000
* Minimum nights after cleaning: 1
* Maximum nights after cleaning: 365

## Output

The cleaned dataset is saved at:
`data/processed/AB_NYC_2019_cleaned.csv`

## How to Run

Open Anaconda Prompt and navigate to the project directory. Run:

```bash
python src/cleaning_pipeline.py
```

## Tools Used

* Python
* pandas
* NumPy
* Matplotlib
* Data quality checks and validation

## Conclusion

The pipeline successfully cleaned the NYC Airbnb dataset and saved the resulting CSV for further exploratory data analysis. Missing review dates and unusually high prices were retained where appropriate for further investigation.
