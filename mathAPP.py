import streamlit as st

st.set_page_config(page_title="تحدي الرياضيات", page_icon="🧠", layout="wide")

def check_password():
    if "password_correct" not in st.session_state:
        st.session_state.password_correct = False

    if st.session_state.password_correct:
        return True

    st.markdown("""
    <style>
    header {display: none;}

    .block-container {
        padding-top: 80px;
        max-width: 720px;
        margin: auto;
    }

    .stApp {
        background-image:
        linear-gradient(rgba(255,255,255,0.55), rgba(255,255,255,0.70)),
        url("https://img.freepik.com/premium-vector/math-theme-blank-banner-with-math-tools_1639-53505.jpg");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }

    .moving-header {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        background: linear-gradient(90deg, #ec4899, #7c3aed, #06b6d4);
        color: white;
        font-size: 26px;
        font-weight: 900;
        padding: 16px 0;
        overflow: hidden;
        z-index: 999999;
    }

    .moving-text {
        display: inline-block;
        white-space: nowrap;
        animation: moveText 15s linear infinite;
    }

    @keyframes moveText {
        0% {transform: translateX(100%);}
        100% {transform: translateX(-100%);}
    }

    .login-title {
        text-align: center;
        color: #25194f;
        font-size: 46px;
        font-weight: 900;
        margin-top: 60px;
        margin-bottom: 25px;
    }

    div[data-testid="stForm"] {
        background: rgba(255,255,255,0.92);
        padding: 45px;
        border-radius: 30px;
        box-shadow: 0 15px 40px rgba(0,0,0,0.18);
        border: 4px solid #ec4899;
    }

    .password-title {
        text-align: center;
        color: #ec4899;
        font-size: 36px;
        font-weight: 900;
        margin-bottom: 30px;
    }

    /* مربع إدخال كلمة المرور */
    div[data-testid="stTextInput"] input {
        background: linear-gradient(90deg, #ffe4f1, #f3e8ff) !important;
        color: #25194f !important;
        border: 3px solid #ec4899 !important;
        border-radius: 18px !important;
        height: 70px !important;
        font-size: 24px !important;
        text-align: center !important;
        box-shadow: none !important;
    }

    div[data-testid="stTextInput"] input::placeholder {
        color: #8b7b92 !important;
        opacity: 1 !important;
    }

    /* إزالة خلفية أيقونة العين السوداء */
    div[data-testid="stTextInput"] button {
        background: transparent !important;
        color: #ec4899 !important;
        border: none !important;
        box-shadow: none !important;
    }

    div[data-testid="stFormSubmitButton"] button {
        height: 70px;
        font-size: 26px;
        font-weight: 900;
        border-radius: 20px;
        border: none;
        color: white;
        background: linear-gradient(90deg, #ec4899, #7c3aed, #06b6d4);
        box-shadow: 0 10px 25px rgba(0,0,0,0.2);
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="moving-header">
        <div class="moving-text">
            💜 I love math &nbsp;&nbsp;&nbsp;
            ✨ Math is fun &nbsp;&nbsp;&nbsp;
            🧠 الرياضيات ممتعة &nbsp;&nbsp;&nbsp;
            📐 أحب الرياضيات &nbsp;&nbsp;&nbsp;
            🎯 التحدي يزيد المتعة
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="login-title">🧠 تحدي عبقري الرياضيات</div>', unsafe_allow_html=True)

    with st.form("password_form"):
        st.markdown('<div class="password-title">🔒 ادخلي كلمة المرور</div>', unsafe_allow_html=True)

        password = st.text_input(
            "كلمة المرور",
            type="password",
            placeholder="اكتبي كلمة المرور هنا",
            label_visibility="collapsed"
        )

        submitted = st.form_submit_button("🚀 دخول", use_container_width=True)

        if submitted:
            if password == st.secrets["APP_PASSWORD"]:
                st.session_state.password_correct = True
                st.rerun()
            else:
                st.error("❌ كلمة المرور غلط")

    return False


if not check_password():
    st.stop()
    
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700;900&display=swap');

html, body, [class*="css"] {
    font-family: 'Tajawal', sans-serif;
    direction: rtl;
}

header {display: none;}

.block-container {
    padding-top: 90px;
}

.stApp {
    background-image:
    linear-gradient(rgba(255,255,255,0.55), rgba(255,255,255,0.70)),
    url("https://img.freepik.com/premium-vector/math-theme-blank-banner-with-math-tools_1639-53505.jpg");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

/* شريط الهيدر */
.moving-header {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    background: linear-gradient(90deg, #6c4cff, #ec4899, #06b6d4, #6c4cff);
    color: white;
    font-size: 26px;
    font-weight: 900;
    padding: 16px 0;
    overflow: hidden;
    z-index: 999999;
    box-shadow: 0 6px 20px rgba(0,0,0,0.25);
}

.moving-text {
    display: inline-block;
    white-space: nowrap;
    animation: moveText 15s linear infinite;
}

@keyframes moveText {
    0% {transform: translateX(100%);}
    100% {transform: translateX(-100%);}
}

.question-box {
    background: white;
    padding: 45px;
    border-radius: 30px;
    text-align: center;
    font-size: 34px;
    font-weight: 900;
    color: #25194f;
    margin: 35px auto;
    width: 55%;
    box-shadow: 0 12px 35px rgba(0,0,0,0.18);
}

.stButton>button {
    height: 70px;
    font-size: 25px;
    font-weight: 900;
    border-radius: 22px;
    border: none;
    color: white;
    background: linear-gradient(135deg, #7c3aed, #ec4899);
    box-shadow: 0 8px 18px rgba(0,0,0,0.18);
}

.stButton>button:hover {
    background: linear-gradient(135deg, #ec4899, #06b6d4);
    transform: scale(1.03);
    color: white;
}

.correct-box {
    text-align: center;
    color: #16a34a;
    background: #eafff1;
    font-size: 34px;
    font-weight: 900;
    padding: 22px;
    border-radius: 25px;
    width: 45%;
    margin: 25px auto;
}

.wrong-box {
    text-align: center;
    color: #dc2626;
    background: #fff0f0;
    font-size: 34px;
    font-weight: 900;
    padding: 22px;
    border-radius: 25px;
    width: 45%;
    margin: 25px auto;
}

.float-shape {
    position: fixed;
    font-size: 45px;
    opacity: 0.55;
    animation: float 5s ease-in-out infinite alternate;
    z-index: 1;
}

.s1 {top: 20%; left: 5%;}
.s2 {top: 35%; right: 8%;}
.s3 {bottom: 15%; left: 12%;}
.s4 {bottom: 20%; right: 15%;}

@keyframes float {
    from {transform: translateY(0px) rotate(0deg);}
    to {transform: translateY(-30px) rotate(10deg);}
}

.sad-face {
    position: fixed;
    top: -50px;
    font-size: 38px;
    animation: sadFall 4s linear infinite;
    z-index: 9999;
}

@keyframes sadFall {
    0% {transform: translateY(0) rotate(0deg);}
    100% {transform: translateY(100vh) rotate(360deg);}
}
</style>
""", unsafe_allow_html=True)


