from fastapi import APIRouter, HTTPException
from ..utils.dialogflow import DialogflowManager
from ..utils.quotes import get_random_quote

router = APIRouter()
dialogflow = DialogflowManager()

@router.post("/chat/{session_id}")
async def chat(session_id: str, message: str):
    try:
        response = dialogflow.detect_intent(session_id, message)
        
        # Handle different intents
        if response["intent"] == "request_quote":
            quote = get_random_quote()
            return {"message": quote}
        elif response["intent"] == "study_tips":
            return {"message": response["fulfillment_text"]}
        else:
            return {"message": response["fulfillment_text"]}
            
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))