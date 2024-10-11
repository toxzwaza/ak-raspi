import requests
from datetime import datetime, timedelta

def send_post_request(temperature, humidity, process_id):
    url = "http://monokanri-manage.local/api/respi"
    
    created_at = (datetime.now() + timedelta(hours=1)).replace(minute=0, second=0).isoformat()
    if created_at in '24:00:00':
        created_at = (datetime.now() + timedelta(days=1)).replace(hour=0, minute=0, second=0).isoformat()
    params = {
        #1:電気炉 2:生型造型 3:フラン 4:中子 5:仕上げ 6:出荷検査 7:工場外
        'process_id': process_id,
        'temperature': temperature,
        'humidity': humidity,
        'created_at': created_at
    }
    response = requests.get(url, json=params)

    return response
