# 🤝 Personalized Networking Assistant

An AI-powered web application designed to process corporate event briefs, generate context-aware conversation starters, and provide live fact verification for professionals.

## 🚀 Live Application
The project is continuously deployed and accessible online:
👉 **https://personalized-networking-app.streamlit.app/**

---

## 🛠️ Tech Stack
* **Frontend:** Streamlit (Interactive Multi-tab UI)
* **Backend:** FastAPI (Asynchronous REST API)
* **Database:** SQLite with SQLAlchemy ORM (Persistent History & Feedback Logging)

---

## 📂 Project Directory Structure
```text
networking_assistant/
├── backend/
│   └── app/
│       ├── main.py           # FastAPI Main Gateway
│       ├── database.py       # SQLite Connection Engine
│       ├── models.py         # SQLAlchemy Database Models
│       ├── schemas.py        # Pydantic Data Validations
│       ├── routes/
│       │   └── api.py        # API Endpoints
│       └── services/         # Logic Layers (Analyzer, Generator, Fact-Checker)
├── frontend/
│   └── app.py                # Streamlit Client Interface
└── requirements.txt          # Unified Python Dependencies



👥 Project Team Matrix
Vyshnavi Mutyalapalli

Rahul Dev Bontha

Bommanaboina Nagaraju

Nishitha Kodi

⚙️ Local Setup Instructions
1. Install Dependencies
Open your project terminal and run:

Bash
pip install -r requirements.txt
2. Start Backend Server (FastAPI)
Bash
uvicorn backend.app.main:app --reload
The interactive Swagger documentation will be available at: http://localhost:8000/docs

3. Start Frontend UI (Streamlit)
Open a separate terminal window and run:

Bash
streamlit run frontend/app.py
The user dashboard will open automatically in your browser at: http://localhost:8501
