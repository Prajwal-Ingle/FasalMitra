"""
FasalMitra AI - Session Analytics & Agronomic Telemetry Section
"""
import streamlit as st
from utils.visualization import (
    create_pest_bar_chart, create_confidence_histogram, 
    create_crop_distribution_pie, create_session_timeline_chart
)

def render_analytics_page():
    """Renders real-time telemetry and distribution charts strictly from session telemetry."""
    st.markdown("### 📊 Session Diagnostic Analytics")
    st.markdown("Visual analytics synthesized dynamically from pest detections conducted during this active browser session.")

    history = st.session_state.get("detection_history", [])

    if not history:
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("""
        <div style="background:#14271C; border:2px dashed #284A36; border-radius:12px; padding:3.5rem 1.5rem; text-align:center;">
            <div style="font-size:3rem; margin-bottom:0.75rem;">📈</div>
            <h4 style="color:#F0FDF4; margin-bottom:0.4rem;">No Session Analytics Available</h4>
            <p style="color:#9CA3AF; max-width:480px; margin:0 auto; font-size:0.9rem;">
                Perform diagnostic scans in the <b>AI Pest Detection</b> studio or test with sample images to populate real session telemetry. 
                FasalMitra does not synthesize fake analytics.
            </p>
        </div>
        """, unsafe_allow_html=True)
        return

    # Aggregate session data
    total_scans = len(history)
    total_pests = sum(h.get("num_detections", 0) for h in history)
    all_confidences = []
    aggregated_classes = {}

    for h in history:
        for b in h.get("boxes", []):
            if "confidence" in b:
                all_confidences.append(b["confidence"])
            cls_name = b.get("class_name", "Unknown")
            aggregated_classes[cls_name] = aggregated_classes.get(cls_name, 0) + 1

    avg_pests_per_scan = (total_pests / total_scans) if total_scans > 0 else 0.0
    avg_conf = (sum(all_confidences) / len(all_confidences) * 100.0) if all_confidences else 0.0

    # Summary KPI Bar
    k1, k2, k3, k4 = st.columns(4)
    with k1:
        st.markdown(f"""
        <div class="fm-card">
            <div class="fm-card-header">Total Session Scans</div>
            <div class="fm-metric-val">{total_scans}</div>
            <div class="fm-metric-sub">Active Session</div>
        </div>
        """, unsafe_allow_html=True)
    with k2:
        st.markdown(f"""
        <div class="fm-card">
            <div class="fm-card-header">Pests Counted</div>
            <div class="fm-metric-val">{total_pests}</div>
            <div class="fm-metric-sub">{avg_pests_per_scan:.1f} Pests / Scan</div>
        </div>
        """, unsafe_allow_html=True)
    with k3:
        st.markdown(f"""
        <div class="fm-card">
            <div class="fm-card-header">Distinct Species</div>
            <div class="fm-metric-val">{len(aggregated_classes)}</div>
            <div class="fm-metric-sub">Identified In Session</div>
        </div>
        """, unsafe_allow_html=True)
    with k4:
        st.markdown(f"""
        <div class="fm-card">
            <div class="fm-card-header">Mean Confidence</div>
            <div class="fm-metric-val">{avg_conf:.1f}<span style="font-size:1.1rem;color:#9CA3AF;">%</span></div>
            <div class="fm-metric-sub">Across All Detections</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Plotly Charts Row 1: Species Distribution & Confidence Histogram
    col_chart1, col_chart2 = st.columns(2)
    with col_chart1:
        fig_bar = create_pest_bar_chart(aggregated_classes)
        st.plotly_chart(fig_bar, use_container_width=True)
    with col_chart2:
        fig_hist = create_confidence_histogram(all_confidences)
        st.plotly_chart(fig_hist, use_container_width=True)

    # Plotly Charts Row 2: Crop Distribution & Session Timeline
    col_chart3, col_chart4 = st.columns(2)
    with col_chart3:
        fig_pie = create_crop_distribution_pie(history)
        st.plotly_chart(fig_pie, use_container_width=True)
    with col_chart4:
        fig_time = create_session_timeline_chart(history)
        st.plotly_chart(fig_time, use_container_width=True)
