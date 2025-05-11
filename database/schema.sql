CREATE TABLE patients (
    patient_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    date_of_birth DATE,
    gender VARCHAR(10),
    contact_info VARCHAR(100)
);

CREATE TABLE deliveries (
    delivery_id SERIAL PRIMARY KEY,
    patient_id INT REFERENCES patients(patient_id),
    delivery_date DATE,
    delivery_method VARCHAR(50),
    outcome VARCHAR(50)
);

CREATE TABLE followups (
    followup_id SERIAL PRIMARY KEY,
    patient_id INT REFERENCES patients(patient_id),
    followup_date DATE,
    notes TEXT
);
