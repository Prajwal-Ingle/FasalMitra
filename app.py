"""
FasalMitra AI (फसल मित्र) — Playful Neo-Brutalist Agricultural Vision Platform
Main Application Entrypoint
"""
import streamlit as st
from PIL import Image

# 1. Page Configuration
st.set_page_config(
    page_title="FasalMitra AI | Crop Pest Protection",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Module Imports
from config import APP_NAME, APP_HINDI_NAME, APP_TAGLINE, APP_VERSION
from components.styles import inject_custom_styles
from components.header import render_header
from core.detector import get_detector
from pages.dashboard import render_dashboard
from pages.detector_page import render_detector_page
from pages.knowledge_center import render_knowledge_center
from pages.history_page import render_history_page
from pages.about_page import render_about_page

# 3. Inject Neo-Brutalist Styling
inject_custom_styles()

# 4. Initialize Session State
if "detection_history" not in st.session_state:
    st.session_state["detection_history"] = []

if "current_nav_page" not in st.session_state:
    st.session_state["current_nav_page"] = "Home"

# 5. Cached Model Loader (Internal only, zero jargon shown to farmer)
@st.cache_resource(show_spinner=False)
def load_detector():
    """Initializes and caches the trained pest detection model."""
    return get_detector()

detector = load_detector()

# 6. Neo-Brutalist Sidebar Navigation
with st.sidebar:
    st.markdown(f"""
    <div style="display:flex; align-items:center; gap:12px; margin-bottom:1.5rem; padding-bottom:1rem; border-bottom:2px solid #1E293B;">
        <div style="width:48px; height:48px; border-radius:14px; border:2px solid #1E293B; background:#FCE7F3; display:flex; align-items:center; justify-content:center; font-size:24px; box-shadow:2px 2px 0px #1E293B;">
            🌾
        </div>
        <div>
            <div style="font-size:1.3rem; font-weight:800; color:#1E293B; letter-spacing:-0.02em;">{APP_NAME}</div>
            <div style="font-size:0.85rem; color:#16A34A; font-weight:700;">{APP_HINDI_NAME}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<p style='font-size:0.85rem; font-weight:800; color:#475569; margin-bottom:0.5rem;'>MAIN MENU</p>", unsafe_allow_html=True)

    nav_options = [
        "🏠 Home",
        "🔍 Pest Detection",
        "📚 Pest Knowledge",
        "🕒 My Detections",
        "🌾 About FasalMitra"
    ]

    page_to_option = {
        "Home": "🏠 Home",
        "Pest Detection": "🔍 Pest Detection",
        "Pest Knowledge": "📚 Pest Knowledge",
        "My Detections": "🕒 My Detections",
        "About FasalMitra": "🌾 About FasalMitra"
    }
    option_to_page = {v: k for k, v in page_to_option.items()}

    current_opt = page_to_option.get(st.session_state["current_nav_page"], "🏠 Home")
    selected_option = st.radio(
        "Navigation",
        options=nav_options,
        index=nav_options.index(current_opt),
        label_visibility="collapsed"
    )

    st.session_state["current_nav_page"] = option_to_page[selected_option]

    st.markdown("<br>", unsafe_allow_html=True)
    
    # Neo-Brutalist Status Card in Sidebar
    st.markdown("""
    <div class="neo-card" style="padding:1.1rem; margin-top:1.5rem; box-shadow:3px 3px 0px #1E293B;">
        <div style="display:flex; align-items:center; gap:8px; margin-bottom:6px;">
            <span style="font-size:1.2rem;">🌱</span>
            <b style="font-size:0.95rem; color:#1E293B;">Crop Health AI</b>
        </div>
        <p style="font-size:0.85rem; color:#475569; margin:0; line-height:1.45; font-weight:600;">
            Camera scanner ready to identify crop pests and provide instant organic remedies.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.caption("FasalMitra AI &bull; Instant crop protection for every farmer.")

# 7. Main Presentation Routing
render_header()

if not detector.is_ready:
    st.error("⚠️ The AI detection system is currently loading. Please check back in a moment or refresh the page.")
else:
    active_page = st.session_state["current_nav_page"]
    if active_page == "Home":
        render_dashboard()
    elif active_page == "Pest Detection":
        render_detector_page(detector)
    elif active_page == "Pest Knowledge":
        render_knowledge_center(detector)
    elif active_page == "My Detections":
        render_history_page()
    elif active_page == "About FasalMitra":
        render_about_page()
