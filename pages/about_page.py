"""
FasalMitra AI - Playful Neo-Brutalist About Platform
"""
import streamlit as st
from config import APP_NAME, APP_HINDI_NAME

def render_about_page():
    """Renders the friendly story, purpose, and farmer benefits in Neo-Brutalist style."""
    
    st.markdown(f"""
    <div style="margin-bottom:1.5rem;">
        <div class="neo-pill mint">
            <span>About FasalMitra AI</span>
        </div>
        <div style="font-size:2.6rem; font-weight:800; color:#1E293B; letter-spacing:-0.02em; margin-bottom:0.4rem;">
            Farmer's Trusted Crop Friend
        </div>
        <div style="font-size:1.05rem; color:#475569; max-width:640px;">
            Supporting growers with instant, private, and accessible pest diagnosis right in the field.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Mission Card
    st.markdown(f"""
    <div class="neo-card" style="box-shadow:6px 6px 0px #1E293B; margin-bottom:2rem;">
        <div style="display:flex; align-items:center; gap:14px; margin-bottom:1rem;">
            <div style="width:48px; height:48px; border-radius:14px; border:2px solid #1E293B; background:#FCE7F3; display:flex; align-items:center; justify-content:center; font-size:24px; box-shadow:2px 2px 0px #1E293B;">
                🌾
            </div>
            <div>
                <div class="neo-card-title" style="margin:0;">Empowering Every Farmer with Instant AI Care</div>
                <div style="font-size:0.9rem; font-weight:700; color:#16A34A;">{APP_NAME} ({APP_HINDI_NAME})</div>
            </div>
        </div>
        <div class="neo-card-desc">
            <b>FasalMitra</b> means <i>"Farmer's Friend"</i>. Our mission is to put expert agricultural pest diagnosis directly into the hands of every farmer. 
            By simply taking a photo with a smartphone, growers can identify crop pests early, protect their harvests, 
            and avoid expensive or unnecessary chemical sprays.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Benefits Grid (Matching Image 3)
    st.markdown("### Why Farmers Trust FasalMitra")
    
    b_col1, b_col2 = st.columns(2)
    with b_col1:
        st.markdown("""
        <div class="neo-card">
            <div style="display:flex; align-items:center; gap:12px; margin-bottom:0.8rem;">
                <div style="width:42px; height:42px; border-radius:12px; border:2px solid #1E293B; background:#DCFCE7; display:flex; align-items:center; justify-content:center; font-size:20px; box-shadow:2px 2px 0px #1E293B;">
                    ⚡
                </div>
                <div class="neo-card-title" style="margin:0; font-size:1.15rem;">Instant Field Diagnosis</div>
            </div>
            <div class="neo-card-desc">
                No waiting days for an expert visit. Get immediate feedback right in the field using your phone camera.
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="neo-card">
            <div style="display:flex; align-items:center; gap:12px; margin-bottom:0.8rem;">
                <div style="width:42px; height:42px; border-radius:12px; border:2px solid #1E293B; background:#FED7AA; display:flex; align-items:center; justify-content:center; font-size:20px; box-shadow:2px 2px 0px #1E293B;">
                    🌿
                </div>
                <div class="neo-card-title" style="margin:0; font-size:1.15rem;">Organic-First Solutions</div>
            </div>
            <div class="neo-card-desc">
                We prioritize preventive neem solutions, cultural farming techniques, and natural predators before recommending chemical treatments.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with b_col2:
        st.markdown("""
        <div class="neo-card">
            <div style="display:flex; align-items:center; gap:12px; margin-bottom:0.8rem;">
                <div style="width:42px; height:42px; border-radius:12px; border:2px solid #1E293B; background:#FEF08A; display:flex; align-items:center; justify-content:center; font-size:20px; box-shadow:2px 2px 0px #1E293B;">
                    💰
                </div>
                <div class="neo-card-title" style="margin:0; font-size:1.15rem;">Save on Input Costs</div>
            </div>
            <div class="neo-card-desc">
                Accurate identification prevents misdiagnosis and stops the wasteful application of ineffective pesticides.
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="neo-card">
            <div style="display:flex; align-items:center; gap:12px; margin-bottom:0.8rem;">
                <div style="width:42px; height:42px; border-radius:12px; border:2px solid #1E293B; background:#BAE6FD; display:flex; align-items:center; justify-content:center; font-size:20px; box-shadow:2px 2px 0px #1E293B;">
                    🔒
                </div>
                <div class="neo-card-title" style="margin:0; font-size:1.15rem;">100% Private & No Accounts</div>
            </div>
            <div class="neo-card-desc">
                No sign-up forms, passwords, or data tracking. Your photos remain in your browser session and are never sold or stored permanently in cloud databases.
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Extension Notice Box
    st.markdown("""
    <div class="neo-card" style="background:#F0FDF4; box-shadow:4px 4px 0px #1E293B;">
        <div style="display:flex; align-items:center; gap:12px; margin-bottom:0.6rem;">
            <div style="width:36px; height:36px; border-radius:10px; border:2px solid #1E293B; background:#DCFCE7; display:flex; align-items:center; justify-content:center; font-size:18px;">
                🌾
            </div>
            <div style="font-weight:800; font-size:1.1rem; color:#15803D;">Agricultural Extension Notice</div>
        </div>
        <div style="font-size:0.92rem; color:#1E293B; line-height:1.6;">
            FasalMitra AI is an educational and diagnostic companion designed to assist field observation. 
            Pesticide regulations and registrations vary across states and districts. 
            Before applying commercial chemical treatments, always check product labels and consult with your local 
            Block Agriculture Officer or Krishi Vigyan Kendra (KVK).
        </div>
    </div>
    """, unsafe_allow_html=True)