# الشريط المتحرك
st.markdown("""
<div class="moving-header">
    <div class="moving-text">
        💜 I love math &nbsp;&nbsp;&nbsp;
        ✨ Math is fun &nbsp;&nbsp;&nbsp;
        🧠 الرياضيات ممتعة &nbsp;&nbsp;&nbsp;
        📐 أحب الرياضيات &nbsp;&nbsp;&nbsp;
        ➕ الأرقام عالم جميل &nbsp;&nbsp;&nbsp;
        🎯 التحدي يزيد المتعة &nbsp;&nbsp;&nbsp;
        💜 I love math &nbsp;&nbsp;&nbsp;
        ✨ Math is fun
    </div>
</div>
""", unsafe_allow_html=True)


# رسوم متحركة بالخلفية
st.markdown("""
<div class="float-shape s1">➕</div>
<div class="float-shape s2">📐</div>
<div class="float-shape s3">✖️</div>
<div class="float-shape s4">🧮</div>
""", unsafe_allow_html=True)


def sad_faces():
    st.markdown("""
    <div class="sad-face" style="left:5%;">😢</div>
    <div class="sad-face" style="left:20%;">😭</div>
    <div class="sad-face" style="left:35%;">☹️</div>
    <div class="sad-face" style="left:50%;">😞</div>
    <div class="sad-face" style="left:65%;">😢</div>
    <div class="sad-face" style="left:80%;">😭</div>
    <div class="sad-face" style="left:95%;">☹️</div>
    """, unsafe_allow_html=True)


