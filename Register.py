# Import necessary libraries
import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu
from PIL import Image
import time
import requests
from streamlit_lottie import st_lottie

# Set the page layout to wide
st.set_page_config(layout="wide")

# -------------------- SECURITY: Password hashing functions --------------------

import hashlib

# Function to hash passwords
def make_hashes(password):
    return hashlib.sha256(str.encode(password)).hexdigest()

# Function to verify passwords by comparing hashes
def check_hashes(password, hashed_text):
    if make_hashes(password) == hashed_text:
        return hashed_text
    return False

# -------------------- DATABASE SETUP AND FUNCTIONS --------------------

import sqlite3 

# Create/connect to SQLite database
conn = sqlite3.connect('data.db')
c = conn.cursor()

# Create user table if it doesn't exist
def create_usertable():
    c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT, password TEXT)')

# Add new user data to database
def add_userdata(username, password):
    c.execute('INSERT INTO userstable(username, password) VALUES (?,?)', (username, password))
    conn.commit()

# Authenticate user login
def login_user(username, password):
    c.execute('SELECT * FROM userstable WHERE username = ? AND password = ?', (username, password))
    data = c.fetchall()
    return data

# View all users (for admin/debugging purposes)
def view_all_users():
    c.execute('SELECT * FROM userstable')
    data = c.fetchall()
    return data

# -------------------- SIDEBAR MENU --------------------

with st.sidebar:
    selected = option_menu(
        menu_title="Start Here!",
        options=["Signup", "Login"],
        icons=["box-seam-fill", "box-seam-fill"],
        menu_icon="home",
        default_index=0
    )

# -------------------- SIGNUP SECTION --------------------

if selected == "Signup":
    st.title(":iphone: :blue[Create New Account]")
    new_user = st.text_input("Username")
    new_password = st.text_input("Password", type='password')
    
    if st.button("Signup"):
        create_usertable()
        add_userdata(new_user, make_hashes(new_password))  # Store hashed password
        st.success("You have successfully created a valid Account")
        st.info("Go to Login Menu to login")

# -------------------- LOGIN SECTION --------------------

elif selected == "Login":
    st.title(":calling: :blue[Login Section]")
    username = st.text_input("User Name")
    password = st.text_input("Password", type='password')
    
    if st.button("Login"):
        create_usertable()  # Ensure table exists
        hashed_pswd = make_hashes(password)
        result = login_user(username, check_hashes(password, hashed_pswd))  # Check credentials

        # Simulate loading with progress bar
        prog = st.progress(0)
        for per_comp in range(100):
            time.sleep(0.05)
            prog.progress(per_comp + 1)
        
        if result:
            st.success("Logged In as {}".format(username))
            st.warning("Go to Dashboard!")
        else:
            st.warning("Incorrect Username/Password")