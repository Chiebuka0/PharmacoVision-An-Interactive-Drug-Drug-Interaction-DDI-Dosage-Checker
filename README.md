# PharmacoVision-An-Interactive-Drug-Drug-Interaction-DDI-Dosage-Checker
This is a web app where a user selects two medications, and the app instantly flags potential Drug-Drug Interactions (DDIs), calculates an approximate renal clearance dosage adjustment (based on a mockup of the Cockcroft-Gault equation), and displays the information in a clean, clinical dashboard.
# 💊 PharmacoVision: Automated Clinical Decision Support Script

An advanced Python-driven clinical toolkit configured to execute via automated CI/CD pipelines. This repository demonstrates the intersection of software logic and clinical pharmacy parameters.

## ⚙️ How to Run This Tool Live on GitHub
1. Navigate to the **Actions** tab at the top of this repository.
2. Select **Execute Clinical Automation Test** from the left sidebar.
3. Click the **Run workflow** dropdown on the right and hit the green button.
4. Open the completed run to view the simulated **Clinical Patient Report** generated natively in the console!

## 🚀 Engineered Clinical Logic
* **Algorithmic Clearance Tracker:** Uses an integrated Cockcroft-Gault calculation formula to map patient serum metrics to renal functional capacity.
* **Dynamic Safety Screener:** Automatically flags high-alert, lethal drug-drug interactions (e.g., Nitrates + PDE5 inhibitors) from an embedded clinical database matrix.
* **Automated Dose Adjustments:** Programmatically flags warnings and recommends alternative drug selection parameters based on computed renal clearance tiers.
