![status](https://img.shields.io/badge/desafio%20T%C3%A9cnico%20Ita%C3%BA-orange?style=for-the-badge)

# TransacaoFinanceira

Case técnico para refatoração e implementação de regras de transferência financeira.

## Informações do desafio

Este projeto implementa um fluxo de transferências entre contas com foco em:

- correção de erros de execução e inconsistências de saldo
- organização de código com boas práticas
- testes unitários para cenários de sucesso e falha
- execução concorrente com controle de seção crítica

## Objetivos atendidos

1. Correção dos problemas de compilação e execução.
2. Ajuste das regras de transferência para impedir inconsistência de saldo.
3. Refatoração da estrutura para melhorar legibilidade e manutenção.
4. Implementação de testes unitários para os fluxos principais.
5. Configuração de ambiente de testes e cobertura no pyproject.

## Tecnologias utilizadas

- Python 3.14
- pytest
- pytest-cov
- Poetry
- Visual Studio Code
- Git e GitHub

## Como executar

1. Instale as dependências.

```bash
poetry install
```

2. Execute a aplicação.

```bash
python -m src.main
```

## Como rodar os testes

```bash
poetry install --with dev
```

```bash
pytest -xvv
```

Com cobertura:

```bash
pytest --cov=src --cov-report=term-missing
```

## Regras de negócio validadas

- transferência com saldo suficiente é efetivada
- conta de origem inexistente cancela a transação
- conta de destino inexistente cancela a transação
- saldo insuficiente cancela a transação
- atualização de conta inexistente lança exceção

## Observações

- O projeto possui execução concorrente com ThreadPoolExecutor.
- A atualização de saldo é protegida por lock para evitar condição de corrida.
- A configuração de cobertura ignora arquivos de teste.
