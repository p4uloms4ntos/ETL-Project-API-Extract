# Projeto ETL com Python

## Descrição
Projeto de ETL (Extract, Transform, Load) desenvolvido em Python para extrair dados da API *Coinbase*, realizar transformações necessárias e carregar em um banco de dados PostgreSQL para alimentar um dashboard.

## Tecnologias Utilizadas
- Python 3.8+
- Requests (para consumo de API)
- Pandas (para manipulação de dados)
- SQLAlchemy (para conexão com banco de dados)

## Instalação

1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/nome-do-projeto.git
cd nome-do-projeto
```

2. Crie um ambiente virtual
```bash
python -m venv venv
```

3. Ative o ambiente virtual
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

4. Instale as dependências
```bash
pip install -r requirements.txt
```

## Estrutura do Projeto
```
projeto/
├── src/
│   ├── pipeline_BTC_value.py  # Pipeline principal de ETL
│   └── database.py            # Modelos e configuração do banco de dados
├── .env                       # Variáveis de ambiente (não versionado)
├── requirements.txt
└── README.md
```

## Como Usar
1. Certifique-se que o PostgreSQL está em execução
2. Execute o pipeline principal:
```bash
python src/pipeline_BTC_value.py
```

## Funcionalidades
- Extração de dados da API Coinbase a cada 15 segundos
- Transformação dos dados (conversão de tipos e formatação)
- Armazenamento em banco PostgreSQL
- Monitoramento contínuo com tratamento de erros
- Registro de timestamp para cada cotação

## Próximos Passos
- Implementar logs estruturados
- Adicionar testes unitários
- Criar dashboard de visualização
- Implementar alertas de preço
- Adicionar suporte a múltiplas criptomoedas

## Autor
Paulo Moreira dos Santos

## Licença
Este projeto está sob a licença MIT.
```

