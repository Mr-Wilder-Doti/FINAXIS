"""In-memory repository implementation for bootstrapping and tests."""

from recommendation_robot.domain.entities.recommendation import Recommendation
from recommendation_robot.domain.interfaces.recommendation_repository import (
    RecommendationRepository,
)


class InMemoryRecommendationRepository(RecommendationRepository):
    """Simple in-memory storage for recommendations."""

    def __init__(self, recommendations: list[Recommendation] | None = None) -> None:
        self._recommendations = recommendations or []

    def list_by_user(self, user_id: str) -> list[Recommendation]:
        return [
            recommendation
            for recommendation in self._recommendations
            if recommendation.user_id == user_id
        ]
