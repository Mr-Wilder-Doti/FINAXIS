"""Repository contract for recommendation persistence/read operations."""

from abc import ABC, abstractmethod

from recommendation_robot.domain.entities.recommendation import Recommendation


class RecommendationRepository(ABC):
    """Defines required repository operations for recommendations."""

    @abstractmethod
    def list_by_user(self, user_id: str) -> list[Recommendation]:
        """Return recommendations for the given user."""
