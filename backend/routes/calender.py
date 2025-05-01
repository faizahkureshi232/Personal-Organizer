from fastapi import APIRouter, Body

from backend.service.calendar_service import fetch_calendar_events, create_event

router = APIRouter()

@router.get("/events")
def get_events():
    events = fetch_calendar_events()
    return {"events": events}

@router.post("/calendar")
def post_event(event: dict = Body(...)):
    event_id = create_event(event)
    return {"event_id": event_id}
router = APIRouter()

@router.post("/calendar")
def create_event(event: dict = Body(...)):
    event_id = calendar_service.create_event(event)
    return {"event_id": event_id}