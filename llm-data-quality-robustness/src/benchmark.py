import json,time,statistics
from pathlib import Path
from .validators import MultiStageValidator
from .metrics import hallucination_rate

def run_benchmark(path:str):
    rows=[json.loads(x) for x in Path(path).read_text().splitlines() if x.strip()]
    v=MultiStageValidator(); out=[]; lat=[]
    for r in rows:
        t=time.perf_counter(); res=v.validate(r["reference"],r["answer"],r.get("valid_sources",[])); lat.append((time.perf_counter()-t)*1000)
        out.append({**r,"passed":res.passed,"validation_score":res.score,"reasons":res.reasons})
    before=hallucination_rate(rows); accepted=[x for x in out if x["passed"]]; after=hallucination_rate(accepted)
    return {"samples":len(rows),"accepted":len(accepted),"hallucination_rate_before":before,"hallucination_rate_after":after,"mean_validation_ms":statistics.mean(lat) if lat else 0,"records":out}
