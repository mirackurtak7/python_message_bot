from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

browser.get("https://web.whatsapp.com/")

# Kullanıcıdan giriş yapmasını beklemek için yeterli bir süre vermek için 10 saniye bekleyelim.
time.sleep(10)

chats = browser.find_elements("css selector", "._1hI5g._1XH7x._1VzZY")

for i in chats:
    if i.text == " ":#person list will be selected 
        i.click()
        time.sleep(2)

        text_area = browser.find_element_by_xpath("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome.lnk")

        for i in range(0, 1001):
            text_area.send_keys("otomatik mesaj")
            time.sleep(0.2)
            text_area.send_keys(Keys.ENTER)

        # 5 saniye beklemek için time.sleep(5) kullanabilirsiniz.
        time.sleep(5)

# İşlem tamamlandığında tarayıcıyı kapatmayı unutmayın.
browser.quit()
