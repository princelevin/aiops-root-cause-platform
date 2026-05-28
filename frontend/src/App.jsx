import { useEffect, useState } from "react";
import "./App.css";

const API_BASE_URL = "http://127.0.0.1:8000";

function App() {
  const [services, setServices] = useState([]);
  const [incidents, setIncidents] = useState([]);
  const [metrics, setMetrics] = useState([]);
  const [loading, setLoading] = useState(true);

  async function fetchDashboardData() {
    try {
      const [servicesRes, incidentsRes, metricsRes] = await Promise.all([
        fetch(`${API_BASE_URL}/api/services`),
        fetch(`${API_BASE_URL}/api/incidents`),
        fetch(`${API_BASE_URL}/api/metrics/latest`),
      ]);

      const servicesData = await servicesRes.json();
      const incidentsData = await incidentsRes.json();
      const metricsData = await metricsRes.json();

      setServices(servicesData.services || []);
      setIncidents(incidentsData.incidents || []);
      setMetrics(metricsData.metrics || []);
    } catch (error) {
      console.error("Failed to fetch dashboard data", error);
    } finally {
      setLoading(false);
    }
  }

  async function generateMetrics() {
    await fetch(`${API_BASE_URL}/api/metrics/generate?count=10`, {
      method: "POST",
    });
    await fetchDashboardData();
  }

  async function detectAnomalies() {
    await fetch(`${API_BASE_URL}/api/anomalies/detect`, {
      method: "POST",
    });
    await fetchDashboardData();
  }

  async function injectFailure(type) {
    await fetch(`${API_BASE_URL}/api/failures/inject/${type}`, {
      method: "POST",
    });
    await fetchDashboardData();
  }

  useEffect(() => {
    fetchDashboardData();
  }, []);

  return (
    <div className="app">
      <aside className="sidebar">
        <h2>AIOps</h2>
        <p>Root Cause Platform</p>
      </aside>

      <main className="main">
        <header className="header">
          <div>
            <h1>AI Ops Root Cause Platform</h1>
            <p>Distributed AI incident detection and root cause analysis dashboard</p>
          </div>
          <span className="status-pill">System Online</span>
        </header>

        <section className="actions">
          <button onClick={generateMetrics}>Generate Metrics</button>
          <button onClick={detectAnomalies}>Detect Anomalies</button>
          <button onClick={() => injectFailure("redis_timeout")}>
            Inject Redis Timeout
          </button>
          <button onClick={() => injectFailure("payment_gateway_failure")}>
            Inject Payment Failure
          </button>
        </section>

        {loading ? (
          <p>Loading dashboard...</p>
        ) : (
          <>
            <section className="cards">
              <div className="card">
                <h3>Total Services</h3>
                <p>{services.length}</p>
              </div>

              <div className="card">
                <h3>Open Incidents</h3>
                <p>{incidents.length}</p>
              </div>

              <div className="card">
                <h3>Latest Metrics</h3>
                <p>{metrics.length}</p>
              </div>

              <div className="card">
                <h3>AI RCA Status</h3>
                <p>Ready</p>
              </div>
            </section>

            <section className="section">
              <h2>Monitored Services</h2>
              <div className="table">
                {services.map((service) => (
                  <div className="row" key={service.name}>
                    <span>{service.name}</span>
                    <span className="healthy">{service.status}</span>
                    <span>{service.latency || "N/A"}</span>
                    <span>active</span>
                  </div>
                ))}
              </div>
            </section>

            <section className="section">
              <h2>Latest Service Metrics</h2>
              <div className="table">
                {metrics.map((metric) => (
                  <div className="row" key={metric.id}>
                    <span>{metric.service}</span>
                    <span>{metric.latency_ms} ms</span>
                    <span>{metric.error_rate}% errors</span>
                    <span>{metric.cpu_usage}% CPU</span>
                  </div>
                ))}
              </div>
            </section>

            <section className="section">
              <h2>Recent Incidents</h2>
              <div className="table">
                {incidents.length === 0 ? (
                  <p>No incidents detected yet.</p>
                ) : (
                  incidents.map((incident) => (
                    <div className="row" key={incident.id}>
                      <span>{incident.title}</span>
                      <span>{incident.service}</span>
                      <span className="severity">{incident.severity}</span>
                      <span>{incident.status}</span>
                    </div>
                  ))
                )}
              </div>
            </section>
          </>
        )}
      </main>
    </div>
  );
}

export default App;