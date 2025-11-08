from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage

class LoginPage(BasePage):

    jobseeker_btn = (By.XPATH, "(//button[@type='button'])[3]")
    sign_btn = (By.XPATH, "//a[contains(text() ,'Sign In')]")
    email_txt = (By.NAME, "email")
    password_txt = (By.NAME, "password")
    submit_btn=(By.XPATH, "//button[@type='submit']")
    error_message = (By.XPATH,"//p[text()='Incorrect Email ID or password. Please try again.']")

    def __init__(self,driver):
        super().__init__(driver)
        self.url = "https://www.hirist.tech/"

    def open_url(self,url):
        self.driver.get(self.url)

    def validate_error(self):
        return self.find_element(self.error_message).text()

    def login(self,username,password):

        self.click_element(self.jobseeker_btn)
        self.click_element(self.sign_btn)
        self.enter_text(self.email_txt,"vivek.pokharkar@gmail.com")
        self.enter_text(self.password_txt, "Logic#01")
        self.click_element(self.submit_btn)

    def redirect_to_jobfeedpage(self):
        return self.wait.until(EC.url_contains("jobfeed"))
