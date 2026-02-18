from __future__ import annotations

import argparse
import json
from pathlib import Path

from src.portfolio.recommendation import generate_mock_recommendation
from src.utils.config import load_config
from src.utils.logging_config import configure_logging, log_event


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="global-portfolio-bot",
        description="CLI do robô de recomendação de carteira global.",
    )
    parser.add_argument(
        "command",
        choices=["run-demo"],
        help="Comando para executar um fluxo mock de recomendação.",
    )
    parser.add_argument(
        "--config",
        default="configs/config.yaml",
        help="Caminho para arquivo de configuração YAML.",
    )
    return parser


def run_demo(config_path: str) -> dict:
    logger = configure_logging()
    config = load_config(config_path)

    log_event(
        logger,
        event="demo_started",
        environment=config.get("environment", "unknown"),
        strategy=config.get("app", {}).get("strategy_name", "mock"),
    )

    recommendation = generate_mock_recommendation()

    log_event(logger, event="demo_finished", output_keys=list(recommendation.keys()))
    print(json.dumps(recommendation, ensure_ascii=False, indent=2))

    return recommendation


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "run-demo":
        run_demo(args.config)


if __name__ == "__main__":
    main()
