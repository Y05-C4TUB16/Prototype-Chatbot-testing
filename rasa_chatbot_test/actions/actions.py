from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import UserUtteranceReverted, ConversationPaused
from rasa_sdk.events import SlotSet


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


# class ActionDefaultFallback(Action):
#
#     def name(self) -> Text:
#         return "action_default_fallback"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         dispatcher.utter_message(response="utter_default")
#
#         return [UserUtteranceReverted()]


# Action Human Handoff
# ---STILL UNDER PROGRESS---
class ActionAskHandoff(Action):
    def name(self) -> Text:
        return "action_ask_handoff"

    def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        # ask the user if they want to be transferred to a human
        dispatcher.utter_message(response="utter_ask_handoff")
        dispatcher.utter_message(response="utter_ask_handoff2")

        return [UserUtteranceReverted()]


class ActionHumanHandoff(Action):
    def name(self) -> Text:
        return "action_handoff_to_human"

    def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        # check if the user wants to transfer to a human
        intent = tracker.latest_message.get('text')

        if intent == "affirm":
            dispatcher.utter_message(text="I am passing you to a human...")
            # take note, it's much better if customized sya based on our limitations on paper and
            # --may option to chat with the chatbot again

            # pause conversation
            return [ConversationPaused()]
        elif intent == "deny":
            # continue conversation
            dispatcher.utter_message(text="Alright, let's continue.")
            return []


class ActionEnrollmentInfo(Action):
    def name(self) -> Text:
        return "action_enrollment_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_old_new")
        return []


class ActionOldOrNew(Action):
    def name(self) -> Text:
        return "action_old_or_new"

    def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        intent = tracker.latest_message.get('intent').get('name')
        if intent == "new_student":
            dispatcher.utter_message(response="utter_educ_level")
            return [SlotSet("student_status", "new_student")]
        elif intent == "old_student":
            dispatcher.utter_message(response="utter_educ_level")
            return [SlotSet("student_status", "old_student")]


class ActionEnrollmentInfoResponse(Action):
    def name(self) -> Text:
        return "action_enrollment_info_response"

    def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        student_status = tracker.get_slot("student_status")
        intent = tracker.latest_message.get('intent').get('name')

        if student_status == "old_student":
            if intent == "grade_level_eed":
                dispatcher.utter_message(response="utter_old_eed")
            elif intent == "grade_level_gs_and_junior":
                dispatcher.utter_message(response="utter_old_gs_and_jhs")
            elif intent == "grade_level_senior":
                dispatcher.utter_message(response="utter_old_shs")
        elif student_status == "new_student":
            if intent == "grade_level_eed":
                dispatcher.utter_message(response="utter_new_eed")
            elif intent == "grade_level_gs_and_junior":
                dispatcher.utter_message(response="utter_new_gs_and_jhs")
            elif intent == "grade_level_senior":
                dispatcher.utter_message(response="utter_new_shs")

        return []


class ActionGradesInfo(Action):
    def name(self) -> Text:
        return "action_grades_info"

    def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        grade = tracker.get_slot('grade_inquiry')
        dispatcher.utter_message(response="utter_grades_info")
        dispatcher.utter_message(response="utter_grades_info2")
        return [SlotSet("grade_inquiry", grade)]


class ActionFinancialInfo(Action):
    def name(self) -> Text:
        return "action_financial_info"

    def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        finance = tracker.get_slot('financial_inquiry')
        dispatcher.utter_message(response="utter_financial_info")
        dispatcher.utter_message(response="utter_financial_info2")
        return [SlotSet("financial_inquiry", finance)]


class ActionAppointmentInfo(Action):
    def name(self) -> Text:
        return "action_appointment_info"

    def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        app = tracker.get_slot('appointment_inquiry')
        dispatcher.utter_message(response="utter_appointment_info")
        dispatcher.utter_message(response="utter_appointment_info2")
        return [SlotSet("appointment_inquiry", app)]

#Feedback section
class ActionHandleFeedback(Action):

    def name(self) -> str:
        return "action_handle_feedback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker,
            domain) -> list:
        stars = tracker.get_slot("stars")

        return []
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
