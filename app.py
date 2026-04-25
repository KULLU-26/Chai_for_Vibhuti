import streamlit as st
import time
from streamlit_lottie import st_lottie
import requests

# Page Config
st.set_page_config(page_title="Sukoon", page_icon="💖", layout="centered")

# --- Optimized Lottie Loaders ---
def load_lottieurl(url: str):
    try:
        r = requests.get(url, timeout=10)
        if r.status_code != 200: return None
        return r.json()
    except: return None

# Using the most stable Lottie links for "Chai" and "Cozy Heart"
lottie_chai = load_lottieurl("https://lottie.host/64295304-4061-469b-9807-681995804561/vjKizf5V70.json")
lottie_final = load_lottieurl("https://lottie.host/33827ec5-3645-42f2-8956-62181518f841/SHeR2Nf1K4.json")

# --- THE "ROMANTIC & CUTE" UI ENGINE ---
st.markdown("""
    <style>
    /* 1. RANDOM FLOATING HEARTS BACKGROUND */
    .stApp {
        background-color: #FFF5F5 !important;
        background-image: 
            url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='100' height='100' viewBox='0 0 100 100'%3E%3Cpath d='M50 30c-5-10-20-10-25 0-5 10 5 20 25 35 20-15 30-25 25-35-5-10-20-10-25 0z' fill='%23FFB7C5' fill-opacity='0.2'/%3E%3C/svg%3E"),
            url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='150' height='150' viewBox='0 0 100 100'%3E%3Cpath d='M20 10c-3-5-12-5-15 0-3 5 3 12 15 22 12-10 18-17 15-22-3-5-12-5-15 0z' fill='%23FFD1DC' fill-opacity='0.15'/%3E%3C/svg%3E");
        background-position: 10% 20%, 80% 50%, 40% 80%, 90% 10%;
        background-attachment: fixed;
    }

    /* 2. CUTE BUTTONS - Forced White Text & Rounded Corners */
    div.stButton > button {
        background: linear-gradient(135deg, #6F4E37 0%, #8B5E3C 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 25px !important;
        padding: 12px 25px !important;
        font-weight: 700 !important;
        font-size: 18px !important;
        box-shadow: 0 6px 15px rgba(111, 78, 55, 0.3) !important;
        transition: all 0.3s ease !important;
    }
    
    div.stButton > button:hover {
        transform: scale(1.03) !important;
        box-shadow: 0 8px 20px rgba(111, 78, 55, 0.4) !important;
    }

    /* Target the text inside the button strictly */
    div.stButton > button p {
        color: white !important;
    }

    /* 3. TYPOGRAPHY */
    h1, h2, h3, p, span, li {
        color: #5D4037 !important;
        font-family: 'Comic Sans MS', 'cursive', sans-serif !important;
    }

    /* 4. THE POLAROID CARD (Surprise Screen) */
    .polaroid-card {
        background: white !important;
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0 15px 35px rgba(0,0,0,0.1);
        border: 1px solid #FFE4E1;
        text-align: center;
    }

    .hinglish-text {
        font-size: 20px;
        text-align: center;
        line-height: 1.5;
        font-weight: 500;
    }

    /* Custom Informational Box Colors */
    .stAlert {
        border-radius: 15px !important;
        background-color: #FFF0F0 !important;
        border: 1px solid #FFB7C5 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- APP LOGIC ---

if 'step' not in st.session_state:
    st.session_state.step = 0
if 'chai_choice' not in st.session_state:
    st.session_state.chai_choice = None

if st.session_state.step == 0:
    st.title("Hey Vibhuti... ✨")
    st.markdown("""
    <div class='hinglish-text'>
    I know Gwalior mein abhi sab kitna hectic chal raha hoga. Haldi, Mehendi, Poojas, and endless relatives... 
    <br><br>Pata hai tum thoda thak gayi ho, aur ye break deserved hai.
    <br><br>
    I can't bring you actual <b>adrak wali chai</b> from Pune yet, 
    par tumhare chehre pe ek smile laane ke liye I made this small 'Virtual Escape'. 
    </div>
    """, unsafe_allow_html=True)
    st.write("")
    if st.button("Take your break ☕💖"):
        st.session_state.step = 1
        st.rerun()

elif st.session_state.step == 1:
    st.title("Mood Check ✨")
    st.markdown("<div class='hinglish-text'>Sachi batana, how tired are you right now?</div>", unsafe_allow_html=True)
    stress_level = st.select_slider(
        "",
        options=["Thoda Tired", "Kaafi Tired", "Bilkul Exhausted", "Bas Ab Pune Jaana Hai!"]
    )
    
    if st.button("Fix my vibe"):
        with st.spinner("Brewing sukoon..."):
            time.sleep(1.5)
        st.session_state.step = 2
        st.rerun()

elif st.session_state.step == 2:
    st.title("Virtual Chai Break ☕")
    if lottie_chai:
        st_lottie(lottie_chai, height=200, key="chai_main")
    else:
        st.header("☕")

    st.markdown("<p style='text-align: center; font-size: 18px;'><b>Aaj kya piyogi?</b></p>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Adrak"): st.session_state.chai_choice = "adrak"
    with col2:
        if st.button("Elaichi"): st.session_state.chai_choice = "elaichi"
    with col3:
        if st.button("Masala"): st.session_state.chai_choice = "masala"

    if st.session_state.chai_choice == "adrak":
        st.info("Strong & refreshing—exactly the energy you need for those 50 extra relatives! 💃")
    elif st.session_state.chai_choice == "elaichi":
        st.success("Calm and sweet. Just take a deep breath... the functions are almost over. 🌸")
    elif st.session_state.chai_choice == "masala":
        st.warning("Handling everything like a pro? This one is for the multitasker in you. 💪")

    if st.session_state.chai_choice:
        st.write("---")
        if st.button("Next? ➡️"):
            st.session_state.step = 3
            st.rerun()

elif st.session_state.step == 3:
    st.title("Chota sa Reminder... 💌")
    st.markdown("""
    <div class='hinglish-text'>
    While you're busy handling the shaadi crowd:
    <br><br>
    ✅ <b>Keep drinking water</b> (Hydrated rehna!)<br>
    ✅ <b>You're doing an amazing job</b>, Vibhuti.<br>
    ✅ <b>I'm waiting in Pune</b> to hear all the gossip once you're free.
    <br><br>
    I'm genuinely proud of how you handle everything with such grace.
    </div>
    """, unsafe_allow_html=True)
    st.write("")
    if st.button("Click for your surprise 🎁"):
        st.session_state.step = 4
        st.rerun()

elif st.session_state.step == 4:
    st.balloons()
    st.title("For You. 💖")
    
    st.markdown('<div class="polaroid-card">', unsafe_allow_html=True)
    if lottie_final:
        st_lottie(lottie_final, height=250, key="final_anim")
    else:
        st.header("🏠❤️")
    
    st.markdown("""
        <div style="padding: 10px 0;">
            <h3 style="color: #6F4E37 !important;">You're doing great, Vibhuti.</h3>
            <p style="font-size: 18px;">
            Efforts are easy when they're for someone as special as you. 
            I hope this chota sa break put a smile on your face today.
            <br><br>
            Can't wait to grab a <b>real</b> chai with you when you're back.
            </p>
            <p style="text-align: right; font-weight: bold; color: #6F4E37 !important; font-size: 24px;">- Pratik</p>
        </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.write("")
    if st.button("Start Over"):
        st.session_state.step = 0
        st.session_state.chai_choice = None
        st.rerun()
