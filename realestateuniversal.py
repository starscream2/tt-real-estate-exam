import streamlit as st
import random

# --- CONFIGURATION ---
st.set_page_config(page_title="T&T Real Estate Exam", page_icon="🏠")

# --- DATA: YOUR QUESTIONS ---
# I've used the questions you provided in the script
QUESTIONS = [
    {"q": "Under the Real Property Act (RPA), what is the 'Curtain Principle'?", "a": "B", "options": ["A) The right to hide the owner's name.", "B) The register is the sole source of information; no need to look behind it.", "C) Taxes are hidden from the public.", "D) The deed is kept in a dark room."]},
    {"q": "What is 'Escheat' in T&T land law?", "a": "C", "options": ["A) Cheating on a land survey.", "B) A type of mortgage.", "C) Reversion of property to the State if there are no heirs.", "D) Building on someone else's land."]},
    {"q": "A 'Search' at the Registrar General's office for Old Law land is meant to:", "a": "A", "options": ["A) Verify the 'Chain of Title' is unbroken.", "B) See how much the agent is getting paid.", "C) Check if the neighbors are nice.", "D) Find buried treasure."]},
    {"q": "Under RPO, a 'Caveat' is used to:", "a": "D", "options": ["A) Speed up a sale.", "B) Reduce stamp duty.", "C) Change the land use to commercial.", "D) Forbid the registration of any dealing with the land until a claim is settled."]},
    {"q": "The 'Insurance Principle' in the Torrens system means:", "a": "B", "options": ["A) You must buy fire insurance.", "B) The State compensates those who lose interest due to administrative error.", "C) The agent must have life insurance.", "D) The bank is insured against default."]},
    {"q": "Which of these is NOT a requirement for an individual license under the 2020 Act?", "a": "D", "options": ["A) Being at least 18 years old.", "B) Being a fit and proper person.", "C) Having the required educational qualifications.", "D) Owning at least three properties in T&T."]},
    {"q": "The 'Committee' established under the 2020 Act is the:", "a": "A", "options": ["A) Real Estate Discharge Committee.", "B) Real Estate Agents Licensing Committee.", "C) Property Tax Committee.", "D) FIU Oversight Body."]},
    {"q": "If an agent changes their business address, they must notify the Registrar within:", "a": "B", "options": ["A) 24 hours.", "B) 5 working days.", "C) 30 days.", "D) 1 year."]},
    {"q": "An 'Auctioneer' selling land in T&T:", "a": "C", "options": ["A) Needs no license.", "B) Must be a lawyer.", "C) Must be a licensed real estate agent or specifically exempted.", "D) Must work for the Central Bank."]},
    {"q": "A 'Property Developer' selling their own developed units:", "a": "A", "options": ["A) Is considered an 'Agent' under the 2020 Act and must be licensed.", "B) Is totally exempt from all laws.", "C) Only needs a driver's license.", "D) Must pay the buyer a commission."]},
    {"q": "What is 'Layering' in money laundering?", "a": "B", "options": ["A) Painting a house with multiple coats.", "B) Moving money through complex transactions to hide its origin.", "C) Buying land in different countries.", "D) Subdividing a large estate."]},
    {"q": "A 'Compliance Officer' in a real estate firm is responsible for:", "a": "C", "options": ["A) Making sure the office is clean.", "B) Checking the sales targets.", "C) Ensuring the firm follows FIU and AML/CFT laws.", "D) Valuing the properties."]},
    {"q": "For AML purposes, 'UBO' stands for:", "a": "A", "options": ["A) Ultimate Beneficial Owner.", "B) Under-Budget Option.", "C) United Business Office.", "D) Universal Bank Operator."]},
    {"q": "An agent must file a Terrorist Property Report (TPR) to the FIU:", "a": "D", "options": ["A) Monthly.", "B) Annually.", "C) Only if they feel like it.", "D) Immediately if they have property in their possession linked to a terrorist."]},
    {"q": "In T&T, 'Structuring' (Smurfing) involves:", "a": "B", "options": ["A) Designing a better house.", "B) Breaking down large cash sums into small amounts to avoid reporting thresholds.", "C) Building multiple houses on one lot.", "D) Creating a fake real estate company."]}
]

# --- SESSION STATE ---
if 'quiz_data' not in st.session_state:
    # Shuffle only once per session
    st.session_state.quiz_data = random.sample(QUESTIONS, len(QUESTIONS))
    st.session_state.score = 0
    st.session_state.submitted = False

# --- UI ---
st.title("🇹🇹 T&T Real Estate Professional Exam")
st.info("Study Module: Real Estate Agents Act 2020, RPO, and AML/CFT.")

with st.form("quiz_form"):
    user_answers = []
    for i, item in enumerate(st.session_state.quiz_data):
        st.markdown(f"**Question {i+1}:** {item['q']}")
        choice = st.radio("Select an option:", item['options'], key=f"q{i}", index=None)
        # Store just the letter (A, B, C, or D) for comparison
        user_answers.append(choice[0] if choice else None)
        st.divider()
    
    submitted = st.form_submit_button("Submit Exam")

if submitted:
    st.session_state.submitted = True
    score = 0
    results = []
    
    for i, item in enumerate(st.session_state.quiz_data):
        if user_answers[i] == item['a']:
            score += 1
        else:
            results.append(f"Question {i+1}: Incorrect. Correct answer was {item['a']}")
    
    st.session_state.score = score
    
    # Display Results
    st.header(f"Final Score: {score} / {len(st.session_state.quiz_data)}")
    percent = (score / len(st.session_state.quiz_data)) * 100
    
    if percent >= 75:
        st.success(f"PASS ({percent}%). You are ready for the Board!")
        st.balloons()
    else:
        st.error(f"FAIL ({percent}%). Study the RPO and Act 2020 again.")
        for r in results:
            st.write(r)

if st.session_state.submitted:
    if st.button("Retake Exam"):
        st.session_state.quiz_data = random.sample(QUESTIONS, len(QUESTIONS))
        st.session_state.submitted = False
        st.rerun()