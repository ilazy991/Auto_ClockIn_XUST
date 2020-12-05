from selenium import webdriver

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

print('abc')

chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options)



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

chrome_options.add_argument('window-size=1024,768')  # 16年之后，chrome给出的解决办法，抢了PhantomJS饭碗
chrome_options.add_argument('--headless')  # 16年之后，chrome给出的解决办法，抢了PhantomJS饭碗
chrome_options.add_argument('--disable-gpu')
#chrome_options.add_argument('--no-sandbox')  # root用户不加这条会无法运行
driver = webdriver.Chrome(options=chrome_options)  # 获取浏览器句柄

# 3.访问西科E站登录页面
driver.get("https://baidu.com")
html = driver.page_source
time.sleep(2)
print(html)

# close web browser
driver.close()
