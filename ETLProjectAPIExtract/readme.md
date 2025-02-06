# Dashboard de Preços do Bitcoin 🪙

Este projeto implementa um pipeline ETL que coleta dados de preços do Bitcoin da API da Coinbase, armazena esses dados em um banco de dados PostgreSQL e exibe esses dados em um dashboard interativo criado com Streamlit.

## 📋 Resumo das Funcionalidades

- **Pipeline**: Extrai dados de preços do Bitcoin da API da Coinbase, transforma os dados e os armazena em um banco de dados PostgreSQL.
- **Monitoramento de Performance**: Utiliza Logfire para monitorar a performance do pipeline, incluindo spans para as etapas de extração, transformação e carregamento.
- **Dashboard Interativo**: Exibe os dados dos preços do Bitcoin, mostrando as tendências ao longo do tempo e fornecendo métricas importantes, como preço atual, máximo e mínimo.

## 🛠️ Principais Bibliotecas Utilizadas

- **Streamlit**: Usada para criar o dashboard interativo
- **Pandas**: Para manipulação e análise de dados
- **SQLAlchemy**: Usada para ORM (Mapeamento Objeto-Relacional) com o banco de dados PostgreSQL
- **psycopg2**: Driver para se conectar ao banco de dados PostgreSQL
- **Requests**: Para fazer requisições HTTP à API da Coinbase e obter os dados de preços do Bitcoin
- **Logfire**: Para monitoramento de performance e logging
- **Altair**: Para criação de gráficos interativos
- **dotenv**: Para carregar variáveis de ambiente a partir de um arquivo .env

## 📦 Estrutura de Pastas

- `app/`: Contém o código do dashboard interativo
- `src/`: Contém o código do pipeline ETL
- `requirements.txt`: Lista de bibliotecas necessárias
