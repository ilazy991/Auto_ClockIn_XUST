# coding=utf-8



import requests
from seleniumwire import webdriver  # Import from seleniumwire
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait

import os
import sys,traceback
import time
from datetime import datetime
import pytz
import json





def getDriver(windows = True):
    mobile_emulation = {"deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},
                        "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"}

    # 配置加载策略
    # desired_capabilities = DesiredCapabilities.CHROME  # 修改页面加载策略
    # desired_capabilities["pageLoadStrategy"] = "eager"  # 注释这两行会导致最后输出结果的延迟，即等待页面加载完成再输出
    chrome_options = Options()  # 实例化一个启动参数对象
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)  # 这里看清楚了，不是add_argument
    prefs = {"profile.managed_default_content_settings.images": 2, 'permissions.default.stylesheet': 2}  # 禁止加载图片和CSS样式
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_argument('window-size=1024,768')  # 16年之后，chrome给出的解决办法，抢了PhantomJS饭碗
    chrome_options.add_argument("--disable-crash-reporter")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-web-security")
    chrome_options.add_argument('--ignore-certificate-errors')

    chrome_options.add_argument('--disable-logging')
    chrome_options.add_argument("--log-level=3")
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_options.add_argument("--disable-dev-shm-usage")

    chrome_options.add_argument("--output=/dev/null")

    wire_options = {
        'connection_timeout': 60
    }
    if windows == False:
        chrome_options.add_argument('--headless')  # 16年之后，chrome给出的解决办法，抢了PhantomJS饭碗
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')  # root用户不加这条会无法运行
    driver = webdriver.Chrome(seleniumwire_options=wire_options, options=chrome_options)  # 获取浏览器句柄
    return driver


def getUID(driver, url, username_text, password_text):
    # 3.访问西科E站登录页面
    driver.get(url)
    # 获取用户与密码输入框并输入
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="mobileUsername"]').send_keys(username_text)
    driver.find_element_by_xpath('//*[@id="mobilePassword"]').send_keys(password_text)
    driver.find_element_by_xpath('// *[ @ id = "load"]').click()# 获取登录按键并点击登录
    time.sleep(1)
    for request in driver.requests:
        if request.response and 'getUser' in request.url:
            res = json.loads(request.response.body.decode('utf-8'))
            uid = res["data"]["user"]["signAccount"]
            return uid

def getDataAndCookies(driver, url):
    data = {
        "xkdjkdk": {
            "procinstid": "",
            "empid": "53816",
            "shzt": "-2",
            "id": "",
            "jrrq1": "",
            "sjh2": "",
            "jrsfzx3": "是",
            "szdd4": "中国 陕西省 西安市 碑林区",
            "xxdz41": "西安科技大学",
            "jrtwfw5": "正常体温:36～37.2℃",
            "jrsfjgwh6": "否",
            "jrsfjghb7": "否",
            "jrsfcxfrzz8": "否",
            "jrsfywhrjc9": "否",
            "jrsfyhbrjc10": "否",
            "jrsfjcgrrq11": "否",
            "jssfyqzysgl12": "否",
            "sfcyglq13": "否",
            "glkssj131": "",
            "gljssj132": "",
            "sfyyqxgzz14": "否",
            "qtxx15": None,
            "gh": "",
            "xm": "",
            "xb": "",
            "sfzh": "",
            "szyx": "",
            "xydm": "",
            "zy": "",
            "zydm": "",
            "bj": "",
            "bjdm": "",
            "jg": "",
            "yx": "",
            "sfxs": "是",
            "xslx": "2",
            "jingdu": "",
            "weidu": "",
            "sfncxaswfx16": "否",
            "dm": "",
            "jdlx": "1",
            "tbsj": "",
            "fcjtgj17Qt": "",
            "fcjtgj17": "",
            "hqddlx": "2",
            "ymtys": "",
            "time": ""
        }
    }
    driver.get(url)
    time.sleep(1)
    cookie = "JSESSIONID="+driver.get_cookies()[0]["value"]

    for request in driver.requests:
        if request.response and 'jkdk.xkdjkdkbiz.getStuXx.biz.ext' in request.url:
            body = request.response.body.decode('utf-8')
            body = json.loads(body)

            res = body["list"][0]
            data['xkdjkdk']["bj"] = res["BJ"]
            data['xkdjkdk']["xm"] = res["XM"]
            data['xkdjkdk']["gh"] = res["XH"]
            data['xkdjkdk']["sjh2"] = res["LXDH"]
            data['xkdjkdk']["xb"] = res["XB"]
            data['xkdjkdk']["szyx"] = res["XY"]
            data['xkdjkdk']["bjdm"] = res["BJDM"]
            data['xkdjkdk']["xydm"] = res["XYDM"]
            data['xkdjkdk']["xslx"] = res["XSLX"]
            data['xkdjkdk']["dm"] = res["BJDM"]
            tz = pytz.timezone('Asia/Shanghai') #东八区
            data['xkdjkdk']["tbsj"] = datetime.fromtimestamp(int(time.time()), pytz.timezone('Asia/Shanghai')).strftime('%Y-%m-%d %H:%M:%S')
            data['xkdjkdk']["jrrq1"] = datetime.fromtimestamp(int(time.time()), pytz.timezone('Asia/Shanghai')).strftime('%Y-%m-%d')
            data['xkdjkdk']["time"] = datetime.fromtimestamp(int(time.time()), pytz.timezone('Asia/Shanghai')).strftime('%Y-%m-%d')
            return data, cookie
    return None, None

