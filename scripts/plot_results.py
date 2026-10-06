from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import json,argparse
import matplotlib.pyplot as plt
p=argparse.ArgumentParser();p.add_argument("--input",default="results/benchmark.json");p.add_argument("--out",default="results/hallucination_rates.png");a=p.parse_args(); d=json.load(open(a.input));
plt.figure();plt.bar(["Before validation","After validation"],[d["hallucination_rate_before"],d["hallucination_rate_after"]]);plt.ylabel("Hallucination rate");plt.tight_layout();plt.savefig(a.out,dpi=160)
