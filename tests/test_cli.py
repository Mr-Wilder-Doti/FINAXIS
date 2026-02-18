from cli import run_demo


def test_run_demo_executes_without_error() -> None:
    output = run_demo("configs/config.yaml")

    assert "carteira_alvo" in output
    assert "pesos" in output
    assert "justificativa_simulada" in output
    assert "timestamp" in output
