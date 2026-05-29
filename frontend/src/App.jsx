import { useEffect, useState } from "react";
import "./App.css";

function App() {
  const [incidents, setIncidents] = useState([]);
  const [metrics, setMetrics] = useState([]);
  const [severityFilter, setSeverityFilter] = useState("all");
  const [serviceFilter, setServiceFilter] = useState("all");
  const [selectedIncident, setSelectedIncident] = useState(null);
  const [correlationData, setCorrelationData] = useState(null);
  const [reportData, setReportData] = useState(null);
  const [guardrailData, setGuardrailData] = useState(null);

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

  const injectFailure = async (failureType) => {
    await fetch(`${BACKEND_URL}/api/failures/inject/${failureType}`, {
      method: "POST",
    });
    await refreshDashboard();
  };

  const fetchCorrelation = async (incidentId) => {
    const response = await fetch(`${BACKEND_URL}/api/correlation/${incidentId}`);
    const data = await response.json();

    setSelectedIncident(incidentId);
    setCorrelationData(data);

    setTimeout(() => {
      document
        .getElementById("correlations")
        ?.scrollIntoView({ behavior: "smooth", block: "start" });
    }, 100);
  };

  const generateReport = async () => {
  if (!selectedIncident) {
    alert("Please select an incident first");
    return;
  }

  await fetch(`${BACKEND_URL}/api/rca/${selectedIncident}`);

  const response = await fetch(
    `${BACKEND_URL}/api/reports/incident/${selectedIncident}`
  );

  const data = await response.json();
    setReportData(data.report);
  };

  const checkGuardrails = async () => {
    if (!selectedIncident) {
      alert("Please select an incident first");
      return;
    }

    await fetch(`${BACKEND_URL}/api/rca/${selectedIncident}`);

    const response = await fetch(
      `${BACKEND_URL}/api/guardrails/incident/${selectedIncident}`
    );

    const data = await response.json();
    setGuardrailData(data.guardrail_result);
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
    .slice(0, 8);

  const p0Count = incidents.filter((i) => i.severity === "P0").length;
  const p1Count = incidents.filter((i) => i.severity === "P1").length;
  const openCount = incidents.filter((i) => i.status === "open").length;

  return (
    <div className="app">
      <header className="topbar">
        <div className="logo-block">
          <div className="logo">AI</div>
          <div>
            <h2>AIOps Command Center</h2>
            <p>Root Cause Analysis Platform</p>
          </div>
        </div>

        <nav className="topnav">
          <a href="#dashboard">Dashboard</a>
          <a href="#incidents">Incidents</a>
          <a href="#metrics">Metrics</a>
          <a href="#reports">Reports</a>
          <a href="#guardrails">Guardrails</a>
        </nav>

        <div className="online-pill">
          <span></span>
          System Online
        </div>
      </header>

      <main className="container" id="dashboard">
        <section className="hero">
          <div>
            <p className="eyebrow">AI-powered incident operations</p>
            <h1>
              Monitor failures, detect incidents, and generate RCA with local AI.
            </h1>
            <p className="hero-text">
              A portfolio-ready AIOps platform that simulates production failures,
              creates incidents, correlates patterns, and validates AI recommendations.
            </p>

            <div className="hero-actions">
              <button className="btn primary" onClick={refreshDashboard}>
                Refresh Dashboard
              </button>
              <button
                className="btn danger"
                onClick={() => injectFailure("payment_gateway_failure")}
              >
                Inject P0 Failure
              </button>
              <button
                className="btn warning"
                onClick={() => injectFailure("redis_timeout")}
              >
                Inject Redis Timeout
              </button>
              <button
                className="btn neutral"
                onClick={() => injectFailure("db_pool_exhausted")}
              >
                Inject DB Issue
              </button>
            </div>
          </div>

          <div className="hero-card">
            <div className="ai-orb">
              <span></span>
              <span></span>
              <span></span>
              <span></span> 
              <strong>AI</strong>
            </div>

          <p>AI RCA Status</p>
          <h3>Ready</h3>
          <span>Ollama + RCA engine enabled</span>
          </div>
        </section>

        <section className="kpi-grid">
          <div className="kpi-card">
            <p>Total Incidents</p>
            <h2>{incidents.length}</h2>
            <span>{openCount} open incidents</span>
          </div>

          <div className="kpi-card">
            <p>Critical / High</p>
            <h2>{p0Count + p1Count}</h2>
            <span>{p0Count} P0, {p1Count} P1</span>
          </div>

          <div className="kpi-card">
            <p>Metrics Generated</p>
            <h2>{metrics.length}</h2>
            <span>Latest service telemetry</span>
          </div>

          <div className="kpi-card">
            <p>Services</p>
            <h2>3</h2>
            <span>Payment, order, inventory</span>
          </div>
        </section>

        <section className="toolbar">
          <select
            value={severityFilter}
            onChange={(e) => setSeverityFilter(e.target.value)}
          >
            <option value="all">All Severities</option>
            <option value="P0">P0 Critical</option>
            <option value="P1">P1 High</option>
            <option value="P2">P2 Medium</option>
            <option value="P3">P3 Low</option>
          </select>

          <select
            value={serviceFilter}
            onChange={(e) => setServiceFilter(e.target.value)}
          >
            <option value="all">All Services</option>
            <option value="payment-service">payment-service</option>
            <option value="order-service">order-service</option>
            <option value="inventory-service">inventory-service</option>
          </select>
        </section>

        <section className="panel" id="incidents">
          <div className="panel-header">
            <div>
              <h2>Latest Incidents</h2>
              <p>Click any incident to view correlated incidents.</p>
            </div>
            <span>{filteredIncidents.length} shown</span>
          </div>

          <div className="incident-table">
            <div className="table-head">
              <span>Service</span>
              <span>Severity</span>
              <span>Incident</span>
              <span>Status</span>
            </div>

            {filteredIncidents.length === 0 ? (
              <div className="empty-state">
                <h3>No incidents yet</h3>
                <p>Inject a failure to see the incident workflow.</p>
              </div>
            ) : (
              filteredIncidents.map((incident) => (
                <div
                  key={incident.id}
                  className={`table-row ${
                    selectedIncident === incident.id ? "active-row" : ""
                  }`}
                  onClick={() => fetchCorrelation(incident.id)}
                >
                  <span>{incident.service}</span>
                  <span className={`badge ${incident.severity.toLowerCase()}`}>
                    {incident.severity}
                  </span>
                  <span>{incident.title}</span>
                  <span className="status">{incident.status}</span>
                </div>
              ))
            )}
          </div>
        </section>

        <section className="panel" id="metrics">
          <div className="panel-header">
            <div>
              <h2>Latest Metrics</h2>
              <p>Generated telemetry from simulated services.</p>
            </div>
          </div>

          <div className="metrics-grid">
            {metrics.map((metric) => (
              <div className="metric-card" key={metric.id}>
                <div>
                  <h3>{metric.service}</h3>
                  <p>{metric.scenario || "normal"}</p>
                </div>

                <div className="metric-values">
                  <span>{metric.latency_ms} ms</span>
                  <span>{metric.error_rate}% errors</span>
                  <span>{metric.cpu_usage}% CPU</span>
                </div>
              </div>
            ))}
          </div>
        </section>

        {correlationData && (
          <section className="panel" id="correlations">
            <div className="panel-header">
              <div>
                <h2>Correlated Incidents</h2>
                <p>Selected Incident ID: {selectedIncident}</p>
              </div>
              <span>{correlationData.related_incidents_count} related</span>
            </div>

            <div className="incident-table">
              <div className="table-head">
                <span>Service</span>
                <span>Score</span>
                <span>Incident</span>
                <span>Reason</span>
              </div>

              {correlationData.related_incidents?.map((item) => (
                <div className="table-row" key={item.incident_id}>
                  <span>{item.service}</span>
                  <span className="score">{item.correlation_score}%</span>
                  <span>{item.title}</span>
                  <span>{item.reasons?.join(", ")}</span>
                </div>
              ))}
            </div>
          </section>
        )}

        <section className="feature-grid">
          <div className="feature-card" id="reports">
            <h2>Reports</h2>
            <p>Generate a full incident report for the selected incident.</p>

            <button className="btn primary" onClick={generateReport}>
              Generate Report
            </button>

            {reportData && (
              <div className="result-box">
                <strong>{reportData.severity} incident in {reportData.service}</strong>
                <span>{reportData.summary}</span>
                <span>Root Cause: {reportData.rca.root_cause}</span>
                <span>Recommendation: {reportData.rca.recommendation}</span>
              </div>
            )}
          </div>

          <div className="feature-card" id="guardrails">
            <h2>Guardrails</h2>
            <p>Check whether the AI RCA output is grounded in incident context.</p>

            <button className="btn neutral" onClick={checkGuardrails}>
              Check Guardrails
            </button>

            {guardrailData && (
              <div className="result-box">
                <strong>Status: {guardrailData.guardrail_status}</strong>
                <span>{guardrailData.message}</span>
              </div>
            )}
          </div>
        </section>
      </main>
    </div>
  );
}

export default App;