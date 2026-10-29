import sys
from pathlib import Path
import pandas as pd


def main():
    if len(sys.argv) != 2:
        print("ussage: python scripts/profile_dataset.py <data-file>")
        return
    file_path = Path(sys.argv[1])
    if not file_path.exists():
        print("file not found:", file_path)
        return

    if file_path.suffix == ".parquet":
        df = pd.read_parquet(file_path)
    elif file_path.suffix == ".csv":
        df = pd.read_csv(file_path)
    else:
        print("please provide a Csv or parquet file.")
        return

    # basic info about dataaset
    print("\nDataset:", file_path.name)
    print("Rows:", len(df))
    print("columns:", len(df.columns))

    print("\ncolumn names:")
    print(list(df.columns))

    print("\ndata types:")
    print(df.dtypes)

    print("\nm issing values:")
    print(df.isna().sum())

    print("\nduplicate rows:", df.duplicated().sum())


if __name__ == "__main__":
    main()
