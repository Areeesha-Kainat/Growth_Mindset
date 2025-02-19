import streamlit as st
import pandas as pd
import numpy as np

# Title of the app
st.title(" Growth Mindset Challenge ")

# Introduction
st.write("""
Welcome to the **Growth Mindset Challenge**! 
This app will help you practice and track your growth mindset journey. 
Let's get started!
""")

# Sidebar for user input
st.sidebar.header("About You")
name = st.sidebar.text_input("What's your name?")
age = st.sidebar.slider("How old are you?", 5, 100, 20)
st.sidebar.write(f"Hi {name}! Let's grow together! 🌱")

# Growth Mindset Quiz
st.header("📝 Growth Mindset Quiz")
st.write("Answer these questions to see how much you embrace a growth mindset!")

# Questions
questions = [
    "I believe I can improve my skills with effort.",
    "I see challenges as opportunities to learn.",
    "I learn from my mistakes and don't feel ashamed of them.",
    "I persist even when things get tough.",
    "I celebrate my effort, not just the results."
]

# User responses
responses = []
for i, question in enumerate(questions):
    response = st.radio(f"Q{i+1}: {question}", ("Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"))
    responses.append(response)

# Calculate score
if st.button("Submit Quiz"):
    score = 0
    for response in responses:
        if response == "Strongly Agree":
            score += 5
        elif response == "Agree":
            score += 4
        elif response == "Neutral":
            score += 3
        elif response == "Disagree":
            score += 2
        else:
            score += 1
    
    st.write(f"Your Growth Mindset Score: **{score}/25**")
    if score >= 20:
        st.success("🎉 Amazing! You have a strong growth mindset!")
    elif score >= 15:
        st.warning("👍 Good job! You're on the right track, but there's room to grow!")
    else:
        st.error("💪 Don't worry! You can develop a growth mindset with practice!")

# Daily Challenge
st.header("💪 Daily Growth Mindset Challenge")
challenge = st.selectbox("Choose a challenge for today:", [
    "Learn something new and share it with a friend.",
    "Reflect on a mistake and write down what you learned.",
    "Try a task you find difficult and don't give up!",
    "Celebrate someone else's effort and progress.",
    "Ask for feedback on something you're working on."
])
st.write(f"Your challenge for today: **{challenge}**")

# Track Progress
st.header("📊 Track Your Progress")
progress = st.slider("How much progress did you make today? (0% - 100%)", 0, 100, 50)
st.write(f"You're **{progress}%** closer to your growth mindset goals!")

# Motivational Quote
st.header("✨ Motivational Quote")
quotes = [
    "The only limit to our realization of tomorrow is our doubts of today. – Franklin D. Roosevelt",
    "It’s not that I’m so smart, it’s just that I stay with problems longer. – Albert Einstein",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. – Winston Churchill",
    "You don’t have to be great to start, but you have to start to be great. – Zig Ziglar",
    "Believe you can and you’re halfway there. – Theodore Roosevelt"
]
random_quote = np.random.choice(quotes)
st.write(f"*{random_quote}*")

# Footer
st.write("---")
st.write("Made by Areesha Kainat")
