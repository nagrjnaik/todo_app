import streamlit as st
from streamlit import session_state

import functions #backend to pass the todos

todos = functions.get_todos()

def add_todo():
    todo1 = st.session_state["new_todo"] + "\n"
    todos.append(todo1)
    functions.write_todos(todos)
    st.session_state["new_todo"] = ""  # Clear the input field


st.title("To-Do List") #title
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    #key holds the session state
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del session_state[todo]
        st.rerun()

st.text_input(label="", placeholder="Add a new todo...",
              on_change=add_todo, key="new_todo")