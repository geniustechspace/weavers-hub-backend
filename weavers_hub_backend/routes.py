from fastapi import APIRouter, HTTPException, status
from firebase_admin import messaging
from firebase_admin.exceptions import FirebaseError

from .schemas import NotificationPayload

router = APIRouter()


@router.post("/send-notification/")
async def send_notification(payload: NotificationPayload):
    """
    Send a notification to a device using Firebase Cloud Messaging (FCM).

    Args:
        payload (NotificationPayload): The payload containing token, title, and body.

    Returns:
        dict: A response message indicating success or failure.
    """
    message = messaging.Message(
        notification=messaging.Notification(
            title=payload.title,
            body=payload.body,
        ),
        token=payload.token,
    )

    try:
        # Send a message to the device corresponding to the provided token
        response: str = messaging.send(message)
        return {"message": "Notification sent successfully", "id": response}
    except ValueError as ve:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=f"Value error: {ve}"
        )
    except FirebaseError as fe:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Failed to send notification: {fe}",
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Unknown error: {e}",
        )
