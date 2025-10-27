import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class EntertainingGamesPage(BasePage):

    PAGE_URL = Links.ENTERTAINING_GAMES

    TREE_FIELD = ("xpath","//div[contains(@class, 'cardGame')]//h6[text()='Наряди Ёлку!']")

    @allure.step("Click tree")
    def click_tree(self):
        tree_field = self.wait.until(EC.element_to_be_clickable(self.TREE_FIELD))
        tree_field.click()