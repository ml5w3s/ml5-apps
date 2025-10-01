
--- 
title: "Repasses"
created: "2025-02-26T14:58:30,804469Z"
updated: "2025-06-10T12:52:35,474505Z"
tags: []
--- 

Repasses

* versionamento
* documentação
* IDE
Tá familiarizado com esses termos?
Ah, criei uma conta lá esses dias na verdade, meu nome de usuário é lucasamarale
Boa tarde Lucas, conforme combinado tenho o MVP versão simplificada para produto viável mínimo.
Preciso validar para entrega, não tem nada a ver com as reuniões de desenvolvimento, que fazemos para você dominar o app.

wine /opt/ Tab415TabWin415.exe

        this.container
        this.data
        this.currentPage
        this.rowsPerPage

Data
Tipo
Procedimento
Quantidade
Valor pago (R$)
Valor Unitário Pago (R$)
Valor Unitário TUNEP/IVR (R$)
Valor Não Pago (R$)

Valor serviços hospitalares,
Val serv hosp
compl federal segundo
Procedimento
Período:

Procedimento
Valor serviços hospitalares
Val serv hosp - compl federal

Pontos para revisar
Integração CSV e processamento: 16-24h
Relatórios em PDF: 24-32h
Filtros: 12-16h
Dashboards: 16-24h
Permissões de usuário e níveis de acesso: 16-24h

complete: function(results)

POO

/projeto-hello
│── index.html
│── app.js
│── main.js
│── hello.js

documentação:
jsdoc -r ./js -d docs -t node_modules/minami

tunep_monumento_formato_numero.csv

Valor atualizado em dez/2021 (R$) = Diferença devida e não paga (R$) * Fator de atualização do CJF até dez/2021

Valor dos juros monetários até dez/2021 (R$) = Valor atualizado em dez/2021 (R$) * Juros Moratórios %

Valor atualização selic (R$) = (Valor atualizado em dez/2021 (R$) + Valor dos juros monetários até dez/2021 (R$)) * Taxa selic de dez/2021 até ago/2024

Valor total Devido em ago/2024 = Valor atualizado em dez/2021 (R$) + Valor 
os juros monetários até dez/2021 (R$) + Valor atualização selic (R$)

irmandade santa casa

Total IVR/Tunep = IVR/Tunep + Correção monetária

Criar uma página de ajustes, haverão as opções de ajuste da tabela, de acordo com o manual do tribunal ou personalização da selic, mora e fator de atualização

Novas colunas calculadas 

Formulário
Número do processo type="text"
Entidade type="text"
CNPJ type="text"
CNES type="number"

• Correção Monetária:
o De jan/1992 até dez/2000: UFIR;
o Até nov/2021: IPCA-E;
o Após nov/2021: SELIC.

• Juros Moratório:
o Até dez/2002: 0,5% ao mês;
o Até jun/2009: SELIC;
o Até abr/2012: 0,5% ao mês;
o Até nov/2021: juros da remuneração da caderneta de poupança;
o Após nov/2021: não incidência em razão da aplicação da SELIC

🗺️ Plano de Ação – Reestruturação com Padrões de Projeto
🎯 Objetivo Geral

Reestruturar o projeto de cálculo de correção monetária e juros com base em CSVs, adotando padrões de design, separação clara de responsabilidades, integração segura com APIs (ex: Bacen), e garantindo escalabilidade, testabilidade e documentação sólida.
🧩 Etapas, Objetivos e Estimativas
1. Planejamento e Reorganização Inicial

Objetivos:

    Consolidar objetivos técnicos e funcionais.

    Criar estrutura de pastas padronizada (ex: services/, core/, utils/, components/, etc).

    Identificar partes reutilizáveis do código antigo.

Estimativa: 1 dia
Branch: restructure/init
Checklist:

Criar repositório (ou nova branch principal refactor-base)

Mapear e classificar arquivos antigos

    Escrever README.md inicial com visão geral e objetivos do refatoramento

2. Criação do Core de Negócio

Objetivos:

    Criar classe principal de processamento (CSVProcessor)

    Criar classe de domínio MonetaryAdjustment com injeção de taxas

    Definir interfaces e abstrações (Strategy, Factory ou Service, conforme necessário)

