from models.result_schema import MatchResultSchema

def calculate_weighted_score(analysis: MatchResultSchema) -> float:
    """
    Computes a predictable final matching score using strict business logic weights.
    Weights: Skills (50%), Projects (20%), Experience (15%), Education (10%), Certs (5%)
    """
    weighted_score = (
        (analysis.skill_score * 0.50) +
        (analysis.project_score * 0.20) +
        (analysis.experience_score * 0.15) +
        (analysis.education_score * 0.10) +
        (analysis.certification_score * 0.05)
    )
    return round(weighted_score, 1)