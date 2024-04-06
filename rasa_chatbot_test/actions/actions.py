from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionAskScholarship(Action):

    def name(self) -> Text:
        return "action_ask_scholarship"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # scholarship = tracker.latest_message['text']
        # ask_scholarship = self.ask_renew_scholarship(scholarship)

        scholarship_slot = next(tracker.get_latest_entity_values("scholarship"), None)
        scholarship = tracker.get_slot("scholarship") or scholarship_slot

        if scholarship:
            response = "You may renew your scholarship in the registrars office upon enrollment."
        else:
            response = "Sorry I could not provide any info regarding your scholarship renewal."

        dispatcher.utter_message(text=response)

        return []
