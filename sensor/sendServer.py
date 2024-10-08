import requests
from datetime import datetime

def send_post_request(temperature, humidity):
    url = "http://monokanri-manage.local/api/respi"
    
    params = {
        #1:電気炉 2:生型造型 3:フラン 4:中子 5:仕上げ 6:出荷検査 7:工場外
        'process_id': 3,
        'temperature': temperature,
        'humidity': humidity,
        'created_at': datetime.now().isoformat()
    }
    response = requests.get(url, params=params)

    return response
