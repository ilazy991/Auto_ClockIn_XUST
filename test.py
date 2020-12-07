# coding=utf-8 
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
import configparser
import os
import sys,traceback
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC




mobile_emulation = {"deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},
                    "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"}

# 配置加载策略
#desired_capabilities = DesiredCapabilities.CHROME  # 修改页面加载策略
#desired_capabilities["pageLoadStrategy"] = "eager"  # 注释这两行会导致最后输出结果的延迟，即等待页面加载完成再输出
chrome_options = Options()  # 实例化一个启动参数对象

chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)  # 这里看清楚了，不是add_argument
# chrome_options.add_argument('--window-size=1366,1400')  # 设置浏览器窗口大小
prefs = {"profile.managed_default_content_settings.images": 2, 'permissions.default.stylesheet': 2}  # 禁止加载图片和CSS样式
chrome_options.add_experimental_option("prefs", prefs)

#chrome_options.add_argument('window-size=1024,768')  # 16年之后，chrome给出的解决办法，抢了PhantomJS饭碗
chrome_options.add_argument('--headless')  # 16年之后，chrome给出的解决办法，抢了PhantomJS饭碗
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')  # root用户不加这条会无法运行
# driver = webdriver.Chrome(options=chrome_options)  # 获取浏览器句柄

# # 3.访问西科E站登录页面
# driver.get("https://baidu.com")
# html = driver.page_source
# time.sleep(2)
# print(html)

# 1.打开浏览器
def fun1(username_text,password_text):
    driver = webdriver.Chrome(options=chrome_options)  # 获取浏览器句柄
    try:
        wait = WebDriverWait(driver, 3)  # 后面可以使用wait对特定元素进行等待
        # 3.访问西科E站登录页面
        driver.get(url_login)
        # 获取用户与密码输入框并输入
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="mobileUsername"]').send_keys(username_text)
        driver.find_element_by_xpath('//*[@id="mobilePassword"]').send_keys(password_text)
        # 获取登录按键并点击登录
        driver.find_element_by_xpath('// *[ @ id = "load"]').click()
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+"\t"+str(username_text) + "\n成功登陆")
        time.sleep(1)
        try:
            driver.find_element_by_xpath('/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-scroll-view/div/div/div/uni-view/uni-scroll-view/div/div/div/uni-view[1]').click()
            time.sleep(3)
        except Exception as e:
            print(e)
            pass
        driver.find_element_by_xpath('/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[2]/uni-button').click()

        time.sleep(1)

        # 获取CheckBox复选框(我已认证阅读)并点击
        btn_div = driver.find_element_by_css_selector('input[type=checkbox]')
        driver.execute_script("arguments[0].click();", btn_div)

        # desired_capabilities["pageLoadStrategy"] = "normal"  # 注释这两行会导致最后输出结果的延迟，即等待页面加载完成再输出

        # 获取继续打卡按钮并点击
        target = driver.find_element_by_xpath("//*[text()='继续打卡']")
        time.sleep(3) #定位到之后等待3s执行click()
        target.click()

        #driver.find_element_by_xpath("/html/body/div/div[3]/p/span[1]").click()
        time.sleep(1)

        # 获取点击获取详细地址按钮并点击
        #target = driver.find_element_by_xpath("//*[text()='点击获取详细地址']")
        target = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[3]/ul[1]/li[3]/span")
        driver.execute_script("arguments[0].scrollIntoView();", target)
        target.click()

        time.sleep(1)
        try:
            driver.switch_to.alert.accept()
            driver.find_element_by_id("district1").find_element_by_xpath("//option[@value='碑林区']").click()
        except Exception as e:
            # print(e)
            pass
        # 输入地址

        time.sleep(1)
        # input = WebDriverWait(driver, 50).until(EC.visibility_of_any_elements_located((By.CSS_SELECTOR, 'input.srk.jiaodian')))
        input = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input.srk.jiaodian')))

        target = driver.find_elements_by_css_selector('input.srk.jiaodian')[1]
        driver.execute_script("arguments[0].scrollIntoView();", target)
        # print(str(input.text))
        # driver.execute_script("arguments[0].onblur();",driver.find_elements_by_css_selector('input.srk.jiaodian')[1])
        # input.send_keys("西安科技大学雁塔校区")
        # js = r'$("input.srk.jiaodian:eq(1)").val(u"西安科技大学")'
        # driver.execute_script(js)

        time.sleep(2)
        driver.find_elements_by_css_selector('input.srk.jiaodian')[1].click()

        driver.switch_to.active_element.send_keys(u'西安科技大学')


        jQuery = r'$("input[name=\'jrtwfw5\']")[0].click()'
        driver.execute_script(jQuery)
        radios = driver.find_elements_by_css_selector('input[type=radio]')
        for radio in radios:
            if radio.get_attribute(u"name") == u"jrsfzx3" and radio.get_attribute(u"value") == u"是":
                if not radio.is_selected():
                    radio.click()
                    print("今日在校：" + radio.get_attribute("value"))

            # if radio.get_attribute(u"name") == u"jrtwfw5" and radio.get_attribute(u"value") == u"正常体温:36～37.2℃":
            #     if not radio.is_selected():
            #         radio.click()
        # 获取提交按钮并点击	jiaodian = driver.find_elements_by_xpath('//*[@id="xxd"]/ul/li/input')[0]
        driver.find_element_by_css_selector('span#submit').click()

        dig_confirm = driver.switch_to.alert
        # 打印对话框的内容
        print(dig_confirm.text)
        # 点击“确认”按钮
        dig_confirm.accept()


        try:
            driver.find_elements_by_xpath("//*[text()='已完成']")
            driver.quit()
            print(username_text+"\t打卡成功")
            return True, "none"
        except Exception as e:
            print(traceback.format_exc())
            return False, e
        finally:
            driver.quit()
    except Exception as e:
        print(traceback.format_exc())
        driver.quit()
        return False, e


url_login = 'http://ids.xust.edu.cn/authserver/login?service=http%3A%2F%2Fehallmobile.xust.edu.cn%2Fossh_server%2FmobileCaslogin'
# username_text = os.environ["SCKEY"]
USERNAME_TEXT = os.environ["USERNAME_TEXT"]
PASSWORD_TEXT = os.environ["PASSWORD_TEXT"]
MSG_TO = os.environ["MSG_TO"]


status, e = fun1(USERNAME_TEXT, PASSWORD_TEXT)
desp=""
if(status == False):
    print("重新再次打卡")
    status, e = fun1(USERNAME_TEXT, PASSWORD_TEXT)
    if(status == False):
        text =  "打卡失败:"
        desp = str(e)
    else:
        text =  "打卡成功:"
else:
    text =  "打卡成功:"

if "SERVERPUSHKEY" in os.environ:
    driver = webdriver.Chrome(options=chrome_options)  # 获取浏览器句柄
    SERVERPUSHKEY = os.environ["SERVERPUSHKEY"]
    url = "https://sc.ftqq.com/"+SERVERPUSHKEY+".send?text="+text
    if(len(desp)):
      url += "desp="+desp
    driver.get(url)

