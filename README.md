# 🩺 Diabetes Risk Prediction API

![Python](https://img.shields.io/badge/Python-3.9-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue)
![HuggingFace](https://img.shields.io/badge/HuggingFace-Live%20Demo-yellow)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

A production-grade ML microservice that predicts diabetes risk using a **Voting Ensemble of XGBoost and Random Forest**, served via **FastAPI** and deployed with **Docker** on HuggingFace Spaces.



## 🚀 Live Demo

**API Docs (Swagger UI):** [https://ayeshaaaa17-diabetes-prediction-api.hf.space/docs](https://ayeshaaaa17-diabetes-prediction-api.hf.space/docs)

Try the `/predict` endpoint directly from your browser, no setup required.

---

## ✨ Features

- **Ensemble Model:** Combines XGBoost + Random Forest via soft voting for higher stability.
- **Data Validation:** Strict input validation using Pydantic schemas.
- **Auto-Documentation:** Interactive Swagger UI for live testing.
- **Containerized:** Dockerized for consistent, portable deployment.
- **CI/CD Ready:** Prepared for automated deployment pipelines.

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.9 |
| API Framework | FastAPI |
| ML Models | XGBoost, Random Forest (scikit-learn) |
| Model Serialization | joblib |
| Containerization | Docker |
| Deployment | HuggingFace Spaces |

---

## 📂 Project Structure

```text
diabetes-fastapi-service/
├── main.py                # FastAPI app & prediction logic
├── diabetes_model.joblib   # Trained Ensemble model artifact
├── Diabetess.csv          # Training dataset
├── Dockerfile             # Docker build instructions
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation



📊 Model Performance
Metric	Score
Accuracy	92.00%
Precision	91.00%
Recall	85.40%
F1-Score	0.88
Methodology: The model was trained on the Frankfurt Diabetes Dataset. I utilized a Pipeline to ensure that data scaling (StandardScaler) and imputation were applied consistently during both training and inference, eliminating data leakage.


📬 About the Author
Ayesha Shahid — ML Researcher | Healthcare AI
BS Information Technology (CGPA: 3.66/4.00)
GitHub: AYESHAASS
LinkedIn: [Your LinkedIn Link Here]


📦 How to Run Locally
code
Bash
# Clone the repo
git clone https://github.com/AYESHAASS/-diabetes-fastapi-service.git


# Run with Docker
docker build -t diabetes-api .
docker run -p 7860:7860 diabetes-api
Visit http://localhost:7860/docs for the Swagger UI.
