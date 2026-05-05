# Legal Aid Agent for India

Legal Aid Agent is a Streamlit-based AI assistant that helps Indian citizens understand legal issues, identify relevant legal domains, retrieve applicable legal provisions, and generate practical next-step guidance. It is designed for educational legal information only and is not a replacement for advice from a qualified advocate.

The application combines a local legal knowledge base with Groq-hosted LLM calls through LangChain. It supports Indian legal domains such as criminal law, consumer disputes, civil matters, constitutional rights, cyber crime, financial fraud, and related hybrid issues.

## Features

- Legal query validation to filter out non-legal questions.
- Automatic language detection for English and major Indian languages.
- Legal domain classification into Criminal, Consumer, Civil, Constitutional, or Hybrid.
- Retrieval of relevant Indian legal provisions using a local TF-IDF vector store.
- AI-generated legal analysis using retrieved provisions.
- Step-by-step action plan with evidence checklist, timelines, portals, and helplines.
- Downloadable reports in PDF, Markdown, and plain text formats.
- Downloadable legal document templates:
  - Legal notice
  - FIR complaint
  - Consumer complaint
- Official portal links for consumer complaints, cyber crime, police/e-FIR, courts, legal aid, constitutional remedies, and financial fraud.
- Sidebar emergency helplines for police, women, cyber crime, consumer complaints, free legal aid, child helpline, and medical emergency.

## Technology Stack

- Python
- Streamlit for the web interface
- LangChain Groq integration for LLM access
- Groq model: `llama-3.3-70b-versatile`
- scikit-learn for TF-IDF vectorization and cosine similarity search
- NumPy for ranking/search utilities
- fpdf2 for PDF report generation
- Pydantic as an installed dependency
- Local JSON data files for legal provisions
- Pickle-based local vector store cache

## Project Structure

```text
legal-aid-agent/
  app.py
  requirements.txt
  README.md
  agents/
    classifier.py
    guide_generator.py
    query_validator.py
    rag_retriever.py
  data/
    bns_sections.json
    bnss_procedures.json
    constitution.json
    consumer_act.json
    it_act.json
  templates/
    consumer_complaint.txt
    fir_complaint.txt
    legal_notice.txt
  utils/
    embeddings.py
    language_detector.py
    portal_links.py
    prompt_templates.py
  vector_store/
    documents.pkl
    tfidf_index.pkl
```

## Main Components

### `app.py`

The Streamlit entry point. It renders the UI, collects user queries, initializes the legal knowledge base, calls the agent pipeline, displays results, and provides report downloads.

### `agents/query_validator.py`

Checks whether the user query is related to Indian legal matters. It uses quick keyword checks first and falls back to Groq-based validation when needed.

### `agents/classifier.py`

Classifies the legal issue into a domain, sub-category, forum, urgency level, keywords, and hybrid domains.

### `agents/rag_retriever.py`

Retrieves relevant provisions from the local vector store and sends them to the LLM for legal analysis.

### `agents/guide_generator.py`

Generates the final step-by-step guide and creates downloadable PDF reports.

### `utils/embeddings.py`

Loads JSON legal data, builds a TF-IDF vector store, caches it under `vector_store/`, and performs cosine similarity search.

### `utils/language_detector.py`

Detects the query language using Unicode script detection and, when available, Groq-based language detection.

### `utils/portal_links.py`

Stores government portal links, e-FIR links, legal aid links, helpline numbers, and domain-specific resources.

## Legal Data Included

The local knowledge base includes JSON data for:

- Bharatiya Nyaya Sanhita 2023
- Bharatiya Nagarik Suraksha Sanhita 2023 procedures
- Consumer Protection Act 2019
- Information Technology Act 2000
- Constitution of India provisions

The app uses these files to build a searchable TF-IDF index. If `vector_store/tfidf_index.pkl` and `vector_store/documents.pkl` already exist, the app loads them directly. If they are missing, they are rebuilt from the files in `data/`.

## Prerequisites

- Python 3.10 or newer
- A Groq API key
- Internet access for Groq LLM requests

