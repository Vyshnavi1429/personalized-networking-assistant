import streamlit as st
import requests

st.set_page_config(page_title="Personalized Networking Assistant", layout="wide")
# పాత లైన్ తీసేసి ఇది పెట్టండి (చివర్లో /api యాడ్ చేసాం)
BACKEND_URL = st.secrets.get("BACKEND_URL", "https://personalized-networking-assistant-xaa1.onrender.com").rstrip('/') + "/api"

st.title("🤝 Personalized Networking Assistant")
st.write("Extract smart themes, generate contextual starters, and quick-verify facts instantly.")

tabs = st.tabs(["💡 Generate Starters", "🔍 Fact Verification", "📜 History & Feedback"])

# Tab 1: Generation Flow
with tabs[0]:
    st.header("Generate Conversation Starters")
    event_desc = st.text_area("Event Description", placeholder="e.g., AI for Sustainable Cities panel discussion...")
    user_ints = st.text_input("Your Interests (comma-separated)", placeholder="e.g., climate change, urban planning")
    
    if st.button("Generate Prompts", type="primary"):
        if event_desc and user_ints:
            interest_list = [i.strip() for i in user_ints.split(",") if i.strip()]
            payload = {"description": event_desc, "interests": interest_list}
            
            with st.spinner("Analyzing event themes and generating strategies..."):
                try:
                    res = requests.post(f"{BACKEND_URL}/generate", json=payload)
                    if res.status_code == 200:
                        data = res.json()
                        st.success("Successfully Processed and Logged to DB!")
                        st.subheader("Extracted Themes")
                        st.write(", ".join(data["themes"]))
                        
                        st.subheader("Tailored Starters")
                        for idx, starter in enumerate(data["starters"], 1):
                            st.info(f"**Starter {idx}:** {starter}")
                    else:
                        st.error("Backend error parsing data schema models.")
                except Exception as e:
                    st.error(f"Connection failure. Make sure backend is running: {e}")

# Tab 2: Fact Verification
with tabs[1]:
    st.header("Quick Fact Verification")
    query = st.text_input("Enter a technical term or concept to verify:", placeholder="e.g., Blockchain in healthcare")
    if st.button("Check Concept"):
        if query:
            with st.spinner("Querying ecosystem documentation references..."):
                try:
                    res = requests.post(f"{BACKEND_URL}/factcheck", json={"query": query})
                    if res.status_code == 200:
                        info = res.json()
                        if info.get("found"):
                            st.success(f"**Source Found:** {info['title']}")
                            st.write(info["summary"])
                            if info.get("url"):
                                st.markdown(f"[Read full article on Wikipedia]({info['url']})")
                        else:
                            st.warning(info["summary"])
                except Exception as e:
                    st.error(f"Connection failure: {e}")

# Tab 3: History View & Feedback
with tabs[2]:
    st.header("Review Past Strategies & Logs")
    
    try:
        res = requests.get(f"{BACKEND_URL}/history")
        if res.status_code == 200:
            history_data = res.json()
            if not history_data:
                st.info("No session records logged in SQLite database yet.")
            
            # Show reversed so newest logs are on top
            for item in reversed(history_data):
                with st.expander(f"Log #{item['id']} - Themes: {', '.join(item['themes'])}"):
                    st.write(f"**Description:** {item['description']}")
                    st.write("**Generated Options:**")
                    for s in item['starters']:
                        st.write(f"- {s}")
                    
                    status = item.get("useful")
                    current_status = "Pending Feedback"
                    if status is True:
                        current_status = "👍 Useful"
                    elif status is False:
                        current_status = "👎 Not Useful"
                        
                    st.write(f"Current Evaluation status: **{current_status}**")
                    
                    c1, c2 = st.columns(2)
                    # Unique keys based on ID to avoid duplicate widget issues
                    if c1.button("Mark Helpful", key=f"up_{item['id']}"):
                        requests.post(f"{BACKEND_URL}/feedback", json={"id": item['id'], "useful": True})
                        st.rerun()
                    if c2.button("Mark Unhelpful", key=f"down_{item['id']}"):
                        requests.post(f"{BACKEND_URL}/feedback", json={"id": item['id'], "useful": False})
                        st.rerun()
        else:
            st.error("Failed to load history schemas from local DB.")
    except Exception as e:
        st.info("Start your backend terminal node to populate persistent history stream logs.")