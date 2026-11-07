"""
FasalMitra AI - Playful Neo-Brutalist My Detections (Session History)
"""
import streamlit as st
from core.postprocessing import convert_image_to_bytes

def render_history_page():
    """Renders the session detection log in Neo-Brutalist style."""
    
    st.markdown("""
    <div style="margin-bottom:1.5rem;">
        <div class="neo-pill coral">
            <span>Session History & Downloads</span>
        </div>
        <div style="font-size:2.6rem; font-weight:800; color:#1E293B; letter-spacing:-0.02em; margin-bottom:0.4rem;">
            My Detections
        </div>
        <div style="font-size:1.05rem; color:#475569; max-width:640px;">
            Revisit crop photos and diagnoses made during your active session. Photos are kept in memory for your privacy and are never permanently stored.
        </div>
    </div>
    """, unsafe_allow_html=True)

    history = st.session_state.get("detection_history", [])

    col_title, col_clear = st.columns([3, 1.2])
    with col_title:
        st.markdown(f"<div style='font-weight:700; color:#475569;'>Total diagnosed crops in this session: <b>{len(history)}</b></div>", unsafe_allow_html=True)
    with col_clear:
        if history:
            if st.button("🗑️ Clear My History", use_container_width=True):
                st.session_state["detection_history"] = []
                st.rerun()

    if not history:
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("""
        <div class="neo-card" style="text-align:center; padding:3.5rem 1.5rem; border-style:dashed;">
            <div style="font-size:3.5rem; margin-bottom:0.75rem;">📋</div>
            <div style="font-size:1.6rem; font-weight:800; color:#1E293B; margin-bottom:0.4rem;">No Saved Detections Yet</div>
            <div style="font-size:1rem; color:#475569; max-width:440px; margin:0 auto;">
                Any leaf diagnosis you run in the <b>Pest Detection</b> tab will appear here during your current visit so you can easily review findings and download photos.
            </div>
        </div>
        """, unsafe_allow_html=True)
        return

    st.markdown("<br>", unsafe_allow_html=True)

    # Render history cards
    for idx, record in enumerate(reversed(history)):
        item_num = len(history) - idx
        pests_count = record.get("num_detections", 0)
        max_c = record.get("max_confidence", 0.0) * 100.0
        classes_str = ", ".join([k.title() for k in record.get("class_counts", {}).keys()]) or "Healthy Leaf"

        with st.expander(f"Diagnosis #{item_num} — {record.get('source', 'Crop Photo')} ({record.get('timestamp')})", expanded=(idx == 0)):
            col_img, col_details = st.columns([1, 1.2])

            with col_img:
                if "annotated_image" in record and record["annotated_image"] is not None:
                    st.image(record["annotated_image"], caption="Diagnosed Photo", use_container_width=True)

            with col_details:
                st.markdown(f"""
                <div class="neo-card" style="padding:1.2rem; margin-bottom:1rem;">
                    <div style="font-size:0.9rem; font-weight:700; color:#475569; margin-bottom:6px;">Time: <span style="color:#1E293B;">{record.get('timestamp')}</span></div>
                    <div style="font-size:0.9rem; font-weight:700; color:#475569; margin-bottom:6px;">Crop: <span style="color:#16A34A;">{record.get('crop')}</span></div>
                    <div style="font-size:0.9rem; font-weight:700; color:#475569; margin-bottom:6px;">Result: <span style="color:#1E293B;">{classes_str}</span></div>
                    <div style="font-size:0.9rem; font-weight:700; color:#475569;">Match Certainty: <span style="color:#15803D;">{max_c:.0f}%</span></div>
                </div>
                """, unsafe_allow_html=True)

                if "annotated_image" in record and record["annotated_image"] is not None:
                    img_bytes = convert_image_to_bytes(record["annotated_image"])
                    st.download_button(
                        label="📥 Download This Photo",
                        data=img_bytes,
                        file_name=f"FasalMitra_Diagnosis_{item_num}.jpg",
                        mime="image/jpeg",
                        key=f"dl_history_{item_num}",
                        use_container_width=True
                    )
