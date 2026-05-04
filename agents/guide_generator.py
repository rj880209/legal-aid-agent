import os
import re
from datetime import datetime
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage
from utils.prompt_templates import GUIDE_PROMPT
from utils.portal_links import get_relevant_portals, PORTAL_LINKS


def get_llm():
    api_key = os.environ.get("GROQ_API_KEY", "")
    return ChatGroq(
        groq_api_key=api_key,
        model_name="llama-3.3-70b-versatile",
        temperature=0.2,
        max_tokens=2048,
    )


def generate_guide(
    query: str,
    classification: dict,
    laws_analysis: str,
    language_instruction: str = "Respond in English.",
) -> str:
    llm          = get_llm()
    domain       = classification.get("domain", "Civil")
    sub_category = classification.get("sub_category", "General")
    forum        = classification.get("forum", "District Court")
    urgency      = classification.get("urgency", "Medium")

    prompt = GUIDE_PROMPT.format(
        language_instruction=language_instruction,
        query=query,
        domain=domain,
        sub_category=sub_category,
        forum=forum,
        urgency=urgency,
        laws=laws_analysis,
    )
    messages = [
        SystemMessage(content=(
            "You are a compassionate legal aid assistant for Indian citizens. "
            "Provide clear, actionable guidance. Use simple language. "
            "Always include specific portal links and helpline numbers. "
            "Never give wrong legal advice - be accurate with section numbers. "
            + language_instruction
        )),
        HumanMessage(content=prompt),
    ]
    return get_llm().invoke(messages).content


def get_portals_for_domain(domain: str, classification: dict) -> dict:
    portals  = get_relevant_portals(domain)
    keywords = classification.get("keywords", [])
    for kw in keywords:
        kw_lower = kw.lower()
        if any(x in kw_lower for x in ["bank", "upi", "financial", "money", "payment"]):
            portals.update(PORTAL_LINKS["financial_fraud"])
        if any(x in kw_lower for x in ["online", "cyber", "internet", "digital"]):
            portals.update(PORTAL_LINKS["cyber_crime"])
    return portals


# ── PDF helpers ────────────────────────────────────────────────────────────────

_UNICODE_REPLACE = {
    "\u2014": "-",   "\u2013": "-",   "\u2018": "'",   "\u2019": "'",
    "\u201c": '"',   "\u201d": '"',   "\u2022": "*",   "\u2023": "*",
    "\u25cf": "*",   "\u25cb": "o",   "\u2713": "OK",  "\u2714": "OK",
    "\u2715": "x",   "\u2716": "x",   "\u00a0": " ",   "\u20b9": "Rs.",
    "\u2026": "...",
}

def _safe(text: str) -> str:
    """Strip markdown and sanitise to Latin-1 safe characters."""
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
    text = re.sub(r"\*(.+?)\*",     r"\1", text)
    text = re.sub(r"#+\s*",         "",    text)
    text = re.sub(r"`(.+?)`",       r"\1", text)
    for src, dst in _UNICODE_REPLACE.items():
        text = text.replace(src, dst)
    return text.encode("latin-1", errors="replace").decode("latin-1").strip()


