import "./App.css";

function App() {
  const services = [
    { name: "payment-service", status: "healthy", latency: "120ms" },
    { name: "order-service", status: "healthy", latency: "95ms" },
    { name: "inventory-service", status: "healthy", latency: "140ms" },
  ];

  const incidents = [
    {
      id: 1,
      service: "payment-service",
      severity: "P1",
      title: "High latency detected",
      status: "open",
    },
  ];

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

        <section className="cards">
          <div className="card">
            <h3>Total Services</h3>
            <p>3</p>
          </div>

          <div className="card">
            <h3>Open Incidents</h3>
            <p>1</p>
          </div>

          <div className="card">
            <h3>Critical Alerts</h3>
            <p>0</p>
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
                <span>{service.latency}</span>
              </div>
            ))}
          </div>
        </section>

        <section className="section">
          <h2>Recent Incidents</h2>
          <div className="table">
            {incidents.map((incident) => (
              <div className="row" key={incident.id}>
                <span>{incident.title}</span>
                <span>{incident.service}</span>
                <span className="severity">{incident.severity}</span>
                <span>{incident.status}</span>
              </div>
            ))}
          </div>
        </section>
      </main>
    </div>
  );
}

export default App;