''' AI Emotional Detection Module '''
import json
import requests

HOST='https://sn-watson-emotion.labs.skills.network'

def emotion_detector(text_to_analyse):
    ''' Request to Watson NLP Library '''
    url = HOST+'/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header =  {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header, timeout=5)

    formatted_response = json.loads(response.text)

    return formatted_response
