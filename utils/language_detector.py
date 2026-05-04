import os
import json
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage

SUPPORTED_LANGUAGES = {
    "hindi":       ("Hindi",       "hi", "हिन्दी"),
    "bengali":     ("Bengali",     "bn", "বাংলা"),
    "tamil":       ("Tamil",       "ta", "தமிழ்"),
    "telugu":      ("Telugu",      "te", "తెలుగు"),
    "marathi":     ("Marathi",     "mr", "मराठी"),
    "gujarati":    ("Gujarati",    "gu", "ગુજરાતી"),
    "kannada":     ("Kannada",     "kn", "ಕನ್ನಡ"),
    "malayalam":   ("Malayalam",   "ml", "മലയാളം"),
    "punjabi":     ("Punjabi",     "pa", "ਪੰਜਾਬੀ"),
    "odia":        ("Odia",        "or", "ଓଡ଼ିଆ"),
    "urdu":        ("Urdu",        "ur", "اردو"),
    "assamese":    ("Assamese",    "as", "অসমীয়া"),
    "english":     ("English",     "en", "English"),
}

DEFAULT_LANG = {"name": "English", "code": "en", "native": "English", "key": "english"}

_HINDI_KEYWORDS = ["मेरा", "मेरी", "मुझे", "मैं", "है", "हैं", "का", "की", "के", "में", "को", "से", "पर", "और", "नहीं", "कर", "था", "थी"]


def _quick_hindi_detect(text: str) -> bool:
    """Fast check for Devanagari script (covers Hindi, Marathi, etc.)."""
    return any("\u0900" <= ch <= "\u097F" for ch in text)


def _quick_script_detect(text: str) -> str | None:
    """Detect script from Unicode block — covers major Indian languages."""
    for ch in text:
        cp = ord(ch)
        if 0x0900 <= cp <= 0x097F: return "hindi"
        if 0x0980 <= cp <= 0x09FF: return "bengali"
        if 0x0A00 <= cp <= 0x0A7F: return "punjabi"
        if 0x0A80 <= cp <= 0x0AFF: return "gujarati"
        if 0x0B00 <= cp <= 0x0B7F: return "odia"
        if 0x0B80 <= cp <= 0x0BFF: return "tamil"
        if 0x0C00 <= cp <= 0x0C7F: return "telugu"
        if 0x0C80 <= cp <= 0x0CFF: return "kannada"
        if 0x0D00 <= cp <= 0x0D7F: return "malayalam"
        if 0x0600 <= cp <= 0x06FF: return "urdu"
        if 0x0980 <= cp <= 0x09FF: return "assamese"
    return None


def detect_language(query: str) -> dict:
    """
    Detect the language of `query`.
    Returns: { name, code, native, key, instruction }
    """
    script_key = _quick_script_detect(query)
    if script_key:
        info = SUPPORTED_LANGUAGES.get(script_key, SUPPORTED_LANGUAGES["hindi"])
        key  = script_key
        lang = {"name": info[0], "code": info[1], "native": info[2], "key": key}
        lang["instruction"] = _build_instruction(lang)
        return lang

    api_key = os.environ.get("GROQ_API_KEY", "")
    if not api_key:
        result = dict(DEFAULT_LANG)
        result["instruction"] = _build_instruction(result)
        return result

    try:
        llm = ChatGroq(
            groq_api_key=api_key,
            model_name="llama-3.3-70b-versatile",
            temperature=0,
            max_tokens=80,
        )
        prompt = (
            f'Detect the language of this text: "{query[:300]}"\n\n'
            "Return ONLY valid JSON:\n"
            '{"language": "<language name in English, e.g. Hindi, Tamil, English, Bengali>"}'
        )
        resp    = llm.invoke([
            SystemMessage(content="You are a language detector. Always return valid JSON only."),
            HumanMessage(content=prompt),
        ])
        content = resp.content.strip()
        if content.startswith("```"):
            lines   = content.split("\n")
            content = "\n".join(lines[1:-1])
        data = json.loads(content)
        lang_name = data.get("language", "English").strip().lower()

        matched = None
        for key, (name, code, native) in SUPPORTED_LANGUAGES.items():
            if key in lang_name or lang_name in name.lower():
                matched = {"name": name, "code": code, "native": native, "key": key}
                break

        if not matched:
            matched = dict(DEFAULT_LANG)

        matched["instruction"] = _build_instruction(matched)
        return matched

    except Exception:
        result = dict(DEFAULT_LANG)
        result["instruction"] = _build_instruction(result)
        return result


def _build_instruction(lang: dict) -> str:
    if lang["code"] == "en":
        return "Respond in English."
    return (
        f"IMPORTANT: You MUST respond entirely in {lang['name']} ({lang['native']}). "
        f"Every word of your response must be in {lang['name']}. "
        f"Do not mix in English except for proper nouns, section numbers, act names, and portal URLs."
    )
