# data_quality_fastapi_app

# 1. Create venv

python3 -m venv venv

source ./.venv/bin/activate

# 2. Install dependencies (requirements.txt)

pip3 install -r requirements.txt

# 3. Run the main.py file

uvicorn app:app --reload

# 4. Upload the input files from postman 

sample files can be found in input_files directory (csv and parquet)

postman POST url - http://127.0.0.1:8000/data/quality-check

# 4. Find the results in the generated "quality_report.csv" file

