import sqlite3

# Conectar ao banco (cria se não existir)
conn = sqlite3.connect("banco.db")
cursor = conn.cursor()

# Criar tabela
cursor.execute(
    """
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL
)
"""
)


# Inserir dados
def inserir_usuario(nome, idade):
    cursor.execute("INSERT INTO usuarios (nome, idade) VALUES (?, ?)", (nome, idade))
    conn.commit()


# Listar dados
def listar_usuarios():
    cursor.execute("SELECT * FROM usuarios")
    for usuario in cursor.fetchall():
        print(usuario)


# Atualizar dados
def atualizar_usuario(id, novo_nome, nova_idade):
    cursor.execute(
        "UPDATE usuarios SET nome = ?, idade = ? WHERE id = ?",
        (novo_nome, nova_idade, id),
    )
    conn.commit()


# Deletar dados
def deletar_usuario(id):
    cursor.execute("DELETE FROM usuarios WHERE id = ?", (id,))
    conn.commit()


# Exemplo de uso
if __name__ == "__main__":
    inserir_usuario("Lucas", 25)
    inserir_usuario("Maria", 30)
    listar_usuarios()
    atualizar_usuario(1, "Lucas Silva", 26)
    deletar_usuario(2)
    listar_usuarios()

# Fechar conexão
conn.close()
