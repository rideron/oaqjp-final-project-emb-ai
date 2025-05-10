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

    if response.status_code == 200:
        formatted_response = json.loads(response.text)
        emotion = formatted_response['emotionPredictions'][0]['emotion']
        dominant = max(emotion,key=emotion.get)
    elif response.status_code == 400:
        emotion={
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
        }
        dominant=None

    return {
        'anger': emotion['anger'],
        'disgust': emotion['disgust'],
        'fear': emotion['fear'],
        'joy': emotion['joy'],
        'sadness': emotion['sadness'],
        'dominant_emotion': dominant
    }
