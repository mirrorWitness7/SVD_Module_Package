# svd_filter.py
from dataclasses import dataclass
import re

@dataclass
class SVDDecision:
    mode: str
    rationale: str

def decide_mode(user_text: str) -> SVDDecision:
    t = user_text.lower()
    if any(w in t for w in ['idiot', 'stupid']):
        return SVDDecision('EC', 'de-escalate ad-hominem heat')
    if 'donate' in t or 'moral' in t:
        return SVDDecision('RR', 'convert moral frame to process')
    if 'proof' in t or 'document' in t:
        return SVDDecision('ED', 'request falsifiable artifacts')
    if 'anyway' in t or 'unrelated' in t:
        return SVDDecision('SC', 'contain scope to remit')
    return SVDDecision('EC', 'acknowledge affect then redirect')

def svd_reply(decision: SVDDecision, context='process'):
    if decision.mode == 'EC':
        return f"[SVD: EC — {decision.rationale}]\nI hear the emotion; let’s anchor on specifics."
    if decision.mode == 'RR':
        return f"[SVD: RR — {decision.rationale}]\nThat’s an ethical stance; this channel moves on {context}."
    if decision.mode == 'ED':
        return f"[SVD: ED — {decision.rationale}]\nPlease provide concrete artifacts to proceed."
    if decision.mode == 'SC':
        return f"[SVD: SC — {decision.rationale}]\nOut of scope here. I can handle A/B; open a new thread for others."
