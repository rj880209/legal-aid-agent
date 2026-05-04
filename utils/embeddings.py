import json
import os
import pickle
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

DATA_DIR = Path(__file__).parent.parent / "data"
VECTOR_STORE_DIR = Path(__file__).parent.parent / "vector_store"
INDEX_PATH = VECTOR_STORE_DIR / "tfidf_index.pkl"
DOCS_PATH = VECTOR_STORE_DIR / "documents.pkl"


def load_legal_documents() -> list[dict]:
    documents = []
    data_files = [
        "bns_sections.json",
        "bnss_procedures.json",
        "consumer_act.json",
        "it_act.json",
        "constitution.json",
    ]
    for filename in data_files:
        filepath = DATA_DIR / filename
        if filepath.exists():
            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
                documents.extend(data)
    return documents


def create_document_text(doc: dict) -> str:
    parts = []
    for key in ("section", "article", "title", "description", "procedure", "penalty"):
        if key in doc and doc[key]:
            parts.append(str(doc[key]))
    if "keywords" in doc:
        parts.append(" ".join(doc["keywords"]))
    return " ".join(parts)


def build_vector_store(force_rebuild: bool = False):
    VECTOR_STORE_DIR.mkdir(exist_ok=True)

    if not force_rebuild and INDEX_PATH.exists() and DOCS_PATH.exists():
        with open(INDEX_PATH, "rb") as f:
            vectorizer = pickle.load(f)
        with open(DOCS_PATH, "rb") as f:
            data = pickle.load(f)
        return vectorizer, data["documents"], data["matrix"]

    documents = load_legal_documents()
    texts = [create_document_text(doc) for doc in documents]

    vectorizer = TfidfVectorizer(
        max_features=5000,
        ngram_range=(1, 2),
        stop_words="english",
        sublinear_tf=True,
    )
    matrix = vectorizer.fit_transform(texts)

    with open(INDEX_PATH, "wb") as f:
        pickle.dump(vectorizer, f)
    with open(DOCS_PATH, "wb") as f:
        pickle.dump({"documents": documents, "matrix": matrix}, f)

    return vectorizer, documents, matrix


def search_documents(query: str, vectorizer, documents: list, matrix, k: int = 5) -> list[dict]:
    query_vec = vectorizer.transform([query])
    scores = cosine_similarity(query_vec, matrix).flatten()
    top_k_idx = np.argsort(scores)[::-1][:k]

    results = []
    for idx in top_k_idx:
        if scores[idx] > 0:
            doc = documents[idx].copy()
            doc["relevance_score"] = float(scores[idx])
            results.append(doc)

    if not results:
        for idx in top_k_idx[:3]:
            doc = documents[idx].copy()
            doc["relevance_score"] = float(scores[idx])
            results.append(doc)

    return results
