from src.eval import evaluate
rows=[{'context':'Paris is the capital of France','reference':'Paris is the capital of France','answer':'Paris is the capital of France.'},{'context':'Water freezes at zero Celsius','reference':'Water freezes at zero Celsius','answer':'Water freezes at zero Celsius and turns purple.'}]
print(evaluate(rows))
