# AI Intelligence Agent

A lightweight Python CLI tool that produces structured geopolitical intelligence reports using the Google Gemini API with grounded search.

Give it any topic — a conflict, policy change, diplomatic event — and it returns a concise report split into **Historical Context** and **Current Events**, backed by cited sources.

---

## Prerequisites

| Requirement | Version |
|-------------|---------|
| Python      | 3.10+   |
| pip         | latest  |
| Gemini API key | [Get one free](https://aistudio.google.com/apikey) |

---

## Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-intelligence-agent.git
cd ai-intelligence-agent
```

### 2. Create a virtual environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure your API key

```bash
cp .env.example .env
```

Open `.env` and replace the placeholder with your real key:

```
GEMINI_API_KEY=your_actual_key_here
```

> **Note:** `.env` is git-ignored and will never be committed.

### 5. Run the agent

```bash
python agent.py
```

---

## Usage

```
============================================================
   AI INTELLIGENCE AGENT
============================================================
Type a topic to investigate, or 'exit' to quit.

🔎 Topic: India-Pakistan water treaty dispute
⏳ Deploying agent to investigate: India-Pakistan water treaty dispute...

============================================================
   INTELLIGENCE REPORT
============================================================
## Historical Context
...

## Current Events
...

🔎 Topic: exit

👋 Agent shut down. Goodbye.
```

---

## Project Structure

```
.
├── agent.py            # Main CLI agent
├── requirements.txt    # Python dependencies
├── .env.example        # Template for environment variables
├── .gitignore          # Files excluded from version control
└── README.md           # This file
```

---

## Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `GEMINI_API_KEY` | ✅ | Your Google Gemini API key |

---

## License

This project is provided as-is for educational and personal use.
