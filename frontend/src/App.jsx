import { useEffect, useState } from "react";
import "./App.css";

function App() {
  const [incidents, setIncidents] = useState([]);
  const [metrics, setMetrics] = useState([]);

  const BACKEND_URL = "http://127.0.0.1:8000";

  // Load incidents
  const loadIncidents = async () => {
    try {
      const response = await fetch(`${BACKEND_URL}/api/incidents`);
      const data = await response.json();

      setIncidents(data.incidents || []);
    } catch (error) {
      console.error("Failed to load incidents", error);
    }
  };

  // Load metrics
  const loadMetrics = async () => {
    try {
      const response = await fetch(
        `${BACKEND_URL}/api/metrics/generate?count=5&scenario=normal`,
        {
          method: "POST",
        }
      );

      const data = await response.json();

      setMetrics(data.metrics || []);
    } catch (error) {
      console.error("Failed to load metrics", error);
    }
  };

  // Refresh everything
  const refreshDashboard = async () => {
    await loadIncidents();
    await loadMetrics();
  };

  // Auto refresh every 5 sec
  useEffect(() => {
    refreshDashboard();

    const interval = setInterval(() => {
      refreshDashboard();
    }, 5000);

    return () => clearInterval(interval);
  }, []);

  return (
    <div className="app">
      <div className="sidebar">
        <h2>AIOps</h2>
        <p>Root Cause Platform</p>
      </div>

      <div className="main">
        <div className="header">
          <div>
            <h1>AI Ops Root Cause Platform</h1>

            <p>
              Distributed AI incident detection and root cause analysis dashboard
            </p>
          </div>

          <div className="status-pill">System Online</div>
        </div>

        <div className="actions">
          <button onClick={refreshDashboard}>
            Refresh Dashboard
          </button>
        </div>

        <div className="cards">
          <div className="card">
            <h3>Total Incidents</h3>
            <p>{incidents.length}</p>
          </div>

          <div className="card">
            <h3>Total Metrics</h3>
            <p>{metrics.length}</p>
          </div>

          <div className="card">
            <h3>Services</h3>
            <p>3</p>
          </div>

          <div className="card">
            <h3>AI RCA Status</h3>
            <p>Ready</p>
          </div>
        </div>

        {/* INCIDENTS */}
        <div className="section">
          <h2>Live Incidents</h2>

          <div className="table">
            {incidents.map((incident) => (
              <div className="row" key={incident.id}>
                <div>{incident.service}</div>

                <div className="severity">
                  {incident.severity}
                </div>

                <div>{incident.title}</div>

                <div>{incident.status}</div>
              </div>
            ))}
          </div>
        </div>

        {/* METRICS */}
        <div className="section">
          <h2>Latest Metrics</h2>

          <div className="table">
            {metrics.map((metric) => (
              <div className="row" key={metric.id}>
                <div>{metric.service}</div>

                <div>{metric.latency_ms} ms</div>

                <div>{metric.error_rate}% errors</div>

                <div>{metric.cpu_usage}% CPU</div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;