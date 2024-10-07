import requests
from datetime import datetime

def send_post_request(temperature, humidity):
    url = "http://monokanri-manage.local/api/respi"
    
    data = {
        #1:電気炉 2:生型造型 3:フラン 4:中子 5:仕上げ 6:出荷検査
        'process_id': 1,
        'temp': temperature,
        'humi': humidity,
        'created_at': datetime.now().isoformat()
    }
    response = requests.post(url, data=data)
    return response
