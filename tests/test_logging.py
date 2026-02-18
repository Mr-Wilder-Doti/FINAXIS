import json

from src.utils.logging_config import configure_logging, log_event


def test_logging_structured_output(capfd) -> None:
    logger = configure_logging("INFO")
    log_event(logger, event="unit_test_event", module="tests")

    captured = capfd.readouterr().out.strip()
    envelope = json.loads(captured)
    message = json.loads(envelope["message"])

    assert message["event"] == "unit_test_event"
    assert message["module"] == "tests"