def generate_pdf_report(
    query: str,
    classification: dict,
    guide: str,
    provisions: list = None,
    laws_analysis: str = "",
    portals: dict = None,
    language_name: str = "English",
) -> bytes:
    try:
        from fpdf import FPDF, XPos, YPos

        provisions = provisions or []
        portals    = portals    or {}

        SAFFRON = (255, 153,  51)
        NAVY    = ( 10,  31,  68)
        GREEN   = ( 19, 136,   8)
        WHITE   = (255, 255, 255)
        LGRAY   = (242, 244, 248)
        MGRAY   = (120, 130, 150)
        DTEXT   = ( 40,  40,  60)

        generated = datetime.now().strftime("%d %b %Y, %I:%M %p")
        lang_note = f"Response Language: {language_name}" if language_name != "English" else ""

        class PDF(FPDF):
            def header(self):
                self.set_fill_color(*NAVY)
                self.rect(0, 0, 210, 16, "F")
                self.set_font("Helvetica", "B", 11)
                self.set_text_color(*WHITE)
                self.set_xy(10, 3)
                self.cell(130, 10, "Legal Aid Agent for India", align="L")
                self.set_font("Helvetica", size=8)
                self.set_xy(0, 3)
                self.cell(0, 10, f"Generated: {generated}  ", align="R")
                self.set_fill_color(*SAFFRON); self.rect(0,  16, 70, 2.5, "F")
                self.set_fill_color(*WHITE);   self.rect(70, 16, 70, 2.5, "F")
                self.set_fill_color(*GREEN);   self.rect(140,16, 70, 2.5, "F")
                self.set_text_color(*DTEXT)
                self.set_xy(self.l_margin, 22)

            def footer(self):
                self.set_y(-12)
                self.set_fill_color(*NAVY)
                self.rect(0, self.get_y(), 210, 12, "F")
                self.set_font("Helvetica", size=7)
                self.set_text_color(*MGRAY)
                self.cell(
                    0, 12,
                    "Disclaimer: Educational purposes only. Not legal advice. "
                    "Consult a qualified advocate.   |   Page " + str(self.page_no()),
                    align="C",
                )

        def heading(pdf, text):
            x, y = pdf.get_x(), pdf.get_y()
            pdf.set_fill_color(*SAFFRON)
            pdf.rect(x, y, 3.5, 8, "F")
            pdf.set_xy(x + 6, y)
            pdf.set_font("Helvetica", "B", 12)
            pdf.set_text_color(*NAVY)
            pdf.cell(0, 8, _safe(text), new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            pdf.set_draw_color(*NAVY)
            pdf.set_line_width(0.2)
            pdf.line(pdf.get_x(), pdf.get_y(), pdf.get_x() + 180, pdf.get_y())
            pdf.ln(3)

        def kv_row(pdf, label, value, shade=False):
            if shade:
                pdf.set_fill_color(*LGRAY)
                pdf.rect(pdf.get_x(), pdf.get_y(), 180, 7, "F")
            pdf.set_font("Helvetica", "B", 9)
            pdf.set_text_color(*NAVY)
            pdf.cell(50, 7, _safe(label))
            pdf.set_font("Helvetica", size=9)
            pdf.set_text_color(*DTEXT)
            pdf.cell(0, 7, _safe(str(value)), new_x=XPos.LMARGIN, new_y=YPos.NEXT)

        def body_text(pdf, text, size=9, indent=0):
            pdf.set_font("Helvetica", size=size)
            pdf.set_text_color(*DTEXT)
            lm = pdf.l_margin + indent
            for raw in _safe(text).split("\n"):
                line = raw.strip()
                if not line:
                    pdf.set_x(lm)
                    pdf.ln(2)
                    continue
                is_step   = bool(re.match(r"^(Step\s*\d+|STEP\s*\d+|\d+\.)\s", line, re.I))
                is_bullet = line[:1] in ("-", "*", "+")
                # Always reset x to left margin before any multi_cell
                pdf.set_x(lm)
                if is_step:
                    pdf.set_font("Helvetica", "B", size)
                    pdf.set_text_color(*NAVY)
                    pdf.multi_cell(0, 5.5, line)
                    pdf.set_x(lm)
                    pdf.set_font("Helvetica", size=size)
                    pdf.set_text_color(*DTEXT)
                elif is_bullet:
                    body = "- " + line.lstrip("-*+[ ] ").strip()
                    pdf.set_x(lm + 3)
                    pdf.multi_cell(0, 5.5, body)
                else:
                    pdf.multi_cell(0, 5.5, line)

        pdf = PDF()
        pdf.set_margins(15, 26, 15)
        pdf.set_auto_page_break(auto=True, margin=16)
        pdf.add_page()

        pdf.set_font("Helvetica", "B", 22)
        pdf.set_text_color(*NAVY)
        pdf.cell(0, 12, "Legal Aid Report", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.set_font("Helvetica", size=9)
        pdf.set_text_color(*MGRAY)
        pdf.cell(
            0, 6,
            "Powered by Groq AI  |  BNS 2023  |  BNSS 2023  |  Consumer Protection Act  |  IT Act  |  Constitution of India",
            align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT,
        )
        if lang_note:
            pdf.set_font("Helvetica", "I", 8)
            pdf.set_text_color(13, 45, 110)
            pdf.cell(0, 6, lang_note, align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.ln(8)

        heading(pdf, "1.  Your Legal Issue")
        pdf.set_fill_color(*LGRAY)
        pdf.set_font("Helvetica", size=9)
        pdf.set_text_color(*DTEXT)
        pdf.multi_cell(0, 6, _safe(query), fill=True)
        pdf.ln(6)

        heading(pdf, "2.  Case Classification")
        kv_row(pdf, "Legal Domain:",      classification.get("domain", "N/A"),        shade=False)
        kv_row(pdf, "Sub-Category:",      classification.get("sub_category", "N/A"),  shade=True)
        kv_row(pdf, "Appropriate Forum:", classification.get("forum", "N/A"),         shade=False)
        kv_row(pdf, "Urgency Level:",     classification.get("urgency", "N/A"),       shade=True)
        kv_row(pdf, "Key Issues:",        ", ".join(classification.get("keywords", [])) or "N/A", shade=False)
        pdf.ln(6)

        if provisions:
            heading(pdf, "3.  Applicable Legal Provisions")
            for i, prov in enumerate(provisions):
                sid   = _safe(prov.get("section") or prov.get("article", ""))
                title = _safe(prov.get("title", ""))
                act   = _safe(prov.get("act", ""))
                desc  = _safe(prov.get("description", ""))
                pen   = _safe(prov.get("penalty", ""))
                rel   = min(int(prov.get("relevance_score", 0) * 100), 99)
                pdf.set_fill_color(*LGRAY)
                pdf.rect(pdf.get_x(), pdf.get_y(), 180, 7, "F")
                pdf.set_font("Helvetica", "B", 9)
                pdf.set_text_color(*NAVY)
                pdf.multi_cell(0, 7, f"{i+1}. {sid} - {title}  [{act}]  (Match: {rel}%)")
                if desc:
                    pdf.set_font("Helvetica", size=8)
                    pdf.set_text_color(*DTEXT)
                    pdf.set_x(pdf.l_margin + 4)
                    pdf.multi_cell(0, 5, desc[:450] + ("..." if len(desc) > 450 else ""))
                if pen:
                    pdf.set_font("Helvetica", "B", 8)
                    pdf.set_text_color(180, 40, 30)
                    pdf.set_x(pdf.l_margin + 4)
                    pdf.multi_cell(0, 5, f"Penalty: {pen}")
                    pdf.set_text_color(*DTEXT)
                pdf.ln(3)
            pdf.ln(3)

        if laws_analysis:
            heading(pdf, "4.  AI Legal Analysis")
            body_text(pdf, laws_analysis)
            pdf.ln(6)

        if guide:
            heading(pdf, "5.  Step-by-Step Legal Action Plan")
            body_text(pdf, guide)
            pdf.ln(6)

        if portals:
            heading(pdf, "6.  Official Portals & Resources")
            for i, (name, url) in enumerate(portals.items()):
                shade = (i % 2 == 0)
                if shade:
                    pdf.set_fill_color(*LGRAY)
                    pdf.rect(pdf.get_x(), pdf.get_y(), 180, 6.5, "F")
                pdf.set_font("Helvetica", "B", 9)
                pdf.set_text_color(*NAVY)
                pdf.cell(60, 6.5, f"  {_safe(name)}")
                pdf.set_font("Helvetica", size=8)
                pdf.set_text_color(13, 45, 110)
                try:
                    pdf.cell(0, 6.5, _safe(str(url)), new_x=XPos.LMARGIN, new_y=YPos.NEXT)
                except Exception:
                    pdf.cell(0, 6.5, "", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            pdf.ln(6)

        heading(pdf, "7.  Emergency Helplines")
        helplines = [
            ("Police Emergency",  "100"),
            ("Women Helpline",    "1091"),
            ("Cyber Crime",       "1930"),
            ("Consumer NCH",      "1915"),
            ("Free Legal Aid",    "15100"),
            ("Child Helpline",    "1098"),
            ("Medical Emergency", "108"),
        ]
        for i, (name, num) in enumerate(helplines):
            shade = (i % 2 == 0)
            if shade:
                pdf.set_fill_color(*LGRAY)
                pdf.rect(pdf.get_x(), pdf.get_y(), 180, 6.5, "F")
            pdf.set_font("Helvetica", size=9)
            pdf.set_text_color(*DTEXT)
            pdf.cell(100, 6.5, f"  {name}")
            pdf.set_font("Helvetica", "B", 9)
            pdf.set_text_color(*NAVY)
            pdf.cell(0, 6.5, num, new_x=XPos.LMARGIN, new_y=YPos.NEXT)

        return bytes(pdf.output())

    except Exception:
        import traceback
        traceback.print_exc()
        return b""
