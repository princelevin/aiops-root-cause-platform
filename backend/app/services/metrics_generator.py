from datetime import datetime
import random

metrics = []
metric_id_counter = 1

SERVICES = ["payment-service", "order-service", "inventory-service"]


def generate_metric():
    global metric_id_counter

    service = random.choice(SERVICES)

    metric = {
        "id": metric_id_counter,
        "service": service,
        "latency_ms": random.randint(50, 1200),
        "error_rate": round(random.uniform(0.0, 15.0), 2),
        "request_count": random.randint(100, 5000),
        "cpu_usage": round(random.uniform(10.0, 95.0), 2),
        "memory_usage": round(random.uniform(20.0, 90.0), 2),
        "timestamp": datetime.utcnow().isoformat(),
    }

    metrics.append(metric)
    metric_id_counter += 1

    return metric


def generate_metrics(count: int = 10):
    return [generate_metric() for _ in range(count)]


def get_metrics():
    return metrics[-100:]


def get_latest_service_metrics():
    latest = {}

    for metric in metrics:
        latest[metric["service"]] = metric

    return list(latest.values())