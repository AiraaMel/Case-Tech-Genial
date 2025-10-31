# Case Report - Motor de Validação de Suitability de Carteira (CVM 30)

&emsp; A Resolução CVM nº 30 exige que as instituições financeiras assegurem que todos os produtos e operações sejam adequados ao perfil de risco do cliente. Isso significa que, antes de cada nova compra, a corretora deve verificar se o risco total da carteira continuará compatível com o nível máximo de risco tolerado.

&emsp; Para isso, foi desenvolvido um Motor de Validação de Suitability de Carteira, capaz de calcular o risco atual e o risco projetado da carteira, simulando a inclusão de um novo ativo.

## Regulação vs. Negócio

Se o cliente receber um alerta e optar por continuar com a compra (situação prevista pela CVM), a Genial deve:

- Registrar um Termo de Ciência Digital, confirmando que o cliente foi informado do risco adicional. Quando o cliente decide seguir com uma operação que ultrapassa o limite de risco, a CVM permite essa execução desde que haja registro formal dessa ciência. Isso garante transparência e protege a Genial legalmente.

- Salvar os dados no banco, como cliente, ativo, data e hora, score de risco. Após o cliente aceitar o risco, o sistema deve gravar essas informações em banco de dados, o que permite auditoria futura e facilita análises internas.

- Gerar logs de auditoria, permitindo rastrear quando e quem autorizou a operação. Essa prática, rastreia cada ação e detectar fraudes ou inconsistências, já que os logs são registros automáticos do sistema.

- Garantir conformidade com a LGPD, que exige que empresas tratem dados pessoais com segurança, necessidade e consentimento, armazenando apenas dados essenciais.

- Integrar o registro ao dashboard do assessor, para acompanhamento posterior, já que permite que o assessor monitore em tempo real os riscos dos clientes.

&emsp; Essas medidas exigem integração entre o motor de validação, o sistema de autenticação do cliente e a camada de banco de dados (API interna). O log de auditoria pode ser gravado com timestamps automáticos e IDs de transação, garantindo rastreabilidade.

## Desenquadramento Passivo

&emsp; O desenquadramento passivo ocorre quando o nível de risco da carteira de um cliente aumenta ssem que o cliente realize novas operações, geralmente devido à volatilidade do mercado financeiro.

&emsp; Por exemplo, uma ação ou fundo imobiliário que antes tinha risco 3.0 pode subir para 3.8 por causa de eventos econômicos. Mesmo que o cliente não compre nada novo, a carteira total pode ultrapassar o limite de risco permitido.

### Identificação automática

O motor de suitability desenvolvido pode ser reutilizado para esse monitoramento, a diferença é que ele não é ativado por uma compra, e sim por atualizações automáticas dos dados de mercado.

- Atualização diária de preços e riscos: o sistema coleta os novos riscos dos ativos, isso pode ser feito via APIs de mercado. Assim, cada ativo da carteira é atualizado com o risco mais recente.

- Reexecução automática do motor: o motor recalcula o risco médio ponderado da carteira com os novos valores. Se o risco projetado ultrapassar o limite do perfil, o sistema gera um alerta automático.

- Classificação de desenquadramento: o sistema envia alertas graduais, conforme a gravidade do desenquadramento. Com o nível normal, que apenas informa via log interno, o alerta leve, que solicita termo de ciência e o severo, que bloqueia novas compras até revisão.

**Comunicação com o cliente**

A comunicação deve ser proativa e clara, o cliente precisa saber que o risco da carteira mudou sem ação direta dele.

- App da Genial: notificações automáticas em tempo real, é uma comunicação rápida, digital e segura.

- E-mail: alerta formal e rastreável, mantém registro oficial da comunicação.

- Assessor de investimentos: em casos severos ou repetitivos, permite contato humano e explicação personalizada.

&emsp; Dessa forma, penalizações são evitadas por não monitorar carteiras fora do perfil e gera confiança do cliente, pois o investidor percebe que a Genial acompanha e avisa proativamente. Isso é possível devido à inovação tecnológica, que transforma o motor de suitability em um sistema dinâmico de risco em tempo real.

&emsp; Com isso, o monitoramento com níveis de aviso transforma o motor de suitability em um sistema preventivo, dinâmico e centrado no cliente.
Ele não apenas evita desenquadramentos, mas também reforça a imagem da Genial como uma instituição que combina compliance, inovação e cuidado com o investidor. 