from web_scrapping.web_scrapping import HeliumWeb, HeliumHotspot


if __name__ == '__main__':
    network = HeliumWeb()
    hotspot = HeliumHotspot()

    print(f'Hotspot is {hotspot.get_status()}. \n'
          f'Percentage of offline rak is {network.get_percentage_of_offline_hotspots()}')

