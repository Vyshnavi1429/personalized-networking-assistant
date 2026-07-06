import os
import requests
import json

class TopicGeneratorService:
    def __init__(self):
        # DIRECT KEY MAPPING: os.getenv lekunda direct ga string pettukundam
        # Ikkada unna AIzaSy... placeholders teesi mee real key petti SAVE cheyi
        self.api_key = "AQ.Ab8RN6LCfH4oc3qgkyiLda8x2Tit_wUgh7VimMmePkoyfSUixg" 

    def generate_starters(self, event_description: str, themes: list, interests: list) -> list:
        # Check to make sure key is replaced
        if "YOUR_ACTUAL_KEY_HERE" in self.api_key or self.api_key == "":
            return ["Please setup your Gemini key string natively in generator.py."]

        # Correct live endpoint format
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={self.api_key}"
        
        prompt = f"""
        You are a smart professional networking coach.
        Generate exactly 3 creative, short conversation starter questions for a professional attending an event.
        Event Context: {event_description}
        Extracted Themes: {', '.join(themes)}
        Interests: {', '.join(interests)}
        
        Return ONLY the 3 questions as lines. No markdown lists, no numbers, no explanations.
        """
        
        payload = {
            "contents": [{
                "parts": [{"text": prompt}]
            }]
        }
        
        headers = {"Content-Type": "application/json"}
        
        try:
            response = requests.post(url, json=payload, headers=headers, timeout=12)
            
            if response.status_code == 200:
                data = response.json()
                raw_text = data['candidates'][0]['content']['parts'][0]['text']
                
                # Split and clean responses safely
                lines = [line.strip("-*• 123456789. \t").strip() for line in raw_text.split("\n") if line.strip()]
                
                if len(lines) >= 3:
                    return lines[:3]
                elif lines:
                    return lines
        except Exception as e:
            pass
            
        # Hard coded default output if connection fails
        return [
            f"Dynamic check: How are you planning to leverage {themes[0] if themes else 'this domain'} techniques?",
            f"What absolute breakthroughs brought you to this event targeting {', '.join(interests[:2])}?",
            "What's your take on the primary speaker's point regarding modern scalable solutions?"
        ]