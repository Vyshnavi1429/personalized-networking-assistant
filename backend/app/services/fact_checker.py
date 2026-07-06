import requests

class FactCheckerService:
    def __init__(self):
        self.base_url = "https://en.wikipedia.org/api/rest_v1/page/summary/"

    def verify_fact(self, query: str) -> dict:
        # 1. Clean extra spaces and format title case matching
        clean_query = query.strip()
        
        # 2. Case normalization for Wikipedia schema mapping 
        # "block chain" or "blockchain" -> converts gracefully
        formatted_query = clean_query.title().replace(" ", "_")
        
        try:
            response = requests.get(f"{self.base_url}{formatted_query}", timeout=5)
            
            # Target fallback to try direct joined letters syntax if spaced query fails
            if response.status_code != 200 and "_" in formatted_query:
                retry_query = formatted_query.replace("_", "")
                response = requests.get(f"{self.base_url}{retry_query}", timeout=5)
                
            if response.status_code == 200:
                data = response.json()
                return {
                    "found": True,
                    "title": data.get("title"),
                    "summary": data.get("extract"),
                    "url": data.get("content_urls", {}).get("desktop", {}).get("page")
                }
        except Exception:
            pass
            
        return {"found": False, "summary": f"No verified Wikipedia records found for '{query}'. Try searching using standard terms like 'Blockchain' or 'Artificial intelligence'."}