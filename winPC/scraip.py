import requests
from bs4 import BeautifulSoup
from sendServer import send_post_request

def scrape_weather():
    url = "https://s.n-kishou.co.jp/w/charge/jikei/jikeih.html?&ba=33&code=33202&lat=34.5850172&lon=133.7722833"
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        today_div = soup.find(id="sct-day01")
        second_tr = today_div.find_all('tr')[1]
        temperature = second_tr.find_all('td')[0].text.replace('℃','')
        humidity = second_tr.find_all('td')[1].text.replace('%','')
        
        if temperature and humidity:
            process_id = 7
            response = send_post_request(temperature, humidity, process_id)
            if response.status_code == 200:
                print('success:成功しました')
            else:
                print('error:失敗しました')
                pass
            
        
        
    else:
        print("リクエストが失敗しました")

scrape_weather()
