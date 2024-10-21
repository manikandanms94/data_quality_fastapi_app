import pandas as pd
from typing import List, Dict


def load_file(file, file_type: str) -> pd.DataFrame:
    """ Load the uploaded file as a pandas DataFrame based on file type. """
    if file_type == "csv":
        return pd.read_csv(file)
    elif file_type == "parquet":
        return pd.read_parquet(file)
    else:
        raise ValueError("Unsupported file format")


def generate_quality_report(df: pd.DataFrame) -> List[Dict]:
    """ Generate a data quality report from a pandas DataFrame. """
    total_records = len(df)
    report = []

    for column in df.columns:
        null_count = df[column].isnull().sum()
        empty_count = (df[column] == '').sum()
        unique_count = df[column].nunique()
        data_type = str(df[column].dtype)
        missing_percentage = (null_count / total_records) * 100
        duplicates = df.duplicated(subset=[column]).sum()

        report.append({
            "column": column,
            "null_count": null_count,
            "empty_count": empty_count,
            "unique_count": unique_count,
            "total_records": total_records,
            "data_type": data_type,
            "missing_percentage": missing_percentage,
            "duplicates": duplicates
        })

    return report


def save_report(report: List[Dict], output_file: str):
    """ Save the quality report to a local CSV file. """
    pd.DataFrame(report).to_csv(output_file, index=False)
