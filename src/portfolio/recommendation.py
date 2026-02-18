from __future__ import annotations

from datetime import datetime, timezone
from typing import Any


def generate_mock_recommendation() -> dict[str, Any]:
    """Return a mock portfolio recommendation payload for demo mode."""
    return {
        "carteira_alvo": "Global Multi-Asset Growth",
        "pesos": {
            "US Equities": 0.35,
            "Developed ex-US Equities": 0.20,
            "Emerging Markets Equities": 0.10,
            "Global Bonds": 0.25,
            "Gold": 0.05,
            "Cash": 0.05,
        },
        "justificativa_simulada": (
            "Alocação mock para demonstrar saída do sistema, "
            "equilibrando crescimento global, diversificação regional "
            "e proteção defensiva."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
