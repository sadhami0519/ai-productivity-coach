from google.cloud import dialogflow_v2
import os

class DialogflowManager:
    def __init__(self):
        self.project_id = os.getenv("DIALOGFLOW_PROJECT_ID")
        self.session_client = dialogflow_v2.SessionsClient()
        
    def detect_intent(self, session_id: str, text: str, language_code: str = "en"):
        session = self.session_client.session_path(self.project_id, session_id)
        text_input = dialogflow_v2.TextInput(text=text, language_code=language_code)
        query_input = dialogflow_v2.QueryInput(text=text_input)
        
        response = self.session_client.detect_intent(
            request={"session": session, "query_input": query_input}
        )
        
        return {
            "fulfillment_text": response.query_result.fulfillment_text,
            "intent": response.query_result.intent.display_name,
            "confidence": response.query_result.intent_detection_confidence
        }