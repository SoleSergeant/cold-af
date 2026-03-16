import streamlit as st
import google.generativeai as genai

# --- PAGE CONFIG ---
st.set_page_config(page_title="ColdAF", page_icon="❄️")

st.title("❄️ ColdAF (Cold As F***)")
st.subheader("Turn deep-dive research into high-conversion outreach.")

# --- SIDEBAR: SETTINGS ---
with st.sidebar:
    st.title("Settings")
    api_key = st.text_input("Enter Gemini API Key:", type="password")
    st.info("Get your key at aistudio.google.com")

# --- INPUT SECTION ---
col1, col2 = st.columns(2)

with col1:
    linkedin_data = st.text_area("LinkedIn 'About' or Recent Posts:", placeholder="Paste their latest post or bio here...")
    x_data = st.text_area("X (Twitter) Insights:", placeholder="What are they ranting about lately?")

with col2:
    tg_data = st.text_area("Telegram Channel Snippets:", placeholder="Any specific alpha they shared?")
    user_goal = st.text_input("Your Goal:", placeholder="e.g., Get a referral for the SWE internship")

# --- THE MAGIC BUTTON ---
if st.button("Generate ColdAF Email"):
    if not api_key:
        st.error("Please enter your API Key in the sidebar!")
    else:
        try:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-1.5-flash')
            
            # The "Super Fan" Prompt
            prompt = f"""
            You are 'ColdAF', an elite cold outreach assistant for students.
            Your style is 'The Super Fan': Deeply researched, high-respect, but zero fluff.
            
            TARGET DATA:
            LinkedIn: {linkedin_data}
            X/Twitter: {x_data}
            Telegram: {tg_data}
            
            STUDENT'S GOAL: {user_goal}
            
            INSTRUCTIONS:
            1. Identify a 'Deep Cut' (a specific technical point or opinion they shared).
            2. Connect that Deep Cut to the Student's Goal.
            3. Write an email that makes the recipient feel like a celebrity/expert.
            4. Keep it under 150 words. No "I hope you are well." Start with the hook.
            """
            
            response = model.generate_content(prompt)
            
            st.success("Analysis Complete! Here is your ColdAF outreach:")
            st.markdown("---")
            st.write(response.text)
            st.markdown("---")
            
        except Exception as e:
            st.error(f"An error occurred: {e}")
