# LinkEdge - Sistema Inteligente de Monitoramento e Comunicação Emergencial

## 📖 Sobre o Projeto

O **LinkEdge** é um sistema desenvolvido em Python para monitoramento de áreas de risco, combinando sensores ambientais, análise de dados e comunicação via rede mesh e satélite.

O projeto foi criado como trabalho acadêmico para a disciplina de programação da **FIAP (Faculdade de Informática e Administração Paulista)**, com o objetivo de aplicar conceitos de lógica de programação, estruturas condicionais, laços de repetição, funções matemáticas e interação com o usuário.

---

## 🎯 Objetivo

O sistema simula uma central de monitoramento capaz de:

* Monitorar temperatura da região;
* Monitorar nível da água;
* Detectar movimentações em áreas de risco;
* Verificar o status da rede de comunicação;
* Verificar conexão com satélite;
* Selecionar automaticamente a melhor rota de comunicação;
* Calcular o ângulo ideal de conexão com satélite;
* Gerar relatórios de emergência.

---

## ⚙️ Funcionalidades

### 1. Monitoramento

Exibe informações coletadas pelos sensores:

* Temperatura
* Nível da água
* Detecção de movimento
* Status da rede
* Status do satélite

### 2. Roteamento Inteligente

Analisa a qualidade do sinal dos nós da rede:

* Nó A
* Nó B
* Nó C

O sistema escolhe automaticamente o nó com melhor sinal para comunicação.

### 3. Cálculo de Ângulo para Satélite

Utiliza funções matemáticas da biblioteca `math` para calcular o ângulo de comunicação com o satélite.

Fórmulas utilizadas:

* `atan()`
* `degrees()`

O sistema informa se a conexão está estável ou instável.

### 4. Relatório de Emergência

Identifica automaticamente situações de risco:

* Enchente
* Incêndio
* Deslizamento
* Área Segura

Também apresenta:

* Melhor nó selecionado
* Status da rede
* Status do satélite
* Tempo estimado de resposta

---

## 🛠️ Tecnologias Utilizadas

* Python 3
* Biblioteca Math

---

## 📂 Estrutura do Sistema

Menu principal:

1 - Monitoramento
2 - Roteamento
3 - Calcular Ângulo
4 - Relatório Final
5 - Sair

---

## 🎓 Trabalho Acadêmico

Projeto desenvolvido como atividade acadêmica da FIAP, aplicando conceitos de:

* Estruturas Condicionais (`if`, `elif`, `else`)
* Laços de Repetição (`while`)
* Entrada e Saída de Dados (`input` e `print`)
* Operadores Lógicos
* Bibliotecas Matemáticas
* Simulação de Sistemas de Monitoramento

---

## 👨‍💻 Integrantes

* Matheus Dionisio Cintra — RM569844
* Leonardo Daniel dos Santos — RM571092
* Kaio Hiroki Kinoshita — RM569127

---
