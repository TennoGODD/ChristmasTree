import allure
import random
from time import sleep
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import MoveTargetOutOfBoundsException


class TreePage(BasePage):

    PAGE_URL = Links.TREE

    CROSS_FIELD = ("xpath","//*[@id='baloonVideo1']/div[1]")
    IFRAME = ("xpath","//iframe")
    CANVAS = ("xpath","//canvas")

    @allure.step("Click cross")
    def close_live(self):
        cross_field = self.wait.until(EC.element_to_be_clickable(self.CROSS_FIELD))
        cross_field.click()

    @allure.step("Click entertaining games")
    def scroll(self):
        self.driver.execute_script("window.scrollTo(0, 150)")

    @allure.step("Decorate Tree")
    def decorate_tree(self):
        iframe = self.wait.until(EC.visibility_of_element_located(self.IFRAME))
        self.driver.switch_to.frame(iframe)
        canvas = self.wait.until(EC.visibility_of_element_located(self.CANVAS))
        canvas_size = canvas.size

        center_x = canvas_size['width'] / 2
        center_y = canvas_size['height'] / 2
        menu_left_border_x = center_x / 2
        menu_width = center_x - menu_left_border_x
        menu_center_x = menu_left_border_x + (menu_width / 2)
        left_column_x = (menu_width / 3) + menu_left_border_x
        right_column_x = ((menu_width / 3) * 2) + menu_left_border_x

        menu_icons_1_row_y = (center_y / 3) * -1
        menu_icons_2_row_y = -15
        menu_icons_3_row_y = center_y / 4
        menu_icons_4_row_y = menu_icons_3_row_y * 2
        menu_icons_5_row_y = menu_icons_3_row_y * 3

        icons = {
            'stars': (left_column_x, menu_icons_1_row_y),
            'rings': (right_column_x, menu_icons_1_row_y),
            'cookies': (left_column_x, menu_icons_2_row_y),
            'ula': (right_column_x, menu_icons_2_row_y),
            'candies': (left_column_x, menu_icons_3_row_y),
            'zoo': (right_column_x, menu_icons_3_row_y),
            'candles': (left_column_x, menu_icons_4_row_y),
            'ball1': (right_column_x, menu_icons_4_row_y),
            'ball2': (left_column_x, menu_icons_5_row_y),
            'ball3': (right_column_x, menu_icons_5_row_y),
            'black_button': (menu_center_x , menu_icons_1_row_y - 40)
        }
        toys = {
            't1': icons['stars'],
            't2': icons['rings'],
            't3': icons['cookies'],
            't4': icons['ula'],
            't5': icons['candies'],
            't6': icons['zoo'],
            't7': icons['candles'],
            't8': icons['ball1'],
            't9': icons['ball2'],
            't10': icons['ball3'],
        }

        def move(coords_source, coords_target):
            actions = ActionChains(self.driver)
            actions.move_to_element_with_offset(canvas, *coords_source)
            actions.click_and_hold()
            actions.move_by_offset(*coords_target)
            actions.release()
            actions.perform()

        def click(coords):
            actions = ActionChains(self.driver)
            actions.move_to_element_with_offset(canvas, *coords)
            actions.click()
            actions.perform()

        count = 0

        while count < 20:
            random_icon_key = random.choice(list(icons.keys()))
            click(icons[random_icon_key])
            sleep(1)
            x = int((menu_center_x - random.randrange(0, 70)) * -1)
            y = random.randint(int((center_y - 30) * -1), int(center_x - 80))
            try:
                random_toy_key = random.choice(list(toys.keys()))
                move(toys[random_toy_key], (x, y))
            except MoveTargetOutOfBoundsException:
                print(f'x:{x}\ny:{y}')
            sleep(1)
            click(icons['black_button'])
            sleep(1)
            count += 1
