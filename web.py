import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    new_todo = st.session_state["new_todo"] + "\n"
    todos.append(new_todo)
    functions.write_to_file(todos)

st.title("To-do App")
#st.subheader("")
st.write("A minimalist to-do app")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_to_file(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="Add todo", label_visibility="collapsed", placeholder="Add new todo...", on_change=add_todo, key='new_todo')