"""Settings and environment configuration."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    """Core settings for the recommendation robot."""

    app_name: str = "recommendation-robot"
    environment: str = "development"
