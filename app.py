import streamlit as st

import tarefas

tarefas.criar_tabela()

st.title("Gerenciador de Tarefas")

# Adicionar nova tarefa
novo_titulo = st.text_input("Nova tarefa")
if st.button("Adicionar"):
    if novo_titulo.strip():
        tarefas.adicionar(novo_titulo.strip())
        st.rerun()
    else:
        st.warning("Digite um título para a tarefa.")

st.divider()

# Lista de tarefas
lista = tarefas.listar()

if not lista:
    st.info("Nenhuma tarefa ainda. Adicione a primeira acima!")

for id_tarefa, titulo, concluida in lista:
    col_check, col_remover = st.columns([6, 1])

    marcada = col_check.checkbox(
        titulo,
        value=bool(concluida),
        disabled=bool(concluida),
        key=f"check_{id_tarefa}",
    )
    if marcada and not concluida:
        tarefas.concluir(id_tarefa)
        st.rerun()

    if col_remover.button("❌", key=f"remover_{id_tarefa}"):
        tarefas.remover(id_tarefa)
        st.rerun()