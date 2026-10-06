# LLM Data Quality & Robustness Evaluation Framework
An evaluation pipeline for detecting hallucination and fidelity failures, applying selective validation, and quantifying the trade-off between quality, acceptance rate, and latency.

## Pipeline
`JSONL benchmark -> fidelity/citation checks -> multi-stage gate -> accepted/rejected outputs -> aggregate metrics -> visualization`

## Included functionality
- semantic fidelity scoring
- citation/source validation
- hallucination-rate aggregation
- configurable multi-stage quality gate
- JSONL benchmark runner
- persisted result artifacts and plotting script
- deterministic tests suitable for CI

## Reproduce
```bash
pip install -e .
python scripts/run_benchmark.py
python scripts/plot_results.py
pytest -q
```

## Dataset format
Each JSONL record contains `reference`, `answer`, `valid_sources`, and a benchmark `hallucinated` label. Replace the included miniature fixture with your full evaluation dataset without changing the pipeline.

## Resume results
The resume reports analysis across 20K+ samples, a 30% hallucination reduction, +18% semantic fidelity, and sub-second inference. These are **reported experiment results from the original project**. The sample fixture is intentionally tiny and exists to reproduce system behavior, not to manufacture the reported benchmark. Run the same scripts against the original 20K+ benchmark to regenerate production metrics.

## Production path
For a full benchmark, plug in embedding-based semantic similarity (SentenceTransformers), NLI/entailment checks, LLM-as-judge with calibration, factuality datasets (e.g. TruthfulQA-style records), bootstrap confidence intervals, and per-domain slices.
