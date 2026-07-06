import re

class EventAnalyzerService:
    def __init__(self):
        # Ikkada simple regex and text processing leda transformers NLP code pipeline pettochu
        pass

    def extract_themes(self, description: str, user_interests: list) -> list:
        # Lowercase extraction logic for simplicity and speed
        desc_lower = description.lower()
        extracted_themes = []
        
        # Simple rule-based extraction matching or default fallback themes
        common_themes = ["ai", "sustainability", "blockchain", "healthcare", "urban planning", "climate change"]
        for theme in common_themes:
            if theme in desc_lower:
                extracted_themes.append(theme.capitalize())
                
        for interest in user_interests:
            if interest.lower() in desc_lower and interest.capitalize() not in extracted_themes:
                extracted_themes.append(interest.capitalize())
                
        if not extracted_themes:
            extracted_themes = ["Networking", "General Innovation"]
            
        return list(set(extracted_themes))