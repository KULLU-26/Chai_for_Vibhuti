import streamlit as st
import streamlit as st
import time
import base64

# --- PAGE CONFIG ---
st.set_page_config(page_title="Sukoon", page_icon="🧸", layout="centered")

# --- LOAD LOCAL GIF (BULLETPROOF METHOD) ---
def load_gif(path):
    with open(path, "rb") as f:
        data = base64.b64encode(f.read()).decode("utf-8")
    return data

# --- THEME / UI ---
st.markdown("""
    <style>
    .stApp {
        background-color: #FFF5F5 !important;
        background-image: 
            url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='100' height='100'%3E%3Cpath d='M50 30c-2-5-10-5-12 0-2 5 2 10 12 18 10-8 14-13 12-18-2-5-10-5-12 0z' fill='%23FFB7C5' fill-opacity='0.3'/%3E%3C/svg%3E");
        background-attachment: fixed;
    }

    div.stButton > button {
        width: 100% !important;
        background-color: #6F4E37 !important;
        border-radius: 25px !important;
        height: 3.5em !important;
        border: none !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.15) !important;
    }

    div.stButton > button p {
        color: #FFFFFF !important;
        font-size: 18px !important;
        font-weight: bold !important;
    }

    h1, h2, h3, p, span, li {
        color: #4b3621 !important;
        font-family: 'Comic Sans MS', cursive !important;
    }

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

# --- SESSION STATE ---
if 'step' not in st.session_state:
    st.session_state.step = 0
if 'chai_choice' not in st.session_state:
    st.session_state.chai_choice = None

# --- FLOW ---

# STEP 0
if st.session_state.step == 0:
    st.title("Hey Vibhuti... ✨")
    st.markdown("""
    <div class='hinglish-text'>
    I know Gwalior mein abhi sab kitna hectic chal raha hoga... 
    <br><br>
    Haldi, Mehendi, pooja, relatives — full chaos mode 😅
    <br><br>
    So I made a tiny break for you.
    <br><br>
    Not real chai yet... but thoda sa sukoon ☕
    </div>
    """, unsafe_allow_html=True)

    if st.button("Take your break ☕💖"):
        st.session_state.step = 1
        st.rerun()

# STEP 1
elif st.session_state.step == 1:
    st.title("Mood Check ✨")
    st.markdown("<div class='hinglish-text'>Sach batao… kitni thak gayi ho?</div>", unsafe_allow_html=True)

    st.select_slider(
        "",
        options=["Thoda Tired", "Kaafi Tired", "Bilkul Exhausted", "Bas Ab Pune Jaana Hai!"]
    )

    if st.button("Fix my vibe"):
        with st.spinner("Brewing sukoon...☕"):
            time.sleep(1.5)
        st.session_state.step = 2
        st.rerun()

# STEP 2
elif st.session_state.step == 2:
    st.title("Tera Chai Break ☕")
    st.markdown("<h1 style='text-align:center;'>☕</h1>", unsafe_allow_html=True)

    st.markdown("<p style='text-align:center;'>Aaj kya piyogi?</p>", unsafe_allow_html=True)

    if st.button("Adrak Wali Chai"):
        st.session_state.chai_choice = "adrak"

    if st.button("Elaichi Wali Chai"):
        st.session_state.chai_choice = "elaichi"

    if st.button("Masala Chai"):
        st.session_state.chai_choice = "masala"

    if st.session_state.chai_choice == "adrak":
        st.info("Strong & refreshing—just like you handling everything 💃")

    elif st.session_state.chai_choice == "elaichi":
        st.success("Calm, sweet… take a breath 🌸")

    elif st.session_state.chai_choice == "masala":
        st.warning("Multitasking queen mode 💪")

    if st.session_state.chai_choice:
        if st.button("Next ➡️"):
            st.session_state.step = 3
            st.rerun()

# STEP 3
elif st.session_state.step == 3:
    st.title("Chota Reminder 💌")

    st.markdown("""
    <div class='hinglish-text'>
    Shaadi chaos ke beech:
    <br><br>
    ✅ Paani peete rehna<br>
    ✅ Thoda rest lena<br>
    ✅ Aur haan… you're doing amazing
    <br><br>
    Main Pune mein wait kar raha hoon — full story sunne ke liye 😌
    </div>
    """, unsafe_allow_html=True)

    if st.button("Open your surprise 🎁"):
        st.session_state.step = 4
        st.rerun()

# STEP 4 (FINAL)
elif st.session_state.step == 4:
    st.toast("You made her smile. Trust me. 💖")
    st.balloons()
    st.title("For You 💖")

    st.markdown('<div class="polaroid">', unsafe_allow_html=True)

    # --- LOAD LOCAL GIF ---
    try:
        gif = load_gif("assets/bear.gif")
        st.markdown(
            f'<img src="data:image/gif;base64,{gif}" width="100%">',
            unsafe_allow_html=True
        )
    except:
        st.warning("Add a GIF in /assets folder named 'bear.gif' 😊")

    st.markdown("""
        <div style="padding: 10px 0;">
            <h3 style="color:#6F4E37;">
            Tum itna sab handle kaise kar leti ho, honestly? 💭
            </h3>

            <p style="font-size:18px;">
            Itni chaos mein bhi tum calm reh leti ho... that's rare.
            <br><br>

            Tum bol dogi “normal hai” — but it’s not.
            <br><br>

            Bas yaad rakhna:
            <br>
            <b>jab overload lage… Pune mein ek chai pending hai ☕</b>
            <br><br>

            (Aur haan, gossip bhi sununga 😌)
            </p>

            <p style="text-align:right; font-weight:bold; font-size:22px;">
            - Pratik
            </p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    if st.button("Start Over"):
        st.session_state.step = 0
        st.session_state.chai_choice = None
        st.rerun()
