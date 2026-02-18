# Global Portfolio Recommendation Bot (Base Skeleton)

Estrutura inicial de um robô de recomendação de carteira global com foco em **arquitetura limpa, modular e expansível**.

> Esta etapa implementa apenas o esqueleto funcional (sem lógica financeira real).

## Requisitos

- Python 3.11+

## Estrutura do Projeto

```text
.
├── cli.py
├── configs/
│   └── config.yaml
├── docs/
├── requirements.txt
├── src/
│   ├── api/
│   ├── backtest/
│   ├── data/
│   ├── features/
│   ├── models/
│   ├── portfolio/
│   │   └── recommendation.py
│   ├── risk/
│   └── utils/
│       ├── config.py
│       └── logging_config.py
└── tests/
    ├── test_cli.py
    ├── test_config.py
    └── test_logging.py
```

## Decisões de Design

1. **Separação por domínios técnicos**
   - `data`, `features`, `models`, `portfolio`, `risk`, `backtest` e `api` foram separados desde o início para permitir evolução independente de módulos.

2. **Configuração externa via `config.yaml`**
   - `configs/config.yaml` permite ajustar ambiente, logging e provedores sem alterar código.
   - Nesta base, o parser usa JSON válido salvo em `.yaml` para manter o bootstrap simples e sem dependências extras.

3. **Logging estruturado em JSON**
   - `src/utils/logging_config.py` centraliza configuração de logger com saída JSON em `stdout`, pronta para ingestão por ferramentas de observabilidade.

4. **CLI como ponto de entrada único**
   - `cli.py` organiza execução via comando (`run-demo`) e prepara terreno para novos subcomandos.

5. **Testes mínimos para contrato de base**
   - Garantimos carregamento de config, execução de CLI e emissão de logs estruturados para reduzir regressões iniciais.

## Instalação

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Execução

Rodar demo:

```bash
python cli.py run-demo
```

Com config customizada:

```bash
python cli.py run-demo --config configs/config.yaml
```

## Saída esperada (run-demo)

O comando imprime uma recomendação mock contendo:

- `carteira_alvo`
- `pesos`
- `justificativa_simulada`
- `timestamp`

## Testes

```bash
pytest -q
```

