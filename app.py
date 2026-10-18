import streamlit as st
import pandas as pd
import numpy as np
import json
import os

# 1. State-of-the-art UI Engine Configuration
st.set_page_config(page_title="APEX // SYNDICATE CORE", layout="wide", initial_sidebar_state="collapsed")

# Premium Glassmorphism & Cyber Onyx CSS Injection
st.markdown("""
    <style>
    @import url('https://googleapis.com');
    
    .stApp {
        background-color: #030305;
        background-image: radial-gradient(circle at 50% 0%, #141208 0%, #030305 70%);
        color: #E5C158;
        font-family: 'Rajdhani', sans-serif;
    }
    
    html, body, [data-testid="stWidgetLabel"] p, .stMarkdown p {
        font-family: 'Rajdhani', sans-serif;
        font-size: 1.1rem;
        letter-spacing: 0.5px;
    }
    
    h1, h2, h3, [data-testid="stMetricLabel"] {
        font-family: 'Orbitron', sans-serif;
        color: #E5C158 !important;
        text-shadow: 0 0 10px rgba(229, 193, 88, 0.2);
    }
    
    /* Premium KPI Glass Cards */
    .metric-card {
        background: rgba(11, 11, 15, 0.6);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(229, 193, 88, 0.15);
        border-top: 3px solid #E5C158;
        padding: 25px;
        border-radius: 12px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        text-align: center;
        transition: all 0.3s ease;
    }
    .metric-card:hover {
        border-color: rgba(229, 193, 88, 0.4);
        box-shadow: 0 8px 32px 0 rgba(229, 193, 88, 0.1);
        transform: translateY(-2px);
    }
    
    /* Interactive Control Surface Inputs */
    .stTextInput>div>div>input, .stNumberInput>div>div>input {
        background-color: #0B0B0F !important;
        color: #E5C158 !important;
        border: 1px solid rgba(229, 193, 88, 0.2) !important;
        border-radius: 6px !important;
    }
    .stTextInput>div>div>input:focus, .stNumberInput>div>div>input:focus {
        border-color: #E5C158 !important;
        box-shadow: 0 0 8px rgba(229, 193, 88, 0.3) !important;
    }
    
    /* Apex Tactical Command Button */
    .stButton>button {
        background: linear-gradient(135deg, #F3D073 0%, #C49A33 100%) !important;
        color: #030305 !important;
        border-radius: 6px !important;
        font-family: 'Orbitron', sans-serif !important;
        font-weight: 700 !important;
        letter-spacing: 1px;
        border: none !important;
        padding: 12px 24px !important;
        box-shadow: 0 4px 15px rgba(229, 193, 88, 0.2) !important;
        transition: all 0.3s ease !important;
        width: 100%;
    }
    .stButton>button:hover {
        transform: translateY(-1px) !important;
        box-shadow: 0 6px 20px rgba(229, 193, 88, 0.4) !important;
    }
    
    /* Tab Navigation Layout Overrides */
    div[data-baseweb="tab-list"] {
        background-color: #0B0B0F;
        border-radius: 8px;
        padding: 6px;
        border: 1px solid rgba(229, 193, 88, 0.05);
    }
    button[data-baseweb="tab"] {
        color: #A0A0A0 !important;
        font-family: 'Orbitron', sans-serif;
        font-weight: 600;
    }
    button[data-baseweb="tab"][aria-selected="true"] {
        color: #E5C158 !important;
        background-color: rgba(229, 193, 88, 0.05) !important;
        border-radius: 6px;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Database Persistence Initialization Layer
DB_DIR = "apex_memory_archive"
DB_FILE = f"{DB_DIR}/ledger_state.json"
if not os.path.exists(DB_DIR):
    os.makedirs(DB_DIR)

DEFAULT_STATE = {
    "core_reserve": 2383.40,
    "weekly_cap": 42,
    "tips_logged": [
        {"id": 0, "horse": "Tommy Pickles", "race": "13:50 Sedgefield", "odds": 1.83, "stake": 10.0, "bookmaker": "Bet365", "status": "Pending"},
        {"id": 1, "horse": "Stay Hopeful", "race": "14:20 Sedgefield", "odds": 2.75, "stake": 10.0, "bookmaker": "Bet365", "status": "Pending"},
        {"id": 2, "horse": "Curious Mrs Fox", "race": "15:50 Sedgefield", "odds": 6.50, "stake": 10.0, "bookmaker": "Bet365", "status": "Pending"},
        {"id": 3, "horse": "Gambino", "race": "16:20 Sedgefield", "odds": 2.75, "stake": 10.0, "bookmaker": "PaddyPower", "status": "Pending"}
    ]
}

if not os.path.exists(DB_FILE):
    with open(DB_FILE, 'w') as f:
        json.dump(DEFAULT_STATE, f, indent=4)

with open(DB_FILE, 'r') as f:
    state = json.load(f)

# 3. Main Operational Header Frame
st.markdown("<h1 style='text-align: center; margin-bottom: 5px;'>⚜️ APEX // SYNDICATE CORE</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #A0A0A0 !important; font-size: 0.9rem; letter-spacing: 2px; margin-bottom: 30px;'>STATE-OF-THE-ART EXECUTIVE CONTROL SURFACE</p>", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["📊 TACTICAL FINANCIAL DESK", "🌐 APEX MEMORY ARCHIVE", "🗺️ NETWORK LINK NODE"])

with tab1:
    # High-End Metric Cards Row Layout
    active_exposure = sum(t['stake'] for t in state['tips_logged'] if t['status'] == 'Pending')
    used_slots = len(state['tips_logged'])
    
    m_col1, m_col2, m_col3 = st.columns(3)
    with m_col1:
        st.markdown(f"<div class='metric-card'><span style='color:#A0A0A0; font-size:0.8rem; font-family:Orbitron; letter-spacing:1px;'>PHYSICAL CORE CAPITAL</span><br><span style='font-size:2.2rem; font-weight:700; color:#E5C158;'>£{state['core_reserve']:.2f}</span></div>", unsafe_allow_html=True)
    with m_col2:
        st.markdown(f"<div class='metric-card'><span style='color:#A0A0A0; font-size:0.8rem; font-family:Orbitron; letter-spacing:1px;'>ACTIVE EXPOSURE</span><br><span style='font-size:2.2rem; font-weight:700; color:#E5C158;'>£{active_exposure:.2f}</span></div>", unsafe_allow_html=True)
    with m_col3:
        st.markdown(f"<div class='metric-card'><span style='color:#A0A0A0; font-size:0.8rem; font-family:Orbitron; letter-spacing:1px;'>WEEKLY CAPACITY LOGGER</span><br><span style='font-size:2.2rem; font-weight:700; color:#E5C158;'>{used_slots} / {state['weekly_cap']}</span></div>", unsafe_allow_html=True)
        
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Left Entry Console / Right Active Grid Layout Split
    left_pane, right_pane = st.columns([1, 2])
    
    with left_pane:
        st.markdown("<h3>📥 DATA INJECTION LINE</h3>", unsafe_allow_html=True)
        with st.form("tip_form", clear_on_submit=True):
            f_horse = st.text_input("HORSE IDENTIFIER")
            f_race = st.text_input("RACE TRACK & TIME")
            f_odds = st.number_input("ADVISED DECIMAL ODDS", min_value=0.0, step=0.01, format="%.2f")
            f_stake = st.number_input("STAKE ALLOCATION (£)", min_value=1.0, value=10.0)
            f_bookie = st.text_input("MARKET BOOKMAKER")
            
            if st.form_submit_button("SYNC TO LEDGER"):
                if used_slots >= state['weekly_cap']:
                    st.error("⚠️ CAPACITY LIMIT DETECTED: 42-tip structural cap reached!")
                elif f_odds < 1.70:
                    st.error("❌ STRATEGIC BOUNDARY FILTER: Odds drop below mandatory 1.70 floor.")
                elif not f_horse or not f_race:
                    st.warning("⚠️ CRITERIA ERROR: Complete all missing metrics fields to log.")
                else:
                    new_id = max([t['id'] for t in state['tips_logged']]) + 1 if state['tips_logged'] else 0
                    new_tip = {"id": new_id, "horse": f_horse, "race": f_race, "odds": f_odds, "stake": f_stake, "bookmaker": f_bookie, "status": "Pending"}
                    state['tips_logged'].append(new_tip)
                    with open(DB_FILE, 'w') as f:
                        json.dump(state, f, indent=4)
                    st.success(f"✅ Telemetry Synced: {f_horse} secured into local block storage.")
                    st.rerun()
                    
    with right_pane:
        st.markdown("<h3>📋 ACTIVE LEDGER REAL-TIME GRID</h3>", unsafe_allow_html=True)
        if state['tips_logged']:
            df = pd.DataFrame(state['tips_logged'])
            st.dataframe(df.style.set_properties(**{'background-color': '#0B0B0F', 'color': '#E5C158', 'border-color': 'rgba(229,193,88,0.1)'}), use_container_width=True)
            
            # Interactive Multi-Function Execution Matrix Panel
            st.markdown("<h3>⚡ ACTIVE LINE SETTLEMENT & DELETION MATRIX</h3>", unsafe_allow_html=True)
            options = [f"{t['id']} | {t['horse']} ({t['race']}) [Status: {t['status']}]" for t in state['tips_logged']]
            selected_entry = st.selectbox("TARGET LEDGER TRANSACTION LINE:", options)
            target_id = int(selected_entry.split(" | ")[0])
            
            s_col1, s_col2, s_col3 = st.columns(3)
            with s_col1:
                if st.button("🔴 SETTLE WIN"):
                    for t in state['tips_logged']:
                        if t['id'] == target_id and t['status'] == "Pending":
                            t['status'] = "Won"
                            profit = (t['stake'] * t['odds']) - t['stake']
                            state['core_reserve'] += profit
                    with open(DB_FILE, 'w') as f:
                        json.dump(state, f, indent=4)
                    st.rerun()
            with s_col2:
                if st.button("⚪ SETTLE LOSS"):
                    for t in state['tips_logged']:
                        if t['id'] == target_id and t['status'] == "Pending":
                            t['status'] = "Lost"
                            state['core_reserve'] -= t['stake']
                    with open(DB_FILE, 'w') as f:
                        json.dump(state, f, indent=4)
                    st.rerun()
            with s_col3:
                if st.button("🗑️ PURGE LINE"):
                    state['tips_logged'] = [t for t in state['tips_logged'] if t['id'] != target_id]
                    with open(DB_FILE, 'w') as f:
                        json.dump(state, f, indent=4)
                    
