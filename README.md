# 🤝 Personalized Networking Assistant

An AI-powered web application designed to process corporate event briefs, generate context-aware conversation starters, and provide live fact verification for professionals.

---

## 🚀 Application URLs & Access Points

### 🌐 Live Deployment
* **Production App (Frontend):** [https://personalized-networking-app.streamlit.app/](https://personalized-networking-app.streamlit.app/)
* **Production API (Backend):** [https://personalized-networking-assistant-xaa1.onrender.com](https://personalized-networking-assistant-xaa1.onrender.com)

### 💻 Local Development Environment
* **Local UI Endpoint:** [http://localhost:8501](http://localhost:8501)
* **Local API Gateway:** [http://localhost:8000](http://localhost:8000)
* **Interactive API Documentation (Swagger UI):** [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 👥 Project Team Matrix
*   **Vyshnavi Mutyalapalli** — *Full-Stack Developer & Integration*
*   **Rahul Dev Bontha** — *Backend Architect*
*   **Bommanaboina Nagaraju** — *Database Administrator*
*   **Nishitha Kodi** — *Frontend UI Engineer*

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
