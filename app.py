import streamlit as st
import time
import base64

# --- PAGE CONFIG ---
st.set_page_config(page_title="For Vibhuti ☕", page_icon="💖", layout="centered")

# --- LOAD GIF FUNCTION ---
def load_gif(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# --- UI STYLING ---
st.markdown("""
<style>
.stApp {
    background-color: #FFF5F5 !important;
}

div.stButton > button {
    width: 100% !important;
    background-color: #6F4E37 !important;
    border-radius: 25px !important;
    height: 3.2em !important;
    border: none !important;
}

div.stButton > button p {
    color: white !important;
    font-size: 17px !important;
    font-weight: bold !important;
}

h1, h2, h3, p {
    color: #4b3621 !important;
    font-family: 'Comic Sans MS', cursive !important;
}

.polaroid {
    background: white;
    padding: 20px;
    border-radius: 20px;
    text-align: center;
    box-shadow: 0 8px 20px rgba(0,0,0,0.1);
}

.center {
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# --- SESSION STATE ---
if "step" not in st.session_state:
    st.session_state.step = 0
if "chai_choice" not in st.session_state:
    st.session_state.chai_choice = None

# ===================== STEP 0 =====================
if st.session_state.step == 0:
    st.title("Hey Vibhuti... ✨")

    st.markdown("""
    <div class='center'>
    Gwalior mein full shaadi chaos chal raha hoga na 😅<br><br>
    Thoda break toh banta hai…<br><br>
    So I made this tiny escape for you ☕
    </div>
    """, unsafe_allow_html=True)

    if st.button("Take your break 💖"):
        st.session_state.step = 1
        st.rerun()

# ===================== STEP 1 =====================
elif st.session_state.step == 1:
    st.title("Mood Check ✨")

    st.markdown("<div class='center'>Sach batao… kitni thak gayi ho?</div>", unsafe_allow_html=True)

    st.select_slider(
        "",
        options=["Thoda Tired", "Kaafi Tired", "Bilkul Exhausted", "Bas Ab Pune Jaana Hai!"]
    )

    if st.button("Fix my vibe ☕"):
        with st.spinner("Brewing sukoon..."):
            time.sleep(1.5)
        st.session_state.step = 2
        st.rerun()

# ===================== STEP 2 =====================
elif st.session_state.step == 2:
    st.title("Tera Chai Break ☕")

    st.markdown("<div class='center'>Aaj kya piyogi?</div>", unsafe_allow_html=True)

    if st.button("Adrak Wali Chai"):
        st.session_state.chai_choice = "adrak"

    if st.button("Elaichi Wali Chai"):
        st.session_state.chai_choice = "elaichi"

    if st.button("Masala Chai"):
        st.session_state.chai_choice = "masala"

    if st.session_state.chai_choice == "adrak":
        st.info("Strong choice… just like you 💃")

    elif st.session_state.chai_choice == "elaichi":
        st.success("Soft & calm… your vibe 🌸")

    elif st.session_state.chai_choice == "masala":
        st.warning("Handling everything like a pro 💪")

    if st.session_state.chai_choice:
        if st.button("Next ➡️"):
            st.session_state.step = 3
            st.rerun()

# ===================== STEP 3 =====================
elif st.session_state.step == 3:
    st.title("Chota Reminder 💌")

    st.markdown("""
    <div class='center'>
    Shaadi chaos ke beech:<br><br>
    ✅ Paani peena mat bhoolna<br>
    ✅ Thoda rest lena<br>
    ✅ And hey… you're doing really well<br><br>
    Main Pune mein wait kar raha hoon 😌
    </div>
    """, unsafe_allow_html=True)

    if st.button("Open your surprise 🎁"):
        st.session_state.step = 4
        st.rerun()

# ===================== STEP 4 =====================
elif st.session_state.step == 4:
    st.balloons()
    st.title("For You 💖")

    st.markdown('<div class="polaroid">', unsafe_allow_html=True)

    # --- GIF SELECTION BASED ON CHOICE ---
    gif_map = {
        "adrak": "assets/chai.gif",
        "elaichi": "assets/cute1.gif",
        "masala": "assets/phone.gif"
    }

    gif_path = gif_map.get(st.session_state.chai_choice, "assets/chai.gif")

    try:
        gif = load_gif(gif_path)
        st.markdown(
            f'<img src="data:image/gif;base64,{gif}" width="100%">',
            unsafe_allow_html=True
        )
    except:
        st.warning("GIF not loading 😅 Check file names in assets folder")

    # --- PERSONAL MESSAGE ---
    st.markdown("""
    <div style="padding-top:10px;">
        <h3>Tum itna sab kaise handle kar leti ho? 💭</h3>

        <p>
        Itni chaos mein bhi calm rehna… that’s rare.<br><br>

        Tum bol dogi “normal hai”… but it's not.<br><br>

        Bas yaad rakhna:<br>
        <b>jab overload lage… Pune mein ek chai pending hai ☕</b><br><br>

        (Aur haan, gossip bhi sununga 😌)
        </p>

        <p style="text-align:right; font-weight:bold;">
        - Pratik
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    if st.button("Start Again 🔄"):
        st.session_state.step = 0
        st.session_state.chai_choice = None
        st.rerun()
