# OS Fácil - Sprint 2: Arquiteturas Disruptivas, IoT e IA Generativa

## 1. Visão Geral e Evolução do Projeto

O **OS Fácil** é um aplicativo de gestão estilo ERP (Enterprise Resource Planning) voltado para oficinas mecânicas. Seu objetivo é digitalizar a criação de Ordens de Serviço (OS), controlar estoque e fornecer análises de Business Intelligence (BI).

### Evolução em Relação à Sprint 1

Na Sprint 2, o projeto evoluiu de uma proposta conceitual para um **Protótipo Funcional Inicial** implantado no Oracle APEX, demonstrando as primeiras integrações de dados e serviços Oracle.

Utilizando as bibliotecas **NumPy** e **Pandas**, foram gerados dados para a demonstração do Oracle APEX.

| Foco | Sprint 1 (Conceito) | Sprint 2 (Protótipo Funcional) |
| :--- | :--- | :--- |
| **Plataforma** | Proposta de uso do APEX | Protótipo em **Oracle APEX** em execução |

---

## 2. Tecnologias Disruptivas e Protótipo APEX

A Sprint 2 comprova a aplicação dos conceitos de dados e IA, integrando-os diretamente ao ecossistema Oracle.

### Ferramentas Oracle e Aplicações

O protótipo inicial do OS Fácil foi construído utilizando as seguintes ferramentas da Oracle:

* **Oracle APEX:** Utilizado para o desenvolvimento rápido do protótipo inicial, atuando como a interface principal do aplicativo de gestão.
* **Autonomous Database (ADB):** O banco de dados para a aplicação, que fornece recursos de auto-tuning e *patching* automático, e que servirá de base para as futuras capacidades de IA.
* **OCI (Oracle Cloud Infrastructure):** Plataforma utilizada para hospedar os serviços.

### Aplicação de Análise de Dados e IA

A principal funcionalidade demonstrada é a ingestão e visualização de dados operacionais que simulam a telemetria de uma oficina. Isso estabelece a fundação para futuros módulos de Análise de Dados e IA Preditiva:

* **Análise de Dados/ML:** Esta integração de dados é a base para a **Otimização Preditiva** (previsão de tempo de mão de obra e otimização de estoque) que será implementada nas próximas Sprints.

---

## 3. Protótipo em Funcionamento e Evolução

As telas do protótipo APEX demonstram a funcionalidade de ingestão e visualização de dados, atendendo ao requisito de protótipo inicial funcional.

### Funcionalidades Efetivamente Demonstradas

* **Tela de Login**
    ![Tela de login](https://github.com/Wugabriel/Sprint2-DisruptiveArchiteturesIotIobEGenerativeIA/blob/main/prints/Captura%20de%20tela%202025-11-09%20171937.png?raw=true)
* **Tela Inicial**
    ![Tela inicial](https://github.com/Wugabriel/Sprint2-DisruptiveArchiteturesIotIobEGenerativeIA/blob/main/prints/Captura%20de%20tela%202025-11-09%20172033.png?raw=true)
* **Dashboard**
    ![Dashboard](https://github.com/Wugabriel/Sprint2-DisruptiveArchiteturesIotIobEGenerativeIA/blob/main/prints/Captura%20de%20tela%202025-11-09%20172052.png?raw=true)
* **Tela de Busca**
    ![Busca](https://github.com/Wugabriel/Sprint2-DisruptiveArchiteturesIotIobEGenerativeIA/blob/main/prints/Captura%20de%20tela%202025-11-09%20172121.png?raw=true)
* **Relatório de Dados (*Data Report*)**
    ![Dados report](https://github.com/Wugabriel/Sprint2-DisruptiveArchiteturesIotIobEGenerativeIA/blob/main/prints/Captura%20de%20tela%202025-11-09%20172145.png?raw=true)

**Resumo da Funcionalidade:** A aplicação APEX demonstra uma tela funcional com a visualização dos dados inseridos, validando o ciclo completo de ingestão, processamento e visualização.

### Próximos Passos (Evolução para as Próximas Sprints)

* **IA Generativa:** Implementar a funcionalidade de **AI Vector Search** no Oracle Database (23ai) para construir o **Assistente Virtual Inteligente** (FAQ Inteligente) para diagnósticos e criação de OS.
* **ML Preditivo:** Desenvolver modelos de Machine Learning (via OCI Data Science) para otimização de estoque e previsão de demanda.
* **Refinamento do APEX:** Evoluir a interface do APEX, integrando as APIs de *backend* desenvolvidas nas outras disciplinas.

---

## 4. Vídeo de Demonstração

* [Vídeo de Demonstração do Protótipo APEX](https://youtu.be/4jw0MrPybso)

---

## Integrantes

* **Fábio Henrique de Souza Eduardo** - RM: 560416
* **Gabriel Wu Castro** - RM: 560210
* **Renato Kenji Sugaki** - RM: 559810
