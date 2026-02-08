import os
from typing import TypedDict, Literal
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, END

# Define the Agent's state [cite: 61]
class AgentState(TypedDict):
    email: str
    urgency: str
    topic: str
    action: str
    response: str

llm = ChatOpenAI(model="gpt-4-turbo", temperature=0)

# NODE 1: Classification [cite: 49, 50]
def classifier(state: AgentState):
    prompt = f"Classify this email by Urgency (Low, Medium, High) and Topic (Account, Billing, Bug, Feature Request, Technical Issue). Email: {state['email']}"
    # In a real app, use structured output here
    prediction = llm.invoke(prompt).content
    # (Simplified parsing logic for demo)
    return {"urgency": "High" if "twice" in state['email'] else "Medium", 
            "topic": "Billing" if "charge" in state['email'] else "Technical"}

# NODE 2: Decision Logic (Escalation vs Auto-reply) [cite: 53, 65]
def router(state: AgentState):
    if state['urgency'] == "High" or state['topic'] in ["Billing", "Technical Issue"]:
        return "escalate"
    return "respond"

# NODE 3: Action Nodes [cite: 52, 54]
def escalate(state: AgentState):
    return {"action": "Human Escalation", "response": "I've flagged this for our specialist team."}

def respond(state: AgentState):
    return {"action": "Auto-Reply", "response": "Thank you for your request. We've received it."}

# Build the Graph 
workflow = StateGraph(AgentState)
workflow.add_node("classify", classifier)
workflow.add_node("escalate", escalate)
workflow.add_node("respond", respond)

workflow.set_entry_point("classify")
workflow.add_conditional_edges("classify", router, {"escalate": "escalate", "respond": "respond"})
workflow.add_edge("escalate", END)
workflow.add_edge("respond", END)

app = workflow.compile()
