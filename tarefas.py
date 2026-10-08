#PROJETO DE EXECUÇÃO DE TAREFA
import sqlite3

DB ="tarefas.db"

def conectar():
    return sqlite3.connect(DB)

def criar_tabela():
    with conectar() as con:
        con.execute(
            """
CREATE TABLE IF NOT EXISTS tarefas(
id INTEGER PRIMARY KEY AUTOINCREMENT,
titulo TEXT NOT NULL,
concluida INTEGER NOT NULL DEFAULT 0
)"""
        )

def adicionar (titulo):
    with conectar() as con:
        cur = con.execute('INSERT INTO tarefas (titulo) VALUES(?)' , (titulo ,))
        return cur.lastrowid
def listar():
    with conectar() as con:
        return con.execute('SELECT id , titulo , concluida FROM TAREFAS').fetchall()

def concluir(id_tarefa):
    with conectar() as con:
        con.execute('UPDATE tarefas SET concluida = 1 WHERE id=?', (id_tarefa,))

def remover(id_tarefa):
    with conectar() as con:
        con.execute ("DELETE FROM tarefas WHERE id =?" , (id_tarefa ,))

#TESTE RAPIDO 
if __name__=="__main__":
    criar_tabela()
    id_nova= adicionar('Estudar python')
    print("Lista:" , listar())
    concluir(id_nova)
    print("Depois de concluir:" , listar())
    remover(id_nova)
    print("Depois remover:" , listar())