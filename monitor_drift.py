import pandas as pd
from evidently import Report
from evidently.presets import DataDriftPreset

print("📊 Starting Clean Data Drift Monitoring Engine...")

# 1. Reference Data (What your model trained on)
reference_data = pd.DataFrame({
    "sqft": [1000.0, 1200.0, 1500.0, 1800.0, 2000.0],
    "rooms": [2.0, 2.0, 3.0, 3.0, 4.0],
})

# 2. Simulated Production Data (New incoming user inputs)
production_data = pd.DataFrame({
    "sqft": [4000.0, 4500.0, 5200.0, 5800.0, 6000.0],
    "rooms": [5.0, 5.0, 6.0, 6.0, 7.0],
})

# 3. Initialize the Report Structure definition
report_definition = Report(metrics=[DataDriftPreset()])

print("🧮 Running statistical drift report pipeline...")

# 4. FIX: Capture the actual evaluation object run output [INDEX]
evaluation_run = report_definition.run(
    reference_data=reference_data, current_data=production_data
)

# 5. Export your interactive visual dashboard using the run output [INDEX]
evaluation_run.save_html("drift_report.html")

print("\n🚨 ANALYSIS COMPLETE 🚨")
print("💾 Interactive visual dashboard securely saved as 'drift_report.html'")

