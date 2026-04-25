import streamlit as st
import time

# Page Config
st.set_page_config(page_title="Sukoon", page_icon="🧸", layout="centered")

# --- THEME-PROOF & CUTE UI ENGINE ---
st.markdown("""
    <style>
    /* 1. SCATTERED HEARTS BACKGROUND (Theme-Proof) */
    .stApp {
        background-color: #FFF5F5 !important;
        background-image: 
            url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='100' height='100' viewBox='0 0 100 100'%3E%3Cpath d='M50 30c-2-5-10-5-12 0-2 5 2 10 12 18 10-8 14-13 12-18-2-5-10-5-12 0z' fill='%23FFB7C5' fill-opacity='0.3'/%3E%3C/svg%3E"),
            url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='150' height='150' viewBox='0 0 100 100'%3E%3Cpath d='M20 10c-1-3-5-3-6 0-1 3 1 6 6 11 5-5 7-8 6-11-1-3-5-3-6 0z' fill='%23FFD1DC' fill-opacity='0.4'/%3E%3C/svg%3E"),
            url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='200' height='200' viewBox='0 0 100 100'%3E%3Cpath d='M80 70c-2-4-8-4-10 0-2 4 2 8 10 15 8-7 12-11 10-15-2-4-8-4-10 0z' fill='%23FFB7C5' fill-opacity='0.2'/%3E%3C/svg%3E");
        background-position: 10% 10%, 40% 60%, 80% 20%;
        background-attachment: fixed;
    }

    /* 2. BUTTONS - Forced Visibility & High Contrast */
    div.stButton > button {
        width: 100% !important;
        background-color: #6F4E37 !important; /* Deep Brown */
        border-radius: 25px !important;
        height: 3.5em !important;
        border: none !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.15) !important;
    }
    
    /* This targets the actual text label inside the button */
    div.stButton > button p {
        color: #FFFFFF !important;
        font-size: 18px !important;
        font-weight: bold !important;
        letter-spacing: 0.5px !important;
    }

    /* 3. TYPOGRAPHY - Deep Brown for Readability */
    h1, h2, h3, p, span, li, label {
        color: #4b3621 !important;
        font-family: 'Comic Sans MS', 'cursive', sans-serif !important;
    }

    /* 4. SURPRISE CARD STYLING */
    .polaroid {
        background: white !important;
        padding: 20px;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
        text-align: center;
        border: 2px solid #FFE4E1;
    }

    .hinglish-text {
        font-size: 20px;
        text-align: center;
        line-height: 1.6;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SESSION LOGIC ---
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
        with st.spinner("Brewing sukoon...☕"):
            time.sleep(1.5)
        st.session_state.step = 2
        st.rerun()

elif st.session_state.step == 2:
    st.title("Tera Virtual Chai Break ☕")
    # Using a high-quality emoji for stability on Step 2
    st.markdown("<h1 style='text-align: center; font-size: 80px;'>☕</h1>", unsafe_allow_html=True)

    st.markdown("<p style='text-align: center; font-size: 18px;'><b>Aaj kya piyogi?</b></p>", unsafe_allow_html=True)
    
    if st.button("Adrak Wali Chai"):
        st.session_state.chai_choice = "adrak"
    if st.button("Elaichi Wali Chai"):
        st.session_state.chai_choice = "elaichi"
    if st.button("Masala Chai"):
        st.session_state.chai_choice = "masala"

    if st.session_state.chai_choice == "adrak":
        st.info("Strong & refreshing—exactly the energy you need for the wedding crowd! 💃")
    elif st.session_state.chai_choice == "elaichi":
        st.success("Calm and sweet. Just take a deep breath... you've got this. 🌸")
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
    
    st.markdown('<div class="polaroid">', unsafe_allow_html=True)
    
    # GUARANTEED IMAGE LOAD: Using a high-quality baby bear couple image
    st.image("https://i.pinimg.com/originals/74/4d/93/744d93563914a27f6e07672251f280c4.gif", use_container_width=True)
    
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
