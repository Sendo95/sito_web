python -m venv env
.\env\Scripts\activate
pip install -r requirements.txt
pip install fastapi uvicorn
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
