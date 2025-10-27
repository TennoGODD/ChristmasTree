from time import sleep
import time
import allure
import pytest

from base.base_test import BaseTest
@allure.feature("Decorate Tree")
class TestDecorateTree(BaseTest):

    @allure.title("Decorate Tree")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_decorate_tree(self):
        self.main_page.open()
        self.main_page.click_games()
        self.games_page.is_open()
        self.games_page.close_cookie_banner()
        self.games_page.click_entertaining_games()
        self.entertaining_games_page.is_open()
        self.entertaining_games_page.click_tree()
        self.tree_page.is_open()
        self.tree_page.close_live()
        self.tree_page.scroll()
        self.tree_page.decorate_tree()

        sleep(2)
        self.tree_page.make_screenshot("Success")
