import re, math
def tokens(s): return set(re.findall(r"[a-z0-9]+",s.lower()))
def semantic_fidelity(reference,answer):
 a,b=tokens(reference),tokens(answer); return len(a&b)/max(1,len(a|b))
def unsupported_claim_rate(context,answer):
 c=tokens(context); claims=[x.strip() for x in re.split(r'[.!?]+',answer) if x.strip()]
 bad=sum(1 for x in claims if len(tokens(x)-c)>max(2,len(tokens(x))*0.5))
 return bad/max(1,len(claims))
def validate(context,reference,answer,threshold=.35):
 f=semantic_fidelity(reference,answer); h=unsupported_claim_rate(context,answer)
 return {'semantic_fidelity':round(f,4),'hallucination_risk':round(h,4),'accepted':f>=threshold and h<=.5}
def evaluate(rows):
 out=[validate(**r) for r in rows]; n=len(out)
 return {'n':n,'acceptance_rate':sum(x['accepted'] for x in out)/n,'mean_fidelity':sum(x['semantic_fidelity'] for x in out)/n,'mean_hallucination_risk':sum(x['hallucination_risk'] for x in out)/n}
