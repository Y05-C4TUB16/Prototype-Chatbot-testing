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


class ActionAskStrand(Action):

    def name(self) -> Text:
        return "action_ask_strand"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # strand = tracker.latest_message['text']
        # ask_strand = self.ask_strand(strand)

        strand_slot = next(tracker.get_latest_entity_values("strand"), None)
        strand = tracker.get_slot("strand") or strand_slot

        if strand:
            response = ("If you wish to know more about our available programs you may visit the school "
                        "for more a knowledge")
        else:
            response = "Sorry, I could not provide any info regarding your question."

        dispatcher.utter_message(text=response)

        return []
