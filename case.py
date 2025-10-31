import json

# Dados de exemplo
perfil_cliente = {
    "perfil": "Moderado",
    "score_max_risco": 2.5
}

carteira_atual = [
    {"ativo": "CDB XPTO", "risco": 1.2, "valor_investido": 50000},
    {"ativo": "Ação ABC", "risco": 4.0, "valor_investido": 10000}
]

nova_ordem_compra = {
    "ativo": "FII YYY",
    "risco": 3.5,
    "valor_ordem": 5000
}

# Risco médio ponderado da carteira atual
def calcular_risco_carteira(carteira):
    total_investido = sum(ativo["valor_investido"] for ativo in carteira)
    soma_ponderada = sum(ativo["risco"] * ativo["valor_investido"] for ativo in carteira)
    return soma_ponderada / total_investido

# Risco médio ponderado após uma nova compra
def calcular_risco_projetado(carteira, nova_ordem):
    total_investido = sum(ativo["valor_investido"] for ativo in carteira) + nova_ordem["valor_ordem"]
    soma_ponderada = sum(ativo["risco"] * ativo["valor_investido"] for ativo in carteira)
    soma_ponderada += nova_ordem["risco"] * nova_ordem["valor_ordem"]
    return soma_ponderada / total_investido


# Validação da nova compra, verifica se está dentro do limite de risco do cliente
def motor_validacao_suitability(perfil, carteira, nova_ordem):
    risco_atual = calcular_risco_carteira(carteira)
    risco_projetado = calcular_risco_projetado(carteira, nova_ordem)
    limite_alerta = perfil["score_max_risco"] * 1.1

    if risco_projetado <= perfil["score_max_risco"]:
        status = "Aprovado"
        mensagem = "Ordem executada. Carteira em conformidade."
    elif risco_projetado <= limite_alerta:
        status = "Alerta"
        mensagem = f"Atenção: o risco projetado ({risco_projetado:.2f}) ultrapassa o limite de {limite_alerta:.2f}. É necessário termo de ciência."
    else:
        status = "Rejeitado"
        mensagem = "Risco excessivo. A operação viola a política de Suitability."

    resultado = {
        "status": status,
        "risco_projetado": round(risco_projetado, 2),
        "mensagem": mensagem
    }

    print(json.dumps(resultado, indent=4))

# Execução do programa
if __name__ == "__main__":
     
    print("\nCaso Aprovado")
    nova_ordem_compra = {"ativo": "CDB Conservador", "risco": 1.0, "valor_ordem": 3000}
    motor_validacao_suitability(perfil_cliente, carteira_atual, nova_ordem_compra)

    print("\nCaso Alerta")
    nova_ordem_compra = {"ativo": "FII Moderado", "risco": 3.5, "valor_ordem": 5000}
    motor_validacao_suitability(perfil_cliente, carteira_atual, nova_ordem_compra)

    print("\nCaso Rejeitado")
    nova_ordem_compra = {"ativo": "Cripto Ativo XYZ", "risco": 5.0, "valor_ordem": 30000}
    motor_validacao_suitability(perfil_cliente, carteira_atual, nova_ordem_compra)
