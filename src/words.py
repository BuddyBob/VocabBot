
import requests
import json
def getSyns(word):
    synonyms = []

    url = "https://synonyms-word-info.p.rapidapi.com/v1/word"

    querystring = {"str":word}

    headers = {
        'x-rapidapi-key': "be5613ee63mshee2af9c5d65ea5fp151699jsnc5b6aa9d7c78",
        'x-rapidapi-host': "synonyms-word-info.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    response = response.text
    y = json.loads(response)
    for i in y["data"]["list"]:
        synonyms.append(i)
    try:
        for x in synonyms[:int(len(synonyms)/1.5)]:
            url = "https://synonyms-word-info.p.rapidapi.com/v1/word"

            querystring = {"str":word}

            headers = {
                'x-rapidapi-key': "be5613ee63mshee2af9c5d65ea5fp151699jsnc5b6aa9d7c78",
                'x-rapidapi-host': "synonyms-word-info.p.rapidapi.com"
                }

            response = requests.request("GET", url, headers=headers, params=querystring)
            response = response.text
            y = json.loads(response)
            for i in y["data"]["list"]:
                synonyms.append(i)
    except Exception as e:
        print(e)

    return synonyms


def getDef(word):

    url = "https://wordsapiv1.p.rapidapi.com/words/"+str(word)

    headers = {
        'x-rapidapi-key': "be5613ee63mshee2af9c5d65ea5fp151699jsnc5b6aa9d7c78",
        'x-rapidapi-host': "wordsapiv1.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers)

    response = response.text
    y = json.loads(response)
    defs = [item['definition'] for item in y['results']]
    defs = [x.split(' ') for x in defs]
    newDefs = [defY for defX in defs for defY in defX]
    def strip(newDefs):
        newDefsX = []
        for defA in newDefs:
            if defA[0] == '(':
                defA = defA[1:]
            if defA[-1] in [')',';']:
                defA = defA[:-1]
            newDefsX.append(defA)
        return newDefsX
    newDefs = strip(newDefs)
    return newDefs


            

    
    
    # print(y["results"][0]["definition"])
getDef('box')