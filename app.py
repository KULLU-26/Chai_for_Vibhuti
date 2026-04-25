import streamlit as st
import time
import base64
import random

# ---------------- CONFIG ----------------
st.set_page_config(page_title="For Vibhuti ☕", page_icon="💖")

# ---------------- LOAD GIF ----------------
def load_gif(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# ---------------- RANDOM HEARTS ----------------
def generate_hearts(n=50):
    hearts_html = ""
    for _ in range(n):
        size = random.randint(12, 30)
        left = random.randint(0, 100)
        top = random.randint(0, 100)
        opacity = round(random.uniform(0.15, 0.4), 3)

        hearts_html += f"""
        <div style="
            position:fixed;
            top:{top}%;
            left:{left}%;
            font-size:{size}px;
            opacity:{opacity};
            pointer-events:none;
            z-index:0;
        ">♥️</div>
        """
    return hearts_html

st.markdown(generate_hearts(), unsafe_allow_html=True)

# ---------------- UI ----------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@400;500;600&display=swap');

html, body {
    font-family: 'Quicksand', sans-serif;
    background-color: #FFF5F5;
    color: #4b3621;
}

/* BUTTONS */
button {
    width: 100%;
    background-color: #6F4E37 !important;
    color: white !important;
    border-radius: 25px !important;
    height: 45px !important;
    margin-top: 10px !important;
    border: none !important;
    font-size: 15px !important;
}

/* CARD */
.card {
    background: white;
    padding: 20px;
    border-radius: 20px;
    text-align: center;
    box-shadow: 0 8px 20px rgba(0,0,0,0.08);
}

/* TEXT CENTER */
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

    st.markdown("<div class='center'>Gwalior mein full shaadi chaos chal raha hoga na 😅</div>", unsafe_allow_html=True)
    st.markdown("<div class='center'>Thoda break toh banta hai…</div>", unsafe_allow_html=True)
    st.markdown("<div class='center'>So I made this tiny chai break for you ☕</div>", unsafe_allow_html=True)

    if st.button("Take a break 💖"):
        st.session_state.step = 1
        st.rerun()

# ================= STEP 1 =================
elif st.session_state.step == 1:
    st.title("Mood Check")

    st.select_slider(
        "Kitni thak gayi ho?",
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

    # --- Feedback messages ---
    if st.session_state.chai == "adrak":
        st.info("Strong choice… just like you handling everything 💃")

    elif st.session_state.chai == "elaichi":
        st.success("Soft & calm… your vibe 🌸")

    elif st.session_state.chai == "masala":
        st.warning("Multitasking queen energy 💪")

    if st.session_state.chai:
        time.sleep(0.3)
        if st.button("Next ➡️"):
            st.session_state.step = 3
            st.rerun()

# ================= STEP 3 =================
elif st.session_state.step == 3:
    st.title("Quick reminder 💌")

    st.markdown("<div class='center'>Paani peena mat bhoolna 💧</div>", unsafe_allow_html=True)
    st.markdown("<div class='center'>Thoda rest lena</div>", unsafe_allow_html=True)
    st.markdown("<div class='center'>Aur haan… you're doing really well</div>", unsafe_allow_html=True)
    st.markdown("<div class='center'>Main Pune mein wait kar raha hoon 😌</div>", unsafe_allow_html=True)

    if st.button("Open surprise 🎁"):
        st.session_state.step = 4
        st.rerun()

# ================= STEP 4 =================
elif st.session_state.step == 4:
    st.balloons()
    st.title("For you 💖")

    gif_map = {
        "adrak": "assets/chai.gif",
        "elaichi": "assets/cute1.gif",
        "masala": "assets/phone.gif"
    }

    gif_path = gif_map.get(st.session_state.chai, "assets/chai.gif")

    try:
        gif = load_gif(gif_path)
        st.markdown(
            f'<div class="card"><img src="data:image/gif;base64,{gif}" width="100%"></div>',
            unsafe_allow_html=True
        )
    except:
        st.warning("Check GIF names in assets folder")

    # --- CLEAN FINAL MESSAGE ---
    st.markdown("### You're handling a lot right now 💭")
    st.markdown("And you're doing it calmly… that’s not normal, that’s rare.")
    st.markdown("Bas ek baat yaad rakhna:")
    st.markdown("**jab overload lage… Pune mein ek chai pending hai ☕**")
    st.markdown("_Aur haan, I’ll listen to all the gossip 😌_")
    st.markdown("**— Pratik**")

    if st.button("Start again 🔄"):
        st.session_state.step = 0
        st.session_state.chai = None
        st.rerun()
