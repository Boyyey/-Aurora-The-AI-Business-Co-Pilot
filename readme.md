# 🌅 Aurora – The AI Business Co-Pilot

🚀 **Your silent, smart, proactive partner in business decisions.**  
Aurora watches your work, learns your patterns, and *anticipates* what you should do next — like a co-founder who never sleeps.

> ✨ **No more missed follow-ups. No more forgotten tasks. No more decision fatigue.**  
> Just **AI-powered clarity**, delivered daily.

---

## 🎯 What It Does

Aurora is a **private, local-first AI assistant** that:
- 🔍 Reads your emails, calendar, and notes (with permission)
- 🧠 Learns your tone, priorities, and habits
- 💡 Gives **proactive insights**: “Follow up with Alex,” “You’re overloaded tomorrow”
- ✉️ Writes **smart replies in your voice**
- 🗄️ Remembers everything in a **searchable AI memory**
- 📊 Runs entirely on your machine — **no data sent to the cloud**

Think:  
> _“What if Excel could think?”_  
> This is the next step.

---

## 🚀 Features

| Feature | Description |
|--------|-------------|
| 📥 **Gmail & Calendar Sync** | Secure OAuth2 integration |
| 🧠 **AI-Powered Insights** | Detects follow-ups, workload, sentiment |
| 📝 **Smart Reply Generator** | Rewrites messages in your tone (T5-powered) |
| 🔍 **Searchable Memory** | FAISS vector DB remembers every decision |
| 📄 **Daily Pulse Dashboard** | Streamlit UI with real-time insights |
| 💻 **Runs Locally** | All data stays on your device — private by design |
| 📤 **Exportable Insights** | Save or share your AI-generated summaries |

---

## 🛠️ Tech Stack

- **Python** – Core logic
- **Streamlit** – Beautiful, reactive UI
- **Hugging Face Transformers (T5)** – Smart rewriting & summarization
- **FAISS (Facebook AI Similarity Search)** – Vector memory
- **Sentence Transformers** – Semantic understanding
- **Google API Client** – Gmail & Calendar integration
- **Local-First Architecture** – No cloud, no tracking, no risk

---

## 🖼️ Screenshots

> 🎥 *Coming soon!*  
> (After you run it — take a screenshot and add it here!)

---

## 📦 Installation

1. **Clone the repo**
   ```bash
   git clone https://github.com/your-username/aurora-co-pilot.git
   cd aurora-co-pilot
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Get Google API Credentials**
   - Go to [Google Cloud Console](https://console.cloud.google.com/)
   - Create a new project
   - Enable: **Gmail API** and **Google Calendar API**
   - Create **OAuth 2.0 Client ID** (Application type: Desktop)
   - Download `credentials.json` and place it in the root folder

4. **Run the app**
   ```bash
   streamlit run app.py
   ```

5. **First Run?**  
   - Click “Sync Gmail & Calendar”
   - Sign in with your Google account
   - Let Aurora learn from your data

---

## 🧪 Usage

| Action | How |
|------|-----|
| 🔄 Sync Data | Click “Sync Gmail & Calendar” |
| 🧠 View Insights | Check “Daily Pulse” tab |
| 🔍 Search Memory | Type “Find that email from Alex” |
| ✉️ Draft a Reply | Use “Smart Draft Generator” |
| 💾 Export Data | Click “Export Memory” |

---

## 🔮 Future Roadmap

- 📄 **PDF Reports**: “Download Weekly Summary”
- 📅 **Auto-Scheduling**: “Book a 15-min with client”
- 🧠 **Tone Mirror**: Fine-tune AI on *your* writing style
- 📎 **Notion / Slack Integration**
- 🖥️ **Desktop App (Tauri)** – Offline, always-available
- 🔊 **Voice Mode**: “Hey Aurora, what should I do today?”

---

## 🛡️ Privacy & Security

✅ All data stays **on your machine**  
✅ No internet required after setup  
✅ Tokens encrypted locally  
✅ You own your AI brain — export anytime

> We believe **AI should work for you — not the other way around.**

---

## 🙌 Contributing

Open to PRs! Want to:
- Add Zoom transcript parsing?
- Build a mobile version?
- Train a custom T5 model?

Just open an issue or PR — let’s build the future of work, together.

---

## 🌟 Inspiration

> _“The best tool is the one that knows you.”_  
> Aurora is the **spiritual successor to Excel** — not a spreadsheet, but a **thinking surface** for business.

---

## 🚀 Built with ❤️ for founders, creators, and thinkers.
