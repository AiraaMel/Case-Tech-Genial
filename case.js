// Dados de exemplo
const perfilCliente = { perfil: "Moderado", score_max_risco: 2.5 };

const carteiraAtual = [
  { ativo: "CDB XPTO", risco: 1.2, valor_investido: 50000 },
  { ativo: "Ação ABC", risco: 4.0, valor_investido: 10000 }
];

const novaOrdemCompra = { ativo: "FII YYY", risco: 3.5, valor_ordem: 5000 };

// Função para calcular o risco atual da carteira
function calcularRiscoCarteira(carteira) {
  const totalInvestido = carteira.reduce(
    (totalAcumulado, ativoAtual) => totalAcumulado + ativoAtual.valor_investido, 0);
  const somaPonderada = carteira.reduce(
    (totalAcumulado, ativoAtual) => totalAcumulado + ativoAtual.risco * ativoAtual.valor_investido, 0);
  return somaPonderada / totalInvestido;
}

// Função para calcular o risco após uma nova compra
function calcularRiscoProjetado(carteira, novaOrdem) {
  const totalInvestido =
    carteira.reduce((totalAcumulado, ativoAtual) => totalAcumulado + ativoAtual.valor_investido, 0) + novaOrdem.valor_ordem;

  const somaPonderada =
    carteira.reduce(
      (totalAcumulado, ativoAtual) => totalAcumulado + ativoAtual.risco * ativoAtual.valor_investido, 0) + novaOrdem.risco * novaOrdem.valor_ordem;
  return somaPonderada / totalInvestido;
}

// Função principal do motor de validação
function motorValidacaoSuitability(perfil, carteira, novaOrdem) {
  const riscoProjetado = calcularRiscoProjetado(carteira, novaOrdem);
  const limiteAlerta = perfil.score_max_risco * 1.1;

  let status, mensagem;

  if (riscoProjetado <= perfil.score_max_risco) {
    status = "Aprovado";
    mensagem = "Ordem executada. Carteira em conformidade.";
  } else if (riscoProjetado <= limiteAlerta) {
    status = "Alerta";
    mensagem = `Atenção: o risco projetado (${riscoProjetado.toFixed(2)}) ultrapassa o limite de ${limiteAlerta.toFixed(2)}. É necessário termo de ciência.`;
  } else {
    status = "Rejeitado";
    mensagem = "Risco excessivo. A operação viola a política de Suitability.";
  }

  const resultado = {
    status,
    risco_projetado: parseFloat(riscoProjetado.toFixed(2)),
    mensagem
  };

  console.log(JSON.stringify(resultado, null, 4));
}

// Execução no terminal
motorValidacaoSuitability(perfilCliente, carteiraAtual, novaOrdemCompra);