Padrões aplicados:

    Strategy (para diferentes políticas de cálculo de juros e correção)

    Singleton ou Service Layer (para acesso a dados de taxas)

    Factory (para instanciação de objetos de cálculo baseados em datas)

Estimativa: 2 a 3 dias
Branch: feature/core-processing
Checklist:

Criar src/core/CSVProcessor.js

Criar src/core/MonetaryAdjustment.js

Criar interface de injeção de taxas (TaxProviderInterface)

    Escrever testes unitários simples

3. Integração com APIs Externas (Bacen)

Objetivos:

    Criar um serviço TaxFetcher com fallback local

    Definir cache/localStorage para evitar requisições repetidas

    Tratar erros de CORS (via PHP Proxy ou backend local)

Estimativa: 2 dias
Branch: feature/api-integration
Checklist:

Criar src/services/fetch-taxas.js

Criar public/data/taxas-local.json como fallback

Implementar proxy PHP/CORS bypass se necessário

    Escrever log de integração com testes simulados

4. Componente de Visualização e UI Interativa

Objetivos:

    Conectar o processamento aos componentes HTML

    Adicionar feedback ao usuário (loading, erros)

    Permitir ajustes manuais nas taxas

Estimativa: 2 dias
Branch: feature/ui-integration
Checklist:

Criar src/components/CSVUploader.js

Criar src/components/TableRenderer.js

Conectar eventos da DOM ao processamento

    Testar fluxo completo

5. Organização de Issues e Documentação Técnica

Objetivos:

    Criar issues no GitHub com milestones

    Documentar design das classes, padrões aplicados e fluxos

    Especificar como evoluir para versões com persistência, gráficos, API própria, etc.

Estimativa: 1 a 2 dias
Branch: docs/structure
Checklist:

Criar Wiki com tópicos: Estrutura do Projeto, Fluxo de Processamento, Estratégia de Fetch de Taxas, Regras de Correção

Criar issues e milestones por feature

    Atualizar README.md com instruções técnicas e visão de arquitetura

🚀 Quando subir código e criar branches?
Ação	Branch
Base do projeto / reorganização	refactor-base
Desenvolvimento da lógica principal	feature/core-processing
Integração com APIs	feature/api-integration
Parte visual e ligação com HTML	feature/ui-integration
Documentação e planejamento	docs/structure
🧠 Benefícios dessa abordagem

    Código testável e modular

    Facilidade de debugging e manutenção

    Facilidade de onboarding para futuros colaboradores

    Documentação útil desde o início

    Histórico limpo e rastreável via branches e commits

🟦 TO DO (planejado, ainda não iniciado)
📂 Organização e Ambiente

    chore: reestruturar pastas para separar componentes e lógica de negócio

    doc: atualizar README com novas funcionalidades previstas

    chore: configurar ambiente local com proxy PHP (para evitar CORS nas APIs do BCB)

🧠 Modelagem de Negócio

    feat(core): implementar Strategy para diferentes políticas de correção

    feat(factory): criar Factory para escolher estratégia com base na data

    feat(service): criar Singleton ou Service Layer para cache e fetch de taxas (SELIC, poupança)

📊 Integração de Dados

    refactor(processor): reescrever CSVProcessor para usar as estratégias

    feat(core): criar fallback para quando não houver dado da API (valores fixos)

    test(core): validar cálculos com datas-chave conhecidas

🧩 Interface e Componentes

    feat(ui): permitir upload de CSV e exibir resultado

    feat(ui): criar tabela formatada com resultados

    feat(ui): botão para exportar CSV corrigido (usando jsPDF ou equivalente)

    chore: mover componentes HTML (header, nav, footer) para pasta /components na raiz

🗃️ Documentação e Versionamento

    doc: iniciar documentação dos padrões usados (Strategy, Factory, Service)

    doc: criar arquivos de exemplo para ajudar usuários a entender estrutura do CSV

🟨 IN PROGRESS (o que estiver sendo feito agora)

    refactor(core): implementar cálculo com integração parcial com API do BCB

    test(service): testar proxy PHP com a API do Banco Central (evitar bloqueio CORS)

