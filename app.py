import streamlit as st
import time
from streamlit_lottie import st_lottie
import requests

# Page Config
st.set_page_config(page_title="Sukoon", page_icon="☕", layout="centered")

# --- Optimized Lottie Loaders ---
def load_lottieurl(url: str):
    try:
        r = requests.get(url, timeout=5)
        if r.status_code != 200: return None
        return r.json()
    except: return None

# Using extremely stable legacy Lottie URLs
lottie_chai = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_08m9z96p.json")
lottie_cozy = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_t9gkkhz4.json")

# --- THEME-PROOF CSS ---
st.markdown("""
    <style>
    /* 1. Force the background to have ACTUAL hearts and beige color */
    .stApp {
        background-color: #fdf5e6 !important;
        background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='40' height='40' viewBox='0 0 20 20'%3E%3Cpath d='M10 3.22l-.61-.6a5.5 5.5 0 0 0-7.78 7.77L10 18.78l8.39-8.4a5.5 5.5 0 0 0-7.78-7.77l-.61.61z' fill='%23ffb7c5' fill-opacity='0.2'/%3E%3C/svg%3E");
    }

    /* 2. Fix Button Visibility - NO MATTER THE THEME */
    div.stButton > button {
        background-color: #6F4E37 !important;
        border: 2px solid #5d4037 !important;
        border-radius: 15px !important;
        padding: 10px !important;
        box-shadow: 0 4px 10px rgba(0,0,0,0.2) !important;
    }
    
    /* Targeting the text specifically inside the button */
    div.stButton > button p {
        color: white !important;
        font-weight: bold !important;
        font-size: 18px !important;
    }

    /* 3. Text Styling (Ensuring everything is readable brown) */
    h1, h2, h3, p, span, li, div {
        color: #4b3621 !important;
    }

    /* 4. Polaroid/Final Card Styling */
    .polaroid {
        background: white !important;
        padding: 20px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
        text-align: center;
        border-radius: 20px;
        border: 1px solid #eee;
    }

    .hinglish-text {
        font-size: 19px;
        text-align: center;
        line-height: 1.6;
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
    I can't bring you actual <b>adrak wali chai</b> from Pune yet, 
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
        with st.spinner("Brewing your sukoon..."):
            time.sleep(1)
        st.session_state.step = 2
        st.rerun()

elif st.session_state.step == 2:
    st.title("Tera Virtual Chai Break ☕")
    if lottie_chai:
        st_lottie(lottie_chai, height=200, key="chai_anim")
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
        st.info("Strong & refreshing—exactly the energy you need for those 50 extra relatives! 💃")
    elif st.session_state.chai_choice == "elaichi":
        st.success("Sweet & calming. Just take a deep breath... you've got this. 🌸")
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
        st_lottie(lottie_cozy, height=250, key="cozy_anim")
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
            <p style="text-align: right; font-weight: bold; color: #6F4E37 !important; font-size: 24px;">- Pratik</p>
        </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.write("")
    if st.button("Start Over"):
        st.session_state.step = 0
        st.session_state.chai_choice = None
        st.rerun()
