# Data Cleaning Report

## Dataset

Dataset: NYC Airbnb Open Data

Original dataset:

- Rows: 48,895
- Columns: 16

## Initial Data Quality Findings

### Missing Values

The original dataset contained missing values in:

- `name`: 16
- `host_name`: 21
- `last_review`: 10,052
- `reviews_per_month`: 10,052

### Duplicate Records

Duplicate rows found:

0

### Suspicious Values

#### Price

- Minimum price: 0
- Maximum price: 10,000
- Zero-price listings: 11

#### Minimum Nights

- Minimum: 1
- Maximum: 1,250
- Listings above 365 nights: 14

## Cleaning Actions

### Missing Values

- Missing `name` values were replaced with `Unknown`.
- Missing `host_name` values were replaced with `Unknown`.
- Missing `reviews_per_month` values were replaced with `0`.
- `last_review` was converted to datetime.
- Missing `last_review` values were retained because no valid date was available.

### Invalid Price Values

Listings with `price = 0` were removed.

Rows removed:

11

### Extreme Minimum-Night Values

Listings with `minimum_nights > 365` were removed.

Rows removed:

14

## Final Dataset

After cleaning:

- Rows: 48,870
- Columns: 16
- Rows removed: 25
- Duplicate rows: 0
- Minimum price: 10
- Maximum price: 10,000
- Minimum nights: 1
- Maximum nights: 365

## Output

The cleaned dataset is saved as:

`data/processed/AB_NYC_2019_cleaned.csv`

## Conclusion

The cleaning pipeline successfully processed the raw NYC Airbnb
dataset and produced a validated cleaned dataset suitable for
further analysis.