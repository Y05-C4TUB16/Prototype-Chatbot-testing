from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import UserUtteranceReverted


# class ActionAskScholarship(Action):

#     def name(self) -> Text:
#         return "action_ask_scholarship"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         # scholarship = tracker.latest_message['text']
#         # ask_scholarship = self.ask_renew_scholarship(scholarship)

#         scholarship_slot = next(tracker.get_latest_entity_values("scholarship"), None)
#         scholarship = tracker.get_slot("scholarship") or scholarship_slot

#         if scholarship:
#             response = "You may renew your scholarship in the registrars office upon enrollment."
#         else:
#             response = "Sorry I could not provide any info regarding your scholarship renewal."

#         dispatcher.utter_message(text=response)

#         return []


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
            response = ("If you wish to know more about our available programs you may visit the school for more a knowledge")
        else:
            response = "Sorry, I could not provide any info regarding your question."

        dispatcher.utter_message(text=response)

        return []
    
    
# Profanity
class ActionHandleSwearing(Action):
    def name(self) -> Text:
        return "action_handle_swearing"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        last_intent = tracker.latest_message['intent'].get('name')
        
        if last_intent == 'swear':
            dispatcher.utter_message(template="utter_warn_profanity")
        
        return []
    
# User Asks for the Programs in the school.
class ActionProvideProgramInformation(Action):
    def name(self) -> Text:
        return "action_provide_program_information"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Programs information to be displayed to the user
        program_info = ("The school offers a diverse range of programs to cater to different interests and needs:"
                        "\n1. Discovery and Play\n2. Senior High school\n3. Advanced Sciences\n4. IT Programs"
                        "\n5. Sports Excellence\n6. Inclusive Program\n"
                        "\nFor more information please visit our website: https://hedcen.education/?")

# Send the program information to the user
        dispatcher.utter_message(text=program_info)

        return []


class ActionDefaultFallback(Action):

    def name(self) -> Text:
        return "action_default_fallback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(response="utter_default")

        return [UserUtteranceReverted()]

# class ActionTwoStageFallback(Action):
# 
#     def name(self) -> Text:
#         return "action_two_stage_fallback"
# 
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
# 
#         dispatcher.utter_message(response="utter_default")
# 
#         return [UserUtteranceReverted()]


# This can be used when the user is given options:
# class ActionArrayString(Action): 
#     def name(self) -> Text:
#         return "action_array_string"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#       'entity' = next(tracker.get_latest_entity_values("'entity'"), None)
#
#       if 'entity' = "'string'":
#           'intent' = ["sample", "sample", "sample"]
#       elif 'entity' = "'string'":
#           'intent' = ["sample", "sample", "sample"]
#       elif 'entity' = "'string'":
#           'intent' = ["sample", "sample", "sample"]
#       else:
#           'intent' = []
#
#       if 'intent':
#           response = f"blablabla  {'entity'} blablablabla" + "." .join('intent')
#       else:
#           response = "sorry boi"
#
#       dispatcher.utter_message(text=response)
#
#       return []
