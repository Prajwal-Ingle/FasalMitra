"""
FasalMitra AI - Playful Neo-Brutalist Pest Detection Studio
"""
import streamlit as st
import os
from datetime import datetime
from PIL import Image

from config import DEFAULT_CONF_THRESHOLD, DEFAULT_IOU_THRESHOLD, SUPPORTED_CROPS, SAMPLES_DIR
from core.preprocessing import validate_image_file, load_and_preprocess_image
from core.postprocessing import (
    draw_annotated_image, calculate_infestation_severity, 
    convert_image_to_bytes, build_detection_report
)
from utils.crop_data import get_pest_details

def render_detector_page(detector):
    """Renders the main, distraction-free pest detection studio in Neo-Brutalist style."""
    
    st.markdown("""
    <div style="margin-bottom:1.5rem;">
        <div class="neo-pill mint">
            <span style="font-size:1.1rem;">●</span>
            <span>Real-Time AI Vision Scanner</span>
        </div>
        <div style="font-size:2.6rem; font-weight:800; color:#1E293B; letter-spacing:-0.02em; margin-bottom:0.4rem;">
            Inspect Crop Foliage
        </div>
        <div style="font-size:1.05rem; color:#475569; max-width:640px;">
            Point your camera at a crop leaf or upload an image to identify insect pests and receive practical field remedies.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # 1. Mode Selector (Neo-Brutalist Style)
    input_choice = st.radio(
        "Choose Input Method:",
        options=["📸 Take Photo with Camera", "📁 Upload Image from Device", "🌾 Use a Sample Crop Photo"],
        horizontal=True,
        index=0 if "selected_sample_for_nav" not in st.session_state else 2
    )

    image_to_process = None
    source_label = "Crop Photo"

    st.markdown("<br>", unsafe_allow_html=True)

    # --- Option A: Camera Capture ---
    if input_choice == "📸 Take Photo with Camera":
        st.markdown("""
        <div class="neo-card" style="margin-bottom:1.2rem;">
            <div style="display:flex; align-items:center; gap:12px; margin-bottom:0.6rem;">
                <div style="width:40px; height:40px; border-radius:10px; border:2px solid #1E293B; background:#BAE6FD; display:flex; align-items:center; justify-content:center; font-size:20px; box-shadow:2px 2px 0px #1E293B;">
                    📸
                </div>
                <div class="neo-card-title" style="margin:0;">Live Camera Scanner</div>
            </div>
            <div class="neo-card-desc">
                Point your phone or webcam closely at the affected leaf or insect. Tap <b>Take Photo</b> to freeze the frame.
            </div>
        </div>
        """, unsafe_allow_html=True)

        camera_capture = st.camera_input("Point camera at leaf or pest")

        if camera_capture is not None:
            img_obj, err = load_and_preprocess_image(camera_capture)
            if err:
                st.error(f"Camera Image Error: {err}")
            else:
                image_to_process = img_obj
                source_label = f"Camera Photo ({datetime.now().strftime('%H:%M:%S')})"
                st.success("✅ Photo captured! Review below and tap 'Run Pest Diagnosis'.")

    # --- Option B: File Upload ---
    elif input_choice == "📁 Upload Image from Device":
        st.markdown("""
        <div class="neo-card" style="margin-bottom:1.2rem;">
            <div style="display:flex; align-items:center; gap:12px; margin-bottom:0.6rem;">
                <div style="width:40px; height:40px; border-radius:10px; border:2px solid #1E293B; background:#FED7AA; display:flex; align-items:center; justify-content:center; font-size:20px; box-shadow:2px 2px 0px #1E293B;">
                    📁
                </div>
                <div class="neo-card-title" style="margin:0;">Upload Crop Photo</div>
            </div>
            <div class="neo-card-desc">
                Select an image from your gallery. Supports JPG, JPEG, PNG, and WEBP formats.
            </div>
        </div>
        """, unsafe_allow_html=True)

        uploaded_file = st.file_uploader(
            "Select an image file:",
            type=["jpg", "jpeg", "png", "webp"],
            help="High-contrast, well-lit photos provide highest detection certainty."
        )

        if uploaded_file is not None:
            is_valid, msg = validate_image_file(uploaded_file)
            if not is_valid:
                st.error(f"Image Error: {msg}")
            else:
                img_obj, err = load_and_preprocess_image(uploaded_file)
                if err:
                    st.error(f"Image Read Error: {err}")
                else:
                    image_to_process = img_obj
                    source_label = uploaded_file.name

    # --- Option C: Sample Photos ---
    elif input_choice == "🌾 Use a Sample Crop Photo":
        sample_files = [f for f in os.listdir(SAMPLES_DIR) if f.lower().endswith((".jpg", ".jpeg", ".png"))]
        
        default_idx = 0
        preset_sample = st.session_state.pop("selected_sample_for_nav", None)
        if preset_sample and preset_sample in sample_files:
            default_idx = sample_files.index(preset_sample)

        selected_sample = st.selectbox(
            "Select a preloaded agricultural test photo:",
            options=sample_files,
            index=default_idx,
            format_func=lambda x: f"🌿 {x.replace('_', ' ').replace('.jpg', '').title()}"
        )

        if selected_sample:
            sample_path = SAMPLES_DIR / selected_sample
            img_obj, err = load_and_preprocess_image(str(sample_path))
            if err:
                st.error(f"Error loading sample: {err}")
            else:
                image_to_process = img_obj
                source_label = selected_sample

    # Empty State Display
    if image_to_process is None:
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("""
        <div class="neo-card" style="text-align:center; padding:3.5rem 1.5rem; border-style:dashed;">
            <div style="font-size:3.5rem; margin-bottom:0.75rem;">🌱</div>
            <div style="font-size:1.6rem; font-weight:800; color:#1E293B; margin-bottom:0.4rem;">No Photo Selected Yet</div>
            <div style="font-size:1rem; color:#475569; max-width:440px; margin:0 auto;">
                Capture a photo using the live camera or upload a picture from your device above to begin instant diagnosis.
            </div>
        </div>
        """, unsafe_allow_html=True)
        return

    # Image Loaded: Action & Execution Area
    st.markdown("<br>", unsafe_allow_html=True)

    col_crop_sel, col_blank = st.columns([1.5, 1])
    with col_crop_sel:
        crop_names = ["General Field Crop"] + list(SUPPORTED_CROPS.keys())
        selected_crop = st.selectbox(
            "Crop Category (Optional):",
            options=crop_names,
            index=0,
            help="Selecting the crop helps tailor the organic and field remedies."
        )

    # Advanced Sensitivity (Optional Expander)
    with st.expander("⚙️ Sensitivity & Detection Options (Optional)", expanded=False):
        conf_threshold = st.slider(
            "Detection Sensitivity Threshold",
            min_value=0.10,
            max_value=0.90,
            value=float(st.session_state.get("conf_threshold_val", DEFAULT_CONF_THRESHOLD)),
            step=0.05
        )
        st.session_state["conf_threshold_val"] = conf_threshold

    if "conf_threshold_val" not in st.session_state:
        conf_threshold = DEFAULT_CONF_THRESHOLD
    else:
        conf_threshold = st.session_state["conf_threshold_val"]

    # Action Buttons
    col_run_btn, col_retake_btn = st.columns([1.5, 1])
    with col_run_btn:
        run_detection = st.button("⚡ Run Pest Diagnosis", use_container_width=True)
    with col_retake_btn:
        if st.button("🔄 Retake / Clear Photo", use_container_width=True):
            st.rerun()

    # Cached execution
    cache_key = f"diagnose_{source_label}_{conf_threshold}"

    if run_detection or cache_key not in st.session_state:
        with st.spinner("Analyzing foliage with agricultural vision..."):
            detection_res = detector.predict(
                image=image_to_process,
                conf_threshold=conf_threshold,
                iou_threshold=DEFAULT_IOU_THRESHOLD
            )
            annotated_img = draw_annotated_image(image_to_process, detection_res)

            st.session_state[cache_key] = {
                "results": detection_res,
                "annotated_image": annotated_img,
                "timestamp": datetime.now().strftime("%I:%M %p, %d %b %Y")
            }

            # Add to session history
            history = st.session_state.setdefault("detection_history", [])
            history.append({
                "timestamp": datetime.now().strftime("%I:%M %p, %d %b %Y"),
                "source": source_label,
                "crop": selected_crop,
                "num_detections": detection_res.get("num_detections", 0),
                "class_counts": detection_res.get("class_counts", {}),
                "max_confidence": detection_res.get("max_confidence", 0.0),
                "annotated_image": annotated_img,
                "original_image": image_to_process,
                "boxes": detection_res.get("boxes", [])
            })

    # Retrieve current data
    current_data = st.session_state.get(cache_key)
    if not current_data:
        return

    detection_res = current_data["results"]
    annotated_img = current_data["annotated_image"]

    num_detections = detection_res.get("num_detections", 0)
    max_conf = detection_res.get("max_confidence", 0.0) * 100.0
    class_counts = detection_res.get("class_counts", {})
    severity = calculate_infestation_severity(num_detections, detection_res.get("max_confidence", 0.0))

    st.markdown("<br>", unsafe_allow_html=True)

    # =========================================================================
    # DIAGNOSIS VERDICT CARD (Neo-Brutalist Presentation)
    # =========================================================================
    if num_detections == 0:
        st.markdown(f"""
        <div class="neo-card" style="background:#F0FDF4; box-shadow:6px 6px 0px #1E293B;">
            <div style="display:flex; align-items:center; gap:16px;">
                <div style="width:54px; height:54px; border-radius:14px; border:2px solid #1E293B; background:#DCFCE7; display:flex; align-items:center; justify-content:center; font-size:28px; box-shadow:2px 2px 0px #1E293B;">
                    ✅
                </div>
                <div>
                    <div style="font-size:1.5rem; font-weight:800; color:#15803D; margin-bottom:4px;">Great News! No Pests Detected</div>
                    <div style="font-size:0.95rem; color:#1E293B;">
                        Our vision scanner analyzed your photo and found no signs of common crop pests. Your foliage looks healthy and clean!
                    </div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        pest_names_list = ", ".join([p.title() for p in class_counts.keys()])
        st.markdown(f"""
        <div class="neo-card" style="box-shadow:6px 6px 0px #1E293B;">
            <div style="display:flex; justify-content:space-between; align-items:flex-start; flex-wrap:wrap; gap:12px;">
                <div>
                    <div class="neo-pill coral">
                        <span>⚠️ {severity['badge']}</span>
                    </div>
                    <div style="font-size:1.8rem; font-weight:800; color:#1E293B; margin-bottom:6px;">
                        {num_detections} Pest Specimen(s) Located: {pest_names_list}
                    </div>
                    <div style="font-size:1rem; color:#475569; max-width:620px;">
                        {severity['description']}
                    </div>
                </div>
                <div style="text-align:right;">
                    <div style="font-size:0.85rem; font-weight:700; color:#475569;">Match Certainty</div>
                    <div style="font-size:2.2rem; font-weight:800; color:#15803D;">{max_conf:.0f}%</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Visual Inspection (Annotated vs Original)
    tab_marked, tab_orig = st.tabs(["🎯 Identified Pests (Marked)", "🖼️ Original Leaf Photo"])
    with tab_marked:
        st.image(annotated_img, caption="FasalMitra AI Marked Photo (Coloured boxes highlight located pests)", use_container_width=True)
    with tab_orig:
        st.image(image_to_process, caption="Your Original Photo", use_container_width=True)

    # Actionable 3-Pillar Practical Remedies (Matching Image 3 & 4 Card Format)
    if num_detections > 0:
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("### 🌾 Practical Field Remedies & Action Steps")

        for pest_name, count in class_counts.items():
            details = get_pest_details(pest_name)
            common_title = details.get("common_name", pest_name.title())
            hindi_sub = f" ({details.get('hindi_name')})" if details.get("hindi_name") else ""

            st.markdown(f"#### 🐛 Recommended Care for {common_title}{hindi_sub}")
            st.caption(f"**How to Confirm on Plant:** {details.get('how_to_spot', 'Check leaf surfaces for feeding punctures.')}")

            r_col1, r_col2, r_col3 = st.columns(3)
            with r_col1:
                st.markdown(f"""
                <div class="neo-card" style="height:100%;">
                    <div style="width:40px; height:40px; border-radius:10px; border:2px solid #1E293B; background:#DCFCE7; display:flex; align-items:center; justify-content:center; font-size:20px; box-shadow:2px 2px 0px #1E293B; margin-bottom:0.75rem;">
                        🌿
                    </div>
                    <div class="neo-card-title" style="font-size:1.1rem;">Organic Care</div>
                    <div class="neo-card-desc">{details.get('prevention_organic', 'Apply neem oil spray every 10 days.')}</div>
                </div>
                """, unsafe_allow_html=True)

            with r_col2:
                st.markdown(f"""
                <div class="neo-card" style="height:100%;">
                    <div style="width:40px; height:40px; border-radius:10px; border:2px solid #1E293B; background:#FEF08A; display:flex; align-items:center; justify-content:center; font-size:20px; box-shadow:2px 2px 0px #1E293B; margin-bottom:0.75rem;">
                        🐞
                    </div>
                    <div class="neo-card-title" style="font-size:1.1rem;">Natural Allies</div>
                    <div class="neo-card-desc">{details.get('natural_predators', 'Friendly spiders and ladybirds hunt this pest.')}</div>
                </div>
                """, unsafe_allow_html=True)

            with r_col3:
                st.markdown(f"""
                <div class="neo-card" style="height:100%;">
                    <div style="width:40px; height:40px; border-radius:10px; border:2px solid #1E293B; background:#BAE6FD; display:flex; align-items:center; justify-content:center; font-size:20px; box-shadow:2px 2px 0px #1E293B; margin-bottom:0.75rem;">
                        🧪
                    </div>
                    <div class="neo-card-title" style="font-size:1.1rem;">Field Treatment</div>
                    <div class="neo-card-desc">{details.get('recommended_treatment', 'Apply registered medicine if population spreads.')}</div>
                </div>
                """, unsafe_allow_html=True)

    # Save & Download Section
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### 💾 Save Your Diagnosis")

    dl_col1, dl_col2 = st.columns(2)
    with dl_col1:
        img_bytes = convert_image_to_bytes(annotated_img)
        st.download_button(
            label="📥 Download Marked Photo (JPEG)",
            data=img_bytes,
            file_name=f"FasalMitra_{source_label.replace(' ', '_')}.jpg",
            mime="image/jpeg",
            use_container_width=True
        )
    with dl_col2:
        report_text = build_detection_report(detection_res, crop_context=selected_crop)
        st.download_button(
            label="📄 Download Diagnostic Summary",
            data=report_text,
            file_name=f"FasalMitra_Summary_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
            mime="application/json",
            use_container_width=True
        )
