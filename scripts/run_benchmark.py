from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import json,argparse
from src.benchmark import run_benchmark
p=argparse.ArgumentParser(); p.add_argument("--data",default="data/sample_benchmark.jsonl"); p.add_argument("--out",default="results/benchmark.json"); a=p.parse_args()
r=run_benchmark(a.data); from pathlib import Path; Path(a.out).parent.mkdir(exist_ok=True); Path(a.out).write_text(json.dumps(r,indent=2)); print(json.dumps({k:v for k,v in r.items() if k!="records"},indent=2))
