# app.py
import streamlit as st
from backend.insights import generate_insights
from backend.google_data import fetch_recent_emails, fetch_upcoming_events
from backend.ai_engine import summarize
from backend.memory import memory

st.set_page_config(page_title="Aurora 🌅", layout="wide")
st.title("🌅 Aurora – AI Business Co-Pilot")

# Sidebar
st.sidebar.header("Actions")
if st.sidebar.button("Sync Gmail & Calendar"):
    with st.spinner("Syncing..."):
        fetch_recent_emails()
        fetch_upcoming_events()
        st.success("Synced!")

st.sidebar.download_button("💾 Export Memory", data=str(memory.metadata), file_name="aurora_memory.txt")

# Dashboard
tab1, tab2, tab3 = st.tabs(["Daily Pulse", "Memory Search", "Smart Draft"])

with tab1:
    st.header("🧠 Daily Pulse")
    insights = generate_insights()
    for insight in insights:
        st.write(insight)

with tab2:
    st.header("🔍 Search Your Memory")
    query = st.text_input("Ask about past emails, meetings, etc.")
    if query:
        results = memory.search(query)
        for meta, score in results:
            st.write(f"**{meta.get('type')}**: {meta.get('subject', meta.get('time', ''))} (Score: {score:.2f})")

with tab3:
    st.header("✉️ Smart Draft Generator")
    text = st.text_area("Input text")
    tone = st.selectbox("Tone", ["Professional", "Friendly", "Urgent", "Apology", "Excited"])
    if st.button("Generate"):
        st.text_area("Output", value=rewrite(text, tone), height=200)

# Auto-save memory
import atexit
atexit.register(memory.save)