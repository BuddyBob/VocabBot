
import requests
import json
def getSyns(word):
    url = "https://synonyms-word-info.p.rapidapi.com/v1/word"

    querystring = {"str":word}

    headers = {
        'x-rapidapi-key': "be5613ee63mshee2af9c5d65ea5fp151699jsnc5b6aa9d7c78",
        'x-rapidapi-host': "synonyms-word-info.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    response = response.text
    y = json.loads(response)
    return ["data"]["list"]