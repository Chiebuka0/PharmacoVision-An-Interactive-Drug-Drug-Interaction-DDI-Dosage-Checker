import sys

def calculate_crcl(age, weight, scr, gender):
    """Calculates patient CrCl using the Cockcroft-Gault equation."""
    modifier = 0.85 if gender.lower() == "female" else 1.0
    if scr == 0: return 0
    return ((140 - age) * weight) / (72 * scr) * modifier

def screen_interactions(drug_a, drug_b):
    """Checks for high-alert drug-drug interactions."""
    pairs = {
        ("warfarin", "aspirin"): "🔴 HIGH RISK: Increased major bleeding risk. Closely monitor INR.",
        ("sildenafil", "nitroglycerin"): "❌ CONTRAINDICATED: Severe, fatal hypotension risk. Do not combine.",
        ("lisinopril", "spironolactone"): "⚠️ MODERATE RISK: Hyperkalemia risk. Monitor serum potassium."
    }
    key = tuple(sorted([drug_a.lower(), drug_b.lower()]))
    return pairs.get(key, "✅ No major high-alert interactions found in this tier.")

def main():
    print("=" * 50)
    print("💊 PHARMACOVISION: CLINICAL TOOLKIT REPORT 💊")
    print("=" * 50)
    
    # Mocking a clinical profile for the automation run
    age, weight, scr, gender = 68, 74, 1.4, "female"
    drug_a, drug_b = "Sildenafil", "Nitroglycerin"
    
    crcl = calculate_crcl(age, weight, scr, gender)
    
    print(f"\n👤 PATIENT CASE STUDY PROFILE:")
    print(f"   Age: {age} yrs | Weight: {weight} kg | Sex: {gender.upper()} | SrCr: {scr} mg/dL")
    print(f"   Calculated CrCl: {crcl:.1f} mL/min")
    
    print(f"\n⚡ ENCOUNTERED PRE-SCRIBER ORDERS:")
    print(f"   Medication A: {drug_a} | Medication B: {drug_b}")
    
    print(f"\n🔍 AUTOMATED CLINICAL ALERTS:")
    print(f"   Interaction Status: {screen_interactions(drug_a, drug_b)}")
    
    if crcl < 30:
        print("   Renal Adjustment: ⚠️ Severe Impairment. Contraindicate Metformin. Reduce Gabapentin.")
    elif crcl < 60:
        print("   Renal Adjustment: ⚠️ Moderate Impairment. Cap Metformin at 1000mg/day.")
    else:
        print("   Renal Adjustment: ✅ Normal clearance profile.")
    print("=" * 50)

if __name__ == "__main__":
    main()
