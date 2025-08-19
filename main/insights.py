# backend/insights.py
from backend.memory import memory
from backend.ai_engine import summarize, rewrite
from datetime import datetime

def generate_insights():
    insights = []

    # 1. Unanswered emails
    unanswered = memory.search("email from client no reply", k=5)
    for meta, score in unanswered:
        if score > 0.3:
            insights.append(f"🔔 **Follow up**: No reply to email '{meta.get('subject', '')}' since {meta.get('date', '')}")

    # 2. Overloaded schedule
    events = memory.search("meeting", k=10)
    today = str(datetime.today().date())
    today_events = [e for e in events if today in e[0].get('time', '')]
    if len(today_events) > 3:
        insights.append(f"⚠️ **Busy day**: {len(today_events)} meetings today — consider breaks.")

    # 3. Positive signals
    positives = memory.search("happy with the work", k=3)
    for meta, score in positives:
        if score > 0.4:
            insights.append(f"✅ **Great feedback**: Client happy with '{meta.get('subject', '')}' — ask for testimonial?")

    # 4. Tone-mirrored draft
    draft = rewrite("I haven't followed up in a while. Sorry for the delay.", tone="friendly")
    insights.append(f"✍️ **Smart Draft**: _{draft}_")

    return insights[:5]