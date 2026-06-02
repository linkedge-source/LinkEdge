# LinkEdge – Sistema Inteligente de Monitoramento e Comunicação Emergencial

## 📖 Sobre o Projeto

O **LinkEdge** é uma solução desenvolvida em Python para monitoramento de áreas de risco e apoio à comunicação em situações de emergência.

O sistema simula a coleta de dados ambientais, análise de condições críticas e seleção de rotas de comunicação por meio de uma rede mesh integrada à comunicação via satélite.

Este projeto foi desenvolvido como trabalho acadêmico da **Global Solution FIAP**, aplicando conceitos fundamentais de programação estudados no primeiro semestre.

---

## 🎯 Objetivo

Desenvolver uma aplicação capaz de auxiliar no monitoramento de regiões vulneráveis, identificando possíveis situações de risco e fornecendo informações para tomada de decisão em cenários de emergência.

---

## ⚙️ Funcionalidades

### 1. Sobre o Projeto

Apresenta uma breve descrição da solução desenvolvida.

### 2. Monitoramento

Permite registrar e visualizar informações coletadas por sensores:

* Temperatura ambiente
* Nível da água
* Detecção de movimento

### 3. Roteamento Inteligente

Recebe os sinais de três nós da rede mesh:

* Nó A
* Nó B
* Nó C

O sistema analisa os sinais e seleciona automaticamente a melhor rota de comunicação.

### 4. Cálculo de Ângulo

Calcula o ângulo ideal de comunicação com o satélite utilizando funções matemáticas da biblioteca `math`.

### 5. Relatório de Risco

Analisa os dados fornecidos pelo usuário e identifica possíveis situações de emergência:

* Enchente
* Incêndio
* Deslizamento
* Área Segura

---

## 🛠️ Tecnologias Utilizadas

* Python 3
* Biblioteca Math

---

## 📚 Conceitos Aplicados

O projeto foi desenvolvido utilizando os conceitos exigidos pela disciplina:

### Estruturas de Decisão

* if
* elif
* else

### Estruturas de Repetição

* while
* for

### Estruturas de Dados

* Listas (list)
* Strings

### Modularização

* Funções (`def`)

### Passagem de Parâmetros

Exemplo:

```python
def gerar_risco(temperatura, nivel_agua, movimento):
```

### Retorno de Funções

Exemplo:

```python
return "ENCHENTE"
```

---

## 📂 Estrutura do Menu

```text
1 - Sobre o Projeto
2 - Monitoramento
3 - Roteamento
4 - Calcular Ângulo
5 - Relatório
6 - Sair
```

---

## 🚀 Como Executar

1. Instale o Python 3 em sua máquina.
2. Clone este repositório:

```bash
git clone https://github.com/SEU-USUARIO/LinkEdge.git
```

3. Acesse a pasta do projeto:

```bash
cd LinkEdge
```

4. Execute o programa:

```bash
python linkedge.py
```

5. Utilize o menu para navegar pelas funcionalidades.

---

## 🌎 Relação com a Global Solution

O LinkEdge foi idealizado para simular uma solução tecnológica voltada ao monitoramento de áreas sujeitas a desastres naturais, permitindo a análise de dados ambientais e a comunicação eficiente em cenários de emergência.

---

## 👨‍💻 Integrantes

* Matheus Dionisio Cintra — RM569844
* Leonardo Daniel dos Santos — RM571092
* Kaio Hiroki Kinoshita — RM569127

---

## 🎓 Instituição

FIAP – Faculdade de Informática e Administração Paulista

Projeto acadêmico desenvolvido para a disciplina de Computational Thinking Using Python – Global Solution.
