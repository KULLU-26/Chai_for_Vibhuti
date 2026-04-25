import streamlit as st
import time
from streamlit_lottie import st_lottie
import requests

# Page Config
st.set_page_config(page_title="Sukoon for Vibhuti", page_icon="☕")

# Helper function for animations
def load_lottieurl(url: str):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    except:
        return None

lottie_chai = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_08m9z96p.json")
lottie_heart = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_96bovdur.json")

# Custom CSS for the "Polaroid" look and vibes
st.markdown("""
    <style>
    .main {
        background-color: #fdf5e6;
    }
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        height: 3em;
        background-color: #6F4E37;
        color: white;
    }
    .polaroid {
        background: white;
        padding: 15px;
        box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
        text-align: center;
        border-radius: 5px;
    }
    .hinglish-text {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        color: #4b3621;
    }
    </style>
    """, unsafe_allow_html=True)

if 'step' not in st.session_state:
    st.session_state.step = 0
if 'chai_type' not in st.session_state:
    st.session_state.chai_type = None

# --- APP LOGIC ---

if st.session_state.step == 0:
    st.title("Hey Vibhuti... ✨")
    st.markdown("""
    <div class='hinglish-text'>
    I know Gwalior mein abhi sab kitna hectic chal raha hoga. Haldi, Mehendi, Poojas, and endless relatives... 
    Pata hai tum thoda thak gayi ho.
    <br><br>
    I can't bring you actual <b>adrak wali chai</b> from Pune yet, but I made this 2-minute 'Virtual Escape' just for you.
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("I need a break! 🙋‍♀️"):
        st.session_state.step = 1
        st.rerun()

elif st.session_state.step == 1:
    st.title("Mood Check 📉")
    st.write("Sach batana, how are you feeling right now?")
    stress_level = st.select_slider(
        "",
        options=["Thoda Tired", "Kaafi Tired", "Bilkul Exhausted", "Bas Ab Ghar Jaana Hai!"]
    )
    
    if st.button("Fix my vibe"):
        with st.spinner("Brewing your sukoon..."):
            time.sleep(1.5)
        st.session_state.step = 2
        st.rerun()

elif st.session_state.step == 2:
    st.title("Tera Virtual Chai Break ☕")
    if lottie_chai:
        st_lottie(lottie_chai, height=200)

    st.markdown("<p style='text-align: center;'><b>What are we drinking?</b></p>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Adrak"):
            st.session_state.chai_type = "adrak"
    with col2:
        if st.button("Elaichi"):
            st.session_state.chai_type = "elaichi"
    with col3:
        if st.button("Masala"):
            st.session_state.chai_type = "masala"

    # Dynamic Messages instead of generic popups
    if st.session_state.chai_type == "adrak":
        st.info("Strong & refreshing—exactly the kind of energy you need to deal with those 50 extra relatives! 💃")
    elif st.session_state.chai_type == "elaichi":
        st.success("Calm and sweet. Just take a deep breath... the functions are almost over. You've got this. 🌸")
    elif st.session_state.chai_type == "masala":
        st.warning("Handling 10 things at once like a pro? This one is for the multitasker in you. 💪")

    if st.session_state.chai_type:
        st.write("---")
        if st.button("Next?"):
            st.session_state.step = 3
            st.rerun()

elif st.session_state.step == 3:
    st.title("A Little Reminder... 💌")
    
    st.markdown("""
    <div class='hinglish-text'>
    While you're busy being the perfect sister at the wedding:
    <br>
    <ul>
        <li>Keep drinking water (sirf chai nahi!).</li>
        <li>You're doing an amazing job, Vibhuti.</li>
        <li>I'm right here in Pune, waiting to hear all the shaadi gossip.</li>
    </ul>
    <b>I'm genuinely so proud of how you handle everything with such grace.</b>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("Click for a final surprise 🎁"):
        st.session_state.step = 4
        st.rerun()

elif st.session_state.step == 4:
    st.balloons()
    st.title("For You. ❤️")
    
    # The "Polaroid" Surprise
    st.markdown("""
    <div class="polaroid">
        <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJueGZueGZueGZueGZueGZueGZueGZueGZueGZueGZueGZueGZ1JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCZjdD1n/3o7TKoWXlo3M1nKSYg/giphy.gif" alt="Chai Love" style="width:100%">
        <div style="padding: 20px;">
            <h3 style="color: #6F4E37;">I genuinely like you, Vibhuti.</h3>
            <p style="color: #4b3621; font-style: italic;">
            Efforts are easy when it's for someone as special as you. 
            Can't wait to grab a <b>real</b> chai with you when you're back in Pune.
            </p>
            <p style="text-align: right; font-weight: bold;">- Pratik</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("Start Over"):
        st.session_state.step = 0
        st.session_state.chai_type = None
        st.rerun()
