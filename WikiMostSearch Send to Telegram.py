import requests
import schedule
import time
import datetime
import urllib3
import jdatetime
import urllib.parse


# INSERT YOUR TOKEN AND CHANNEL ID BELOW
TELEGRAM_TOKEN = 'Bot Token'
TELEGRAM_CHANNEL = 'Telegram ID of Channel You Want to Send Data'


headers = {
    "Authority": "wikimedia.org",
    "Method": "GET",
    "Path": "/api/rest_v1/metrics/pageviews/top/fa.wikipedia.org/all-access/2023/08/19",
    "Scheme": "https",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Cache-Control": "max-age=0",
    "Cookie": "GeoIP=FI:18:Helsinki:60.18:24.93:v4; WMF-Last-Access=20-Aug-2023; WMF-Last-Access-Global=20-Aug-2023; NetworkProbeLimit=0.001",
    "Sec-Ch-Ua": "\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"Google Chrome\";v=\"114\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

def dateMaker(firstday):

    yesterday = datetime.date.today() - datetime.timedelta(days=firstday)
    one_before_yesterday = datetime.date.today() - datetime.timedelta(days=(firstday+1))
    
    yester_year = yesterday.strftime("%Y")
    yester_month = yesterday.strftime("%m")
    yester_day = yesterday.strftime("%d")

    one_before_year = one_before_yesterday.strftime("%Y")
    one_before_month = one_before_yesterday.strftime("%m")
    one_before_day = one_before_yesterday.strftime("%d")
        
    return yester_year, yester_month, yester_day, one_before_year, one_before_month, one_before_day
    

def getJsonDataFromWeb(url, head, max_retries=5, wait_time=5):
    for i in range(max_retries):
        try:
            response = requests.get(url, headers=head, verify=False)
            response.raise_for_status()
            data = response.json()
            return data["items"][0]['articles']
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            print(f"Retrying in {wait_time} seconds...")
            time.sleep(wait_time)
    print(f"Failed to fetch data from {url} after {max_retries} retries.")
    return None

def UrlMaker(yy, ym, yd, oby, obm, obd):
    
    API_URL_yesterday = f'https://wikimedia.org/api/rest_v1/metrics/pageviews/top/fa.wikipedia.org/all-access/{yy}/{ym}/{yd}'
    API_URL_one_before = f'https://wikimedia.org/api/rest_v1/metrics/pageviews/top/fa.wikipedia.org/all-access/{oby}/{obm}/{obd}'
    Wiki_makhzan = f'https://stats.wikimedia.org/#/fa.wikipedia.org/reading/top-viewed-articles/normal%7Ctable%7C{yy}-{ym}-{yd}~{yy}-{ym}-{yd}%7C(access)~desktop*mobile-app*mobile-web%7Cdaily'
    return API_URL_yesterday, API_URL_one_before, Wiki_makhzan


def firstMessage(date, urllink):
    message2 = f'''===================================
☀ ترند های امروز
🗓 تاریخ: {date}
🔗 <a href="{urllink}">لینک تمامی ترند های امروز</a>
===================================
            '''
    encoded_message = urllib.parse.quote(message2)
    send_message_url2 = f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage?chat_id={TELEGRAM_CHANNEL}&text={encoded_message}&parse_mode=HTML'
    requests.get(send_message_url2)
    

def mainMessage(kalame, date, ranking, views):
    kalame_under = kalame.replace("_", " ")
    message3 = f'''📍 گوگل (ایران):            <a href="https://trends.google.com/trends/explore?date=today%205-y&geo=IR&q={kalame_under}&hl=en-US">5Y</a> | <a href="https://trends.google.com/trends/explore?geo=IR&q={kalame_under}&hl=en-US">12M</a> | <a href="https://trends.google.com/trends/explore?date=today%203-m&geo=IR&q={kalame_under}&hl=en-US">3M</a> | <a href="https://trends.google.com/trends/explore?date=today%201-m&geo=IR&q={kalame_under}&hl=en-US">1M</a> | <a href="https://trends.google.com/trends/explore?date=now%207-d&geo=IR&q={kalame_under}&hl=en-US">7D</a>'''
    message4 = f'''📍 یوتیوب (ایران):         <a href="https://trends.google.com/trends/explore?date=today%205-y&geo=IR&gprop=youtube&q={kalame_under}&hl=en-US">5Y</a> | <a href="https://trends.google.com/trends/explore?geo=IR&gprop=youtube&q={kalame_under}&hl=en-US">12M</a> | <a href="https://trends.google.com/trends/explore?date=today%203-m&geo=IR&gprop=youtube&q={kalame_under}&hl=en-US">3M</a> | <a href="https://trends.google.com/trends/explore?date=today%201-m&geo=IR&gprop=youtube&q={kalame_under}&hl=en-US">1M</a> | <a href="https://trends.google.com/trends/explore?date=now%207-d&geo=IR&gprop=youtube&q={kalame_under}&hl=en-US">7D</a>'''
    message5 = f'''🌍 سرچ گوگل (جهان):    <a href="https://trends.google.com/trends/explore?date=today%205-y&q={kalame_under}&hl=en-US">5Y</a> | <a href="https://trends.google.com/trends/explore?q={kalame_under}&hl=en-US">12M</a> | <a href="https://trends.google.com/trends/explore?date=today%203-m&q={kalame_under}&hl=en-US">3M</a> | <a href="https://trends.google.com/trends/explore?date=today%201-m&q={kalame_under}&hl=en-US">1M</a> | <a href="https://trends.google.com/trends/explore?date=now%207-d&q={kalame_under}&hl=en-US">7D</a>'''
    message6 = f'''🌍 سرچ یوتیوب (جهان): <a href="https://trends.google.com/trends/explore?date=today%205-y&gprop=youtube&q={kalame_under}&hl=en-US">5Y</a> | <a href="https://trends.google.com/trends/explore?gprop=youtube&q={kalame_under}&hl=en-US">12M</a> | <a href="https://trends.google.com/trends/explore?date=today%203-m&gprop=youtube&q={kalame_under}&hl=en-US">3M</a> | <a href="https://trends.google.com/trends/explore?date=today%201-m&gprop=youtube&q={kalame_under}&hl=en-US">1M</a> | <a href="https://trends.google.com/trends/explore?date=now%207-d&gprop=youtube&q={kalame_under}&hl=en-US">7D</a>'''

    message = f'''🔴 عنوان ترند:  {kalame_under}

📅 تاریخ: {date}
🏅 جایگاه ترند: {ranking}
🪟 تعداد بازدید: {views:,}
🔗 <a href="https://fa.wikipedia.org/wiki/{kalame.encode('utf-16', 'surrogatepass').decode('utf-16')}">لینک ویکی پدیا</a>

⭐گوگل ترند:
'''
    merged_message = message + '\n' + message3 + '\n' + message4 + '\n' + message5 + '\n' + message6
            
    params = {
            'chat_id': TELEGRAM_CHANNEL,
            'text': merged_message,
            'parse_mode': 'HTML'
            }
            
    requests.get(f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage", params=params)



def lastMessage(date):
    message2 = f'''===================================
☀ انتهای ترند های امروز
🗓 تاریخ: {date}
===================================
            '''
    send_message_url2 = f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage?chat_id={TELEGRAM_CHANNEL}&text={message2}'
    requests.get(send_message_url2)



def main():
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    
    datetoday = dateMaker(1)
    
    Urlmaker = UrlMaker(datetoday[0], datetoday[1], datetoday[2], datetoday[3], datetoday[4], datetoday[5])

    json_array = []
    
    # jDate = "1402/07/02"
    jDate = jdatetime.date.today().strftime('%Y/%m/%d')

    firstMessage(jDate, Urlmaker[2])
    
    yesterday_json = getJsonDataFromWeb(Urlmaker[1], headers)
    
    for i in range(50):
        json_array.append(yesterday_json[i]['article'])
    
    today_json = getJsonDataFromWeb(Urlmaker[0], headers)
    
    for i in range(50):
        if today_json[i]['article'] in json_array:
            print("Boud")
        else:
            mainMessage(today_json[i]['article'], jDate, today_json[i]['rank'], today_json[i]['views'])

    lastMessage(jDate)
            



schedule.every().day.at("07:00").do(main)

if __name__ == "__main__":
    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except Exception as e: 
        print(f"The Error is ")