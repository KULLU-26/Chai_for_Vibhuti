import streamlit as st
import time
import base64
import random

st.set_page_config(page_title="For Vibhuti ☕", page_icon="💖")

# -------- LOAD GIF --------
def load_gif(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# -------- RANDOM HEARTS --------
def generate_hearts(n=15):
    hearts_html = ""
    for _ in range(n):
        size = random.randint(12, 28)
        left = random.randint(0, 100)
        top = random.randint(0, 100)
        opacity = random.uniform(0.2, 0.6)

        hearts_html += f"""
        <div style="
            position:fixed;
            top:{top}%;
            left:{left}%;
            font-size:{size}px;
            opacity:{opacity};
            pointer-events:none;
        ">💗</div>
        """
    return hearts_html

st.markdown(generate_hearts(), unsafe_allow_html=True)

# -------- FONT & UI --------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@400;500;600&display=swap');

html, body {
    font-family: 'Quicksand', sans-serif;
    background-color: #FFF5F5;
    color: #4b3621;
}

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

.card {
    background: white;
    padding: 20px;
    border-radius: 20px;
    text-align: center;
    box-shadow: 0 8px 20px rgba(0,0,0,0.08);
}
</style>
""", unsafe_allow_html=True)

# -------- STATE --------
if "step" not in st.session_state:
    st.session_state.step = 0
if "chai" not in st.session_state:
    st.session_state.chai = None

# ================= STEP 0 =================
if st.session_state.step == 0:
    st.title("Hey Vibhuti ✨")

    st.write("Gwalior mein full shaadi chaos chal raha hoga na 😅")
    st.write("Thoda break toh banta hai…")
    st.write("So I made this tiny chai break for you ☕")

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
        time.sleep(1)
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

    if st.session_state.chai:
        if st.button("Next ➡️"):
            st.session_state.step = 3
            st.rerun()

# ================= STEP 3 =================
elif st.session_state.step == 3:
    st.title("Quick reminder 💌")

    st.write("Paani peena mat bhoolna 💧")
    st.write("Thoda rest lena")
    st.write("Aur haan… you're doing really well")
    st.write("Main Pune mein wait kar raha hoon 😌")

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
        st.warning("Check GIF names")

    # CLEAN TEXT (NO HTML BUG)
    st.write("### You're handling a lot right now 💭")
    st.write("And you're doing it calmly… that’s not normal, that’s rare.")
    st.write("Bas ek baat yaad rakhna:")
    st.write("**jab overload lage… Pune mein ek chai pending hai ☕**")
    st.write("(Aur haan, I’ll listen to all the gossip 😌)")
    st.write("— Pratik")

    if st.button("Start again 🔄"):
        st.session_state.step = 0
        st.session_state.chai = None
        st.rerun()
