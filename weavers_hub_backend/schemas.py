from pydantic import BaseModel


# Pydantic model for the request body
class NotificationPayload(BaseModel):
    token: str
    title: str
    body: str
