"""Recommendation domain entity."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Recommendation:
    """Represents a recommendation generated for a user."""

    user_id: str
    item_id: str
    score: float
