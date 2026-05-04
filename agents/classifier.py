import json
import os
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage
from utils.prompt_templates import CLASSIFICATION_PROMPT


def get_llm():
    api_key = os.environ.get("GROQ_API_KEY", "")
    return ChatGroq(
        groq_api_key=api_key,
        model_name="llama-3.3-70b-versatile",
        temperature=0.1,
        max_tokens=512,
    )


def classify_query(user_query: str) -> dict:
    llm = get_llm()
    prompt = CLASSIFICATION_PROMPT.format(user_query=user_query)

    messages = [
        SystemMessage(content="You are a precise Indian legal classification expert. Always return valid JSON only."),
        HumanMessage(content=prompt),
    ]

    response = llm.invoke(messages)
    content = response.content.strip()

    if content.startswith("```"):
        lines = content.split("\n")
        content = "\n".join(lines[1:-1]) if lines[-1] == "```" else "\n".join(lines[1:])

    try:
        result = json.loads(content)
    except json.JSONDecodeError:
        import re
        json_match = re.search(r'\{.*\}', content, re.DOTALL)
        if json_match:
            result = json.loads(json_match.group())
        else:
            result = {
                "domain": "Civil",
                "sub_category": "General Legal Issue",
                "forum": "District Court",
                "urgency": "Medium",
                "keywords": [],
                "hybrid_domains": [],
            }

    if "hybrid_domains" not in result:
        result["hybrid_domains"] = []

    return result
