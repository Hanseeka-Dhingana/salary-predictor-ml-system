# Salary Predictor ML System
A Machine Learning application to **predict salary based on years of experience** using a trained model. The system features a **FastAPI backend**, optional **Streamlit frontend**, and is **Dockerized for easy deployment**.



## Project Structure
```
salary-predictor-ml-system/
│
├─ .venv/
├─ backend/
│  ├─ app/
│  │  ├─ main.py          # FastAPI application
│  │  ├─ model.py         # Model loading & prediction
│  │  └─ requirements.txt
│  └─ Dockerfile          # Dockerfile for backend
│  
│
├─ frontend/
│  ├─ streamlit_app.py    # Streamlit frontend
│  └─ requirements.txt
│
└─ README.md
```

## Features
* Predict salary based on years of experience
* Scalable **FastAPI backend** with Docker support
* **Streamlit frontend** for interactive use
* Deployment-ready for platforms like **Railway**
* Lightweight and easy-to-use machine learning model (Linear Regression)

## Backend API
### Base URL

```
https://salary-predictor-api-production.up.railway.app
```

### Endpoints

1. **Root**

```
GET /
```

Response:

```json
{
  "message": "Welcome to the Salary Predictor API."
}
```

2. **Predict Salary**

```
POST /predict
```

**Request Body**:

```json
{
  "experience_years": 3
}
```

**Response**:

```json
{
  "predicted_salary": 45000
}
```

## Deployment
The backend is **Dockerized** for easy deployment on cloud platforms such as Railway, Fly.io, or any container-based service.

You can either pull the pre-built Docker image or build your own from the repository.

## Frontend
* Streamlit app to interact with the API
* Run locally to visualize and test predictions

```bash
streamlit run frontend/app.py
```

## Technologies
* **Backend:** FastAPI
* **Model:** scikit-learn Linear Regression
* **Frontend:** Streamlit
* **Deployment:** Docker, Railway

