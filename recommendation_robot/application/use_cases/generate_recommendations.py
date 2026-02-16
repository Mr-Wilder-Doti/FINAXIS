"""Use case for recommendation generation."""

from recommendation_robot.domain.entities.recommendation import Recommendation
from recommendation_robot.domain.interfaces.recommendation_repository import (
    RecommendationRepository,
)


class GenerateRecommendations:
    """Orchestrates recommendation retrieval/generation workflow."""

    def __init__(self, repository: RecommendationRepository) -> None:
        self._repository = repository

    def execute(self, user_id: str) -> list[Recommendation]:
        """Return recommendations for a user."""
        return self._repository.list_by_user(user_id)
