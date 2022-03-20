from selenium import webdriver
from selenium.webdriver.firefox.options import Options


class HeliumWebScrapper:
    def __init__(self):
        options = Options()
        options.add_argument("--headless")
        self._driver = webdriver.Firefox(options=options)
        self._browser_wait = 1

    def get_info(self, url: str, xpath: str) -> str:
        self._driver.get(url)
        self._driver.minimize_window()
        self._driver.implicitly_wait(self._browser_wait)
        el = self._driver.find_element('xpath', xpath)
        el_property = el.get_property("innerHTML")
        return el_property


class HeliumWeb(HeliumWebScrapper):
    def __init__(self):
        super().__init__()

    def get_percentage_of_offline_hotspots(self) -> int:
        rak_hss_status = self.get_info(
            'https://app.hotspotty.net/hotspots/makers/14h2zf1gEr9NmvDb2U53qucLN2jLrKU1ECBoxGnSnQ6tiT6V2kM/statistics',
            '/html/body/div[1]/div[1]/div/div[3]/main/div[2]/div[3]/dl/div[2]/div/dd/div/p/div')
        perc_iter = rak_hss_status.find('%')
        offline_percentage = int(rak_hss_status[:perc_iter])
        return offline_percentage


class HeliumHotspot(HeliumWebScrapper):
    def __init__(self):
        super().__init__()
        self._name = '11uGsSyeedD1kt1rfazDpWQKfrPrqP9E53ZH4gXViy4pXruqNVG'

    def get_status(self) -> str:
        status = self.get_info(f'https://explorer.helium.com/hotspots/{self._name}',
                               '/html/body/div/div/div/div[2]/div/div[3]/div/div[2]/div[2]/div/div[2]/div[2]'
                               '/span/p/span')
        return status.lower()
