# README do Projeto ETL - Extraindo Dados da API

## Descrição do Projeto
Este projeto tem como objetivo implementar um processo de ETL (Extração, Transformação e Carga) para extrair dados de uma API específica e armazená-los em um banco de dados. O fluxo de trabalho é projetado para ser eficiente e escalável, permitindo a coleta de dados em intervalos regulares.

## Tecnologias Utilizadas
- Python
- Pandas
- Requests
- SQLAlchemy (conexão com o DB)
- PostgreSQL (ou outro banco de dados)
- Render (Postgresql, Dashboard e deploy)
- LogFire (Observabilidade) (Não codificado ainda, apenas instalada a biblioteca e o codigo inicial comentado). Para implementar, ver live apropriada

## Estrutura do Projeto
```
etl_project/
│
├── src/
│   ├── extract.py       # Código para extração de dados da API
│   ├── transform.py     # Código para transformação de dados
│   └── load.py          # Código para carga de dados no banco
│
├── config/
│   ├── config.yaml      # Configurações do projeto
│
├── requirements.txt      # Dependências do projeto
└── README.md             # Este arquivo
```

## Instruções de Uso

1. **Configuração do Ambiente:**
   - Certifique-se de ter o Python instalado.
   - Crie um ambiente virtual e ative-o.
   - Instale as dependências usando `pip install -r requirements.txt`.

2. **Configuração da API:**
   - Abra o arquivo `config/config.yaml` e insira as credenciais e endpoints da API.

3. **Execução do Processo ETL:**
   - Execute o script principal usando:
     ```
     python src/extract.py
     python src/transform.py
     python src/load.py
     ```

## Contribuição
Sinta-se à vontade para contribuir com melhorias ou relatar problemas. Abra um pull request ou uma issue no repositório.

## Licença
Este projeto está licenciado sob a MIT License.

