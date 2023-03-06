from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime

from configs.settings import options
from parsing.models import Announcement
from parsing.page import Paginator

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


class AnnouncementParser(Paginator):
    def _get_html(self):
        driver.get(self.url)
        return driver.page_source

    def get_data(self):
        data = self._get_soup().find_all('div', class_='search-item')
        res = []
        for announcement in data:
            try:
                image = announcement.find('div', class_='image').img.get('data-src')
            except AttributeError:
                image = ''
            try:
                added_at = announcement.find('span', class_='date-posted').text.split('/')
                added_at = '-'.join(added_at)
            except AttributeError:
                added_at = ''
            try:
                price = announcement.find('div', class_='price').text.strip()
            except AttributeError:
                price = ''
            date = datetime.now().strftime('%m-%d-%Y')
            res.append(Announcement(
                image=image,
                price=price,
                added_at=added_at,
                date=date
            ))
        Announcement.bulk_create(res)