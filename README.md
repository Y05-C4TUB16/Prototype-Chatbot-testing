# Prototype-Chatbot-testing
Thesis Prototype chatbot for testing and evaluating user interaction and engagement. The chatbot prototype is designed to simulate various scenarios and user queries to gather insights into user behavior, preferences, and potential challenges in natural language processing. 


## TO KNOW:

_note: these are done in the terminal, so create a terminal whenever you want to execute this._

- When you want to create a chatbot, type:
```
rasa init
```
then click enter when asked which directory.then Y, then N.

- When you want train the bot, type:
```
rasa train
```
_note: do this whenever you perform changes within the code._

- When you want to test the chatbot, type:
```
rasa shell
```

- When you want to test the chatbot w/ actions, in another terminal type:
```
rasa run actions
```

***We will embedd the system in Facebook Messenger***
- If you want the chatbot to run on Messenger, type in the terminal:
```
rasa run
```


***The only Files you need***

- nlu.yml
- domain.yml
- rules.yml
- stories.yml
- action.py

