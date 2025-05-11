-- Patients with most follow-ups
SELECT p.patient_id, p.first_name, p.last_name, COUNT(f.followup_id) AS followup_count
FROM patients p
JOIN followups f ON p.patient_id = f.patient_id
GROUP BY p.patient_id
ORDER BY followup_count DESC;

-- Delivery trends per month
SELECT DATE_TRUNC('month', delivery_date) AS month, COUNT(*) AS delivery_count
FROM deliveries
GROUP BY month
ORDER BY month;