✅ DONE (movido conforme finalizado)

(Aqui você moverá manualmente conforme for concluindo as tarefas.)
📌 Dicas para uso:

    Use cada item como uma Issue no GitHub.

    Adicione etiquetas como enhancement, bug, docs, core, ui.

    Crie uma nova branch por item relevante (ex: feature/strategy-pattern).

    Escreva commits descritivos seguindo o padrão:
    feat(core): aplicar strategy para política de juros de 2009-2012

/js/
├── App.js                                                           # Entrada principal da aplicação
├── csv-processor.js                                      # Context (Strategy), coordena a escolha da calculadora e o processamento
│
├── core/
│   ├──  constants/
│   │   ├── regras-correcao.js                # Cria instâncias de calculadoras de correção
│   │   └── regras-juros.js                        # Cria instâncias de calculadoras de juros
│   │
│   ├── strategy/                                             # Estratégias de cálculo específicas
│   │   ├── calculadora-atual.js
│   │   ├── calculadora-poupanca.js    
│   │   ├── calculadora-ufir.js                  # Cálculo com base na UFIR
│   │   ├── calculadora-ipcae.js             # Cálculo com base no IPCA-E
│   │   ├── calculadora-selic.js               # Cálculo com base na SELIC
│   │   ├── calculadora-correcao.js     # Interface base de correção monetária
│   │   └── calculadora-juros.js              # Interface base de juros moratórios
│   │
│   └── factory/                                               # Fábricas de criação de estratégias
│       └── calculadora-factory.js          # Factory geral que chama as fábricas específicas
│
/data/
└── tunep_monum.csv                               # Dados de entrada CSV

import { CalculadoraUFIR } from '../../../js/core/strategy/calculadora-ufir.js';

describe('CalculadoraUFIR', () => {
  test('deve calcular o valor corrigido corretamente', () => {
    // Arrange
    const taxaUFIR = 0.05; // 5%
    const valorOriginal = 1000;
    const dataExemplo = new Date('1995-01-01');
    const calculadora = new CalculadoraUFIR(taxaUFIR);

    // Act
    const resultado = calculadora.calcular(valorOriginal, dataExemplo);

    // Assert
    expect(resultado).toBeDefined();
    expect(resultado.indice).toBe('UFIR');
    expect(resultado.valorCorrigido).toBeCloseTo(1050, 2);
    expect(resultado.fator).toBeCloseTo(1.05, 2);
  });
});



