# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
import requests
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionAskCity(Action):

    def name(self) -> Text:
        return "action_ask_city"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        url='https://auth.feedni.net/settings?type=Cities&app=seekers'
        json_data=requests.get(url).json()
        length=len(json_data['data']['options'])
        ask_city= "Where would you like to have it ?"
        total=""
        for city in range(1,length):
            cities_list= str(city) + ". "+json_data['data']['options'][city]['name']+ "\n"
            total+=cities_list
        dispatcher.utter_message(text=ask_city)
        total=str(total)
        dispatcher.utter_message(text=total)
        return []
