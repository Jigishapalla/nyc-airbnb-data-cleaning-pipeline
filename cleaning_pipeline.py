import pandas as pd

# Load the raw dataset
df = pd.read_csv("data/raw/AB_NYC_2019.csv/AB_NYC_2019.csv")

print("===== DATASET OVERVIEW =====")
print("Rows and columns:", df.shape)

print("\n===== FIRST 5 ROWS =====")
print(df.head())

print("\n===== COLUMN NAMES =====")
print(df.columns.tolist())

print("\n===== DATA TYPES =====")
print(df.dtypes)

print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

print("\n===== DUPLICATE ROWS =====")
print(df.duplicated().sum())

print("\n===== BASIC STATISTICS =====")
print(df.describe(include="all"))
# ==========================================
# DATA CLEANING
# ==========================================

print("\n===== STARTING DATA CLEANING =====")

# Make a copy of the original data
cleaned_df = df.copy()

# Fill missing text values
cleaned_df["name"] = cleaned_df["name"].fillna("Unknown")
cleaned_df["host_name"] = cleaned_df["host_name"].fillna("Unknown")

# Fill missing review values
cleaned_df["reviews_per_month"] = cleaned_df["reviews_per_month"].fillna(0)

# Convert last_review to datetime
cleaned_df["last_review"] = pd.to_datetime(
    cleaned_df["last_review"],
    errors="coerce"
)

print("\n===== MISSING VALUES AFTER CLEANING =====")
print(cleaned_df.isnull().sum())
# ==========================================
# CHECK SUSPICIOUS VALUES
# ==========================================

print("\n===== SUSPICIOUS VALUES CHECK =====")

print("\nPrice:")
print("Minimum price:", cleaned_df["price"].min())
print("Maximum price:", cleaned_df["price"].max())
print("Zero price rows:", (cleaned_df["price"] == 0).sum())

print("\nMinimum nights:")
print("Minimum:", cleaned_df["minimum_nights"].min())
print("Maximum:", cleaned_df["minimum_nights"].max())

print("\nAvailability:")
print("Minimum:", cleaned_df["availability_365"].min())
print("Maximum:", cleaned_df["availability_365"].max())
# ==========================================
# REMOVE INVALID PRICE VALUES
# ==========================================

print("\n===== REMOVING INVALID PRICE VALUES =====")

before_rows = len(cleaned_df)

cleaned_df = cleaned_df[cleaned_df["price"] > 0].copy()

after_rows = len(cleaned_df)

print("Rows before:", before_rows)
print("Rows after:", after_rows)
print("Rows removed:", before_rows - after_rows)
# ==========================================
# CHECK EXTREME MINIMUM NIGHTS
# ==========================================

print("\n===== EXTREME MINIMUM NIGHTS =====")

print(
    "Listings with minimum_nights > 365:",
    (cleaned_df["minimum_nights"] > 365).sum()
)

print("\nTop 10 highest minimum_nights values:")
print(
    cleaned_df["minimum_nights"]
    .sort_values(ascending=False)
    .head(10)
    .to_list()
)
# ==========================================
# REMOVE EXTREME MINIMUM-NIGHT VALUES
# ==========================================

print("\n===== REMOVING EXTREME MINIMUM NIGHTS =====")

before_rows = len(cleaned_df)

cleaned_df = cleaned_df[
    cleaned_df["minimum_nights"] <= 365
].copy()

after_rows = len(cleaned_df)

print("Rows before:", before_rows)
print("Rows after:", after_rows)
print("Rows removed:", before_rows - after_rows)
# ==========================================
# FINAL VALIDATION
# ==========================================

print("\n===== FINAL VALIDATION =====")

print("Final dataset shape:", cleaned_df.shape)

print("\nMissing values:")
print(cleaned_df.isnull().sum())

print("\nDuplicate rows:")
print(cleaned_df.duplicated().sum())

print("\nPrice range:")
print("Minimum:", cleaned_df["price"].min())
print("Maximum:", cleaned_df["price"].max())

print("\nMinimum nights range:")
print("Minimum:", cleaned_df["minimum_nights"].min())
print("Maximum:", cleaned_df["minimum_nights"].max())


# ==========================================
# SAVE CLEANED DATASET
# ==========================================

output_path = "data/processed/AB_NYC_2019_cleaned.csv"

cleaned_df.to_csv(output_path, index=False)

print("\n===== CLEANING COMPLETED =====")
print("Cleaned dataset saved to:", output_path)