Etapa final, porém esses erros parecem estar ligados 

 FAIL  teste/core/strategy/calculadora-juros.test.js
  ● CalculadoraJuros › obterTaxa › deve retornar a taxa fixa para datas anteriores a 2020

    TypeError: Cannot read properties of undefined (reading 'tipo')

      12 |     const regra = regrasJuros.find(r => r.cond(data));
      13 |
    > 14 |     if (regra.tipo === 'FIXO') return regra.valor;
         |               ^
      15 |     if (regra.tipo === 'SELIC') return TAXAS.SELIC;
      16 |     if (regra.tipo === 'POUPANCA') return TAXAS.POUPANCA;
      17 |     return 0;

      at Function.tipo [as obterTaxa] (js/core/strategy/calculadora-juros.js:14:15)
      at Object.obterTaxa (teste/core/strategy/calculadora-juros.test.js:19:31)

  ● CalculadoraJuros › obterTaxa › deve retornar 0 para datas que não correspondem a nenhuma regra

    TypeError: Cannot read properties of undefined (reading 'tipo')

      12 |     const regra = regrasJuros.find(r => r.cond(data));
      13 |
    > 14 |     if (regra.tipo === 'FIXO') return regra.valor;
         |               ^
      15 |     if (regra.tipo === 'SELIC') return TAXAS.SELIC;
      16 |     if (regra.tipo === 'POUPANCA') return TAXAS.POUPANCA;
      17 |     return 0;

      at Function.tipo [as obterTaxa] (js/core/strategy/calculadora-juros.js:14:15)
      at Object.obterTaxa (teste/core/strategy/calculadora-juros.test.js:39:31)

  ● CalculadoraJuros › aplicar › deve aplicar a taxa fixa corretamente

    TypeError: Cannot read properties of undefined (reading 'tipo')

      12 |     const regra = regrasJuros.find(r => r.cond(data));
      13 |
    > 14 |     if (regra.tipo === 'FIXO') return regra.valor;
         |               ^
      15 |     if (regra.tipo === 'SELIC') return TAXAS.SELIC;
      16 |     if (regra.tipo === 'POUPANCA') return TAXAS.POUPANCA;
      17 |     return 0;

      at Function.tipo [as obterTaxa] (js/core/strategy/calculadora-juros.js:14:15)
      at Function.obterTaxa [as aplicar] (js/core/strategy/calculadora-juros.js:21:23)
      at Object.aplicar (teste/core/strategy/calculadora-juros.test.js:47:31)

  ● CalculadoraJuros › aplicar › deve aplicar a taxa da Poupança corretamente

    expect(received).toBeCloseTo(expected, precision)

    Expected: 12
    Received: 1200

    Expected precision:    2
    Expected difference: < 0.005
    Received difference:   1188

      57 |       const valor = 2000;
      58 |       const data = new Date('2021-09-05');
    > 59 |       expect(CalculadoraJuros.aplicar(valor, data)).toBeCloseTo(12, 2); // 2000 * 0.006
         |                                                     ^
      60 |     });
      61 |
      62 |     test('deve aplicar a taxa fixa para datas futuras corretamente', () => {

      at Object.toBeCloseTo (teste/core/strategy/calculadora-juros.test.js:59:53)

  ● CalculadoraJuros › aplicar › deve retornar 0 se a taxa for 0

    TypeError: Cannot read properties of undefined (reading 'tipo')

      12 |     const regra = regrasJuros.find(r => r.cond(data));
      13 |
    > 14 |     if (regra.tipo === 'FIXO') return regra.valor;
         |               ^
      15 |     if (regra.tipo === 'SELIC') return TAXAS.SELIC;
      16 |     if (regra.tipo === 'POUPANCA') return TAXAS.POUPANCA;
      17 |     return 0;

      at Function.tipo [as obterTaxa] (js/core/strategy/calculadora-juros.js:14:15)
      at Function.obterTaxa [as aplicar] (js/core/strategy/calculadora-juros.js:21:23)
      at Object.aplicar (teste/core/strategy/calculadora-juros.test.js:71:31)

test/
├── core/
│   ├── calculators/
│   │   ├── correction-calculator.test.js
│   │   └── interest-calculator.test.js
│   ├── constants/
│   │   ├── correction-rules.test.js
│   │   └── interest-rules.test.js
│   └── models/
│        ├── correction-factor.test.js
│        └── interest-rule.test.js
└── index.js

js/
├── core/
│   ├── calculators/
│   │   ├── correction-calculator.js
│   │   └── interest-calculator.js
│   ├── constants/
│   │   ├── correction-rules.js
│   │   └── interest-rules.js
│   ├── models/
│   │   ├── correction-factor.js
│   │   └── interest-rule.js
│   └── utils/
│       └── date-utils.js

Atual estrutura

js/
├── core/
│   ├── calculators/               # Estratégias concretas (padrão Strategy)
│   │   ├── monetary-correction-calculator.js
│   │   ├── simple-interest-calculator.js
│   │   └── index.js               # (opcional) exporta todas as estratégias
│   │
│   ├── factory/
│   │   └── calculation-strategy-factory.js
│   │
│   ├── constants/
│   │   ├── correction-rules.js
│   │   └── interest-rules.js
│   │
│   ├── processor/
│   │   └── csv-processor.js       # Usa a factory para aplicar cálculo
│   │
│   ├── models/
│   │   └── correction-factor.js       # Usa o model para 
│   │
│   └── utils/
│       └── formatter.js           # Funções auxiliares como formatar valores
│
├── app.js                         # Orquestra o processamento e UI
└── index.html


js/
├── components/
│   ├── footer.html/  
│   ├── header.html/
│   ├── navbar.html/
│   └── navbar.js/
│
├── main.js 
└── table-renderer.js

//csv-viewer.html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Correção de Repasses CSV</title>
  <link rel="stylesheet" href="style/base.css" />
  <script src="