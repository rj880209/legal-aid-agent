import os
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage
from utils.embeddings import build_vector_store, search_documents
from utils.prompt_templates import RAG_PROMPT

_vectorizer = None
_documents  = None
_matrix     = None


def get_vector_store():
    global _vectorizer, _documents, _matrix
    if _vectorizer is None:
        _vectorizer, _documents, _matrix = build_vector_store()
    return _vectorizer, _documents, _matrix


def retrieve_legal_provisions(query: str, domain: str, k: int = 5) -> list[dict]:
    vectorizer, documents, matrix = get_vector_store()
    enriched_query = f"{domain} law India {query}"
    return search_documents(enriched_query, vectorizer, documents, matrix, k=k)


def format_provisions_for_llm(provisions: list[dict]) -> str:
    formatted = []
    for i, prov in enumerate(provisions, 1):
        section_id  = prov.get("section") or prov.get("article", "Unknown")
        title       = prov.get("title", "")
        description = prov.get("description", "")
        penalty     = prov.get("penalty", "")
        procedure   = prov.get("procedure", "")
        act         = prov.get("act", "")
        text = f"{i}. **{section_id} - {title}** ({act})\n   {description}"
        if penalty:
            text += f"\n   Penalty: {penalty}"
        if procedure:
            text += f"\n   Procedure: {procedure}"
        formatted.append(text)
    return "\n\n".join(formatted)


def analyze_with_rag(
    query: str,
    domain: str,
    language_instruction: str = "Respond in English.",
) -> tuple[list[dict], str]:
    provisions = retrieve_legal_provisions(query, domain)

    api_key = os.environ.get("GROQ_API_KEY", "")
    llm = ChatGroq(
        groq_api_key=api_key,
        model_name="llama-3.3-70b-versatile",
        temperature=0.1,
        max_tokens=1024,
    )

    context = format_provisions_for_llm(provisions)
    prompt  = RAG_PROMPT.format(
        language_instruction=language_instruction,
        context=context,
        query=query,
    )

    messages = [
        SystemMessage(content=(
            "You are an expert in Indian law. Cite only the most relevant legal provisions for this specific case. "
            + language_instruction
        )),
        HumanMessage(content=prompt),
    ]

    response = llm.invoke(messages)
    return provisions, response.content
