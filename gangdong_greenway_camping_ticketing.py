import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC

# Chrome WebDriver 경로 설정
chrome_driver_path = 'C:/Users/gunwoo/Desktop/workspace/python/python_practice/chromedriver-win64/chromedriver.exe'

# Chrome WebDriver 서비스 초기화
service = Service(chrome_driver_path)

# Chrome WebDriver 초기화
driver = webdriver.Chrome(service=service)

# 웹 페이지로 이동
url = "https://camp.xticket.kr/web/main?shopEncode=5f9422e223671b122a7f2c94f4e15c6f71cd1a49141314cf19adccb98162b5b0"
driver.get(url)

my_loop = True
camp_names = ['마로니에', '청단풍', '자작나무', '이팝나무']

# 공지사항을 3번 클릭하는 함수
def notice_3_click():
    # 공지사항 창을 연달아 클릭
    notice1 = driver.find_element(By.XPATH, '/html/body/div[7]/div/div/div/fieldset/ul/li/button/img')
    notice1.click()

    notice2 = driver.find_element(By.XPATH, '//*[@id="notice_layer_745"]/div/div/div/fieldset/ul/li/button/img')
    notice2.click()

    notice3 = driver.find_element(By.XPATH, '//*[@id="notice_layer_333"]/div/div/div/fieldset/ul/li/button/img')
    notice3.click()

# 달력에서 원하는 일자를 고르는 함수
def date_choose():
    # 달력에서 화살표 클릭
    date_link = driver.find_element(By.XPATH, '//*[@id="contents"]/div[2]/div[1]/div[1]/ul[2]/li[2]/a')
    date_link.click()
    time.sleep(0.5)

    # 달력에서 날짜 클릭
    date_link2 = driver.find_element(By.XPATH, '//*[@id="calendarTable"]/tbody/tr[2]/td[7]/a')
    date_link2.click()
    time.sleep(1)


# 예매 여부를 확인 하는 함수
def ticket_choose(name):
    if name == '마로니에':
        loop_num = 11
        ticket_index = '1'
    elif name == '청단풍':
        loop_num = 9
        ticket_index = '2'
    elif name == '자작나무':
        loop_num = 9
        ticket_index = '3'
    else:
        loop_num = 10
        ticket_index = '0'
        
    for i in range(loop_num):
        myid = '//*[@id="0001' + ticket_index + '0' + str(i+1).zfill(2) + '"]'
        camping = driver.find_element(By.XPATH, myid)
        camping_src = camping.get_attribute("src")
        if camping_src == 'https://camp.xticket.kr/resources/images/icon/product_map_sold20x20.png':
            print(f'{name} {i+1}번 예매완료')
        else:
            for _ in range(30):
                print(f'{name} {i + 1}번 취소매물!!!!!')
            fin_url = "https://www.youtube.com/watch?v=xbO1CY1PXkE"
            driver.get(fin_url)
            time.sleep(10000)


if __name__=='__main__':
    while my_loop:
        driver.refresh()

        notice_3_click()

        date_choose()

        for name in camp_names:
            ticket_choose(name)
        