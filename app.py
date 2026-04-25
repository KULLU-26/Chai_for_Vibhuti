import streamlit as st
import time
import base64

# ---------------- CONFIG ----------------
st.set_page_config(page_title="For Vibhuti ☕", page_icon="💖", layout="centered")

# ---------------- LOAD GIF ----------------
def load_gif(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# ---------------- UI ----------------
st.markdown("""
<style>

/* FONT */
@import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@400;500;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Quicksand', sans-serif !important;
    color: #4b3621 !important;
}

/* BACKGROUND WITH HEARTS */
.stApp {
    background-color: #FFF5F5 !important;
    background-image:
        url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='120' height='120'%3E%3Cpath d='M50 30c-2-5-10-5-12 0-2 5 2 10 12 18 10-8 14-13 12-18-2-5-10-5-12 0z' fill='%23FFB7C5' fill-opacity='0.25'/%3E%3C/svg%3E"),
        url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='180' height='180'%3E%3Cpath d='M20 10c-1-3-5-3-6 0-1 3 1 6 6 11 5-5 7-8 6-11-1-3-5-3-6 0z' fill='%23FFD1DC' fill-opacity='0.35'/%3E%3C/svg%3E");
    background-position: 10% 20%, 80% 60%;
    background-attachment: fixed;
}

/* TEXT */
h1 {
    font-size: 30px !important;
    font-weight: 600 !important;
}

p {
    font-size: 17px !important;
    line-height: 1.7 !important;
}

/* BUTTONS */
div.stButton > button {
    width: 100% !important;
    background-color: #6F4E37 !important;
    border-radius: 25px !important;
    height: 3.2em !important;
    margin-top: 10px !important;
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
    padding: 22px;
    border-radius: 20px;
    text-align: center;
    box-shadow: 0 10px 25px rgba(0,0,0,0.08);
    border: 2px solid #FFE4E1;
}

.center {
    text-align: center;
}

</style>
""", unsafe_allow_html=True)

# ---------------- STATE ----------------
if "step" not in st.session_state:
    st.session_state.step = 0

if "chai" not in st.session_state:
    st.session_state.chai = None

# ================= STEP 0 =================
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

# ================= STEP 1 =================
elif st.session_state.step == 1:
    st.title("Mood Check ✨")

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

# ================= STEP 2 =================
elif st.session_state.step == 2:
    st.title("Pick your chai ☕")

    if st.button("Adrak wali"):
        st.session_state.chai = "adrak"

    if st.button("Elaichi wali"):
        st.session_state.chai = "elaichi"

    if st.button("Masala chai"):
        st.session_state.chai = "masala"

    if st.session_state.chai == "adrak":
        st.info("Strong choice… just like you 💃")

    elif st.session_state.chai == "elaichi":
        st.success("Soft & calm… your vibe 🌸")

    elif st.session_state.chai == "masala":
        st.warning("Multitasking queen energy 💪")

    if st.session_state.chai:
        if st.button("Next ➡️"):
            st.session_state.step = 3
            st.rerun()

# ================= STEP 3 =================
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

# ================= STEP 4 =================
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
        st.warning("Check your GIF names in assets folder")

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

        <p style="text-align:right; font-weight:600;">
        - Pratik
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    if st.button("Start again 🔄"):
        st.session_state.step = 0
        st.session_state.chai = None
        st.rerun()
