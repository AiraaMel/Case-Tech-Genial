# Motor de Validação de Suitability (CVM 30)

Case para demonstrar um motor de validação de suitability de carteira conforme a Resolução CVM nº 30. O motor calcula o risco médio ponderado da carteira antes e depois de uma nova ordem e classifica a operação como "Aprovado", "Alerta" ou "Rejeitado".

## Arquivos
- `case.py`: implementação em Python com três cenários (aprovado, alerta, rejeitado) e saída em JSON.
- `case-report.md`: relatório explicativo sobre requisitos regulatórios e considerações de negócio.

## Requisitos
- Python 3.8+ (testado localmente com Python 3.x)

## Como executar
- Python:
  - `python case.py`


A saída é impressa no terminal em formato JSON, com `status`, `risco_projetado` e `mensagem`.

## Personalização rápida
Edite os objetos de exemplo nos arquivos para simular diferentes cenários:
- Python (`case.py:1`): `perfil_cliente`, `carteira_atual`, `nova_ordem_compra`

## Observações
- O arquivo `case-report.md` traz detalhes sobre: registro de termo de ciência, logs de auditoria, LGPD e monitoramento de desenquadramento passivo.

## Desenvolvido por
**[AiraaMel](https://www.linkedin.com/in/aira-mel/)**