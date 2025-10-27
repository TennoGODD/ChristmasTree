import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class GamesPage(BasePage):

    PAGE_URL = Links.GAMES

    ENTERTAINING_GAMES_FIELD = ("xpath","(//a[text()='Развлекательные игры'])[1]")
    COOKIE_BANNER_FIELD = ("xpath","//button[text()='ХОРОШО']")

    @allure.step("Click entertaining games")
    def click_entertaining_games(self):
        entertaining_games_field = self.wait.until(EC.element_to_be_clickable(self.ENTERTAINING_GAMES_FIELD))
        entertaining_games_field.click()

    @allure.step("Close cookie banner")
    def close_cookie_banner(self):
        cookie_banner_field = self.wait.until(EC.element_to_be_clickable(self.COOKIE_BANNER_FIELD))
        cookie_banner_field.click()
