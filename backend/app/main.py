from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Optional
from sqlalchemy.orm import Session
import json

from backend.app.database import engine, Base, get_db
from backend.app.models import ConversationHistory
from backend.app.services.analyzer import EventAnalyzerService
from backend.app.services.generator import TopicGeneratorService
from backend.app.services.fact_checker import FactCheckerService

# Create database tables dynamically
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Personalized Networking Assistant API Pipeline")

analyzer_service = EventAnalyzerService()
generator_service = TopicGeneratorService()
fact_checker_service = FactCheckerService()

class GenerationRequest(BaseModel):
    description: str
    interests: List[str]

class FactCheckRequest(BaseModel):
    query: str

class FeedbackRequest(BaseModel):
    id: int
    useful: bool

@app.post("/api/generate")
def generate_networking_prompts(req: GenerationRequest, db: Session = Depends(get_db)):
    themes = analyzer_service.extract_themes(req.description, req.interests)
    starters = generator_service.generate_starters(req.description, themes, req.interests)
    
    # Database entry definition
    db_record = ConversationHistory(
        description=req.description,
        themes=",".join(themes),
        starters="|".join(starters),
        useful=None
    )
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    
    return {
        "id": db_record.id,
        "description": db_record.description,
        "themes": themes,
        "starters": starters,
        "useful": db_record.useful
    }

@app.post("/api/factcheck")
def factcheck_endpoint(req: FactCheckRequest):
    return fact_checker_service.verify_fact(req.query)

@app.get("/api/history")
def get_history(db: Session = Depends(get_db)):
    records = db.query(ConversationHistory).all()
    history_list = []
    for r in records:
        history_list.append({
            "id": r.id,
            "description": r.description,
            "themes": r.themes.split(","),
            "starters": r.starters.split("|"),
            "useful": r.useful
        })
    return history_list

@app.post("/api/feedback")
def log_feedback(req: FeedbackRequest, db: Session = Depends(get_db)):
    record = db.query(ConversationHistory).filter(ConversationHistory.id == req.id).first()
    if not record:
        raise HTTPException(status_code=404, detail="Log entry reference matching mismatch parameter")
    
    record.useful = req.useful
    db.commit()
    return {"status": "success", "msg": "Feedback updated in SQLite schema database successfully."}