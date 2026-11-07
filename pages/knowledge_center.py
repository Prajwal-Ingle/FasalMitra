"""
FasalMitra AI - Playful Neo-Brutalist Pest Knowledge Centre
"""
import streamlit as st
from config import SUPPORTED_CROPS
from utils.crop_data import PEST_INTELLIGENCE, get_pest_details

def render_knowledge_center(detector):
    """Renders the friendly, educational pest encyclopedia in Neo-Brutalist style."""
    
    st.markdown("""
    <div style="margin-bottom:1.5rem;">
        <div class="neo-pill blue">
            <span>Pest Library & Remedies</span>
        </div>
        <div style="font-size:2.6rem; font-weight:800; color:#1E293B; letter-spacing:-0.02em; margin-bottom:0.4rem;">
            Pest Knowledge Centre
        </div>
        <div style="font-size:1.05rem; color:#475569; max-width:640px;">
            Learn how to recognize common crop pests in the field, spot early damage symptoms, and protect your crops naturally.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Search and Filter
    col_search, col_crop = st.columns([2, 1.2])
    with col_search:
        search_query = st.text_input("🔍 Search by Pest Name or Symptom:", placeholder="e.g. aphid, borer, fly, caterpillar, hopper...")
    with col_crop:
        crop_filter = st.selectbox(
            "Filter by Crop:",
            options=["All Crops"] + list(SUPPORTED_CROPS.keys())
        )

    all_pests = list(PEST_INTELLIGENCE.keys())

    # Filter logic
    filtered = []
    for p in all_pests:
        info = PEST_INTELLIGENCE[p]
        matches_search = True
        if search_query:
            q = search_query.lower()
            matches_search = (
                q in p.lower() or 
                q in info.get("common_name", "").lower() or 
                q in info.get("hindi_name", "").lower() or
                q in info.get("how_to_spot", "").lower()
            )

        matches_crop = True
        if crop_filter != "All Crops":
            matches_crop = crop_filter in info.get("crops", [])

        if matches_search and matches_crop:
            filtered.append(p)

    st.markdown(f"<div style='font-weight:700; color:#475569; margin-bottom:1rem;'>Showing <b>{len(filtered)}</b> practical pest guides</div>", unsafe_allow_html=True)

    if not filtered:
        st.markdown("""
        <div class="neo-card" style="text-align:center; padding:2rem;">
            <div style="font-size:2rem; margin-bottom:6px;">🔍</div>
            <div class="neo-card-title">No Pests Found</div>
            <div class="neo-card-desc">Try searching for 'aphid', 'hopper', 'borer', or 'caterpillar'.</div>
        </div>
        """, unsafe_allow_html=True)
        return

    # Render pest cards (2-column grid matching Image 2 style)
    for i in range(0, len(filtered), 2):
        col1, col2 = st.columns(2)
        batch = filtered[i:i+2]
        
        for idx, p_name in enumerate(batch):
            target_col = col1 if idx == 0 else col2
            with target_col:
                info = PEST_INTELLIGENCE[p_name]
                common = info.get("common_name", p_name.title())
                hindi = f" ({info.get('hindi_name')})" if info.get("hindi_name") else ""
                crops_str = ", ".join(info.get("crops", ["Field Crops"]))

                st.markdown(f"""
                <div class="neo-card">
                    <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:0.8rem;">
                        <div style="width:44px; height:44px; border-radius:12px; border:2px solid #1E293B; background:#FED7AA; display:flex; align-items:center; justify-content:center; font-size:22px; box-shadow:2px 2px 0px #1E293B;">
                            🐛
                        </div>
                        <div style="display:inline-flex; align-items:center; gap:4px; padding:4px 10px; border-radius:9999px; border:2px solid #1E293B; background:#DCFCE7; font-weight:800; font-size:0.8rem; color:#15803D;">
                            ★ Host: {crops_str}
                        </div>
                    </div>
                    <div class="neo-card-title">{common}{hindi}</div>
                    <div style="font-size:0.88rem; color:#16A34A; font-weight:700; margin-bottom:0.6rem;">{info.get('scientific_name', '')}</div>
                    <div class="neo-card-desc" style="margin-bottom:0.8rem;"><b>How to Spot:</b> {info.get('how_to_spot', '')}</div>
                    <div style="background:#F0FDF4; border:1.5px solid #1E293B; border-radius:10px; padding:0.6rem 0.8rem; font-size:0.85rem; color:#1E293B; margin-bottom:0.6rem;">
                        <b>🌿 Organic Remedy:</b> {info.get('prevention_organic', '')}
                    </div>
                    <div style="background:#EFF6FF; border:1.5px solid #1E293B; border-radius:10px; padding:0.6rem 0.8rem; font-size:0.85rem; color:#1E293B;">
                        <b>🧪 Safe Field Spray:</b> {info.get('recommended_treatment', '')}
                    </div>
                </div>
                """, unsafe_allow_html=True)
