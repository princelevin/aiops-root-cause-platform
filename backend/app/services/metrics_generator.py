from datetime import datetime
import random

metrics = []
metric_id_counter = 1

SERVICES = ["payment-service", "order-service", "inventory-service"]


SCENARIOS = {
    "normal": {
        "latency_range": (80, 300),
        "error_rate_range": (0.0, 3.0),
        "cpu_range": (20.0, 55.0),
        "memory_range": (30.0, 60.0),
    },
    "cpu_spike": {
        "latency_range": (400, 900),
        "error_rate_range": (3.0, 8.0),
        "cpu_range": (85.0, 98.0),
        "memory_range": (45.0, 70.0),
    },
    "memory_leak": {
        "latency_range": (300, 850),
        "error_rate_range": (2.0, 7.0),
        "cpu_range": (40.0, 75.0),
        "memory_range": (82.0, 98.0),
    },
    "error_burst": {
        "latency_range": (300, 900),
        "error_rate_range": (12.0, 25.0),
        "cpu_range": (50.0, 80.0),
        "memory_range": (45.0, 75.0),
    },
    "latency_degradation": {
        "latency_range": (950, 1400),
        "error_rate_range": (4.0, 10.0),
        "cpu_range": (45.0, 75.0),
        "memory_range": (45.0, 75.0),
    },
}


def generate_metric(scenario: str = "normal"):
    global metric_id_counter

    if scenario not in SCENARIOS:
        scenario = "normal"

    config = SCENARIOS[scenario]
    service = random.choice(SERVICES)

    metric = {
        "id": metric_id_counter,
        "service": service,
        "scenario": scenario,
        "latency_ms": random.randint(*config["latency_range"]),
        "error_rate": round(random.uniform(*config["error_rate_range"]), 2),
        "request_count": random.randint(100, 5000),
        "cpu_usage": round(random.uniform(*config["cpu_range"]), 2),
        "memory_usage": round(random.uniform(*config["memory_range"]), 2),
        "timestamp": datetime.utcnow().isoformat(),
    }

    metrics.append(metric)
    metric_id_counter += 1

    return metric


def generate_metrics(count: int = 10, scenario: str = "normal"):
    return [generate_metric(scenario) for _ in range(count)]


def get_metrics():
    return metrics[-100:]


def get_latest_service_metrics():
    latest = {}

    for metric in metrics:
        latest[metric["service"]] = metric

    return list(latest.values())


def get_metric_scenarios():
    return list(SCENARIOS.keys())