def daka(username, password):

    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Content-Type": "text/json",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
        "X-Requested-With": "XMLHttpRequest",
        "Cache-Control": "no-cache",
        "Referer": "https://ehallplatform.xust.edu.cn/default/jkdk/mobile/mobJkdkAdd_test.jsp",
        "Cookie": "JSESSIONID=DF4DFA3320DCCBFE2E15C3B85A865F2F",
        # "Content-Length": "941",
        "Host": "ehallplatform.xust.edu.cn",
        "Origin": "https://ehallplatform.xust.edu.cn"
    }

    driver = getDriver(False)

    # wait = WebDriverWait(driver, 3)  # 后面可以使用wait对特定元素进行等待
    UID = getUID(driver, "http://ids.xust.edu.cn/authserver/login?service=http://ehallmobile.xust.edu.cn/ossh_server/mobileCaslogin", username_text, password_text)
    if UID == None:
        print("获取UID失败")
        return "error"
    else:
        print("获取UID成功")

    url = "http://ehallplatform.xust.edu.cn/default/jkdk/mobile/mobJkdkAdd_test.jsp?uid=" + UID
    data, cookies = getDataAndCookies(driver, url)
    if data == None or cookies == None:
        print("个人信息获取失败")
        return "error"
    headers["Cookie"] = cookies

    r = requests.post("http://ehallplatform.xust.edu.cn/default/jkdk/mobile/com.primeton.eos.jkdk.xkdjkdkbiz.jt.biz.ext", json = data, headers = headers)

    driver.quit()
    if r._content == b'{}':
        print("获取个人信息成功")
        return "success"
    else:
        return "error"
    return "error"


if __name__ == '__main__':

    driver = getDriver(False)
    wait = WebDriverWait(driver, 3)  # 后面可以使用wait对特定元素进行等待
    username_text = os.environ["USERNAME_TEXT"]
    password_text = os.environ["PASSWORD_TEXT"]
    msg_to = os.environ["MSG_TO"]
    
    status= ""
    print("开始为"+username_text+"打卡")
    try:
        status = daka(username_text, password_text)
    except Exception as e:
        print(traceback.format_exc())
    if(status == "error"):
        print("重新再次打卡")
        try:
            status = daka(username_text, password_text)
        except Exception as e:
            print(traceback.format_exc())
            
    if status == "success":
        print("打卡成功"+username_text)
    else:
    
        SERVERPUSHKEY = os.environ["SERVERPUSHKEY"]
        url = "https://sc.ftqq.com/"+SERVERPUSHKEY+".send?text="+"打卡失败"
        if(len(desp)):
          url += "desp="+username_text
        driver.get(url)
        print("打卡失败"+username_text)
    
    driver.quit()