You can get a Groq API key from the Groq console.

## Setup

Open a terminal in the project folder:

```powershell
cd C:\Users\91901\Downloads\legal-aid-agent\legal-aid-agent
```

Create a virtual environment:

```powershell
python -m venv .venv
```

Activate the virtual environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
pip install -r requirements.txt
```

## Configure Groq API Key

The app reads the Groq key from the `GROQ_API_KEY` environment variable. You can set it before running the app:

```powershell
$env:GROQ_API_KEY="your_groq_api_key_here"
```

Alternatively, if the key is not set, the app shows a password input in the Streamlit sidebar where you can paste the key during runtime.

Note: `python-dotenv` is listed in `requirements.txt`, but the current code reads directly from environment variables and does not currently call `load_dotenv()`.

## Run the Application

Start the Streamlit app:

```powershell
streamlit run app.py
```

Streamlit will show a local URL similar to:

```text
http://localhost:8501
```

Open that URL in your browser.

## How to Use

1. Start the app with `streamlit run app.py`.
2. Enter your Groq API key in the sidebar if it is not already configured.
3. Choose one of the example legal issues or type your own issue.
4. Click `Get Legal Guidance`.
5. Review the generated output:
   - Case classification
   - Applicable legal provisions
   - AI legal analysis
   - Step-by-step action plan
   - Official portals and resources
   - Legal document templates
6. Download the report as PDF, Markdown, or plain text if needed.

## Example Queries

You can test the app with issues such as:

- Defective product or warranty refusal
- Online banking fraud or UPI fraud
- Cyberstalking or misuse of personal photos
- Landlord refusing to return security deposit
- Medical negligence
- Investment scam
- Airline refund or service deficiency
- Personal data breach

## Application Flow

```text
User query
  -> Language detection
  -> Legal/non-legal validation
  -> Legal domain classification
  -> Retrieval from local legal knowledge base
  -> LLM legal analysis
  -> Step-by-step guide generation
  -> Portal/template/report rendering
```

## Environment Variables

| Variable | Required | Description |
|---|---|---|
| `GROQ_API_KEY` | Yes | API key used by LangChain Groq to call `llama-3.3-70b-versatile`. |

## Dependencies

The required packages are listed in `requirements.txt`:

```text
streamlit>=1.31.0
langchain-groq>=0.0.1
pydantic>=2.5.0
python-dotenv>=1.0.0
fpdf2>=2.7.6
scikit-learn>=1.3.0
```

## Generated Outputs

The app can generate:

- On-screen legal analysis and action plan
- PDF legal aid report
- Markdown legal aid report
- Plain text legal aid report
- Legal notice template
- FIR complaint template
- Consumer complaint template

## Troubleshooting

### `Please enter your Groq API Key`

Set `GROQ_API_KEY` in your terminal or paste the key in the sidebar.

### `Invalid Groq API Key`

Check that the key is active and correctly copied from Groq.

### Rate limit error

Wait for the Groq rate limit window to reset, then retry.

### Failed to load legal knowledge base

Make sure the `data/` directory exists and contains the required JSON files. If the vector store files are corrupted, delete the files inside `vector_store/` and restart the app so they can be rebuilt.

### Streamlit command not found

Make sure dependencies are installed in the active virtual environment:

```powershell
pip install -r requirements.txt
```

### PowerShell script activation is blocked

If virtual environment activation is blocked by execution policy, run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

## Important Disclaimer

This project provides educational legal information only. It does not create an advocate-client relationship and does not constitute legal advice. Users should consult a qualified advocate or legal services authority for advice specific to their facts and jurisdiction.

## Possible Improvements

- Add `.env` loading through `python-dotenv`.
- Add automated tests for the classifier, retriever, and language detector.
- Add source citations with exact document IDs in generated reports.
- Add admin tools to update and rebuild the legal knowledge base.
- Improve encoding consistency for multilingual UI text.
- Add Docker support for simpler deployment.
- Add deployment instructions for Streamlit Community Cloud or other hosting platforms.
