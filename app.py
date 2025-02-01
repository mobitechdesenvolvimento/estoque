from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Função para conectar ao banco de dados
def get_db_connection():
    conn = sqlite3.connect('estoque.db')
    conn.row_factory = sqlite3.Row
    return conn

# Função para criar a tabela se não existir
def criar_tabela():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            quantidade INTEGER NOT NULL,
            preco REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Rota principal
@app.route('/')
def index():
    return render_template('index.html')

# Adicionar produto
@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar_produto():
    if request.method == 'POST':
        nome = request.form['nome']
        quantidade = int(request.form['quantidade'])
        preco = float(request.form['preco'])

        conn = get_db_connection()
        conn.execute('INSERT INTO produtos (nome, quantidade, preco) VALUES (?, ?, ?)',
                     (nome, quantidade, preco))
        conn.commit()
        conn.close()
        return redirect(url_for('listar_produtos'))
    return render_template('adicionar_produto.html')

# Remover produto
@app.route('/remover/<int:id>', methods=['POST'])
def remover_produto(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM produtos WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('listar_produtos'))

# Atualizar produto
@app.route('/atualizar/<int:id>', methods=['GET', 'POST'])
def atualizar_produto(id):
    conn = get_db_connection()
    if request.method == 'POST':
        # Captura os dados do formulário
        nome = request.form['nome']
        quantidade = int(request.form['quantidade'])
        preco = float(request.form['preco'])

        # Atualiza o produto no banco de dados
        conn.execute('''
            UPDATE produtos
            SET nome = ?, quantidade = ?, preco = ?
            WHERE id = ?
        ''', (nome, quantidade, preco, id))
        conn.commit()
        conn.close()
        return redirect(url_for('listar_produtos'))
    
    # Se for GET, busca os dados atuais do produto
    produto = conn.execute('SELECT * FROM produtos WHERE id = ?', (id,)).fetchone()
    conn.close()
    return render_template('atualizar_produto.html', produto=produto)

# Listar produtos
@app.route('/listar')
def listar_produtos():
    conn = get_db_connection()
    produtos = conn.execute('SELECT * FROM produtos').fetchall()
    conn.close()
    return render_template('listar_produtos.html', produtos=produtos)

# Verificar estoque baixo
@app.route('/estoque_baixo', methods=['GET', 'POST'])
def verificar_estoque_baixo():
    if request.method == 'POST':
        limite = int(request.form['limite'])
        conn = get_db_connection()
        produtos = conn.execute('SELECT * FROM produtos WHERE quantidade < ?', (limite,)).fetchall()
        conn.close()
        return render_template('estoque_baixo.html', produtos=produtos)
    return render_template('estoque_baixo.html')

# Executar a criação da tabela ao iniciar o aplicativo
criar_tabela()

if __name__ == '__main__':
    app.run(debug=True)