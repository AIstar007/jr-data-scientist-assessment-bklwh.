import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Bar } from 'react-chartjs-2';

const Dashboard = () => {
  const [summary, setSummary] = useState({});

  useEffect(() => {
    axios.get('http://localhost:5000/api/summary') // Ensure your Flask API is running on port 5000
      .then(response => {
        setSummary(response.data);
      })
      .catch(error => console.error('Error fetching summary', error));
  }, []);

  const data = {
    labels: ['Total Patients'],
    datasets: [{
      label: 'Number of Patients',
      data: [summary.patient_count || 0],
      backgroundColor: 'rgba(75,192,192,0.4)',
      borderColor: 'rgba(75,192,192,1)',
      borderWidth: 1
    }]
  };

  return (
    <div style={{ padding: '20px' }}>
      <h2>Hospital Dashboard</h2>
      <Bar data={data} />
    </div>
  );
};

export default Dashboard;