questions = [
    {
        "q": "في مثلث قائم، إذا كان الضلعان القائمان 3 و 4، فما طول الوتر؟",
        "a": ["5", "6", "7", "8"],
        "c": "5"
    },
    {
        "q": "في مثلث قائم، الوتر = 13 وأحد الضلعين = 5، أوجد قيمة س للضلع الآخر.",
        "a": ["8", "10", "12", "14"],
        "c": "12"
    },
    {
        "q": "إذا كان س² + 6² = 10²، فما قيمة س؟",
        "a": ["6", "7", "8", "9"],
        "c": "8"
    },
    {
        "q": "في مثلث قائم، إذا كان الوتر 15 وأحد الضلعين 9، فما طول الضلع الآخر؟",
        "a": ["10", "11", "12", "13"],
        "c": "12"
    },
    {
        "q": "أي مجموعة أطوال تمثل مثلثًا قائم الزاوية؟",
        "a": ["6، 8، 10", "4، 5، 6", "7، 8، 9", "5، 6، 8"],
        "c": "6، 8، 10"
    }
]


if "page" not in st.session_state:
    st.session_state.page = "home"
if "i" not in st.session_state:
    st.session_state.i = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "answered" not in st.session_state:
    st.session_state.answered = False
if "selected" not in st.session_state:
    st.session_state.selected = ""
if "result" not in st.session_state:
    st.session_state.result = ""


if st.session_state.page == "home":
    st.markdown("<h1 style='text-align:center; color:#25194f;'>🧠 تحدي عبقري الرياضيات</h1>", unsafe_allow_html=True)

    if st.button("🚀 ابدأ التحدي", use_container_width=True):
        st.session_state.page = "quiz"
        st.rerun()


elif st.session_state.page == "quiz":
    q = questions[st.session_state.i]

    st.markdown(f"<h1 style='text-align:center; color:#25194f;'>السؤال {st.session_state.i + 1} من 5</h1>", unsafe_allow_html=True)
    st.markdown(f"<h2 style='text-align:center; color:#25194f;'>النقاط: {st.session_state.score}</h2>", unsafe_allow_html=True)

    st.markdown(f'<div class="question-box">{q["q"]}</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        if st.button(q["a"][0], use_container_width=True, disabled=st.session_state.answered):
            st.session_state.selected = q["a"][0]
            st.session_state.answered = True
            st.session_state.result = "correct" if q["a"][0] == q["c"] else "wrong"
            if st.session_state.result == "correct":
                st.session_state.score += 1
            st.rerun()

        if st.button(q["a"][2], use_container_width=True, disabled=st.session_state.answered):
            st.session_state.selected = q["a"][2]
            st.session_state.answered = True
            st.session_state.result = "correct" if q["a"][2] == q["c"] else "wrong"
            if st.session_state.result == "correct":
                st.session_state.score += 1
            st.rerun()

    with col2:
        if st.button(q["a"][1], use_container_width=True, disabled=st.session_state.answered):
            st.session_state.selected = q["a"][1]
            st.session_state.answered = True
            st.session_state.result = "correct" if q["a"][1] == q["c"] else "wrong"
            if st.session_state.result == "correct":
                st.session_state.score += 1
            st.rerun()

        if st.button(q["a"][3], use_container_width=True, disabled=st.session_state.answered):
            st.session_state.selected = q["a"][3]
            st.session_state.answered = True
            st.session_state.result = "correct" if q["a"][3] == q["c"] else "wrong"
            if st.session_state.result == "correct":
                st.session_state.score += 1
            st.rerun()

    if st.session_state.result == "correct":
        st.markdown('<div class="correct-box">✅ إجابة صحيحة 🎉</div>', unsafe_allow_html=True)
        st.balloons()

    elif st.session_state.result == "wrong":
        st.markdown('<div class="wrong-box">❌ إجابة خاطئة 😢</div>', unsafe_allow_html=True)
        sad_faces()

    if st.session_state.answered:
        if st.button("التالي ➡️", use_container_width=True):
            st.session_state.answered = False
            st.session_state.selected = ""
            st.session_state.result = ""

            if st.session_state.i < 4:
                st.session_state.i += 1
                st.rerun()
            else:
                st.session_state.page = "end"
                st.rerun()


elif st.session_state.page == "end":
    st.markdown("<h1 style='text-align:center; color:#25194f;'>🎉 انتهى التحدي</h1>", unsafe_allow_html=True)
    st.markdown(f"<h2 style='text-align:center;'>درجتك: {st.session_state.score} من 5</h2>", unsafe_allow_html=True)

    if st.button("🔁 إعادة التحدي", use_container_width=True):
        st.session_state.page = "home"
        st.session_state.i = 0
        st.session_state.score = 0
        st.session_state.answered = False
        st.session_state.selected = ""
        st.session_state.result = ""
        st.rerun()
