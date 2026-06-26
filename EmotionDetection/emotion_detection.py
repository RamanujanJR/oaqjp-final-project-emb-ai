import requests
import json

def emotion_detector(text_to_analyse):
    # URL và Headers của API Watson NLP
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Định dạng dữ liệu gửi đi
    input_json = { "raw_document": { "text": text_to_analyse } }

    # Gửi yêu cầu POST đến API
    response = requests.post(url, json=input_json, headers=headers)

    # Chuyển đổi chuỗi JSON phản hồi thành Python Dictionary
    formatted_response = json.loads(response.text)

    # Trích xuất các giá trị cảm xúc từ cấu trúc lồng nhau của API
    # Cấu trúc gốc: formatted_response['emotionPredictions'][0]['emotion']
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']

    # Tìm cảm xúc có điểm số cao nhất (Cảm xúc chủ đạo)
    dominant_emotion = max(emotions, key=emotions.get)

    # Trả về kết quả theo đúng định dạng yêu cầu của hệ thống chấm điểm
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }