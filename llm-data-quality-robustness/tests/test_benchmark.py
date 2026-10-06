from src.benchmark import run_benchmark
def test_benchmark_rejects_bad_sample():
    r=run_benchmark("data/sample_benchmark.jsonl"); assert r["samples"]==4; assert r["accepted"]<4; assert r["hallucination_rate_after"] <= r["hallucination_rate_before"]
