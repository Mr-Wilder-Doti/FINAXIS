from src.utils.config import load_config


def test_load_config_success() -> None:
    config = load_config("configs/config.yaml")

    assert config["environment"] == "dev"
    assert config["app"]["name"] == "global-portfolio-recommendation-bot"
