# Importa o módulo sqlite3 para interagir com banco de dados SQLite
import sqlite3

# Função que cria e retorna uma conexão com o banco de dados agenda.db
def criar_conexao():
    return sqlite3.connect("agenda.db")

# Função que cria a tabela "contatos" no banco de dados, se ela ainda não existir
def criar_tabela():
    # Cria a conexão com o banco de dados
    conexao = criar_conexao()
    # Cria um cursor para executar comandos SQL
    cursor = conexao.cursor()
    # Executa o comando SQL para criar a tabela com os campos desejados
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS contatos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,  # ID único e automático
            nome TEXT NOT NULL,                   # Campo obrigatório: nome
            telefone TEXT NOT NULL,               # Campo obrigatório: telefone
            endereco TEXT,                        # Campo opcional: endereço
            cpf TEXT                              # Campo opcional: CPF
        )
    """)
    # Salva (confirma) as alterações no banco
    conexao.commit()
    # Fecha a conexão com o banco
    conexao.close()

# Função para adicionar um novo contato ao banco de dados
def adicionar_contato(nome, telefone, endereco, cpf):
    conexao = criar_conexao()
    cursor = conexao.cursor()
    # Insere os dados do contato na tabela
    cursor.execute("INSERT INTO contatos (nome, telefone, endereco, cpf) VALUES (?, ?, ?, ?)",
                   (nome, telefone, endereco, cpf))
    conexao.commit()
    conexao.close()

# Função para buscar todos os contatos cadastrados
def listar_contatos():
    conexao = criar_conexao()
    cursor = conexao.cursor()
    # Executa uma consulta para selecionar todos os contatos
    cursor.execute("SELECT * FROM contatos")
    contatos = cursor.fetchall()  # Obtém todos os resultados
    conexao.close()
    return contatos  # Retorna os dados obtidos

# Função para buscar contatos pelo nome (busca parcial)
def buscar_contato(nome):
    conexao = criar_conexao()
    cursor = conexao.cursor()
    # Executa uma consulta com filtro LIKE para buscar nomes parcialmente
    cursor.execute("SELECT * FROM contatos WHERE nome LIKE ?", ('%' + nome + '%',))
    contatos = cursor.fetchall()
    conexao.close()
    return contatos

# Função para remover um contato pelo ID
def remover_contato(id):
    conexao = criar_conexao()
    cursor = conexao.cursor()
    # Executa a exclusão do contato com ID específico
    cursor.execute("DELETE FROM contatos WHERE id = ?", (id,))
    conexao.commit()
    conexao.close()