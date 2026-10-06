from difflib import SequenceMatcher
import re

def semantic_fidelity(reference:str, answer:str)->float:
    return SequenceMatcher(None, reference.lower(), answer.lower()).ratio()
def citation_precision(answer:str, valid_sources:set[str])->float:
    cites=set(re.findall(r"\[(S\d+)\]",answer)); return 1.0 if not cites else len(cites & valid_sources)/len(cites)
def hallucination_rate(records:list[dict])->float:
    if not records:return 0.0
    return sum(bool(x.get("hallucinated")) for x in records)/len(records)
