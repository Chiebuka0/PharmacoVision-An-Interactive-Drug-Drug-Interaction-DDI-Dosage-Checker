import streamlit as st

# Set up page configurations
st.set_page_config(page_title="PharmacoVision Dashboard", page_icon="💊", layout="wide")

st.title("💊 PharmacoVision: Clinical Decision Support Tool")
st.markdown("### Advanced Drug-Drug Interaction & Renal Dosage Calculator")
st.write("---")

# Sidebar for Patient Vitals
st.sidebar.header("👤 Patient Demographics & Vitals")
age = st.sidebar.number_input("Age (years)", min_value=1, max_value=120, value=65)
weight = st.sidebar.number_input("Weight (kg)", min_value=10, max_value=200, value=70)
serum_creatinine = st.sidebar.number_input("Serum Creatinine (mg/dL)", min_value=0.2, max_value=10.0, value=1.2, step=0.1)
gender = st.sidebar.radio("Biological Sex", ["Male", "Female"])

# Calculate Mock Cockcroft-Gault CrCl
gender_modifier = 0.85 if gender == "Female" else 1.0
crcl = ((140 - age) * weight) / (72 * serum_creatinine) * gender_modifier

st.sidebar.metric(label="Estimated CrCl (mL/min)", value=f"{crcl:.1f}")

# Main Layout: DDI Checker
st.header("⚡ Drug-Drug Interaction (DDI) Screener")
col1, col2 = st.columns(2)

with col1:
    drug_a = st.selectbox("Select Medication A", ["None", "Warfarin", "Sildenafil", "Simvastatin", "Lisinopril"])
with col2:
    drug_b = st.selectbox("Select Medication B", ["None", "Aspirin", "Nitroglycerin", "Amlodipine", "Spironolactone"])

# Interaction Logic Database
interactions = {
    ("Warfarin", "Aspirin"): ("🔴 High Risk", "Increased risk of major bleeding. Monitor INR closely."),
    ("Sildenafil", "Nitroglycerin"): ("🔴 Contraindicated", "Severe, potentially fatal hypotension. Do not co-administer."),
    ("Simvastatin", "Amlodipine"): ("🟡 Moderate Risk", "Amlodipine increases simvastatin exposure. Limit simvastatin to 20mg daily."),
    ("Lisinopril", "Spironolactone"): ("🟡 Moderate Risk", "Hyperkalemia risk. Monitor serum potassium levels regularly.")
}

if drug_a != "None" and drug_b != "None":
    result = interactions.get((drug_a, drug_b)) or interactions.get((drug_b, drug_a))
    
    if result:
        severity, mechanism = result
        if "🔴" in severity:
            st.error(f"**{severity}**\n\n**Clinical Mechanism:** {mechanism}")
        else:
            st.warning(f"**{severity}**\n\n**Clinical Mechanism:** {mechanism}")
    else:
        st.success("✅ No major documented interaction found between selected drugs in this database tier.")
else:
    st.info("Select two medications above to analyze potential kinetic or dynamic interactions.")

# Section 2: Renal Adjustments Based on Calculated CrCl
st.write("---")
st.header("📉 Renal Clearance Adjustments")

if crcl < 30:
    st.error("⚠️ **Severe Renal Impairment (CrCl < 30 mL/min)**")
    st.markdown("- **Metformin:** Contraindicated.")
    st.markdown("- **Gabapentin:** Reduce maintenance dose significantly (e.g., 300mg every other day).")
elif crcl < 60:
    st.warning("⚠️ **Moderate Renal Impairment (CrCl 30-59 mL/min)**")
    st.markdown("- **Metformin:** Max dose 1000mg/day. Monitor eGFR closely.")
    st.markdown("- **Enoxaparin:** Adjust therapeutic dosing to 1mg/kg every 24 hours.")
else:
    st.success("✅ **Normal to Mildly Decreased Renal Function (CrCl ≥ 60 mL/min)**")
    st.write("Standard empirical dosing protocols apply for most cleared therapeutics.")
