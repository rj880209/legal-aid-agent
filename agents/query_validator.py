import os
import json
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage
from utils.prompt_templates import NON_LEGAL_PROMPT

LEGAL_TOPICS = [
    "crime", "fraud", "cheating", "theft", "assault", "harassment", "stalking",
    "defamation", "murder", "arrest", "bail", "fir", "police", "court",
    "consumer", "refund", "warranty", "defective", "product", "service",
    "property", "land", "rent", "landlord", "tenant", "eviction", "dispute",
    "constitutional", "fundamental rights", "article", "writ", "habeas corpus",
    "divorce", "maintenance", "custody", "marriage", "family",
    "cyber", "hacking", "online fraud", "data breach", "privacy",
    "cheque bounce", "contract", "agreement", "compensation",
    "insurance", "medical negligence", "hospital", "doctor",
    "employment", "termination", "salary", "labour", "workplace",
    "income tax", "gst", "tax", "debt", "loan", "bank",
    "intellectual property", "copyright", "trademark", "patent",
    "rti", "government", "corruption", "bribe", "public servant",
    "accident", "negligence", "damages", "legal notice", "lawyer",
    # Hindi/regional legal keywords
    "मुकदमा", "अदालत", "पुलिस", "एफआईआर", "शिकायत", "धोखा", "जमानत",
    "संपत्ति", "किराया", "तलाक", "उपभोक्ता", "भ्रष्टाचार", "मुआवजा",
]

CLEARLY_NON_LEGAL = [
    "recipe", "cook", "food", "weather", "joke", "movie", "song", "music",
    "sport", "cricket", "football", "game", "fitness", "exercise", "yoga",
    "travel", "hotel", "tourism", "holiday", "vacation",
    "programming", "code", "python", "javascript", "software",
    "math", "physics", "chemistry", "biology", "science",
    "fashion", "beauty", "makeup", "clothes", "shopping",
    "astrology", "horoscope", "zodiac",
]


def check_for_legal_keywords(query: str) -> bool | None:
    query_lower = query.lower()
    legal_hit     = any(kw in query_lower for kw in LEGAL_TOPICS)
    non_legal_hit = sum(1 for kw in CLEARLY_NON_LEGAL if kw in query_lower)
    if legal_hit:
        return True
    if non_legal_hit >= 2:
        return False
    return None


def _get_localized_message(query: str, category: str, language_instruction: str) -> str:
    """Use Groq to generate a non-legal rejection message in the user's language."""
    api_key = os.environ.get("GROQ_API_KEY", "")
    if not api_key:
        return (
            "This platform is exclusively for Indian legal matters such as criminal complaints, "
            "consumer disputes, property issues, cyber crime, and constitutional rights. "
            "Please describe a legal issue you are facing."
        )
    try:
        llm = ChatGroq(
            groq_api_key=api_key,
            model_name="llama-3.3-70b-versatile",
            temperature=0.2,
            max_tokens=200,
        )
        prompt = NON_LEGAL_PROMPT.format(
            language_instruction=language_instruction,
            query=query,
            category=category,
        )
        resp = llm.invoke([
            SystemMessage(content="You generate polite redirection messages for a legal aid platform."),
            HumanMessage(content=prompt),
        ])
        return resp.content.strip()
    except Exception:
        return (
            "This platform is exclusively for Indian legal matters. "
            "Please describe your legal issue to get assistance."
        )


def validate_legal_query(user_query: str, language_instruction: str = "Respond in English.") -> dict:
    quick_check = check_for_legal_keywords(user_query)
    if quick_check is True:
        return {"is_legal": True, "reason": "Legal query detected", "message": ""}

    api_key = os.environ.get("GROQ_API_KEY", "")
    if not api_key:
        return {"is_legal": True, "reason": "No API key - skipping validation", "message": ""}

    llm = ChatGroq(
        groq_api_key=api_key,
        model_name="llama-3.3-70b-versatile",
        temperature=0,
        max_tokens=200,
    )

    prompt = f"""You are a query classifier for a Legal Aid platform for Indian citizens.

Determine if this query is related to Indian legal matters (criminal law, consumer rights, civil disputes,
constitutional rights, family law, cyber crime, property, employment, taxation, or any other legal topic in India).
The query may be in any language (Hindi, Tamil, Bengali, English, etc.) — classify based on meaning, not language.

Query: "{user_query}"

Respond with ONLY valid JSON:
{{
  "is_legal": true or false,
  "category": "legal topic or non-legal category",
  "reason": "brief reason"
}}

Examples of LEGAL queries: filing FIR, consumer complaint, property dispute, divorce, cyber fraud, tenant rights, medical negligence, RTI, bail, fundamental rights.
Examples of NON-LEGAL queries: cooking recipes, weather forecast, programming help, sports scores, movie recommendations."""

    try:
        response = llm.invoke([
            SystemMessage(content="You classify queries as legal or non-legal for an Indian legal aid platform. Always respond with valid JSON only."),
            HumanMessage(content=prompt),
        ])
        content = response.content.strip()
        if content.startswith("```"):
            lines   = content.split("\n")
            content = "\n".join(lines[1:-1]) if lines[-1].strip() == "```" else "\n".join(lines[1:])

        result   = json.loads(content)
        is_legal = result.get("is_legal", True)

        if not is_legal:
            category = result.get("category", "general")
            message  = _get_localized_message(user_query, category, language_instruction)
            return {
                "is_legal": False,
                "reason":   result.get("reason", "Not a legal query"),
                "category": category,
                "message":  message,
            }

        return {"is_legal": True, "reason": result.get("reason", "Legal query"), "message": ""}

    except Exception:
        return {"is_legal": True, "reason": "Validation inconclusive - proceeding", "message": ""}
