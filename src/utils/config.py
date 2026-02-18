from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def load_config(config_path: str | Path) -> dict[str, Any]:
    """Load configuration from a YAML-compatible JSON file."""
    path = Path(config_path)
    if not path.exists():
        raise FileNotFoundError(f"Config file not found: {path}")

    content = path.read_text(encoding="utf-8")
    loaded = json.loads(content)

    if not isinstance(loaded, dict):
        raise ValueError("Config root must be a dictionary/object")

    return loaded
