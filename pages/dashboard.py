"""
FasalMitra AI - Playful Neo-Brutalist Home & Welcome Dashboard
"""
import streamlit as st
from config import SAMPLES_DIR

def render_dashboard():
    """Renders the Neo-Brutalist home page matching the LearnHub design reference."""

    # =========================================================================
    # SECTION 1: HERO (Matching Image 1)
    # =========================================================================
    hero_col_left, hero_col_right = st.columns([1.2, 1])

    with hero_col_left:
        st.markdown("""
        <div class="neo-pill mint">
            <span style="font-size:1.1rem;">●</span>
            <span>New: AI-Powered Crop Protection</span>
        </div>
        <div class="neo-hero-title">
            Protect Any Crop,<br>
            <span class="neo-hero-green">Anytime,</span><br>
            Anywhere!
        </div>
        <div class="neo-hero-desc">
            Join thousands of farmers across India. Protect your harvest with instant smartphone pest detection, 
            crop health diagnosis, and safe field remedies.
        </div>
        """, unsafe_allow_html=True)

        btn_c1, btn_c2 = st.columns([1.1, 1])
        with btn_c1:
            if st.button("Start Diagnosis Free →", key="hero_btn_detect", use_container_width=True):
                st.session_state["current_nav_page"] = "Pest Detection"
                st.rerun()
        with btn_c2:
            if st.button("Browse Crop Pests", key="hero_btn_browse", use_container_width=True):
                st.session_state["current_nav_page"] = "Pest Knowledge"
                st.rerun()

    with hero_col_right:
        # Interactive Hero Card with corner badges (Exact replica of Image 1 right card)
        st.markdown("""
        <div style="position:relative; margin-top:1.5rem; margin-bottom:1.5rem;">
            <div class="neo-card" style="padding:1.8rem; margin:0; box-shadow:6px 6px 0px #1E293B;">
                <!-- Decorative Corner Badges -->
                <div class="corner-badge top-right">🎯</div>
                <div class="corner-badge bottom-right">⭐</div>
                <div class="corner-badge bottom-left">🌾</div>

                <!-- Card Content -->
                <div style="display:flex; align-items:center; gap:14px; margin-bottom:1.2rem;">
                    <div style="width:50px; height:50px; border-radius:14px; border:2px solid #1E293B; background:#BAE6FD; display:flex; align-items:center; justify-content:center; font-size:24px; box-shadow:2px 2px 0px #1E293B;">
                        ▶️
                    </div>
                    <div>
                        <div style="font-size:1.25rem; font-weight:800; color:#1E293B;">Paddy Leaf Scan</div>
                        <div style="font-size:0.9rem; color:#475569; font-weight:600;">Active Tillering &bull; Live Camera Ready</div>
                    </div>
                </div>

                <!-- Progress Section -->
                <div style="display:flex; justify-content:space-between; font-size:0.85rem; font-weight:700; color:#475569; margin-bottom:6px;">
                    <span>AI Model Confidence</span>
                    <span style="color:#16A34A;">94%</span>
                </div>
                <div style="width:100%; height:14px; background:#E2E8F0; border-radius:10px; border:2px solid #1E293B; overflow:hidden; margin-bottom:1.4rem;">
                    <div style="width:94%; height:100%; background:#22C55E;"></div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Test sample shortcuts inside hero
        if st.button("📸 Try a Sample Leaf Photo Now", key="hero_btn_sample", use_container_width=True):
            st.session_state["selected_sample_for_nav"] = "sample_pest_1.jpg"
            st.session_state["current_nav_page"] = "Pest Detection"
            st.rerun()

    st.markdown("<br><br>", unsafe_allow_html=True)

    # =========================================================================
    # SECTION 2: POPULAR PEST THREATS (Matching Image 2)
    # =========================================================================
    st.markdown("""
    <div style="text-align:center; margin-bottom:2rem;">
        <div class="neo-pill blue">
            <span>Popular Pests & Threats</span>
        </div>
        <div style="font-size:2.4rem; font-weight:800; color:#1E293B; letter-spacing:-0.02em; margin-bottom:0.4rem;">
            Explore Top Crop Threats
        </div>
        <div style="font-size:1.05rem; color:#475569; max-width:600px; margin:0 auto;">
            Learn to spot early symptoms and protect your yield with real-world remedies
        </div>
    </div>
    """, unsafe_allow_html=True)

    grid_r1_c1, grid_r1_c2 = st.columns(2)
    with grid_r1_c1:
        st.markdown("""
        <div class="neo-card">
            <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:1rem;">
                <div style="width:48px; height:48px; border-radius:14px; border:2px solid #1E293B; background:#FED7AA; display:flex; align-items:center; justify-content:center; font-size:24px; box-shadow:2px 2px 0px #1E293B;">
                    🌾
                </div>
                <div style="display:inline-flex; align-items:center; gap:4px; padding:4px 12px; border-radius:9999px; border:2px solid #1E293B; background:#DCFCE7; font-weight:800; font-size:0.85rem; color:#15803D;">
                    ★ 4.9 High Risk
                </div>
            </div>
            <div class="neo-card-title">Rice Leaf Roller (Folder)</div>
            <div style="font-size:0.9rem; color:#16A34A; font-weight:700; margin-bottom:0.75rem;">Cnaphalocrocis medinalis</div>
            <div class="neo-card-desc" style="margin-bottom:1rem;">Folds leaf edges together and scrapes green tissue, turning leaves whitish and papery.</div>
            <div style="display:flex; gap:16px; font-size:0.85rem; font-weight:700; color:#475569;">
                <span>📖 14 Pests Mapped</span>
                <span>⏱️ Fast Diagnosis</span>
                <span>👥 12.5k Scans</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with grid_r1_c2:
        st.markdown("""
        <div class="neo-card">
            <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:1rem;">
                <div style="width:48px; height:48px; border-radius:14px; border:2px solid #1E293B; background:#BAE6FD; display:flex; align-items:center; justify-content:center; font-size:24px; box-shadow:2px 2px 0px #1E293B;">
                    🐛
                </div>
                <div style="display:inline-flex; align-items:center; gap:4px; padding:4px 12px; border-radius:9999px; border:2px solid #1E293B; background:#DCFCE7; font-weight:800; font-size:0.85rem; color:#15803D;">
                    ★ 4.8 Severe
                </div>
            </div>
            <div class="neo-card-title">Brown Planthopper (BPH)</div>
            <div style="font-size:0.9rem; color:#16A34A; font-weight:700; margin-bottom:0.75rem;">Nilaparvata lugens</div>
            <div class="neo-card-desc" style="margin-bottom:1rem;">Sucks sap from base of tillers causing rapid drying patches termed 'Hopperburn'.</div>
            <div style="display:flex; gap:16px; font-size:0.85rem; font-weight:700; color:#475569;">
                <span>📖 10 Pests Mapped</span>
                <span>⏱️ Fast Diagnosis</span>
                <span>👥 8.2k Scans</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    grid_r2_c1, grid_r2_c2 = st.columns(2)
    with grid_r2_c1:
        st.markdown("""
        <div class="neo-card">
            <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:1rem;">
                <div style="width:48px; height:48px; border-radius:14px; border:2px solid #1E293B; background:#E0E7FF; display:flex; align-items:center; justify-content:center; font-size:24px; box-shadow:2px 2px 0px #1E293B;">
                    ☁️
                </div>
                <div style="display:inline-flex; align-items:center; gap:4px; padding:4px 12px; border-radius:9999px; border:2px solid #1E293B; background:#DCFCE7; font-weight:800; font-size:0.85rem; color:#15803D;">
                    ★ 4.9 High Risk
                </div>
            </div>
            <div class="neo-card-title">Cotton Aphids & Whitefly</div>
            <div style="font-size:0.9rem; color:#16A34A; font-weight:700; margin-bottom:0.75rem;">Aphis gossypii & Whiteflies</div>
            <div class="neo-card-desc" style="margin-bottom:1rem;">Sucks plant juices causing leaf curling and sticky sooty mold that stains cotton lint.</div>
            <div style="display:flex; gap:16px; font-size:0.85rem; font-weight:700; color:#475569;">
                <span>📖 10 Pests Mapped</span>
                <span>⏱️ Fast Diagnosis</span>
                <span>👥 15.3k Scans</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with grid_r2_c2:
        st.markdown("""
        <div class="neo-card">
            <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:1rem;">
                <div style="width:48px; height:48px; border-radius:14px; border:2px solid #1E293B; background:#DCFCE7; display:flex; align-items:center; justify-content:center; font-size:24px; box-shadow:2px 2px 0px #1E293B;">
                    🌽
                </div>
                <div style="display:inline-flex; align-items:center; gap:4px; padding:4px 12px; border-radius:9999px; border:2px solid #1E293B; background:#DCFCE7; font-weight:800; font-size:0.85rem; color:#15803D;">
                    ★ 4.7 Moderate
                </div>
            </div>
            <div class="neo-card-title">Maize & Fall Armyworm</div>
            <div style="font-size:0.9rem; color:#16A34A; font-weight:700; margin-bottom:0.75rem;">Spodoptera frugiperda</div>
            <div class="neo-card-desc" style="margin-bottom:1rem;">Feeds aggressively inside the central leaf whorl leaving sawdust-like frass and windowpanes.</div>
            <div style="display:flex; gap:16px; font-size:0.85rem; font-weight:700; color:#475569;">
                <span>📖 9 Pests Mapped</span>
                <span>⏱️ Fast Diagnosis</span>
                <span>👥 9.8k Scans</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    # =========================================================================
    # SECTION 3: WHY CHOOSE FASALMITRA (Matching Image 3)
    # =========================================================================
    st.markdown("""
    <div style="text-align:center; margin-bottom:2rem;">
        <div class="neo-pill coral">
            <span>Why Choose Us</span>
        </div>
        <div style="font-size:2.4rem; font-weight:800; color:#1E293B; letter-spacing:-0.02em; margin-bottom:0.4rem;">
            Everything You Need to Protect Your Crops
        </div>
    </div>
    """, unsafe_allow_html=True)

    wc_col1, wc_col2, wc_col3, wc_col4 = st.columns(4)
    with wc_col1:
        st.markdown("""
        <div class="neo-card" style="text-align:center;">
            <div style="width:50px; height:50px; border-radius:14px; border:2px solid #1E293B; background:#FCE7F3; margin:0 auto 1rem auto; display:flex; align-items:center; justify-content:center; font-size:24px; box-shadow:2px 2px 0px #1E293B;">
                ⏱️
            </div>
            <div class="neo-card-title" style="font-size:1.15rem;">Diagnose in Seconds</div>
            <div class="neo-card-desc">Scan leaves instantly right in your field using your phone's browser camera.</div>
        </div>
        """, unsafe_allow_html=True)

    with wc_col2:
        st.markdown("""
        <div class="neo-card" style="text-align:center;">
            <div style="width:50px; height:50px; border-radius:14px; border:2px solid #1E293B; background:#BAE6FD; margin:0 auto 1rem auto; display:flex; align-items:center; justify-content:center; font-size:24px; box-shadow:2px 2px 0px #1E293B;">
                🌿
            </div>
            <div class="neo-card-title" style="font-size:1.15rem;">Organic Remedies</div>
            <div class="neo-card-desc">Practical neem recipes, cultural controls, and natural biological predators.</div>
        </div>
        """, unsafe_allow_html=True)

    with wc_col3:
        st.markdown("""
        <div class="neo-card" style="text-align:center;">
            <div style="width:50px; height:50px; border-radius:14px; border:2px solid #1E293B; background:#E0E7FF; margin:0 auto 1rem auto; display:flex; align-items:center; justify-content:center; font-size:24px; box-shadow:2px 2px 0px #1E293B;">
                💰
            </div>
            <div class="neo-card-title" style="font-size:1.15rem;">Save Input Costs</div>
            <div class="neo-card-desc">Stop wasting money on incorrect pesticides with verified species identification.</div>
        </div>
        """, unsafe_allow_html=True)

    with wc_col4:
        st.markdown("""
        <div class="neo-card" style="text-align:center;">
            <div style="width:50px; height:50px; border-radius:14px; border:2px solid #1E293B; background:#DCFCE7; margin:0 auto 1rem auto; display:flex; align-items:center; justify-content:center; font-size:24px; box-shadow:2px 2px 0px #1E293B;">
                🔒
            </div>
            <div class="neo-card-title" style="font-size:1.15rem;">100% Private & Free</div>
            <div class="neo-card-desc">No login required, no cloud photo tracking. Completely free for all farmers.</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    # =========================================================================
    # SECTION 4: FARMER STORIES & TESTIMONIALS (Matching Image 4)
    # =========================================================================
    st.markdown("""
    <div style="text-align:center; margin-bottom:2rem;">
        <div class="neo-pill mint">
            <span>Farmer Stories</span>
        </div>
        <div style="font-size:2.4rem; font-weight:800; color:#1E293B; letter-spacing:-0.02em; margin-bottom:0.4rem;">
            What Our Farmers Say
        </div>
    </div>
    """, unsafe_allow_html=True)

    test_c1, test_c2, test_c3 = st.columns(3)
    with test_c1:
        st.markdown("""
        <div class="neo-card">
            <div style="color:#FBBF24; font-size:1.3rem; margin-bottom:0.75rem;">★★★★★</div>
            <div class="neo-card-desc" style="font-style:italic; margin-bottom:1.5rem; color:#1E293B;">
                "FasalMitra helped me spot rice leaf folder caterpillars two weeks before the neighbor's field. The neem spray advice saved my paddy crop completely!"
            </div>
            <div style="display:flex; align-items:center; gap:12px;">
                <div style="width:42px; height:42px; border-radius:12px; border:2px solid #1E293B; background:#FCE7F3; display:flex; align-items:center; justify-content:center; font-weight:800; font-size:1.1rem; box-shadow:2px 2px 0px #1E293B;">
                    R
                </div>
                <div>
                    <div style="font-weight:800; color:#1E293B; font-size:0.95rem;">Ramesh Patel</div>
                    <div style="font-size:0.8rem; color:#475569; font-weight:600;">Paddy Farmer, Punjab</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with test_c2:
        st.markdown("""
        <div class="neo-card">
            <div style="color:#FBBF24; font-size:1.3rem; margin-bottom:0.75rem;">★★★★★</div>
            <div class="neo-card-desc" style="font-style:italic; margin-bottom:1.5rem; color:#1E293B;">
                "The camera scan worked directly on my phone in the field with no app download. It identified whitefly immediately and told me the exact organic remedy."
            </div>
            <div style="display:flex; align-items:center; gap:12px;">
                <div style="width:42px; height:42px; border-radius:12px; border:2px solid #1E293B; background:#BAE6FD; display:flex; align-items:center; justify-content:center; font-weight:800; font-size:1.1rem; box-shadow:2px 2px 0px #1E293B;">
                    D
                </div>
                <div>
                    <div style="font-weight:800; color:#1E293B; font-size:0.95rem;">Devendra Solanki</div>
                    <div style="font-size:0.8rem; color:#475569; font-weight:600;">Cotton Grower, Gujarat</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with test_c3:
        st.markdown("""
        <div class="neo-card">
            <div style="color:#FBBF24; font-size:1.3rem; margin-bottom:0.75rem;">★★★★★</div>
            <div class="neo-card-desc" style="font-style:italic; margin-bottom:1.5rem; color:#1E293B;">
                "Best agricultural tool I've used this season. Simple language, no complicated technical words, and gives real remedies that work."
            </div>
            <div style="display:flex; align-items:center; gap:12px;">
                <div style="width:42px; height:42px; border-radius:12px; border:2px solid #1E293B; background:#DCFCE7; display:flex; align-items:center; justify-content:center; font-weight:800; font-size:1.1rem; box-shadow:2px 2px 0px #1E293B;">
                    M
                </div>
                <div>
                    <div style="font-weight:800; color:#1E293B; font-size:0.95rem;">Manish Deshmukh</div>
                    <div style="font-size:0.8rem; color:#475569; font-weight:600;">Soybean Farmer, Maharashtra</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    # =========================================================================
    # SECTION 5: READY TO START (Matching Image 5)
    # =========================================================================
    st.markdown("""
    <div class="neo-canvas-blue">
        <div class="neo-card" style="max-width:760px; margin:0 auto; text-align:center; box-shadow:6px 6px 0px #1E293B; padding:2.5rem 2rem;">
            <div style="font-size:2.4rem; font-weight:800; color:#1E293B; letter-spacing:-0.02em; margin-bottom:0.8rem;">
                Ready to Protect Your Crops?
            </div>
            <div style="font-size:1.05rem; color:#475569; margin-bottom:1.8rem; max-width:540px; margin-left:auto; margin-right:auto;">
                Join thousands of farmers protecting their harvests today. Fast, private, and 100% free crop pest detection.
            </div>
    """, unsafe_allow_html=True)

    cta_c1, cta_c2, cta_c3 = st.columns([1, 1.4, 1])
    with cta_c2:
        if st.button("Start Free Diagnosis →", key="cta_bottom_start", use_container_width=True):
            st.session_state["current_nav_page"] = "Pest Detection"
            st.rerun()

    st.markdown("""
            <div style="display:flex; justify-content:center; gap:24px; font-size:0.9rem; font-weight:700; color:#475569; margin-top:1.5rem; flex-wrap:wrap;">
                <span>✓ No app download required</span>
                <span>✓ Completely free forever</span>
                <span>✓ Zero data stored in cloud</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
