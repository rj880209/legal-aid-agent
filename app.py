import os
import sys
import base64
import streamlit as st

sys.path.insert(0, os.path.dirname(__file__))

st.set_page_config(
    page_title="Legal Aid Agent — India",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded",
)

_FLAG_SVG_RAW = (
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 600">'
    '<rect width="900" height="200" fill="#FF9933"/>'
    '<rect y="200" width="900" height="200" fill="#FFFFFF"/>'
    '<rect y="400" width="900" height="200" fill="#138808"/>'
    '<circle cx="450" cy="300" r="90" fill="none" stroke="#000088" stroke-width="7"/>'
    '<circle cx="450" cy="300" r="10" fill="#000088"/>'
    '<g stroke="#000088" stroke-width="3.5">'
    '<line x1="450" y1="210" x2="450" y2="390"/>'
    '<line x1="362" y1="255" x2="538" y2="345"/>'
    '<line x1="362" y1="345" x2="538" y2="255"/>'
    '<line x1="360" y1="300" x2="540" y2="300"/>'
    '<line x1="387" y1="225" x2="513" y2="375"/>'
    '<line x1="387" y1="375" x2="513" y2="225"/>'
    '<line x1="420" y1="212" x2="480" y2="388"/>'
    '<line x1="420" y1="388" x2="480" y2="212"/>'
    '<line x1="363" y1="270" x2="537" y2="330"/>'
    '<line x1="363" y1="330" x2="537" y2="270"/>'
    '<line x1="376" y1="244" x2="524" y2="356"/>'
    '<line x1="376" y1="356" x2="524" y2="244"/>'
    '</g>'
    '<g fill="#000088">'
    '<circle cx="450" cy="210" r="5"/><circle cx="450" cy="390" r="5"/>'
    '<circle cx="362" cy="255" r="5"/><circle cx="538" cy="345" r="5"/>'
    '<circle cx="362" cy="345" r="5"/><circle cx="538" cy="255" r="5"/>'
    '<circle cx="360" cy="300" r="5"/><circle cx="540" cy="300" r="5"/>'
    '<circle cx="387" cy="225" r="5"/><circle cx="513" cy="375" r="5"/>'
    '<circle cx="387" cy="375" r="5"/><circle cx="513" cy="225" r="5"/>'
    '<circle cx="420" cy="212" r="5"/><circle cx="480" cy="388" r="5"/>'
    '<circle cx="420" cy="388" r="5"/><circle cx="480" cy="212" r="5"/>'
    '<circle cx="363" cy="270" r="5"/><circle cx="537" cy="330" r="5"/>'
    '<circle cx="363" cy="330" r="5"/><circle cx="537" cy="270" r="5"/>'
    '<circle cx="376" cy="244" r="5"/><circle cx="524" cy="356" r="5"/>'
    '<circle cx="376" cy="356" r="5"/><circle cx="524" cy="244" r="5"/>'
    '</g></svg>'
)
_FLAG_B64 = base64.b64encode(_FLAG_SVG_RAW.encode()).decode()
_FLAG_DATA_URL = f"data:image/svg+xml;base64,{_FLAG_B64}"

def _flag_img(w=54, h=36):
    return (
        f'<img src="{_FLAG_DATA_URL}" width="{w}" height="{h}" '
        f'style="border-radius:3px;box-shadow:0 1px 4px rgba(0,0,0,0.35);vertical-align:middle;">'
    )

st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {{ font-family: 'Inter', sans-serif; }}

/* ─── Page background ─── */
.main .block-container {{
    padding-top: 1rem;
    background: #f4f6fb;
}}

