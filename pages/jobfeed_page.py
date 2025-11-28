import logging
from itertools import count

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class Jobfeed(BasePage):
    cb = (By.XPATH,"//input[@type='checkbox']//parent::span")
    apply_btn = (By.XPATH,"//button[text()='Apply All']")
    posting_dropdown = (By.XPATH,"//div[@data-name='posting']")

    def __init__(self,driver):
        super().__init__(driver)

    def find_checkboxes(self):
        return self.find_elements(self.cb)

    def find_posting_dropdown(self):
        return self.find_element(self.posting_dropdown)

    def find_length_posting_dropdown(self):
        return Select(self.find_posting_dropdown()).options

    def select_checkboxes(self):
        try:
            # Wait up to 20 seconds for at least one checkbox
            checkboxes = WebDriverWait(self.driver, 20).until(
                EC.presence_of_all_elements_located(self.cb)
            )
            for checkbox in checkboxes:
                if checkbox.is_displayed() and not checkbox.is_selected():
                    checkbox.click()
        except Exception as e:
            self.driver.save_screenshot("checkbox_error.png")
            print("Error selecting checkboxes:", e)
            raise

    def find_apply_btn(self):
        return self.find_element(self.apply_btn)

    def click_apply_btn(self):
        return self.click_element(self.apply_btn)










