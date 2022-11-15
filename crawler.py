import os
import time

import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


# 切換事件
def event_switch():
    eventSwitch = browser.find_element_by_xpath("//md-select-value[@id='select_value_label_0']")
    eventSwitch.click()
    actions = ActionChains(browser)
    actions.move_to_element(eventSwitch)

    for up in range(Up):
        actions.send_keys(Keys.UP)

    actions.send_keys(Keys.ENTER)
    actions.perform()
    time.sleep(1)
    browser.refresh()


def download():
    global i
    for tr in trs:
        tds = tr.find_all('td')
        city = tds[2].text.strip()
        town_ship = tds[3].text.strip()
        village = tds[4].text.strip()
        pics = tds[16].find_all('a')
        folder = city + town_ship + village
        os.makedirs("./%s/%s" % (event, folder), exist_ok=True)

        for pic in pics:
            pic_url = pic['href']
            picture = requests.get(pic_url)
            picture.raise_for_status()
            with open("./%s/%s/%s.jpg" % (event, folder, i), 'wb') as f:
                f.write(picture.content)
            print('%s 圖片寫入成功' % pic_url)
            i += 1


driverPath = "D:\geckodriver\chromedriver.exe"
account = "帳號"
pwd = "密碼"

# 操作指南:
# 最新事件 new_event 保持True , 否則改 False, 要注意大小寫
# 若有向上次數 請改Up數字
# new_event = True 時 Up 沒有作用
new_event = True
Up = 1

browser = webdriver.Chrome(driverPath)
# 固定視窗大小迴避 element not interactable 的 error
browser.set_window_size(1200, 800)
browser.get("https://wrafpc.tw/main/index2.php")
accountInput = browser.find_element_by_xpath("//body/div[2]/div[1]/div[2]/form[1]/input[1]")
pwdInput = browser.find_element_by_xpath("//body/div[2]/div[1]/div[2]/form[1]/input[2]")
accountInput.send_keys(account)
pwdInput.send_keys(pwd)
submitBtn = browser.find_element_by_xpath("//body/div[2]/div[1]/div[2]/form[1]/input[3]")
submitBtn.click()
browser.find_element_by_xpath("//a[contains(text(),'顯示啟動狀態')]").click()
browser.find_element_by_xpath("//span[contains(text(),'災前整備 填寫結果')]").click()

if not new_event:
    event_switch()

# 資料本體
i = 1
soup = bs(browser.page_source, 'html.parser')
trs = soup.select('tbody tr')
event = soup.find("h2", "ng-binding").text.strip()
os.makedirs('./%s/' % event, exist_ok=True)
download()
browser.find_element_by_xpath("//body/div[2]/div[1]/div[2]/button[3]").click()

if not new_event:
    event_switch()

soup = bs(browser.page_source, 'html.parser')
trs = soup.select('tbody tr')
event = soup.find("h2", "ng-binding").text.strip()
os.makedirs('./%s/' % event, exist_ok=True)
download()
print("下載完成")
print('總共{}張圖片'.format(i-1))
