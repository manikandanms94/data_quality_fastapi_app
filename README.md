# data_quality_fastapi_app

1. Run the main.py file

uvicorn app:app --reload

2. Upload the input files from postman 

# sample files can be found in input_files directory

postman POST url - http://127.0.0.1:8000/data/quality-check

3. Find the results in the generated "quality_report.csv" file

