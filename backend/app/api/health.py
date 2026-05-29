from fastapi import APIRouter


# Simple API to check if backend is running
router = APIRouter()


@router.get("/health")
def health_check():
    """
    Check backend health.
    """

    return {
        "status": "ok",
        "service": "aiops-root-cause-platform",
    }