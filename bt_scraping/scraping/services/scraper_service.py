import requests
from bs4 import BeautifulSoup
from abc import ABC, abstractmethod


class Scraper(ABC):
    
    @abstractmethod
    def get_data(self):
        pass
    
    
class BTScraper(Scraper):
    
    def get_data(self):
        request = requests.get('https://www.btassetmanagement.ro/en/bt-am-investors/funds-evolution')
        body = request.text
        # get all the html
        html = BeautifulSoup(body, 'html.parser')
        # get only the table as a list with every row
        table = html.find(class_="evolution-table hidden-mobile").contents
        # eliminate the lable row and the unnecessary \n's
        table_with_relevant_data = list(filter(lambda n : n != '\n', table))[1:]
        # create list with pairs of fund name and fund value as tuples
        data = list(map(lambda row : (row.find_all(class_="td")[0].text.replace('*', ''), row.find_all(class_="td")[1].text) ,table_with_relevant_data))
        return data
    

class Factory(ABC):
    
    def get_data(self) -> list:
        scraper: Scraper = self.create_scraper()
        return scraper.get_data()
    
    @abstractmethod 
    def create_scraper(self):
        pass


class ScraperFactory(Factory):
    
    def create_scraper(self):
        return BTScraper()
    
def scrap_BT():
    factory = ScraperFactory()
    return factory.get_data()
