import pytest

from pages.main_page import MainPage
from pages.games_page import GamesPage
from pages.entertaining_games_page import EntertainingGamesPage
from pages.tree_page import TreePage

class BaseTest:

    main_page: MainPage
    games_page: GamesPage
    entertaining_games_page: EntertainingGamesPage
    tree_page: TreePage

    @pytest.fixture(autouse=True)
    def setup(self,request,driver):
        request.cls.driver = driver
        request.cls.main_page = MainPage(driver)
        request.cls.games_page = GamesPage(driver)
        request.cls.entertaining_games_page = EntertainingGamesPage(driver)
        request.cls.tree_page = TreePage(driver)