/* ─── Hero header ─── */
.hero-banner {{
    background: linear-gradient(120deg, #0a1f44 0%, #0d2d6e 55%, #0f3460 100%);
    border-radius: 14px;
    padding: 28px 36px 24px;
    margin-bottom: 6px;
    position: relative;
    overflow: hidden;
    box-shadow: 0 4px 24px rgba(10,31,68,0.18);
}}
.hero-banner::before {{
    content: "⚖";
    position: absolute;
    right: 32px; top: 50%;
    transform: translateY(-50%);
    font-size: 9rem;
    opacity: 0.06;
    line-height: 1;
}}
.hero-top {{ display:flex; align-items:center; gap:18px; margin-bottom:12px; }}
.hero-title {{
    color: #FFFFFF;
    font-size: 2.05rem;
    font-weight: 800;
    letter-spacing: -0.3px;
    margin: 0;
    line-height: 1.2;
}}
.hero-title span {{ color: #FF9933; }}
.hero-sub {{
    color: #9bb8e8;
    font-size: 0.88rem;
    margin: 4px 0 0;
    letter-spacing: 0.2px;
}}

/* ─── Tricolor stripe ─── */
.tricolor {{
    display: flex;
    height: 5px;
    border-radius: 0 0 4px 4px;
    overflow: hidden;
    margin-bottom: 20px;
}}
.tc-s {{ background:#FF9933; flex:1; }}
.tc-w {{ background:#FFFFFF; flex:1; }}
.tc-g {{ background:#138808; flex:1; }}

/* ─── Act pills in hero ─── */
.act-pills {{ display:flex; flex-wrap:wrap; gap:8px; margin-top:14px; }}
.act-pill {{
    background: rgba(255,255,255,0.1);
    border: 1px solid rgba(255,255,255,0.2);
    color: #c8d8f5;
    border-radius: 20px;
    padding: 3px 12px;
    font-size: 0.75rem;
    font-weight: 500;
    backdrop-filter: blur(4px);
}}

/* ─── Section titles ─── */
.sec-title {{
    display: flex;
    align-items: center;
    gap: 9px;
    color: #0a1f44;
    font-size: 1.05rem;
    font-weight: 700;
    margin: 20px 0 12px;
    padding-bottom: 8px;
    border-bottom: 2px solid #e8eef8;
}}
.sec-title .sec-dot {{
    width: 4px; height: 22px;
    background: #FF9933;
    border-radius: 3px;
    display: inline-block;
}}

/* ─── Example query buttons ─── */
.stButton > button {{
    border-radius: 8px !important;
    font-size: 0.84rem !important;
    font-weight: 500 !important;
    transition: all 0.15s ease !important;
    border: 1.5px solid #dde4f0 !important;
    background: #ffffff !important;
    color: #2c3e6b !important;
}}
.stButton > button:hover {{
    border-color: #FF9933 !important;
    color: #FF9933 !important;
    background: #fff8f0 !important;
    transform: translateY(-1px);
    box-shadow: 0 3px 10px rgba(255,153,51,0.12) !important;
}}
.stButton > button[kind="primary"] {{
    background: linear-gradient(90deg, #0a1f44, #1a3a7c) !important;
    color: #ffffff !important;
    border: none !important;
    font-weight: 700 !important;
    font-size: 0.95rem !important;
    letter-spacing: 0.2px !important;
    box-shadow: 0 3px 12px rgba(10,31,68,0.22) !important;
}}
.stButton > button[kind="primary"]:hover {{
    background: linear-gradient(90deg, #FF9933, #e67e22) !important;
    color: #ffffff !important;
    box-shadow: 0 4px 16px rgba(255,153,51,0.35) !important;
    transform: translateY(-1px) !important;
}}

/* ─── Input area ─── */
.stTextArea textarea {{
    border: 2px solid #dde4f0 !important;
    border-radius: 10px !important;
    font-size: 0.93rem !important;
    background: #ffffff !important;
    transition: border-color 0.2s;
}}
.stTextArea textarea:focus {{
    border-color: #0d2d6e !important;
    box-shadow: 0 0 0 3px rgba(13,45,110,0.08) !important;
}}

/* ─── Domain badges ─── */
.domain-badge {{
    display: inline-flex; align-items: center; gap: 6px;
    padding: 5px 13px; border-radius: 20px; font-size: 0.8rem;
    font-weight: 600; border: 1.5px solid; margin: 3px;
}}
.db-criminal  {{ background:#fff0f0; color:#c0392b; border-color:#e74c3c; }}
.db-consumer  {{ background:#fff9e6; color:#b7770d; border-color:#f39c12; }}
.db-civil     {{ background:#eaf4ff; color:#1a5276; border-color:#2980b9; }}
.db-const     {{ background:#eafaf1; color:#1e8449; border-color:#27ae60; }}
.db-cyber     {{ background:#f5eaff; color:#7d3c98; border-color:#8e44ad; }}

/* ─── Info card (provision) ─── */
.prov-card {{
    background: #ffffff;
    border: 1px solid #e0e8f5;
    border-left: 4px solid #0d2d6e;
    border-radius: 10px;
    padding: 14px 18px;
    margin-bottom: 12px;
    box-shadow: 0 1px 6px rgba(10,31,68,0.05);
}}
.prov-card-title {{ font-weight: 700; color: #0a1f44; font-size: 0.95rem; }}
.prov-card-act   {{ color: #7f8c9a; font-size: 0.76rem; margin: 2px 0 6px; font-style: italic; }}
.prov-card-desc  {{ color: #444; font-size: 0.87rem; line-height: 1.65; }}
.penalty-tag {{
    display: inline-block; margin-top: 8px;
    background: #fdecea; color: #c0392b;
    border-radius: 5px; padding: 3px 10px;
    font-size: 0.78rem; font-weight: 600;
}}

/* ─── Non-legal error ─── */
.nl-error {{
    background: linear-gradient(135deg, #fff8f0, #fef3e2);
    border: 1.5px solid #f0a040;
    border-left: 6px solid #FF9933;
    border-radius: 12px;
    padding: 24px 28px;
    margin: 16px 0;
}}
.nl-error h3 {{ color: #b7510a; font-size: 1.1rem; margin: 0 0 10px; }}
.nl-error p  {{ color: #5a4a3a; line-height: 1.65; margin: 0 0 8px; }}
.nl-error ul {{ color: #444; margin: 8px 0 0 20px; line-height: 1.8; }}

/* ─── Metric cards ─── */
[data-testid="stMetric"] {{
    background: #ffffff;
    border: 1px solid #e0e8f5;
    border-radius: 10px;
    padding: 12px 16px !important;
    box-shadow: 0 1px 5px rgba(10,31,68,0.06);
}}
[data-testid="stMetricLabel"] {{ color: #7f8c9a !important; font-size: 0.78rem !important; font-weight: 600 !important; text-transform: uppercase; letter-spacing: 0.4px; }}
[data-testid="stMetricValue"] {{ color: #0a1f44 !important; font-size: 1.05rem !important; font-weight: 700 !important; }}

/* ─── Sidebar ─── */
[data-testid="stSidebar"] {{
    background: #ffffff !important;
    border-right: 1px solid #e0e8f5 !important;
}}
[data-testid="stSidebar"] .stMarkdown {{ color: #2c3e6b; }}

/* ─── Expander ─── */
[data-testid="stExpander"] {{
    border: 1px solid #e0e8f5 !important;
    border-radius: 10px !important;
    background: #ffffff !important;
}}

/* ─── Download buttons ─── */
[data-testid="stDownloadButton"] button {{
    background: #f0f4ff !important;
    color: #0a1f44 !important;
    border: 1.5px solid #b0c4e8 !important;
    border-radius: 8px !important;
    font-weight: 600 !important;
}}
[data-testid="stDownloadButton"] button:hover {{
    background: #0a1f44 !important;
    color: #ffffff !important;
    border-color: #0a1f44 !important;
}}

/* ─── Status / progress ─── */
[data-testid="stStatusWidget"] {{ border-radius: 10px !important; }}

/* ─── Divider ─── */
hr {{ border-color: #e8eef8 !important; margin: 1.2rem 0 !important; }}

/* ─── Helpline rows ─── */
.helpline-row {{
    display: flex; justify-content: space-between; align-items: center;
    padding: 6px 10px; border-radius: 7px; margin-bottom: 4px;
    background: #f4f6fb;
}}
.helpline-name {{ color: #2c3e6b; font-size: 0.82rem; }}
.helpline-num  {{ color: #0a1f44; font-weight: 800; font-size: 0.9rem; }}

/* ─── Footer disclaimer ─── */
.footer-bar {{
    background: #0a1f44;
    color: #9bb8e8;
    border-radius: 10px;
    padding: 12px 20px;
    font-size: 0.78rem;
    text-align: center;
    margin-top: 24px;
    line-height: 1.7;
}}
</style>
""", unsafe_allow_html=True)

from agents.classifier import classify_query
from agents.rag_retriever import analyze_with_rag
from agents.guide_generator import generate_guide, get_portals_for_domain, generate_pdf_report
from agents.query_validator import validate_legal_query
from utils.portal_links import PORTAL_LINKS, STATE_EFIR_PORTALS
from utils.embeddings import build_vector_store
from utils.language_detector import detect_language


EXAMPLE_QUERIES = [
    ("🛒 Defective Product", "I bought a refrigerator from an online store for Rs. 45,000. It stopped working after 2 weeks. The company is refusing to replace it despite a 1-year warranty. I have the invoice and warranty card."),
    ("💻 Online Fraud", "Someone called me pretending to be from my bank and asked for my OTP. They transferred Rs. 85,000 from my account. This happened 3 days ago. I have the transaction details and call recordings."),
    ("📱 Cyberstalking", "My ex-partner is constantly sending threatening messages on WhatsApp and Instagram, creating fake profiles in my name, and posting my photos without consent. This has been going on for 2 months."),
    ("🏠 Property Dispute", "My landlord is refusing to return my security deposit of Rs. 1.5 lakh after I vacated the flat. He claims there was damage but I have photos showing it was in good condition when I left."),
    ("🏥 Medical Negligence", "The hospital performed the wrong surgery on my father and now his condition has worsened. The doctors are denying any mistake. We have the medical records and discharge summary."),
    ("📊 Financial Fraud", "A company promised 30% monthly returns on investment. I invested Rs. 2 lakhs. Now they are unreachable and their office is closed. Other investors are also affected."),
    ("✈️ Service Deficiency", "My flight was cancelled without prior notice. The airline is refusing to refund the ticket cost of Rs. 25,000 or provide any compensation. I have the booking confirmation."),
    ("🔐 Data Privacy Breach", "My personal data including Aadhaar and bank details were leaked by an app I used. I am now receiving phishing calls daily. I have screenshots of the data that was leaked."),
]

DOMAIN_META = {
    "Criminal":      ("🔴", "db-criminal"),
    "Consumer":      ("🟡", "db-consumer"),
    "Civil":         ("🔵", "db-civil"),
    "Constitutional":("🟢", "db-const"),
    "Hybrid":        ("🟠", "db-cyber"),
}

URGENCY_META = {
    "High":   ("🚨", "#c0392b", "#fdecea"),
    "Medium": ("⚠️", "#b7770d", "#fef9e7"),
    "Low":    ("ℹ️", "#1e8449", "#eafaf1"),
}


def init_session_state():
    for key, default in [
        ("conversation_history", []),
        ("vector_store_ready", False),
        ("current_result", None),
        ("query_input", ""),
        ("non_legal_error", None),
        ("detected_language", None),
    ]:
        if key not in st.session_state:
            st.session_state[key] = default


@st.cache_resource(show_spinner=False)
def initialize_vector_store():
    return build_vector_store()


def render_header():
    st.markdown(f"""
    <div class="hero-banner">
      <div class="hero-top">
        {_flag_img(54, 36)}
        <div>
          <div class="hero-title">⚖️ Legal Aid Agent <span>for India</span></div>
          <div class="hero-sub">Your AI-powered legal companion for Indian citizens</div>
        </div>
      </div>
      <div class="act-pills">
        <span class="act-pill">📜 Bharatiya Nyaya Sanhita 2023</span>
        <span class="act-pill">📋 BNSS 2023</span>
        <span class="act-pill">🛒 Consumer Protection Act 2019</span>
        <span class="act-pill">💻 IT Act 2000</span>
        <span class="act-pill">🏛️ Constitution of India</span>
      </div>
    </div>
    <div class="tricolor"><div class="tc-s"></div><div class="tc-w"></div><div class="tc-g"></div></div>
    """, unsafe_allow_html=True)


def render_sidebar():
    with st.sidebar:
        st.markdown(f"""
        <div style='text-align:center; padding:16px 0 10px;'>
          {_flag_img(72, 48)}
          <div style='margin-top:10px; font-size:1.05rem; font-weight:800; color:#0a1f44;'>Legal Aid Agent</div>
          <div style='font-size:0.76rem; color:#7f8c9a; margin-top:3px;'>Powered by Groq AI · For Indian Citizens</div>
        </div>
        """, unsafe_allow_html=True)

        st.divider()

        api_key = os.environ.get("GROQ_API_KEY", "")
        if not api_key:
            st.error("⚠️ Groq API Key Required")
            entered_key = st.text_input(
                "Enter Groq API Key:",
                type="password",
                placeholder="gsk_...",
                help="Get your free key at console.groq.com",
            )
            if entered_key:
                os.environ["GROQ_API_KEY"] = entered_key
                st.success("✅ Connected!")
                st.rerun()
        else:
            st.markdown("""
            <div style='background:#eafaf1; border:1.5px solid #27ae60; border-radius:8px;
                        padding:9px 14px; color:#1e8449; font-weight:600; font-size:0.85rem;'>
              ✅ Groq AI Connected
            </div>""", unsafe_allow_html=True)

        st.divider()
        st.markdown('<div style="font-weight:700; color:#0a1f44; font-size:0.88rem; margin-bottom:8px;">📚 Legal Domains Covered</div>', unsafe_allow_html=True)

        domains = [
            ("db-criminal",  "🔴", "Criminal", "BNS 2023"),
            ("db-consumer",  "🟡", "Consumer", "CP Act 2019"),
            ("db-civil",     "🔵", "Civil",     "Property & Contract"),
            ("db-const",     "🟢", "Constitutional", "Writs & FRs"),
            ("db-cyber",     "🟣", "Cyber Crime", "IT Act 2000"),
        ]
        for cls, icon, name, sub in domains:
            st.markdown(f"""
            <div class="domain-badge {cls}" style="margin-bottom:5px; width:100%; box-sizing:border-box;">
              {icon} <span>{name}</span> <span style="font-weight:400; opacity:0.7; font-size:0.73rem;">— {sub}</span>
            </div>""", unsafe_allow_html=True)

        st.divider()
        st.markdown('<div style="font-weight:700; color:#0a1f44; font-size:0.88rem; margin-bottom:8px;">🆘 Emergency Helplines</div>', unsafe_allow_html=True)

        helplines = [
            ("🚔 Police Emergency", "100"),
            ("👩 Women Helpline", "1091"),
            ("💻 Cyber Crime", "1930"),
            ("🛒 Consumer NCH", "1915"),
            ("⚖️ Free Legal Aid", "15100"),
            ("👶 Child Helpline", "1098"),
            ("🚑 Medical Emergency", "108"),
        ]
        for name, num in helplines:
            st.markdown(f"""
            <div class="helpline-row">
              <span class="helpline-name">{name}</span>
              <span class="helpline-num">{num}</span>
            </div>""", unsafe_allow_html=True)

        st.divider()
        if st.session_state.conversation_history:
            if st.button("🗑️ Clear Session", use_container_width=True):
                st.session_state.conversation_history = []
                st.session_state.current_result = None
                st.session_state.non_legal_error = None
                st.rerun()

        st.markdown("""
        <div style='margin-top:16px; background:#f4f6fb; border-radius:8px; padding:10px 12px;
                    font-size:0.74rem; color:#7f8c9a; line-height:1.6;'>
          ⚠️ <strong>Disclaimer:</strong> This tool provides educational legal information only.
          Always consult a qualified advocate for advice specific to your situation.
        </div>""", unsafe_allow_html=True)


def sec(icon, title):
    st.markdown(f"""
    <div class="sec-title">
      <span class="sec-dot"></span>{icon} {title}
    </div>""", unsafe_allow_html=True)


def render_non_legal_error(error_info: dict):
    category = error_info.get("category", "Non-legal topic")
    message  = error_info.get("message", "")
    st.markdown(f"""
    <div class="nl-error">
      <h3>⛔ Query Outside Legal Scope</h3>
      <p>Your query appears to be about: <strong>{category}</strong>.<br>
      {message}</p>
      <p><strong>This Legal Aid Agent handles:</strong></p>
      <ul>
        <li>🔴 <strong>Criminal matters</strong> — FIR, bail, BNS 2023 offences, harassment</li>
        <li>🟡 <strong>Consumer disputes</strong> — defective products, refunds, e-commerce fraud</li>
        <li>🔵 <strong>Civil issues</strong> — property, rent, contract, divorce, family law</li>
        <li>🟢 <strong>Constitutional rights</strong> — fundamental rights, writs, PIL, discrimination</li>
        <li>🟣 <strong>Cyber crimes</strong> — online fraud, hacking, identity theft, stalking</li>
        <li>💰 <strong>Financial fraud</strong> — banking fraud, investment scams, cheque bounce</li>
      </ul>
      <p style="margin-top:12px; font-size:0.85rem; color:#8a7060;">
        Please describe a legal issue you are facing and we will guide you step by step.
      </p>
    </div>
    """, unsafe_allow_html=True)


def render_example_queries():
    sec("💡", "Common Legal Issues — Click to Try")
    cols = st.columns(4)
    for i, (label, query) in enumerate(EXAMPLE_QUERIES):
        with cols[i % 4]:
            if st.button(label, use_container_width=True, key=f"ex_{i}"):
                st.session_state.query_input = query
                st.session_state.non_legal_error = None
                st.rerun()


def process_query(user_query: str):
    result = {}
    with st.status("🔍 Analyzing your legal issue...", expanded=True) as status:

        st.write("🌐 Detecting language...")
        lang = detect_language(user_query)
        st.session_state.detected_language = lang
        lang_instruction = lang["instruction"]
        lang_display = lang["native"] if lang["code"] != "en" else "English"
        st.write(f"✅ Language detected: **{lang['name']}** ({lang_display})")

        st.write("🛡️ Validating query scope...")
        validation = validate_legal_query(user_query, lang_instruction)
        if not validation["is_legal"]:
            status.update(label="⚠️ Query Outside Legal Scope", state="error", expanded=False)
            return {"non_legal": True, "error_info": validation}

        st.write("📂 Classifying legal domain...")
        classification = classify_query(user_query)
        result["classification"] = classification
        st.write(f"✅ **{classification.get('domain')}** domain · Forum: **{classification.get('forum')}**")

        st.write("📖 Retrieving applicable legal provisions...")
        provisions, laws_analysis = analyze_with_rag(
            user_query, classification.get("domain", "Civil"), lang_instruction
        )
        result["provisions"] = provisions
        result["laws_analysis"] = laws_analysis
        st.write(f"✅ Found **{len(provisions)}** relevant legal provisions")

        st.write("📋 Generating your step-by-step action plan...")
        guide = generate_guide(user_query, classification, laws_analysis, lang_instruction)
        result["guide"] = guide
        result["portals"] = get_portals_for_domain(classification.get("domain", ""), classification)
        result["language"] = lang
        st.write("✅ Action plan is ready!")

        status.update(label="✅ Legal Analysis Complete", state="complete", expanded=False)
    return result


def render_language_badge(lang: dict):
    if not lang or lang.get("code") == "en":
        return
    name   = lang.get("name", "")
    native = lang.get("native", "")
    st.markdown(f"""
    <div style="display:inline-flex; align-items:center; gap:8px;
                background:linear-gradient(90deg,#FF9933,#138808);
                border-radius:20px; padding:5px 16px; margin-bottom:12px;">
      <span style="font-size:1.1rem;">🌐</span>
      <span style="color:#fff; font-weight:700; font-size:0.88rem;">
        Responding in {name} &nbsp;·&nbsp; {native}
      </span>
    </div>
    """, unsafe_allow_html=True)


def render_classification(classification: dict, lang: dict = None):
    domain      = classification.get("domain", "N/A")
    forum       = classification.get("forum", "N/A")
    urgency     = classification.get("urgency", "Medium")
    sub_cat     = classification.get("sub_category", "N/A")
    keywords    = classification.get("keywords", [])

    icon, _   = DOMAIN_META.get(domain, ("⚪", "db-civil"))
    u_icon, u_color, u_bg = URGENCY_META.get(urgency, ("ℹ️", "#1e8449", "#eafaf1"))

    if lang:
        render_language_badge(lang)

    sec("📊", "Case Classification")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Legal Domain", f"{icon} {domain}")
    c2.metric("Appropriate Forum", forum)
    c3.metric("Issue Category", sub_cat)
    c4.metric("Urgency", f"{u_icon} {urgency}")

    if keywords:
        pills = "".join([
            f'<span style="background:#eef2ff;border:1px solid #c0ccf0;color:#1a3580;'
            f'border-radius:14px;padding:3px 11px;font-size:0.78rem;margin:3px 3px 0 0;display:inline-block;">{k}</span>'
            for k in keywords
        ])
        st.markdown(f'<div style="margin-top:10px;"><span style="font-size:0.82rem;color:#7f8c9a;font-weight:600;">KEY ISSUES</span><br>{pills}</div>', unsafe_allow_html=True)


def render_provisions(provisions: list, laws_analysis: str):
    sec("⚖️", "Applicable Legal Provisions")

    with st.expander("📜 View Retrieved Legal Sections", expanded=True):
        for prov in provisions:
            sid   = prov.get("section") or prov.get("article", "Unknown")
            title = prov.get("title", "")
            act   = prov.get("act", "")
            desc  = prov.get("description", "")
            pen   = prov.get("penalty", "")
            rel   = min(prov.get("relevance_score", 0) * 100, 99)

            col1, col2 = st.columns([5, 1])
            with col1:
                st.markdown(f"""
                <div class="prov-card">
                  <div class="prov-card-title">📌 {sid} — {title}</div>
                  <div class="prov-card-act">{act}</div>
                  <div class="prov-card-desc">{desc[:340]}{"..." if len(desc) > 340 else ""}</div>
                  {"<div class='penalty-tag'>⚖️ Penalty: " + pen + "</div>" if pen else ""}
                </div>""", unsafe_allow_html=True)
            with col2:
                st.metric("Match", f"{rel:.0f}%")

    sec("🧠", "AI Legal Analysis")
    st.markdown(laws_analysis)


def render_guide(guide: str):
    sec("📋", "Your Step-by-Step Legal Action Plan")
    st.markdown(guide)


def render_portals(portals: dict):
    if not portals:
        return
    sec("🔗", "Official Portals & Government Resources")
    items = list(portals.items())
    cols  = st.columns(3)
    for i, (name, url) in enumerate(items):
        with cols[i % 3]:
            if url.startswith("http"):
                st.markdown(f"🔗 [{name}]({url})")
            else:
                st.markdown(f"📞 **{name}**: `{url}`")


def render_templates(classification: dict):
    domain = classification.get("domain", "")
    forum  = classification.get("forum", "")
    sec("📝", "Legal Document Templates")
    tdir = os.path.join(os.path.dirname(__file__), "templates")
    c1, c2, c3 = st.columns(3)

    def _dl(col, label, fname, path):
        fp = os.path.join(tdir, path)
        if os.path.exists(fp):
            with open(fp) as f:
                data = f.read()
            with col:
                st.download_button(label, data=data, file_name=fname, mime="text/plain", use_container_width=True)

    _dl(c1, "📄 Legal Notice Template", "legal_notice_template.txt", "legal_notice.txt")
    if "Criminal" in domain or "Police" in forum:
        _dl(c2, "🚔 FIR Complaint Template", "fir_complaint_template.txt", "fir_complaint.txt")
    if "Consumer" in domain:
        _dl(c3, "🛒 Consumer Complaint", "consumer_complaint_template.txt", "consumer_complaint.txt")


def render_state_portals():
    with st.expander("🗺️ State-wise Police & e-FIR Portals"):
        cols  = st.columns(4)
        items = list(STATE_EFIR_PORTALS.items())
        n     = -(-len(items) // 4)
        for i, col in enumerate(cols):
            with col:
                for state, url in items[i * n:(i + 1) * n]:
                    st.markdown(f"🔗 [{state}]({url})")


def render_downloads(result: dict):
    cl         = result["classification"]
    query      = result.get("query", "")
    guide      = result.get("guide", "")
    provisions = result.get("provisions", [])
    analysis   = result.get("laws_analysis", "")
    portals    = result.get("portals", {})
    domain     = cl.get("domain", "N/A")
    forum      = cl.get("forum", "N/A")
    urgency    = cl.get("urgency", "N/A")
    sub_cat    = cl.get("sub_category", "N/A")
    keywords   = ", ".join(cl.get("keywords", []))
    timestamp  = __import__("datetime").datetime.now().strftime("%d %b %Y, %I:%M %p")

    st.markdown("""
    <div style="
        background: linear-gradient(135deg, #0a1f44 0%, #0d2d6e 100%);
        border-radius: 14px;
        padding: 28px 32px 24px;
        margin: 8px 0 4px;
        box-shadow: 0 4px 20px rgba(10,31,68,0.18);
    ">
      <div style="display:flex; align-items:center; gap:12px; margin-bottom:6px;">
        <span style="font-size:2rem;">📥</span>
        <div>
          <div style="color:#ffffff; font-size:1.15rem; font-weight:800; letter-spacing:-0.2px;">
            Download Your Complete Legal Report
          </div>
          <div style="color:#9bb8e8; font-size:0.82rem; margin-top:3px;">
            Includes your issue summary, case classification, all legal provisions,
            AI analysis, step-by-step action plan, portals &amp; helplines
          </div>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)

    lang        = result.get("language", {})
    language_name = lang.get("name", "English") if lang else "English"

    with c1:
        with st.spinner("Building PDF..."):
            pdf = generate_pdf_report(
                query=query,
                classification=cl,
                guide=guide,
                provisions=provisions,
                laws_analysis=analysis,
                portals=portals,
                language_name=language_name,
            )
        if pdf:
            st.download_button(
                label="📄 Full Report (PDF)",
                data=pdf,
                file_name="legal_aid_report.pdf",
                mime="application/pdf",
                use_container_width=True,
                help="Complete report with all sections — provisions, analysis, guide, portals & helplines",
            )
        else:
            st.warning("PDF generation failed. Try the text downloads below.")

    with c2:
        prov_lines = ""
        for i, p in enumerate(provisions, 1):
            sid  = p.get("section") or p.get("article", "")
            act  = p.get("act", "")
            desc = p.get("description", "")
            pen  = p.get("penalty", "")
            prov_lines += (
                f"\n### {i}. {sid} — {p.get('title','')}\n"
                f"**Act:** {act}\n\n{desc}\n"
                + (f"\n**Penalty:** {pen}\n" if pen else "") + "\n"
            )

        portal_lines = "\n".join(
            f"- [{n}]({u})" if u.startswith("http") else f"- **{n}:** {u}"
            for n, u in portals.items()
        ) if portals else ""

        md = f"""# Legal Aid Report — India
*Generated by Legal Aid Agent | {timestamp}*

---

## Your Legal Issue
{query}

---

## Case Classification
| Field | Value |
|---|---|
| **Legal Domain** | {domain} |
| **Sub-Category** | {sub_cat} |
| **Appropriate Forum** | {forum} |
| **Urgency** | {urgency} |
| **Key Issues** | {keywords} |

---

## Applicable Legal Provisions
{prov_lines}

---

## AI Legal Analysis
{analysis}

---

## Step-by-Step Legal Action Plan
{guide}

---

## Official Portals & Resources
{portal_lines}

---

## Emergency Helplines
| Helpline | Number |
|---|---|
| Police Emergency | 100 |
| Women Helpline | 1091 |
| Cyber Crime | 1930 |
| Consumer NCH | 1915 |
| Free Legal Aid | 15100 |
| Child Helpline | 1098 |
| Medical Emergency | 108 |

---

> ⚠️ **Disclaimer:** This report is for educational purposes only and does not constitute legal advice.
> Always consult a qualified advocate for advice specific to your situation.
"""
        st.download_button(
            label="📝 Full Guide (Markdown)",
            data=md,
            file_name="legal_aid_report.md",
            mime="text/markdown",
            use_container_width=True,
            help="Complete report in Markdown — open in any text editor or Notion",
        )

    with c3:
        txt = f"""LEGAL AID REPORT — INDIA
Generated by Legal Aid Agent | {timestamp}
{'='*60}

YOUR LEGAL ISSUE
{'-'*40}
{query}

CASE CLASSIFICATION
{'-'*40}
Legal Domain    : {domain}
Sub-Category    : {sub_cat}
Forum           : {forum}
Urgency         : {urgency}
Key Issues      : {keywords}

APPLICABLE LEGAL PROVISIONS
{'-'*40}
"""
        for i, p in enumerate(provisions, 1):
            sid  = p.get("section") or p.get("article", "")
            desc = p.get("description", "")
            pen  = p.get("penalty", "")
            txt += (
                f"\n{i}. {sid} — {p.get('title','')} [{p.get('act','')}]\n"
                f"   {desc[:300]}{'...' if len(desc)>300 else ''}\n"
                + (f"   Penalty: {pen}\n" if pen else "")
            )

        txt += f"""
{'='*60}
AI LEGAL ANALYSIS
{'-'*40}
{analysis}

{'='*60}
STEP-BY-STEP LEGAL ACTION PLAN
{'-'*40}
{guide}

{'='*60}
OFFICIAL PORTALS
{'-'*40}
"""
        for name, url in portals.items():
            txt += f"  {name}: {url}\n"

        txt += f"""
EMERGENCY HELPLINES
{'-'*40}
  Police Emergency  : 100
  Women Helpline    : 1091
  Cyber Crime       : 1930
  Consumer NCH      : 1915
  Free Legal Aid    : 15100
  Child Helpline    : 1098
  Medical Emergency : 108

{'='*60}
DISCLAIMER: This report is for educational purposes only and does
not constitute legal advice. Consult a qualified advocate for your
specific situation.
"""
        st.download_button(
            label="📋 Plain Text (.txt)",
            data=txt,
            file_name="legal_aid_report.txt",
            mime="text/plain",
            use_container_width=True,
            help="Simple plain-text version — works everywhere, easy to print or share",
        )


def render_footer():
    st.markdown("""
    <div class="footer-bar">
      ⚖️ <strong>Legal Aid Agent for India</strong> &nbsp;|&nbsp;
      Powered by <strong>Groq AI</strong> (llama-3.3-70b-versatile) &nbsp;|&nbsp;
      Covers <strong>BNS 2023 · BNSS 2023 · Consumer Protection Act · IT Act · Constitution of India</strong><br>
      <span style="font-size:0.72rem;">⚠️ This platform provides educational legal information only and does not constitute legal advice.
      Consult a qualified advocate for your specific situation.</span>
    </div>
    """, unsafe_allow_html=True)


def main():
    init_session_state()
    render_header()
    render_sidebar()

    with st.spinner("Loading legal knowledge base..."):
        try:
            initialize_vector_store()
            st.session_state.vector_store_ready = True
        except Exception as e:
            st.error(f"Failed to load legal knowledge base: {e}")

    render_example_queries()
    st.divider()

    sec("📝", "Describe Your Legal Issue")
    st.markdown('<div style="font-size:0.85rem; color:#7f8c9a; margin:-8px 0 10px;">Provide details about your situation — the more context you give, the more precise the guidance will be.</div>', unsafe_allow_html=True)

    user_query = st.text_area(
        label="Legal Issue",
        value=st.session_state.query_input,
        placeholder=(
            "Example: My landlord has not returned my security deposit of Rs. 2 lakhs even after "
            "6 months of vacating the flat. He is ignoring my calls and messages. I have the rent "
            "agreement and bank transfer receipts as evidence..."
        ),
        height=130,
        label_visibility="collapsed",
    )

    c1, c2 = st.columns([4, 1])
    with c1:
        submit = st.button("🔍 Get Legal Guidance", type="primary", use_container_width=True)
    with c2:
        if st.button("🗑️ Clear", use_container_width=True):
            st.session_state.query_input = ""
            st.session_state.current_result = None
            st.session_state.non_legal_error = None
            st.rerun()

    api_key = os.environ.get("GROQ_API_KEY", "")

    if submit:
        st.session_state.non_legal_error = None
        st.session_state.current_result  = None
        query = user_query.strip()
        if not query:
            st.warning("⚠️ Please describe your legal issue before submitting.")
        elif len(query) < 20:
            st.warning("⚠️ Please provide more details (minimum 20 characters).")
        elif not api_key:
            st.error("🔑 Please enter your Groq API Key in the sidebar to proceed.")
        else:
            try:
                result = process_query(query)
                if result.get("non_legal"):
                    st.session_state.non_legal_error = result["error_info"]
                else:
                    result["query"] = query
                    st.session_state.current_result = result
                    st.session_state.conversation_history.append(result)
                    st.session_state.query_input = ""
            except Exception as e:
                err = str(e)
                if "api_key" in err.lower() or "authentication" in err.lower() or "401" in err:
                    st.error("🔑 Invalid Groq API Key. Please check your key in the sidebar.")
                elif "rate" in err.lower():
                    st.error("⏳ Rate limit reached. Please wait a moment and try again.")
                else:
                    st.error(f"An error occurred: {err}")

    if st.session_state.non_legal_error:
        render_non_legal_error(st.session_state.non_legal_error)

    if st.session_state.current_result:
        result = st.session_state.current_result
        st.divider()
        render_classification(result["classification"], result.get("language"))
        st.divider()
        render_provisions(result["provisions"], result["laws_analysis"])
        st.divider()
        render_guide(result["guide"])
        st.divider()
        render_portals(result["portals"])
        st.divider()
        render_templates(result["classification"])
        st.divider()
        render_state_portals()
        st.divider()
        render_downloads(result)

    if len(st.session_state.conversation_history) > 1:
        st.divider()
        sec("📜", "Previous Queries This Session")
        for i, hist in enumerate(reversed(st.session_state.conversation_history[:-1]), 1):
            preview = hist.get("query", "")[:80] + "..."
            domain  = hist["classification"].get("domain", "N/A")
            icon, _ = DOMAIN_META.get(domain, ("⚪", ""))
            with st.expander(f"{icon} Query {i}: {preview}  [{domain}]"):
                render_classification(hist["classification"])
                st.markdown(hist["guide"][:600] + "\n\n*— Full report available via Download button above*")

    render_footer()


if __name__ == "__main__":
    main()
