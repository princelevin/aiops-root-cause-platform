import { useEffect, useState } from "react";
import "./App.css";

function App() {
  const [incidents, setIncidents] = useState([]);
  const [metrics, setMetrics] = useState([]);
  const [severityFilter, setSeverityFilter] = useState("all");
  const [serviceFilter, setServiceFilter] = useState("all");

  const BACKEND_URL = "http://127.0.0.1:8000";

  const loadIncidents = async () => {
    const response = await fetch(`${BACKEND_URL}/api/incidents`);
    const data = await response.json();
    setIncidents(data.incidents || []);
  };

  const loadMetrics = async () => {
    const response = await fetch(
      `${BACKEND_URL}/api/metrics/generate?count=5&scenario=normal`,
      { method: "POST" }
    );
    const data = await response.json();
    setMetrics(data.metrics || []);
  };

  const refreshDashboard = async () => {
    await loadIncidents();
    await loadMetrics();
  };

  useEffect(() => {
    refreshDashboard();
    const interval = setInterval(refreshDashboard, 5000);
    return () => clearInterval(interval);
  }, []);

  const filteredIncidents = incidents
    .filter((incident) =>
      severityFilter === "all" ? true : incident.severity === severityFilter
    )
    .filter((incident) =>
      serviceFilter === "all" ? true : incident.service === serviceFilter
    )
    .slice(0, 10);

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
            <p>Distributed AI incident detection and root cause analysis dashboard</p>
          </div>
          <div className="status-pill">System Online</div>
        </div>

        <div className="actions">
          <button onClick={refreshDashboard}>Refresh Dashboard</button>
        </div>

        <div className="cards">
          <div className="card">
            <h3>Total Incidents</h3>
            <p>{incidents.length}</p>
          </div>
          <div className="card">
            <h3>Showing</h3>
            <p>{filteredIncidents.length}</p>
          </div>
          <div className="card">
            <h3>Total Metrics</h3>
            <p>{metrics.length}</p>
          </div>
          <div className="card">
            <h3>AI RCA Status</h3>
            <p>Ready</p>
          </div>
        </div>

        <div className="filters">
          <select value={severityFilter} onChange={(e) => setSeverityFilter(e.target.value)}>
            <option value="all">All Severities</option>
            <option value="P0">P0 Critical</option>
            <option value="P1">P1 High</option>
            <option value="P2">P2 Medium</option>
            <option value="P3">P3 Low</option>
          </select>

          <select value={serviceFilter} onChange={(e) => setServiceFilter(e.target.value)}>
            <option value="all">All Services</option>
            <option value="payment-service">payment-service</option>
            <option value="order-service">order-service</option>
            <option value="inventory-service">inventory-service</option>
          </select>
        </div>

        <div className="section">
          <h2>Latest Incidents</h2>

          <div className="incident-header">
            <span>Service</span>
            <span>Severity</span>
            <span>Title</span>
            <span>Status</span>
          </div>

          <div className="table">
            {filteredIncidents.map((incident) => (
              <div className="incident-row" key={incident.id}>
                <span>{incident.service}</span>
                <span className={`badge ${incident.severity.toLowerCase()}`}>
                  {incident.severity}
                </span>
                <span>{incident.title}</span>
                <span>{incident.status}</span>
              </div>
            ))}
          </div>
        </div>

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