# quick script to check missing data in our transit datasets
# author: Jay Vaghela (TODO: clean this up later into a proper module)

import sys
from pathlib import Path
import pandas as pd

# Global debug flag, used this once when testing parquet files on the server
DEBUG = False


def main():
    # check args, classic cli stuff
    if len(sys.argv) != 2:
        print("usage: python scripts/profile_dataset.py <data-file>")
        return

    path_str = sys.argv[1]
    file_path = Path(path_str)

    # just making sure the file is actually there lol
    if not file_path.exists():
        print("file not found:", file_path)
        return

    # TODO: maybe add json support later if needed? stick to csv/parquet for now
    ext = file_path.suffix.lower()

    if ext == ".parquet":
        df = pd.read_parquet(file_path)
    elif ext == ".csv":
        # sometimes low_memory causes issues with mixed types, but whatever, keeping it simple
        df = pd.read_csv(file_path)
    else:
        print("please provide a csv or parquet file.")
        return

    if DEBUG:
        print("Loaded dataframe successfully! Shape:", df.shape)

    # basic info about the dataset
    print("\nDataset:", file_path.name)
    print("Rows:", len(df))
    print("Columns:", len(df.columns))

    print("\ncolumn names:")
    print(list(df.columns))

    print("\ndata types:")
    print(df.dtypes)

    # check missing values - doing it the standard pandas way
    missing = df.isna().sum()
    missing_percent = (missing / len(df) * 100).round(2)

    # Let's combine them into a summary df
    summary_df = pd.DataFrame({"count": missing, "percent": missing_percent})

    print("\nmissing values:")
    print(summary_df)

    rows_with_missing = df.isna().any(axis=1).sum()
    print("\nrows with missing values:", rows_with_missing)

    missing_rows = df[df.isna().any(axis=1)]

    # Hardcoding this column name because it's specific to our GTFS / transit data format
    print("\nmissing values by route:")

    if "route_short_name" in missing_rows.columns:
        print(missing_rows["route_short_name"].value_counts().head(10))
    else:
        print("Warning: route_short_name not found in columns!")

    print("\nexamples of affected rows:")

    # selecting a bunch of columns to display
    cols_to_show = [
        "route_short_name",
        "direction_id",
        "trip_id",
        "stop_time",
        "n-boardings",
        "n-alighting",
        "loading",
    ]

    # filter out columns that might not exist just in case
    actual_cols = [c for c in cols_to_show if c in missing_rows.columns]

    print(missing_rows[actual_cols].head(10).to_string(index=False))

    columns_to_check = [
        "n-boardings",
        "n-alighting",
        "lag_loading",
        "balance",
        "loading",
    ]

    valid_check_cols = [c for c in columns_to_check if c in missing_rows.columns]

    print("\nmissing value combinations:")

    try:
        print(missing_rows[valid_check_cols].isna().value_counts())
    except Exception as e:
        print("Couldn't compute value counts for combinations:", e)

    print("\nmissing rows by trip:")

    if "route_short_name" in missing_rows.columns and "trip_id" in missing_rows.columns:
        print(
            missing_rows.groupby(["route_short_name", "trip_id"])
            .size()
            .sort_values(ascending=False)
            .head(10)
        )

    # check duplicate rows
    dup_count = df.duplicated().sum()
    print("\nduplicate rows:", dup_count)

    print("\nDone profiling! ✨")


if __name__ == "__main__":
    main()
