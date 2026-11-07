"""
FasalMitra AI - Floating Neo-Brutalist Header
"""
import streamlit as st
from config import APP_NAME, APP_HINDI_NAME

def render_header():
    """Renders the floating neo-brutalist navigation header matching the LearnHub aesthetic."""
    st.markdown(f"""
    <div class="neo-header">
        <div class="neo-logo-box">
            <div class="neo-logo-icon">🌾</div>
            <div>
                <span class="neo-logo-title">{APP_NAME}</span>
                <span style="font-size:0.95rem; font-weight:700; color:#16A34A; margin-left:6px;">({APP_HINDI_NAME})</span>
            </div>
        </div>
        <div style="display:flex; align-items:center; gap:20px; font-weight:700; font-size:0.95rem; color:#475569; flex-wrap:wrap;">
            <span style="color:#1E293B;">Home</span>
            <span style="color:#475569;">Pest Detection</span>
            <span style="color:#475569;">Pest Knowledge</span>
            <span style="color:#475569;">My Detections</span>
            <span style="color:#475569;">About</span>
        </div>
        <div style="display:flex; align-items:center; gap:12px;">
            <div style="display:inline-flex; align-items:center; gap:6px; background:#DCFCE7; border:2px solid #1E293B; border-radius:12px; padding:6px 14px; font-weight:800; font-size:0.85rem; box-shadow:2px 2px 0px #1E293B; color:#15803D;">
                <span style="width:8px; height:8px; border-radius:50%; background:#16A34A; display:inline-block;"></span>
                <span>Diagnosis Ready</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
