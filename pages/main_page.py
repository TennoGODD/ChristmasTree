import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):

    PAGE_URL = Links.MAIN

    GAMES_FIELD = ("xpath","//a[text()='Игры']")

    @allure.step("Click games")
    def click_games(self):
        games_field = self.wait.until(EC.element_to_be_clickable(self.GAMES_FIELD))
        games_field.click()