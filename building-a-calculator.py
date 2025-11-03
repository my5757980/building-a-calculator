# calc.py  ←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←
# Calculator Pro – FULLY FIXED! No Pylance Errors!

import streamlit as st
import math

# Page Config
st.set_page_config(page_title="Calculator Pro", page_icon="🧮", layout="centered")

# CSS
st.markdown("""
<style>
    .main {background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);}
    .stApp {background-color: #1a1a2e;}
    h1 {color: #ffd700 !important; text-align: center;}
    .stButton > button {background: #00ff88; color: black; font-weight: bold; font-size: 1.5em; height: 70px; width: 100%; border-radius: 15px; margin: 5px;}
    .display {background: #16213e; padding: 20px; border-radius: 15px; text-align: right; font-size: 2.5em; color: #00ff88; font-family: monospace;}
    .history {background: #1a1a2e; padding: 10px; border-radius: 10px; margin: 5px 0;}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>🧮 Calculator Pro</h1>", unsafe_allow_html=True)

# Session State
if 'expression' not in st.session_state:
    st.session_state.expression = ""
if 'history' not in st.session_state:
    st.session_state.history = []

# Display
st.markdown(f"<div class='display'>{st.session_state.expression or '0'}</div>", unsafe_allow_html=True)

# Buttons
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("C"):
        st.session_state.expression = ""
        st.rerun()
with col2:
    if st.button("("):
        st.session_state.expression += "("
        st.rerun()
with col3:
    if st.button(")"):
        st.session_state.expression += ")"
        st.rerun()
with col4:
    if st.button("÷"):
        st.session_state.expression += "/"
        st.rerun()

# Row 2
with col1:
    if st.button("7"):
        st.session_state.expression += "7"
        st.rerun()
with col2:
    if st.button("8"):
        st.session_state.expression += "8"
        st.rerun()
with col3:
    if st.button("9"):
        st.session_state.expression += "9"
        st.rerun()
with col4:
    if st.button("×"):
        st.session_state.expression += "*"
        st.rerun()

# Row 3
with col1:
    if st.button("4"):
        st.session_state.expression += "4"
        st.rerun()
with col2:
    if st.button("5"):
        st.session_state.expression += "5"
        st.rerun()
with col3:
    if st.button("6"):
        st.session_state.expression += "6"
        st.rerun()
with col4:
    if st.button("−"):
        st.session_state.expression += "-"
        st.rerun()

# Row 4
with col1:
    if st.button("1"):
        st.session_state.expression += "1"
        st.rerun()
with col2:
    if st.button("2"):
        st.session_state.expression += "2"
        st.rerun()
with col3:
    if st.button("3"):
        st.session_state.expression += "3"
        st.rerun()
with col4:
    if st.button("+"):
        st.session_state.expression += "+"
        st.rerun()

# Row 5
with col1:
    if st.button("0"):
        st.session_state.expression += "0"
        st.rerun()
with col2:
    if st.button("."):
        st.session_state.expression += "."
        st.rerun()
with col3:
    if st.button("="):
        try:
            result = eval(st.session_state.expression)
            st.session_state.history.append(f"{st.session_state.expression} = {result}")
            st.session_state.expression = str(result)
        except:
            st.session_state.expression = "Error"
        st.rerun()
with col4:
    if st.button("√"):
        try:
            result = math.sqrt(float(st.session_state.expression))
            st.session_state.history.append(f"√{st.session_state.expression} = {result}")
            st.session_state.expression = str(result)
        except:
            st.session_state.expression = "Error"
        st.rerun()

# Scientific
col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("sin"):
        st.session_state.expression += "math.sin(math.radians("
        st.rerun()
with col2:
    if st.button("cos"):
        st.session_state.expression += "math.cos(math.radians("
        st.rerun()
with col3:
    if st.button("π"):
        st.session_state.expression += "math.pi"
        st.rerun()
with col4:
    if st.button("Clear History"):
        st.session_state.history = []
        st.rerun()

# History
if st.session_state.history:
    st.markdown("### History")
    for entry in reversed(st.session_state.history[-10:]):
        st.markdown(f"<div class='history'>{entry}</div>", unsafe_allow_html=True)

# Premium
st.markdown("---")
st.info("**Premium:** Graph Plotter, Voice Input, PDF Export!")
st.caption("Built with Streamlit + uv | Math Made Easy!")