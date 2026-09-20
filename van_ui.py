import os
import tkinter as tk
from tkinter import filedialog

import streamlit as st
import van_status
import van_add
import van_commit
import van_init
import van_log



st.title("VAN UI")

if "repo_dir" not in st.session_state:
    st.session_state.repo_dir = os.getcwd()


def browse_folder():
    root = tk.Tk()
    root.withdraw()
    root.wm_attributes("-topmost", 1)
    selected = filedialog.askdirectory(master=root)
    root.destroy()
    if selected:
        st.session_state.repo_dir = selected


col1, col2 = st.columns([4, 1])
with col1:
    repo_dir = st.text_input("Repository folder", key="repo_dir")
with col2:
    st.write("")
    st.button("Browse", on_click=browse_folder)

if not os.path.isdir(repo_dir):
    st.error(f"Not a folder: {repo_dir}")
    st.stop()

os.chdir(repo_dir)

st.write("Select an action:")

if st.button("Status"):
    van_status.status()

filename = st.text_input("Filename to add")
if st.button("Add"):
    van_add.add(filename)

message = st.text_input("Commit message")
if st.button("Commit"):
    van_commit.commit(message)

if st.button("Init"):
    van_init.init()

if st.button("Log"):
    van_log.log()