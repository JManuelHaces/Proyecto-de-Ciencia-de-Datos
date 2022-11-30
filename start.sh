uvicorn main:app --host 0.0.0.0 --port=8001 &
streamlit run ./frontend/cnn-app.py --server.port=8501 --server.address=0.0.0.0