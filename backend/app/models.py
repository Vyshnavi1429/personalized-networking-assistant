from sqlalchemy import Column, Integer, String, Boolean
from backend.app.database import Base

class ConversationHistory(Base):
    __tablename__ = "conversation_history"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, index=True)
    themes = Column(String)  # Stored as comma-separated values
    starters = Column(String)  # Stored as pipe-separated values
    useful = Column(Boolean, nullable=True)