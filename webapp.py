import streamlit as st
import functions #backend to pass the todos

todos = functions.get_todos()

st.title("To-Do List") #title
for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add a new todo...")