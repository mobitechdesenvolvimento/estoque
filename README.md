---

# Sistema de Gestão de Estoque

Este é um sistema de gestão de estoque desenvolvido em **Python** com **Flask** e **SQLite**. Ele permite gerenciar produtos, verificar estoque baixo e analisar métricas através de um dashboard.

## Funcionalidades

1. **Adicionar Produto**:

   - Cadastre novos produtos com nome, quantidade e preço.

2. **Listar Produtos**:

   - Visualize todos os produtos cadastrados em uma tabela.

3. **Atualizar Produto**:

   - Edite o nome, quantidade ou preço de um produto existente.

4. **Remover Produto**:

   - Exclua um produto do estoque.

5. **Verificar Estoque Baixo**:

   - Defina um limite e veja quais produtos estão com estoque abaixo desse valor.

6. **Dashboard de Métricas**:
   - Visualize métricas importantes, como:
     - Total de produtos.
     - Valor total do estoque.
     - Número de produtos com estoque baixo.
     - Produto mais caro e mais barato.

## Pré-requisitos

Antes de começar, certifique-se de ter instalado:

- Python 
- Pip (gerenciador de pacotes do Python)

## Instalação

1. **Clone o repositório**:

   ```bash
   git clone https://github.com/mobitechdesenvolvimento/estoque.git
   ```

2. **Crie um ambiente virtual** (opcional, mas recomendado):

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. **Instale as dependências**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Execute o banco de dados**:

   - O banco de dados SQLite será criado automaticamente na primeira execução.

5. **Inicie o servidor Flask**:

   ```bash
   python app.py
   ```

6. **Acesse a aplicação**:
   - Abra o navegador e acesse: `http://127.0.0.1:5000`.

## Estrutura do Projeto

```
estoque/
├── app.py                  # Aplicação principal
├── templates/              # Templates HTML
│   ├── base.html           # Layout base
│   ├── index.html          # Página inicial
│   ├── adicionar_produto.html
│   ├── listar_produtos.html
│   ├── atualizar_produto.html
│   ├── estoque_baixo.html
├── static/                 # Arquivos estáticos (CSS, JS, imagens)
│   ├── css/
│   │   └── styles.css      # Estilos personalizados
│   └── js/
│       └── scripts.js      # Scripts JavaScript
├── requirements.txt        # Dependências do projeto
└── README.md               # Documentação do projeto
```

## Como Usar

1. **Adicionar Produto**:

   - Na página inicial, clique em "Adicionar Produto".
   - Preencha os campos e clique em "Adicionar".

2. **Listar Produtos**:

   - Na página inicial, clique em "Listar Produtos".
   - Veja todos os produtos cadastrados em uma tabela.

3. **Atualizar Produto**:

   - Na lista de produtos, clique em "Atualizar" ao lado do produto desejado.
   - Edite os campos e clique em "Atualizar".

4. **Remover Produto**:

   - Na lista de produtos, clique em "Remover" ao lado do produto desejado.

5. **Verificar Estoque Baixo**:

   - Na página inicial, clique em "Verificar Estoque Baixo".
   - Defina um limite e veja os produtos com estoque abaixo desse valor.

6. **Dashboard de Métricas**:
   - Na página inicial, clique em "Dashboard".
   - Visualize métricas importantes sobre o estoque.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **Flask**: Framework web para desenvolvimento da aplicação.
- **SQLite**: Banco de dados para armazenamento dos produtos.
- **Bootstrap**: Framework CSS para o design da interface.
- **Bootstrap Icons**: Ícones para melhorar a experiência do usuário.

---
