import streamlit as st
import random

# --- CONFIGURATION ---
st.set_page_config(page_title="T&T Real Estate Exam", page_icon="🏠")

# --- DATA: THE 30 QUESTIONS ---
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
    {"q": "In T&T, 'Structuring' (Smurfing) involves:", "a": "B", "options": ["A) Designing a better house.", "B) Breaking down large cash sums into small amounts to avoid reporting thresholds.", "C) Building multiple houses on one lot.", "D) Creating a fake real estate company."]},
    {"q": "The 'Residual Method' is primarily used to value:", "a": "C", "options": ["A) Old houses.", "B) Government buildings.", "C) Land with development or redevelopment potential.", "D) Rented apartments."]},
    {"q": "What is 'Market Value'?", "a": "A", "options": ["A) The estimated price between a willing buyer and willing seller at arm's length.", "B) The price the owner wants.", "C) The price the bank says it is worth for a quick sale.", "D) The tax assessment value."]},
    {"q": "A 'Valuation Report' in T&T must be signed by:", "a": "D", "options": ["A) The Real Estate Agent.", "B) The Lawyer.", "C) The Buyer.", "D) A qualified professional Valuer (usually a member of RICS or similar)."]},
    {"q": "The 'Investment Method' uses 'Years Purchase' (YP). What does YP represent?", "a": "B", "options": ["A) The number of years the owner has held the property.", "B) The multiplier used to convert annual income into capital value.", "C) The age of the building.", "D) The length of the mortgage."]},
    {"q": "In construction, 'Liquidated Damages' are:", "a": "C", "options": ["A) Damage caused by a flood.", "B) Money paid to the agent if the sale fails.", "C) A pre-agreed sum paid by a contractor for late completion.", "D) The cost of tearing down a wall."]},
    {"q": "A 'Fixed Rate Mortgage' means:", "a": "A", "options": ["A) The interest rate stays the same for a set period.", "B) The house is fixed to the ground.", "C) The bank cannot sell the house.", "D) The price of the house is fixed."]},
    {"q": "What is an 'Equity' in a property?", "a": "C", "options": ["A) The total debt.", "B) The legal title.", "C) The market value minus any outstanding mortgages/liens.", "D) The monthly rent."]},
    {"q": "In T&T, 'Stamp Duty' on a $2.5 Million residential property is roughly:", "a": "B", "options": ["A) 0% (Exempt).", "B) Calculated on a tiered scale (5%, 7.5%, etc.).", "C) Flat fee of $500.", "D) Paid by the government."]},
    {"q": "An 'Encroachment' occurs when:", "a": "D", "options": ["A) A tenant leaves early.", "B) A buyer backs out.", "C) The bank raises interest rates.", "D) A neighbor builds a structure that crosses the property boundary line."]},
    {"q": "Which of the following is an 'Incorporeal Hereditament'?", "a": "A", "options": ["A) An Easement (Right of Way).", "B) A physical house.", "C) A bag of cement.", "D) A fence."]},
    {"q": "Who pays the 'Deed of Lease' preparation fee usually?", "a": "B", "options": ["A) The Landlord.", "B) The Tenant.", "C) The Agent.", "D) The FIU."]},
    {"q": "What is a 'Negative Covenant'?", "a": "C", "options": ["A) A bad review of the agent.", "B) A debt owed to the bank.", "C) A promise NOT to do something on the land (e.g., no commercial use).", "D) An unsigned contract."]},
    {"q": "What is 'Adverse Possession' in T&T?", "a": "A", "options": ["A) Gaining legal title to land by occupying it without permission for 16+ years (Old Law).", "B) Buying land from the state.", "C) Renting a property for a long time.", "D) Inheriting property from a stranger."]},
    {"q": "A 'Qualified Title' under RPO means:", "a": "B", "options": ["A) The owner is a qualified doctor.", "B) The title has some reservation or defect that the Registrar has noted.", "C) The title is perfect.", "D) The land is for farming only."]},
    {"q": "What is the 'Highest and Best Use' concept in valuation?", "a": "D", "options": ["A) Building the tallest skyscraper possible.", "B) Using the land for a park.", "C) Selling the land as quickly as possible.", "D) The use that is legally permissible, physically possible, and results in the highest value."]}
]

# --- SESSION STATE ---
if 'quiz_data' not in st.session_state:
    st.session_state.quiz_data = random.sample(QUESTIONS, len(QUESTIONS))
    st.session_state.submitted = False

# --- UI ---
st.title("🇹🇹 T&T Real Estate Professional Exam")
st.info("Study Module: Real Estate Agents Act 2020, RPO, and AML/CFT.")

with st.form("quiz_form"):
    user_answers = []
    for i, item in enumerate(st.session_state.quiz_data):
        st.markdown(f"**Question {i+1}:** {item['q']}")
        choice = st.radio("Select an option:", item['options'], key=f"q{i}", index=None)
        # Extract the letter from the chosen string (e.g., "A) Option" -> "A")
        user_answers.append(choice[0] if choice else None)
        st.divider()
    
    submitted = st.form_submit_button("Submit Exam")

if submitted:
    st.session_state.submitted = True
    score = 0
    incorrect_indices = []
    
    for i, item in enumerate(st.session_state.quiz_data):
        if user_answers[i] == item['a']:
            score += 1
        else:
            incorrect_indices.append(i)
    
    # Results Summary
    st.header(f"Final Score: {score} / {len(st.session_state.quiz_data)}")
    percent = (score / len(st.session_state.quiz_data)) * 100
    
    if percent >= 75:
        st.success(f"PASS ({percent:.1f}%). Excellent work!")
        st.balloons()
    else:
        st.error(f"FAIL ({percent:.1f}%). Keep studying the RPO and Act 2020.")

    # --- THE "CORRECT ANSWERS" SECTION ---
    if incorrect_indices:
        with st.expander("🔍 Review Incorrect Answers"):
            for idx in incorrect_indices:
                q_item = st.session_state.quiz_data[idx]
                st.markdown(f"**Question {idx+1}:** {q_item['q']}")
                st.write(f"❌ **Your Answer:** {user_answers[idx] if user_answers[idx] else 'No answer provided'}")
                # Find the full text of the correct answer for clarity
                correct_text = next((opt for opt in q_item['options'] if opt.startswith(q_item['a'])), q_item['a'])
                st.write(f"✅ **Correct Answer:** {correct_text}")
                st.divider()
    else:
        st.success("Perfect score! No corrections needed.")

if st.session_state.submitted:
    if st.button("Retake Exam"):
        st.session_state.quiz_data = random.sample(QUESTIONS, len(QUESTIONS))
        st.session_state.submitted = False
        st.rerun()
