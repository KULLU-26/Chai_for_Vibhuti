import streamlit as st
import time
from streamlit_lottie import st_lottie
import requests

# Page Config - Optimized for Mobile
st.set_page_config(page_title="Sukoon", page_icon="☕", layout="centered")

# --- Optimized Lottie Loaders with Stable URLs ---
def load_lottieurl(url: str):
    try:
        r = requests.get(url)
        if r.status_code != 200: return None
        return r.json()
    except: return None

lottie_chai = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_08m9z96p.json") # Tea pouring
lottie_cozy = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_t9gkkhz4.json") # Cozy coffee shop vibe for finale

# --- Custom CSS for Coziness, Fonts, Colors & Mobile ---
st.markdown("""
    <style>
    /* Cozy light base background and refined typography */
    .main { background-color: #fdf5e6; position: relative; overflow: hidden; }
    h1, h2, h3, p, li { color: #4b3621; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
    
    /* Make buttons bigger and easier to tap on mobile */
    .stButton>button {
        width: 100%;
        border-radius: 18px;
        height: 3.5em;
        background-color: #6F4E37; /* Chocolate brown */
        color: white;
        font-weight: bold;
        font-size: 16px;
        border: none;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 12px;
        transition: all 0.3s ease;
    }
    .stButton>button:active {
        background-color: #8b5e3c;
        transform: translateY(2px);
    }
    
    /* Elegant "Polaroid" Container for the finale */
    .polaroid {
        background: white;
        padding: 25px;
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
        text-align: center;
        border-radius: 18px;
        border: 1px solid #eee;
        margin-top: 20px;
    }
    .polaroid p { color: #4b3621; font-size: 16px; line-height: 1.6; }
    
    /* Hinglish & formatting helper classes */
    .hinglish-text { font-size: 18px; text-align: center; margin-bottom: 15px; }
    .highlight { color: #6F4E37; font-weight: bold; }

    /* Animated CSS Floating Hearts Background Pattern (Wow Factor) */
    @keyframes heartbeat {
        0%, 100% { transform: scale(1) translateY(0); }
        50% { transform: scale(1.1) translateY(-10px); }
    }
    
    .floating-hearts-pattern {
        position: absolute;
        width: 100%;
        height: 100%;
        top: 0;
        left: 0;
        background-image: url('https://icons.iconarchive.com/icons/custom-icon-design/heart/256/heart-icon.png');
        background-size: 50px;
        background-position: 0 0, 25px 25px;
        animation: heartbeat 3s infinite;
        opacity: 0.15; /* Transparent but visible */
        z-index: -1;
    }
    </style>
    """, unsafe_allow_html=True)

# Session State for app logic
if 'step' not in st.session_state:
    st.session_state.step = 0
if 'chai_choice' not in st.session_state:
    st.session_state.chai_choice = None

# --- APP LOGIC FLOW ---

if st.session_state.step == 0:
    st.title("Hey Vibhuti... ✨")
    st.markdown("""
    <div class='hinglish-text'>
    I know Gwalior mein abhi sab kitna hectic chal raha hoga. Haldi, Mehendi, Poojas, and endless relatives... 
    <br>Pata hai tum thoda thak gayi ho.
    <br><br>
    I can't bring you actual <span class='highlight'>adrak wali chai</span> from Pune yet, 
    par tumhare chote se break ke liye I made this small 'Virtual Escape'. Just for you.
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
    # Using Lottie here ensures reliable, high-quality rendering
    if lottie_chai:
        st_lottie(lottie_chai, height=200, key="chai_pour")
    else:
        st.header("☕") # Basic emoji fallback

    st.markdown("<p style='text-align: center; color: #4b3621;'><b>What's your pick today?</b></p>", unsafe_allow_html=True)
    
    # Stacked buttons are ideal for mobile tap targets
    if st.button("Adrak Wali Chai"):
        st.session_state.chai_choice = "adrak"
    if st.button("Elaichi Wali Chai"):
        st.session_state.chai_choice = "elaichi"
    if st.button("Masala Chai"):
        st.session_state.chai_choice = "masala"

    # Display dynamic feedback text based on choice
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
    # Trigger balloons for celebration
    st.balloons()
    st.title("For You. ✨")
    
    # Trigger the floating hearts pattern background on the main div
    st.markdown('<div class="floating-hearts-pattern"></div>', unsafe_allow_html=True)
    
    # The "Polaroid" Style Container
    st.markdown('<div class="polaroid">', unsafe_allow_html=True)
    # Cozy vibe animation
    if lottie_cozy:
        st_lottie(lottie_cozy, height=200, key="cozy_finale")
    else:
        st.header("🏠❤️") # Fallback
    
    # Refined, heartfelt text
    st.markdown("""
        <div style="padding: 15px 0;">
            <h3 style="color: #6F4E37;">You're doing great, Vibhuti.</h3>
            <p>
            Efforts are easy when they're for someone as special as you. I hope this chota sa break put a smile on your face.
            <br><br>
            Can't wait to grab a <b>real</b> chai with you when you're back in Pune.
            </p>
            <p style="text-align: right; font-weight: bold; color: #6F4E37; font-size: 20px;">- Pratik</p>
        </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.write("")
    if st.button("Start Over"):
        st.session_state.step = 0
        st.session_state.chai_choice = None
        st.rerun()
