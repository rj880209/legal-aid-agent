PORTAL_LINKS = {
    "consumer": {
        "e-Daakhil (Online Consumer Complaint)": "https://edaakhil.nic.in",
        "National Consumer Helpline (NCH)": "https://consumerhelpline.gov.in",
        "National Consumer Helpline Number": "1915",
        "NCDRC (National Consumer Disputes Redressal Commission)": "https://ncdrc.nic.in",
        "Consumer App (NCH Mobile)": "https://play.google.com/store/apps/details?id=co.in.consumerhelpline",
    },
    "cyber_crime": {
        "National Cyber Crime Reporting Portal": "https://cybercrime.gov.in",
        "Cyber Crime Helpline Number": "1930",
        "CERT-In (Cyber Emergency Response Team)": "https://cert-in.org.in",
        "RBI Banking Fraud Reporting": "https://sachet.rbi.org.in",
        "TRAI (Telecom Regulatory - Spam/Fraud Calls)": "https://trai.gov.in",
        "DoT - Sanchar Saathi (Lost/Stolen Mobile)": "https://sancharsaathi.gov.in",
    },
    "police_efir": {
        "Delhi Police e-FIR": "https://delhipolice.gov.in",
        "Maharashtra Police Citizen Portal": "https://citizen.mahapolice.gov.in",
        "Karnataka Police e-Lost Report": "https://ksp.karnataka.gov.in",
        "UP Police e-FIR / Complaint": "https://uppolice.gov.in",
        "Rajasthan Police": "https://police.rajasthan.gov.in",
        "Tamil Nadu Police": "https://eservices.tnpolice.gov.in",
        "Telangana Police": "https://www.tspolice.gov.in",
        "Gujarat Police": "https://police.gujarat.gov.in",
        "West Bengal Police": "https://wbpolice.gov.in",
    },
    "legal_aid": {
        "NALSA (National Legal Services Authority)": "https://nalsa.gov.in",
        "eCourts - Case Status": "https://ecourts.gov.in",
        "Supreme Court e-Filing": "https://efiling.sci.gov.in",
        "Vakalatnama / Legal Documents": "https://districts.ecourts.gov.in",
        "Tele-Law (Free Legal Advice)": "https://tele-law.in",
        "Pro Bono Legal Services": "https://nalsa.gov.in/lsams",
    },
    "constitutional": {
        "Supreme Court of India": "https://sci.gov.in",
        "High Court e-Filing (Delhi)": "https://delhihighcourt.nic.in",
        "High Court e-Filing (Bombay)": "https://bombayhighcourt.nic.in",
        "High Court e-Filing (Madras)": "https://hcmadras.tn.nic.in",
        "High Court e-Filing (Calcutta)": "https://calcuttahighcourt.gov.in",
        "PIL Filing Guidelines": "https://sci.gov.in/guidelines-for-filing-pil",
        "National Human Rights Commission (NHRC)": "https://nhrc.nic.in",
    },
    "civil": {
        "eCourts Services": "https://ecourts.gov.in",
        "LIMBS (Legal Information Management)": "https://limbs.gov.in",
        "NALSA Free Legal Aid": "https://nalsa.gov.in",
        "Mediation / Lok Adalat": "https://nalsa.gov.in/lok-adalat",
        "RTI Online Portal": "https://rtionline.gov.in",
    },
    "financial_fraud": {
        "RBI Ombudsman": "https://rbionlineodb.rbi.org.in",
        "SEBI SCORES (Investor Complaints)": "https://scores.sebi.gov.in",
        "IRDAI Bima Bharosa (Insurance Complaints)": "https://bimabharosa.irdai.gov.in",
        "Cyber Crime Portal (Financial Fraud)": "https://cybercrime.gov.in",
        "Banking Fraud Helpline": "1930",
        "UPI Fraud - NPCI": "https://www.npci.org.in/what-we-do/upi/dispute-redressal-mechanism",
    },
}

STATE_EFIR_PORTALS = {
    "Andhra Pradesh": "https://appolice.gov.in",
    "Assam": "https://assampolice.gov.in",
    "Bihar": "https://biharpolice.bih.nic.in",
    "Delhi": "https://delhipolice.gov.in",
    "Goa": "https://www.goapolice.gov.in",
    "Gujarat": "https://police.gujarat.gov.in",
    "Haryana": "https://haryanapolice.gov.in",
    "Himachal Pradesh": "https://hppolice.gov.in",
    "Jharkhand": "https://jhpolice.gov.in",
    "Karnataka": "https://ksp.karnataka.gov.in",
    "Kerala": "https://keralapolice.gov.in",
    "Madhya Pradesh": "https://mppolice.gov.in",
    "Maharashtra": "https://citizen.mahapolice.gov.in",
    "Odisha": "https://odishapolice.gov.in",
    "Punjab": "https://punjabpolice.gov.in",
    "Rajasthan": "https://police.rajasthan.gov.in",
    "Tamil Nadu": "https://eservices.tnpolice.gov.in",
    "Telangana": "https://www.tspolice.gov.in",
    "Uttar Pradesh": "https://uppolice.gov.in",
    "Uttarakhand": "https://uttarakhandpolice.uk.gov.in",
    "West Bengal": "https://wbpolice.gov.in",
}


def get_relevant_portals(domain: str) -> dict:
    domain_lower = domain.lower()
    portals = {}

    if "consumer" in domain_lower:
        portals.update(PORTAL_LINKS["consumer"])
    if "criminal" in domain_lower or "cyber" in domain_lower:
        portals.update(PORTAL_LINKS["cyber_crime"])
        portals.update(PORTAL_LINKS["police_efir"])
    if "constitutional" in domain_lower:
        portals.update(PORTAL_LINKS["constitutional"])
        portals.update(PORTAL_LINKS["legal_aid"])
    if "civil" in domain_lower:
        portals.update(PORTAL_LINKS["civil"])
    if "financial" in domain_lower or "fraud" in domain_lower or "bank" in domain_lower:
        portals.update(PORTAL_LINKS["financial_fraud"])

    portals.update(PORTAL_LINKS["legal_aid"])
    return portals
