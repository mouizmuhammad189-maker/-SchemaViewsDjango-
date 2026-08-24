import sqlite3

connection = sqlite3.connect("db.sqlite3")
cursor = connection.cursor()

tables = [
    "alpha_clinic_system_Doctor",
    "alpha_clinic_system_Patient",
    "alpha_clinic_system_Appointment",
    "alpha_clinic_system_LabTest",
    "alpha_clinic_system_Prescription",
    "alpha_clinic_system_Medicine",
    "alpha_clinic_system_MedicalRecord",
    "alpha_clinic_system_Bill",
]

for table in tables:
    cursor.execute(f"DROP TABLE IF EXISTS {table}")
    print(f"Dropped: {table}")

connection.commit()
connection.close()

print("Vehicle rental tables removed.")