from dataclasses import dataclass
from .metrics import semantic_fidelity, citation_precision
@dataclass
class ValidationResult:
    passed: bool; score: float; reasons: list[str]
class MultiStageValidator:
    def __init__(self,min_fidelity=.55,min_citation_precision=.8): self.min_fidelity=min_fidelity; self.min_citation_precision=min_citation_precision
    def validate(self,reference,answer,valid_sources):
        f=semantic_fidelity(reference,answer); c=citation_precision(answer,set(valid_sources)); reasons=[]
        if f<self.min_fidelity: reasons.append("low_semantic_fidelity")
        if c<self.min_citation_precision: reasons.append("invalid_or_unsupported_citation")
        return ValidationResult(not reasons,round((f+c)/2,4),reasons)
