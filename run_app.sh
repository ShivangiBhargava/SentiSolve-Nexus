#!/bin/bash

echo "Starting FastAPI backend..."
uvicorn app.api:app --reload &

sleep 2

echo "Starting Streamlit frontend..."
streamlit run app/frontend.py
