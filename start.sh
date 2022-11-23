uvicorn main:app --host localhost --port=8001 &
streamlit run ./frontend/cnn-app.py --server.port=8501 --server.address=localhost