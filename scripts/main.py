from selenium import webdriver
import time

if __name__ == '__main__':
    driver = webdriver.Firefox()

    driver.get("https://explorer.helium.com/hotspots/11uGsSyeedD1kt1rfazDpWQKfrPrqP9E53ZH4gXViy4pXruqNVG/")
    time.sleep(10)
    el = driver.find_element('xpath',
                             '/html/body/div/div/div/div[2]/div/div[3]/div/div[2]/div[2]/div/div[2]')
    print(f'Malza status: {el.text}')

    driver.get('https://app.hotspotty.net/hotspots/makers/14h2zf1gEr9NmvDb2U53qucLN2jLrKU1ECBoxGnSnQ6tiT6V2kM/statistics/')
    time.sleep(10)
    el2 = driver.find_element('xpath',
                             '/html/body/div[1]/div[1]/div/div[3]/main/div[2]/div[3]/dl/div[1]/div/dd/div/p/div')
    print(f'Perctange of offline routers: {el2.text}')
    driver.close()
