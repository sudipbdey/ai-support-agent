import os
from dotenv import load_dotenv
from agent import app  # Importing the compiled LangGraph workflow

# Load environment variables (API Keys)
load_dotenv()

def run_test_scenarios():
    # The 5 required scenarios from the assignment
    test_emails = [
        "How do I reset my password?",
        "The export feature crashes when I select PDF format.",
        "I was charged twice for my subscription!",
        "Can you add dark mode to the mobile app?",
        "Our API integration fails intermittently with 504 errors."
    ]

    print("="*50)
    print("🚀 STARTING AI SUPPORT AGENT DEMO")
    print("="*50)

    for i, email in enumerate(test_emails, 1):
        print(f"\n📩 SCENARIO {i}:")
        print(f"Input: \"{email}\"")
        
        # Invoke the LangGraph workflow
        # The 'app' handles classification, RAG, and routing
        result = app.invoke({"email": email})
        
        print(f"✅ Topic: {result.get('topic')}")
        print(f"⚠️ Urgency: {result.get('urgency')}")
        print(f"🤖 Action: {result.get('action')}")
        print(f"📝 Draft Response: {result.get('response')}")
        print("-" * 30)

if __name__ == "__main__":
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ ERROR: Please set your OPENAI_API_KEY in the .env file.")
    else:
        run_test_scenarios()
