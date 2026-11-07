"""
FasalMitra AI - Crop Intelligence & Extension Readiness Section
"""
import streamlit as st
from config import SUPPORTED_CROPS
from utils.crop_data import get_pest_details

def render_crop_intelligence():
    """Renders multi-crop agronomic profile, model mapping, and extensibility."""
    st.markdown("### 🌾 Multi-Crop Pest Intelligence")
    st.markdown(
        "Explore pest vulnerability matrices across 8 primary agricultural crops. "
        "FasalMitra connects verified IP102 neural classes to real-world crop protection workflows."
    )

    crop_names = list(SUPPORTED_CROPS.keys())
    selected_crop_tab = st.selectbox(
        "Select Crop to Inspect Intelligence:",
        options=crop_names,
        format_func=lambda c: f"{SUPPORTED_CROPS[c]['icon']} {c} ({SUPPORTED_CROPS[c]['scientific_name']})"
    )

    crop_data = SUPPORTED_CROPS[selected_crop_tab]
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Crop Header Card
    st.markdown(f"""
    <div style="background:#14271C; border:1px solid #284A36; border-radius:8px; padding:1.5rem; margin-bottom:1.5rem;">
        <div style="display:flex; align-items:center; gap:12px; margin-bottom:0.8rem;">
            <span style="font-size:2.2rem;">{crop_data['icon']}</span>
            <div>
                <h3 style="margin:0; color:#F0FDF4;">{selected_crop_tab} Intelligence Matrix</h3>
                <span style="font-size:0.9rem; color:#34D399; font-style:italic;">{crop_data['scientific_name']}</span>
            </div>
        </div>
        <p style="color:#9CA3AF; margin-bottom:0.5rem; font-size:0.95rem;">{crop_data['description']}</p>
        <div style="margin-top:0.8rem;">
            <span class="status-badge">Mapped IP102 Model Pests: {len(crop_data['pests'])}</span>
            <span style="margin-left:8px; font-size:0.8rem; color:#6B7280;">Architecture: YOLO11s Multiclass</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Two column layout: Left: Pests detected by current model, Right: Extensibility & Future Models
    col_left, col_right = st.columns([1.2, 0.8])

    with col_left:
        st.markdown(f"#### 🔍 Covered Pests in {selected_crop_tab}")
        st.caption("Pests identifiable by the current pretrained YOLO11s model:")

        for pest_name in crop_data["pests"]:
            details = get_pest_details(pest_name)
            with st.expander(f"🐛 {details.get('common_name', pest_name)} ({details.get('scientific_name', '')})"):
                st.markdown(f"**Field Symptoms:** {details.get('symptoms', 'N/A')}")
                st.markdown(f"**Vulnerable Crop Stage:** `{details.get('damage_stage', 'All stages')}`")
                st.markdown(f"**ETL Benchmark:** `{details.get('etl', 'N/A')}`")
                
                ipm = details.get("ipm", {})
                st.markdown(f"**IPM Cultural:** {ipm.get('cultural', 'N/A')}")
                st.markdown(f"**IPM Biological:** {ipm.get('biological', 'N/A')}")
                st.markdown(f"**IPM Chemical:** {ipm.get('chemical', 'N/A')}")

    with col_right:
        st.markdown("#### 🚀 Modular Extensibility Framework")
        st.markdown(f"""
        <div style="background:#14271C; border:1px solid #284A36; border-radius:8px; padding:1.2rem; margin-bottom:1rem;">
            <h5 style="color:#F0FDF4; margin-bottom:0.4rem;">Crop-Specific Model Slot</h5>
            <p style="font-size:0.85rem; color:#9CA3AF;">
                FasalMitra AI is architected with modular detector slots. While the base YOLO11s model covers 102 broad agricultural pests from IP102, specialized fine-tuned models can be registered into <code>models/</code> without altering interface contracts.
            </p>
            <div style="border-top:1px solid #22382C; padding-top:0.8rem; margin-top:0.8rem;">
                <b style="font-size:0.8rem; color:#34D399;">Planned Crop Fine-Tunes:</b>
                <ul style="font-size:0.82rem; color:#9CA3AF; padding-left:1.2rem; margin-top:0.4rem;">
                    <li><b>Cotton:</b> Pectinophora gossypiella (Pink Bollworm internal damage)</li>
                    <li><b>Rice:</b> Brown plant hopper biometric density scoring</li>
                    <li><b>Citrus:</b> Diaphorina citri (Asian Citrus Psyllid micro-scale nymph detection)</li>
                    <li><b>Tomato:</b> Tuta absoluta (South American Tomato Pinworm leaf mines)</li>
                </ul>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("#### 📐 Model Boundaries & Limitations")
        st.markdown("""
        <div style="background:rgba(245, 158, 11, 0.08); border:1px solid rgba(245, 158, 11, 0.3); border-radius:8px; padding:1rem; font-size:0.84rem; color:#E2EBE5;">
            <b>Operational Guardrails:</b>
            <ul style="padding-left:1.2rem; margin:0.4rem 0 0 0;">
                <li>The model identifies external visible insect pests, larval stages, and prominent damage signatures.</li>
                <li>Root endoparasitic nematodes and microscopic viral/fungal pathogens without macroscopic vector insects require lab tissue assays.</li>
                <li>Lighting conditions and extreme motion blur degrade confidence; users should take photos under uniform daylight.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
