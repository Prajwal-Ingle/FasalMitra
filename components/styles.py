"""
FasalMitra AI - Playful Neo-Brutalist Design System & Styles
"""
import streamlit as st

def inject_custom_styles():
    """Injects high-craft Playful Neo-Brutalist CSS matching LearnHub visual identity."""
    st.markdown("""
    <style>
    /* Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700;0,9..40,800;1,9..40,400&display=swap');

    /* Global Root & Typography */
    html, body, [class*="css"] {
        font-family: 'DM Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif !important;
        color: #1E293B !important;
        background-color: #FFFDF7 !important;
    }

    .stApp {
        background-color: #FFFDF7 !important;
    }

    .block-container {
        padding-top: 1.5rem;
        padding-bottom: 4.5rem;
        max-width: 1180px;
    }

    /* Hide standard Streamlit header and footer */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Sidebar Styling - Neo-Brutalist */
    section[data-testid="stSidebar"] {
        background-color: #FFFDF7 !important;
        border-right: 2.5px solid #1E293B !important;
    }

    section[data-testid="stSidebar"] .block-container {
        padding-top: 1.5rem;
    }

    /* --- NEO-BRUTALIST FLOATING HEADER --- */
    .neo-header {
        background: #FFFFFF;
        border: 2.5px solid #1E293B;
        border-radius: 22px;
        box-shadow: 4px 4px 0px #1E293B;
        padding: 0.85rem 1.4rem;
        margin-bottom: 2rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
        flex-wrap: wrap;
        gap: 12px;
    }

    .neo-logo-box {
        display: flex;
        align-items: center;
        gap: 12px;
    }

    .neo-logo-icon {
        width: 44px;
        height: 44px;
        border-radius: 12px;
        border: 2px solid #1E293B;
        background: #FCE7F3;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 22px;
        box-shadow: 2px 2px 0px #1E293B;
    }

    .neo-logo-title {
        font-size: 1.45rem;
        font-weight: 800;
        color: #1E293B;
        letter-spacing: -0.02em;
    }

    /* --- NEO-BRUTALIST PILL BADGES --- */
    .neo-pill {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        padding: 6px 16px;
        border-radius: 9999px;
        border: 2px solid #1E293B;
        font-weight: 700;
        font-size: 0.85rem;
        box-shadow: 2px 2px 0px #1E293B;
        margin-bottom: 1rem;
        line-height: 1.2;
    }

    .neo-pill.mint {
        background: #DCFCE7;
        color: #15803D;
    }

    .neo-pill.blue {
        background: #BAE6FD;
        color: #0369A1;
    }

    .neo-pill.coral {
        background: #FED7AA;
        color: #C2410C;
    }

    .neo-pill.yellow {
        background: #FEF08A;
        color: #A16207;
    }

    /* --- NEO-BRUTALIST CARDS --- */
    .neo-card {
        background: #FFFFFF;
        border: 2.5px solid #1E293B;
        border-radius: 20px;
        box-shadow: 4px 4px 0px #1E293B;
        padding: 1.6rem;
        margin-bottom: 1.5rem;
        position: relative;
        transition: transform 0.15s ease, box-shadow 0.15s ease;
    }

    .neo-card:hover {
        transform: translate(-2px, -2px);
        box-shadow: 6px 6px 0px #1E293B;
    }

    .neo-card-title {
        font-size: 1.25rem;
        font-weight: 800;
        color: #1E293B;
        margin-bottom: 0.4rem;
        letter-spacing: -0.01em;
    }

    .neo-card-desc {
        font-size: 0.95rem;
        color: #475569;
        line-height: 1.6;
    }

    /* Decorative Corner Icon Badges */
    .corner-badge {
        position: absolute;
        width: 38px;
        height: 38px;
        border-radius: 12px;
        border: 2px solid #1E293B;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 18px;
        box-shadow: 2px 2px 0px #1E293B;
    }

    .corner-badge.top-right {
        top: -14px;
        right: -14px;
        background: #FED7AA;
    }

    .corner-badge.bottom-right {
        bottom: -14px;
        right: -14px;
        background: #DCFCE7;
        border-radius: 50%;
    }

    .corner-badge.bottom-left {
        bottom: -14px;
        left: -14px;
        background: #E0E7FF;
    }

    /* --- TYPOGRAPHY HERO --- */
    .neo-hero-title {
        font-size: 3rem;
        font-weight: 800;
        color: #1E293B;
        line-height: 1.15;
        letter-spacing: -0.03em;
        margin-bottom: 1rem;
    }

    .neo-hero-green {
        color: #22C55E !important;
    }

    .neo-hero-desc {
        font-size: 1.1rem;
        color: #475569;
        line-height: 1.65;
        margin-bottom: 1.8rem;
        max-width: 580px;
    }

    /* --- NEO-BRUTALIST BUTTONS (Streamlit Overrides) --- */
    div.stButton > button {
        background-color: #22C55E !important;
        color: #FFFFFF !important;
        border: 2.5px solid #1E293B !important;
        border-radius: 14px !important;
        font-weight: 800 !important;
        font-size: 1.05rem !important;
        min-height: 52px !important;
        padding: 0.75rem 1.8rem !important;
        box-shadow: 4px 4px 0px #1E293B !important;
        cursor: pointer !important;
        transition: transform 0.1s ease, box-shadow 0.1s ease !important;
    }

    div.stButton > button:hover {
        background-color: #16A34A !important;
        transform: translate(2px, 2px) !important;
        box-shadow: 2px 2px 0px #1E293B !important;
        color: #FFFFFF !important;
    }

    div.stButton > button:active {
        transform: translate(4px, 4px) !important;
        box-shadow: 0px 0px 0px #1E293B !important;
    }

    /* Secondary Download Buttons */
    div.stDownloadButton > button {
        background-color: #93C5FD !important;
        color: #1E293B !important;
        border: 2.5px solid #1E293B !important;
        border-radius: 14px !important;
        font-weight: 800 !important;
        font-size: 1rem !important;
        min-height: 48px !important;
        padding: 0.7rem 1.5rem !important;
        box-shadow: 4px 4px 0px #1E293B !important;
        transition: all 0.1s ease !important;
    }

    div.stDownloadButton > button:hover {
        background-color: #BAE6FD !important;
        transform: translate(2px, 2px) !important;
        box-shadow: 2px 2px 0px #1E293B !important;
        color: #1E293B !important;
    }

    /* --- RADIO BUTTONS (Neo-Brutalist Pill Tabs) --- */
    div[data-testid="stRadio"] > div {
        display: flex;
        gap: 12px;
        flex-wrap: wrap;
    }

    div[data-testid="stRadio"] label {
        background: #FFFFFF;
        border: 2px solid #1E293B;
        border-radius: 12px;
        padding: 10px 18px;
        box-shadow: 3px 3px 0px #1E293B;
        font-weight: 700;
        cursor: pointer;
        transition: all 0.1s ease;
    }

    div[data-testid="stRadio"] label:hover {
        transform: translate(1px, 1px);
        box-shadow: 2px 2px 0px #1E293B;
    }

    /* --- INPUT CONTAINERS --- */
    div[data-testid="stCameraInput"], div[data-testid="stFileUploader"] {
        background: #FFFFFF;
        border: 2.5px solid #1E293B;
        border-radius: 18px;
        box-shadow: 4px 4px 0px #1E293B;
        padding: 1.2rem;
    }

    /* Input text fields & selectboxes */
    div[data-baseweb="input"], div[data-baseweb="select"] {
        border: 2px solid #1E293B !important;
        border-radius: 12px !important;
        box-shadow: 2px 2px 0px #1E293B !important;
    }

    /* --- TABS --- */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
        background: transparent;
        padding: 0;
        border: none;
    }

    .stTabs [data-baseweb="tab"] {
        background: #FFFFFF !important;
        border: 2px solid #1E293B !important;
        border-radius: 12px !important;
        padding: 10px 20px !important;
        font-weight: 700 !important;
        color: #1E293B !important;
        box-shadow: 3px 3px 0px #1E293B !important;
    }

    .stTabs [aria-selected="true"] {
        background: #DCFCE7 !important;
        color: #15803D !important;
        transform: translate(2px, 2px);
        box-shadow: 1px 1px 0px #1E293B !important;
    }

    /* --- EXPANDERS --- */
    .streamlit-expanderHeader {
        background-color: #FFFFFF !important;
        border-radius: 14px !important;
        border: 2px solid #1E293B !important;
        box-shadow: 3px 3px 0px #1E293B !important;
        font-weight: 800 !important;
        color: #1E293B !important;
        padding: 1rem 1.2rem !important;
    }

    .streamlit-expanderContent {
        background-color: #FFFFFF !important;
        border: 2px solid #1E293B !important;
        border-top: none !important;
        border-bottom-left-radius: 14px !important;
        border-bottom-right-radius: 14px !important;
        box-shadow: 3px 3px 0px #1E293B !important;
        padding: 1.4rem !important;
    }

    /* Section Blue Canvas (for CTA & Special Areas like Image 5) */
    .neo-canvas-blue {
        background-color: #D9EBF5;
        border: 2.5px solid #1E293B;
        border-radius: 24px;
        box-shadow: 5px 5px 0px #1E293B;
        padding: 2.5rem 1.8rem;
        margin-top: 2rem;
        margin-bottom: 2rem;
    }
    </style>
    """, unsafe_allow_html=True)
