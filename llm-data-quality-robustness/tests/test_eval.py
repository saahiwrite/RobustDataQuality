from src.eval import *
def test_fidelity(): assert semantic_fidelity('a b c','a b')>.5
def test_eval():
 x=evaluate([{'context':'a b','reference':'a b','answer':'a b'}]); assert x['n']==1 and x['acceptance_rate']==1
