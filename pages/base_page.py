from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import get_logger

class BasePage:
    def __init__(self, driver, timeout=20):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)
        get_logger(self.__class__.__name__)

    def find_element(self, by_locator):
        by,value = by_locator
        return self.wait.until(EC.visibility_of_element_located((by,value)))

    def find_elements(self, by_locator):
        by,value = by_locator
        return self.wait.until(EC.presence_of_all_elements_located((by,value)))

    def click_element(self, by_locator):
        by, value = by_locator
        element = self.driver.find_element(by,value)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((by,value)))

        element.click()

    def enter_text(self, by_locator, text):
        by, value = by_locator
        return self.find_element((by, value)).send_keys(text)

    def get_title(self):
        return self.driver.title

