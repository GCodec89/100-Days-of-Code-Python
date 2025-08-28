import requests


parameters = {
    "amount": 10,
    "type": "boolean",
}
response_trivia = requests.get("https://opentdb.com/api.php", params=parameters)
response_trivia.raise_for_status()
data_trivia = response_trivia.json()
question_data = data_trivia["results"]
