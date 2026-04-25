import streamlit as st
import time
import base64

# ------------------ CONFIG ------------------
st.set_page_config(page_title="For Vibhuti ☕", page_icon="💖", layout="centered")

# ------------------ LOAD GIF ------------------
def load_gif(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# ------------------ UI / FONT ------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif !important;
    color: #4b3621 !important;
}

.stApp {
    background-color: #FFF5F5 !important;
}

h1 {
    font-size: 28px !important;
    font-weight: 600 !important;
}

p {
    font-size: 16px !important;
    line-height: 1.6 !important;
}

/* BUTTONS */
div.stButton > button {
    width: 100% !important;
    background-color: #6F4E37 !important;
    border-radius: 25px !important;
    height: 3.2em !important;
    border: none !important;
}

div.stButton > button p {
    color: white !important;
    font-size: 16px !important;
    font-weight: 500 !important;
}

/* CARD */
.card {
    background: white;
    padding: 18px;
    border-radius: 18px;
    text-align: center;
    box-shadow: 0 6px 18px rgba(0,0,0,0.08);
}

.center {
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# ------------------ STATE ------------------
if "step" not in st.session_state:
    st.session_state.step = 0

if "chai" not in st.session_state:
    st.session_state.chai = None

# ================== STEP 0 ==================
if st.session_state.step == 0:
    st.title("Hey Vibhuti ✨")

    st.markdown("""
    <div class='center'>
    Gwalior mein full shaadi chaos chal raha hoga na 😅<br>
    Thoda break toh banta hai…
    <br><br>
    So I made this tiny chai break for you ☕
    </div>
    """, unsafe_allow_html=True)

    if st.button("Take a 1-min break 💖"):
        st.session_state.step = 1
        st.rerun()

# ================== STEP 1 ==================
elif st.session_state.step == 1:
    st.title("Mood Check")

    st.markdown("<div class='center'>Kitni thak gayi ho?</div>", unsafe_allow_html=True)

    st.select_slider(
        "",
        options=["Thoda", "Kaafi", "Exhausted", "Bas Pune aana hai 😌"]
    )

    if st.button("Fix my vibe ☕"):
        with st.spinner("Brewing sukoon..."):
            time.sleep(1.2)
        st.session_state.step = 2
        st.rerun()

# ================== STEP 2 ==================
elif st.session_state.step == 2:
    st.title("Pick your chai ☕")

    if st.button("Adrak wali"):
        st.session_state.chai = "adrak"

    if st.button("Elaichi wali"):
        st.session_state.chai = "elaichi"

    if st.button("Masala chai"):
        st.session_state.chai = "masala"

    if st.session_state.chai == "adrak":
        st.info("Strong choice… just like you handling everything 💃")

    elif st.session_state.chai == "elaichi":
        st.success("Soft & calm… your vibe 🌸")

    elif st.session_state.chai == "masala":
        st.warning("Multitasking queen energy 💪")

    if st.session_state.chai:
        if st.button("Next ➡️"):
            st.session_state.step = 3
            st.rerun()

# ================== STEP 3 ==================
elif st.session_state.step == 3:
    st.title("Quick reminder 💌")

    st.markdown("""
    <div class='center'>
    Paani peena mat bhoolna 💧<br>
    Thoda rest lena<br>
    Aur haan… you're doing really well
    <br><br>
    Main Pune mein wait kar raha hoon 😌
    </div>
    """, unsafe_allow_html=True)

    if st.button("Open your surprise 🎁"):
        st.session_state.step = 4
        st.rerun()

# ================== STEP 4 ==================
elif st.session_state.step == 4:
    st.balloons()
    st.title("For you 💖")

    st.markdown('<div class="card">', unsafe_allow_html=True)

    gif_map = {
        "adrak": "assets/chai.gif",
        "elaichi": "assets/cute1.gif",
        "masala": "assets/phone.gif"
    }

    gif_path = gif_map.get(st.session_state.chai, "assets/chai.gif")

    try:
        gif = load_gif(gif_path)
        st.markdown(
            f'<img src="data:image/gif;base64,{gif}" width="100%">',
            unsafe_allow_html=True
        )
    except:
        st.warning("Add GIFs in assets folder 😊")

    st.markdown("""
    <div style="padding-top:10px;">
        <h3>You're handling a lot right now 💭</h3>

        <p>
        And you're doing it calmly… that’s not normal, that’s rare.
        <br><br>

        Bas ek baat yaad rakhna:
        <br>
        <b>jab overload lage… Pune mein ek chai pending hai ☕</b>
        <br><br>

        (Aur haan, I’ll listen to all the gossip 😌)
        </p>

        <p style="text-align:right; font-weight:500;">
        - Pratik
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    if st.button("Start again 🔄"):
        st.session_state.step = 0
        st.session_state.chai = None
        st.rerun()
