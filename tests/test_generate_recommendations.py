from recommendation_robot.application.use_cases.generate_recommendations import (
    GenerateRecommendations,
)
from recommendation_robot.domain.entities.recommendation import Recommendation
from recommendation_robot.infrastructure.repositories.in_memory_recommendation_repository import (
    InMemoryRecommendationRepository,
)


def test_generate_recommendations_filters_by_user() -> None:
    repository = InMemoryRecommendationRepository(
        recommendations=[
            Recommendation(user_id="u-1", item_id="i-1", score=0.95),
            Recommendation(user_id="u-2", item_id="i-2", score=0.75),
        ]
    )
    use_case = GenerateRecommendations(repository=repository)

    result = use_case.execute("u-1")

    assert len(result) == 1
    assert result[0].item_id == "i-1"
