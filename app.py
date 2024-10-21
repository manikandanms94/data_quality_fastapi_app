from fastapi import FastAPI, UploadFile, File
from main import load_file, generate_quality_report, save_report
import numpy as np
import os

app = FastAPI()

# Helper function to handle NumPy types
def convert_numpy_types(data):
    if isinstance(data, np.integer):
        return int(data)
    elif isinstance(data, np.floating):
        return float(data)
    elif isinstance(data, np.ndarray):
        return data.tolist()  # Convert numpy arrays to lists
    return data

# Recursive function to handle both lists and dictionaries
def process_report(report):
    if isinstance(report, dict):
        return {key: process_report(value) for key, value in report.items()}
    elif isinstance(report, list):
        return [process_report(item) for item in report]
    else:
        return convert_numpy_types(report)

@app.post("/data/quality-check")
async def quality_check(file: UploadFile = File(...)):
    # Determine file extension and load the file
    file_type = "csv" if file.filename.endswith(".csv") else "parquet" if file.filename.endswith(".parquet") else None
    
    if not file_type:
        return {"error": "Unsupported file format"}

    # Load file into DataFrame using the load_file function
    df = load_file(file.file, file_type)
    
    # Generate the quality report
    report = generate_quality_report(df)

    # Process report to handle NumPy types
    processed_report = process_report(report)
    
    # Save the report locally as a CSV file
    output_file = "quality_report.csv"
    save_report(processed_report, output_file)

    return {
        "message": "Data quality check complete",
        "report": processed_report,
        "output_file": output_file
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
