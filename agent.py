"""
AI Intelligence Agent — CLI tool for geopolitical research.

Uses the Google Gemini API with grounded search to produce structured
intelligence reports on any topic the user provides.
"""

import os
import sys

from dotenv import load_dotenv
from google import genai
from google.genai import types

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

MODEL_NAME = "gemini-2.5-flash"

SYSTEM_INSTRUCTION = """\
You are an expert geopolitical intelligence agent. Your task is to provide
a comprehensive, unbiased timeline and current status of the requested topic.

Strict Execution Rules:
1. Use your search tool to retrieve the most up-to-date information.
2. Separate your output into exactly two sections:
   - "Historical Context" — the root of the issue.
   - "Current Events" — what is happening right now.
3. Ground your claims in specific, cited events and dates.
4. Do not provide commentary, opinions, or speculative analysis.
"""

# ---------------------------------------------------------------------------
# Core logic
# ---------------------------------------------------------------------------


def run_intelligence_agent(topic: str) -> None:
    """Send *topic* to Gemini and print a structured intelligence report."""

    client = genai.Client()

    print(f"\n⏳ Deploying agent to investigate: {topic}...\n")

    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=topic,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_INSTRUCTION,
                tools=[{"google_search": {}}],
                temperature=0.2,
            ),
        )

        print("=" * 60)
        print("   INTELLIGENCE REPORT")
        print("=" * 60)
        print(response.text)

    except types.ClientError as exc:
        print(f"\n❌ API authentication or request error: {exc}")
        print("   Check that your GEMINI_API_KEY is valid.")
    except ConnectionError as exc:
        print(f"\n❌ Network error — could not reach the Gemini API: {exc}")
    except Exception as exc:
        print(f"\n❌ Unexpected error during agent execution: {exc}")


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------


def main() -> None:
    """Interactive REPL — prompts for topics until the user types 'exit'."""

    # Load .env file if present (no-op when file is missing).
    load_dotenv()

    if not os.environ.get("GEMINI_API_KEY"):
        print(
            "\n❌ GEMINI_API_KEY is not set.\n"
            "   1. Copy .env.example to .env\n"
            "   2. Paste your API key into .env\n"
            "   3. Re-run the agent.\n"
            "   Get a key at: https://aistudio.google.com/apikey"
        )
        sys.exit(1)

    print("\n" + "=" * 60)
    print("   AI INTELLIGENCE AGENT")
    print("=" * 60)
    print("Type a topic to investigate, or 'exit' to quit.\n")

    try:
        while True:
            try:
                topic = input("🔎 Topic: ")
            except EOFError:
                # stdin closed (e.g. piped input exhausted)
                break

            if topic.strip().lower() == "exit":
                break

            if not topic.strip():
                print("⚠️  Please enter a valid topic.\n")
                continue

            run_intelligence_agent(topic.strip())

    except KeyboardInterrupt:
        # Ctrl+C — exit cleanly without a traceback
        print()

    print("\n👋 Agent shut down. Goodbye.")


if __name__ == "__main__":
    main()