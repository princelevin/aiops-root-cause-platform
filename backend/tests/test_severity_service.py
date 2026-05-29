from app.services.severity_service import calculate_severity


def test_payment_gateway_failure_is_p0():
    assert calculate_severity("payment_gateway_failure", 720) == "P0"


def test_redis_timeout_is_p1():
    assert calculate_severity("redis_timeout", 950) == "P1"


def test_high_latency_is_p1():
    assert calculate_severity("unknown", 950) == "P1"


def test_medium_latency_is_p2():
    assert calculate_severity("unknown", 750) == "P2"


def test_low_latency_is_p3():
    assert calculate_severity("unknown", 300) == "P3"