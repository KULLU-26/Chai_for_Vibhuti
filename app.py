import streamlit as st
import time
from streamlit_lottie import st_lottie
import requests

# Page Config
st.set_page_config(page_title="Sukoon", page_icon="☕", layout="centered")

# --- Lottie Loaders ---
def load_lottieurl(url: str):
    try:
        r = requests.get(url)
        if r.status_code != 200: return None
        return r.json()
    except: return None

# Stable Lottie URLs
lottie_chai = load_lottieurl("https://lottie.host/64295304-4061-469b-9807-681995804561/vjKizf5V70.json")
lottie_cozy = load_lottieurl("https://lottie.host/93a0b810-7212-4217-889a-080e72251f28/mS7lV6mZ25.json")

# --- CUSTOM CSS (The Fix) ---
st.markdown("""
    <style>
    /* 1. Force the background color and Hearts pattern for ALL screens */
    .stApp {
        background-color: #fdf5e6;
        background-image:  
            radial-gradient(#ffb7c5 10%, transparent 10%),
            radial-gradient(#ffb7c5 10%, transparent 10%);
        background-size: 50px 50px;
        background-position: 0 0, 25px 25px;
        opacity: 0.9;
    }

    /* 2. Fix Button Visibility - Force White Text */
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        height: 3.5em;
        background-color: #6F4E37 !important; /* Brown */
        color: white !important; /* FORCED WHITE TEXT */
        font-weight: bold !important;
        font-size: 18px !important;
        border: none !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        margin-bottom: 12px;
    }

    /* 3. Text Styling */
    h1, h2, h3, p, span {
        color: #4b3621 !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    /* 4. Polaroid Styling */
    .polaroid {
        background: white;
        padding: 20px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15);
        text-align: center;
        border-radius: 15px;
        border: 2px solid #fff;
    }

    .hinglish-text {
        font-size: 19px;
        text-align: center;
        line-height: 1.6;
    }

    .highlight {
        color: #6F4E37;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# Session State
if 'step' not in st.session_state:
    st.session_state.step = 0
if 'chai_choice' not in st.session_state:
    st.session_state.chai_choice = None

# --- APP FLOW ---

if st.session_state.step == 0:
    st.title("Hey Vibhuti... ✨")
    st.markdown("""
    <div class='hinglish-text'>
    I know Gwalior mein abhi sab kitna hectic chal raha hoga. Haldi, Mehendi, Poojas, and endless relatives... 
    <br>Pata hai tum thoda thak gayi ho.
    <br><br>
    I can't bring you actual <span class='highlight'>adrak wali chai</span> from Pune yet, 
    par tumhare chote se break ke liye I made this 'Virtual Escape'. Just for you.
    </div>
    """, unsafe_allow_html=True)
    st.write("")
    if st.button("Take a 2-minute break ☕✨"):
        st.session_state.step = 1
        st.rerun()

elif st.session_state.step == 1:
    st.title("Mood Check 📉")
    st.markdown("<div class='hinglish-text'>Sach batana, how are you feeling right now?</div>", unsafe_allow_html=True)
    stress_level = st.select_slider(
        "",
        options=["Thoda Tired", "Kaafi Tired", "Bilkul Exhausted", "Bas Ab Pune Jaana Hai!"]
    )
    
    if st.button("Fix my vibe ✨"):
        with st.spinner("Brewing your sukoon...☕"):
            time.sleep(1.5)
        st.session_state.step = 2
        st.rerun()

elif st.session_state.step == 2:
    st.title("Tera Virtual Chai Break ☕")
    if lottie_chai:
        st_lottie(lottie_chai, height=200, key="chai")
    else:
        st.header("☕")

    st.markdown("<p style='text-align: center;'><b>What's your pick today?</b></p>", unsafe_allow_html=True)
    
    if st.button("Adrak Wali Chai"):
        st.session_state.chai_choice = "adrak"
    if st.button("Elaichi Wali Chai"):
        st.session_state.chai_choice = "elaichi"
    if st.button("Masala Chai"):
        st.session_state.chai_choice = "masala"

    if st.session_state.chai_choice == "adrak":
        st.info("Strong & refreshing—exactly the energy you need to handle those 50 extra relatives! 💃")
    elif st.session_state.chai_choice == "elaichi":
        st.success("Calm and sweet. Just take a deep breath... the functions are almost over. You've got this. 🌸")
    elif st.session_state.chai_choice == "masala":
        st.warning("Handling 10 things at once like a pro? This one is for the multitasker in you. 💪")

    if st.session_state.chai_choice:
        st.write("---")
        if st.button("Next? ➡️"):
            st.session_state.step = 3
            st.rerun()

elif st.session_state.step == 3:
    st.title("Chota sa Reminder... 💌")
    st.markdown("""
    <div class='hinglish-text'>
    While you're busy being the perfect sister at the wedding:
    <br><br>
    ✅ <b>Keep drinking water</b> (Sirf chai nahi!)<br>
    ✅ <b>You're doing an amazing job</b>, Vibhuti.<br>
    ✅ <b>I'm right here in Pune</b>, waiting to hear all the shaadi gossip.
    <br><br>
    I'm genuinely so proud of how you handle everything with such grace.
    </div>
    """, unsafe_allow_html=True)
    st.write("")
    if st.button("Click for a final surprise 🎁✨"):
        st.session_state.step = 4
        st.rerun()

elif st.session_state.step == 4:
    st.balloons()
    st.title("For You. ✨")
    
    st.markdown('<div class="polaroid">', unsafe_allow_html=True)
    if lottie_cozy:
        st_lottie(lottie_cozy, height=250, key="finale")
    else:
        st.header("🏠❤️")
    
    st.markdown("""
        <div style="padding: 10px 0;">
            <h3 style="color: #6F4E37 !important;">You're doing great, Vibhuti.</h3>
            <p style="color: #4b3621 !important;">
            Efforts are easy when they're for someone as special as you. I hope this chota sa break put a smile on your face.
            <br><br>
            Can't wait to grab a <b>real</b> chai with you when you're back in Pune.
            </p>
            <p style="text-align: right; font-weight: bold; color: #6F4E37 !important; font-size: 22px;">- Pratik</p>
        </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.write("")
    if st.button("Start Over"):
        st.session_state.step = 0
        st.session_state.chai_choice = None
        st.rerun()
