import pandas as pd

# 1. Load dataset
df = pd.read_csv("data/diabetic_data.csv")

# 2. Basic cleaning
# Replace '?' with NaN
df = df.replace("?", pd.NA)

# Drop columns with too many missing values (like weight, payer_code, medical_specialty)
df = df.drop(columns=["weight", "payer_code", "medical_specialty"])

# 3. Focus on key columns
cols_to_keep = [
    "race", "gender", "age", "admission_type_id", "discharge_disposition_id",
    "admission_source_id", "time_in_hospital", "num_lab_procedures",
    "num_procedures", "num_medications", "number_outpatient",
    "number_emergency", "number_inpatient", "diag_1", "diag_2", "diag_3",
    "number_diagnoses", "readmitted"
]
df = df[cols_to_keep]

# 4. Encode readmission flag
# Values are: '<30', '>30', 'NO'
df["readmitted_flag"] = df["readmitted"].apply(lambda x: 1 if x == "<30" else 0)

# 5. Save processed file
df.to_csv("data/processed_readmission.csv", index=False)

print("✅ Processed readmission dataset saved at /data/processed_readmission.csv")

