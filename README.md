# 🤖 AI-Powered Customer Support Agent

An autonomous support system built with **LangChain** and **LangGraph** designed to process customer emails from ingestion to resolution. The agent classifies intent, retrieves policy information via RAG, and makes intelligent decisions on when to escalate to a human specialist.

## 🏗️ Architecture & Workflow

The system is designed as a **State Machine** using LangGraph to ensure a controlled and predictable workflow.



### 🛠️ Core Components
- **Classifier Node**: Uses GPT-4 to identify the **Urgency** (Low, Medium, High) and **Topic** (Account, Billing, Bug, Feature Request, Technical Issue).
- **RAG Retriever**: Searches the `knowledge_base.json` for specific company policies and technical documentation.
- **Router logic**: Determines if the agent can resolve the issue automatically or if it requires a human handoff.

---

## 🚦 Escalation Logic (Deliverable 2)

Our escalation policy is built on "Risk and Complexity" boundaries. The agent is programmed to hand over the "keys" to a human in the following scenarios:

1. **Financial Risk (Billing)**: Any issue involving money (e.g., "I was charged twice") is flagged as **High Urgency**. These are automatically escalated to ensure a human reviews the transaction history.
2. **Infrastructure Failure**: Technical issues like **504 API errors** are escalated because they indicate server-side timeouts that a front-line AI cannot fix.
3. **Ambiguity**: If the RAG search returns no relevant documentation or the confidence score is low, the issue is escalated to prevent "hallucinated" support.

---

## 📅 Follow-up System
The agent handles ongoing issues by scheduling follow-up actions:
- **Bugs**: If a bug is confirmed (e.g., PDF export crash), the agent drafts a response to the user and logs a **Follow-up** task for 3 business days later to update the customer on the engineering fix.

---

## 🚀 Getting Started

### 1. Prerequisites
- Python 3.10+
- OpenAI API Key

### 2. Installation
```bash
git clone https://github.com/sudipbdey/ai-support-agent.git
cd ai-support-agent
pip install -r requirements.txt
