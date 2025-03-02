import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
import time

# Page config
st.set_page_config(page_title="Growth Mindset Challenge", page_icon="🌱", layout="wide")

# Custom CSS for background color
st.markdown("""
    <style>
        .main { background-color: #F4F7FA; }
        .block-container { padding-top: 20px; }
        h1, h2, h3 { color: #3563E9; }
        .sidebar .sidebar-content { background-color: #E3ECF9; }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("Growth Mindset Challenge")

# Sidebar
st.sidebar.header(" About You")
name = st.sidebar.text_input("Enter your name:")
age = st.sidebar.slider("Select your age:", 5, 100, 20)
st.sidebar.success(f"Welcome, {name}!" if name else "Please enter your name.")

st.markdown("---")
# Growth Mindset Quiz
st.header(" Growth Mindset Quiz")
questions = [
    "I believe I can improve my skills with effort.",
    "I see challenges as opportunities to learn.",
    "I learn from my mistakes.",
    "I persist even when things get tough.",
    "I celebrate my effort."
]
responses = []
for i, question in enumerate(questions):
    response = st.radio(
        f"{question}",
        ("Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"),
        key=f"q{i}"
    )
    responses.append(response)

if st.button("Submit Quiz"):
    score = sum({
        "Strongly Disagree": 1,
        "Disagree": 2,
        "Neutral": 3,
        "Agree": 4,
        "Strongly Agree": 5
    }[response] for response in responses)

    st.progress(score / 25)
    st.info(f"Your Growth Mindset Score: **{score}/25**")

    if score >= 20:
        st.success("🌟 Excellent Growth Mindset!")
    elif score >= 15:
        st.warning("💡 Good job! Keep developing your mindset.")
    else:
        st.error("🔄 Keep practicing your growth mindset!")

# Separator between Quiz and Daily Challenge
st.markdown("---")

# Daily Growth Mindset Challenge
st.header(" Daily Growth Mindset Challenge")
challenge = st.selectbox(
    "Choose your challenge for today:",
    [
        "Learn something new.",
        "Reflect on a mistake.",
        "Try a difficult task.",
        "Support someone's progress.",
        "Ask for feedback."
    ]
)
st.success(f"Today's Challenge: **{challenge}**")


st.markdown("---")

# Daily Reflection Journal
st.header("Daily Reflection Journal")
reflection = st.text_area("What did you learn today?")
if st.button("Save Reflection"):
    if reflection:
        if "reflections" not in st.session_state:
            st.session_state.reflections = []
        st.session_state.reflections.append({"date": datetime.date.today(), "reflection": reflection})
        st.success("Reflection saved!")

if "reflections" in st.session_state and st.session_state.reflections:
    st.subheader("🗂️ Your Past Reflections")
    for entry in st.session_state.reflections:
        st.write(f"**{entry['date']}** — {entry['reflection']}")

st.markdown("---")

# Progress Tracker
st.header("Track Your Progress")
progress = st.slider("Progress Today (%):", 0, 100, 50)

if st.button("Save Progress"):
    if "progress_data" not in st.session_state:
        st.session_state.progress_data = []
    st.session_state.progress_data.append({"date": datetime.date.today(), "progress": progress})
    st.success("Progress saved!")

if "progress_data" in st.session_state and st.session_state.progress_data:
    df = pd.DataFrame(st.session_state.progress_data)
    df['date'] = pd.to_datetime(df['date']).dt.strftime('%b %d')  # Format dates like 'Mar 02'
    
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(df['date'], df['progress'], color='#3563E9', alpha=0.8)
    
    ax.set_xlabel('Date', fontsize=12)
    ax.set_ylabel('Progress (%)', fontsize=12)
    ax.set_title('📊 Your Progress Over Time', fontsize=14, color='#3563E9')
    ax.set_ylim(0, 100)
    
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.xticks(rotation=45)
    
    st.pyplot(fig)


st.markdown("---")

# Growth Mindset Focus Timer
st.header(" Growth Mindset Focus Timer")

if "timer_running" not in st.session_state:
    st.session_state.timer_running = False

duration_minutes = st.number_input("Set Timer (minutes):", min_value=1, max_value=120, value=1)
duration_seconds = st.number_input("Set Timer (additional seconds):", min_value=0, max_value=59, value=0)

total_seconds = duration_minutes * 60 + duration_seconds

if st.button("Start Timer"):
    st.session_state.timer_running = True
    timer_placeholder = st.empty()
    end_time = time.time() + total_seconds
    st.success(f"Timer started for {duration_minutes} min {duration_seconds} sec!")

    while True:
        remaining = int(end_time - time.time())
        if remaining <= 0:
            timer_placeholder.markdown("## Time's up!")
            st.balloons()
            st.session_state.timer_running = False
            break
        mins, secs = divmod(remaining, 60)
        timer_placeholder.markdown(f"##  Time left: **{mins:02d}:{secs:02d}**")
        time.sleep(1)


st.markdown("---")

# Motivational Quote
st.header("💬 Motivational Quote of the Day")
quotes = [
    "“The only limit to our realization of tomorrow is our doubts of today.”",
    "“It’s not that I’m so smart, it’s just that I stay with problems longer.”",
    "“Success is not final, failure is not fatal.”",
    "“You don’t have to be great to start, but you have to start to be great.”",
    "“Believe you can and you’re halfway there.”"
]
st.info(np.random.choice(quotes))

st.markdown("---")
st.markdown("<center>Developed by Areesha Kainat</center>", unsafe_allow_html=True)
