from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import UserUtteranceReverted
# New Imported
from rasa_sdk.events import SlotSet


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
            response = ("If you wish to know more about our available programs you "
                        "may visit the school for more a knowledge")
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


# User Asks School Program list.
class ActionProvideProgramInfo(Action):
    def name(self) -> Text:
        return "action_provide_program_list"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_list_program")

        return []


class ActionSetProgramOption(Action):
    def name(self) -> Text:
        return "action_set_program_option"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        intent_name = tracker.latest_message["intent"].get("name")
        program_option = intent_name.split("_")[-1]

        return [SlotSet("program_option", program_option)]


# I'm not sure about this code sasabog na utak ko kaka trial and error - YOS

# class ActionUtterDetailsProgram(Action):
#     def name(self) -> Text:
#         return "action_utter_details_program"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         program_option = tracker.get_slot("program_option")
#
#         if program_option in ["1", "2", "3", "4", "5", "6"]:
#             # Use the program_option to determine which program details to provide
#             template_name = f"utter_details_program{program_option}"
#             dispatcher.utter_message(template=template_name)
#         else:
#             dispatcher.utter_message(template="utter_invalid_option")
#
#         return []

# class ActionUtterDetailsProgram(Action):
#     def name(self) -> Text:
#         return "action_utter_details_program"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         program_option = tracker.get_slot("program_option")
#
#         if program_option == "1":
#             dispatcher.utter_message(template="utter_details_program1")
#         elif program_option == "2":
#             dispatcher.utter_message(template="utter_details_program2")
#         elif program_option == "3":
#             dispatcher.utter_message(template="utter_details_program3")
#         elif program_option == "4":
#             dispatcher.utter_message(template="utter_details_program4")
#         elif program_option == "5":
#             dispatcher.utter_message(template="utter_details_program5")
#         elif program_option == "6":
#             dispatcher.utter_message(template="utter_details_program6")
#
#         return []


# Action Default fallback

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
