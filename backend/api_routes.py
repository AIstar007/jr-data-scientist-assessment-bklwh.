from flask import Blueprint, jsonify, request
import psycopg2

api_blueprint = Blueprint('api', __name__)

def get_db_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="hospital_db",
        user="your_user",
        password="your_password"
    )
    return conn

@api_blueprint.route('/patient/<int:patient_id>', methods=['GET'])
def get_patient(patient_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM patients WHERE patient_id = %s;', (patient_id,))
    patient = cur.fetchone()
    cur.close()
    conn.close()
    if patient:
        return jsonify(patient)
    else:
        return jsonify({"error": "Patient not found"}), 404

@api_blueprint.route('/summary', methods=['GET'])
def get_summary():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT COUNT(*) FROM patients;')
    patient_count = cur.fetchone()[0]
    # Add additional queries as needed
    cur.close()
    conn.close()
    return jsonify({"patient_count": patient_count})
