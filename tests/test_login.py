import time
import pytest
from pages.login_page import LoginPage
from utils.logger import get_logger
log = get_logger(__name__)

class Test_Login:
    @pytest.mark.parametrize("user_type",["valid_user","invalid_user","invalid_pass"])
    def test_valid_user(self,browser,test_data,user_type):
        log.info("Starting test for valid login user")
        login_page = LoginPage(browser)

        login_page.open_url(test_data["base_url"])
        username = test_data["login_data"]["user_type"]["email"]
        password = test_data["login_data"]["user_type"]["password"]
        log.info("sending username password")
        login_page.login(username,password)
        log.info("verifying successfully valid user login ")
        if user_type == "valid_user":
            log.info("verifying successfully valid user login ")
            assert login_page.redirect_to_jobfeedpage() , "Login not successful"
        else:
            log.info("verifying successfully invalid user login ")
            assert login_page.validate_error() , "Error message not displayed for invalid login"

    '''def test_invalid_user(self,browser,test_data):
        login_page = LoginPage(browser)

        login_page.open_url(test_data["base_url"])
        username = test_data["login_data"]["invalid_user"]["email"]
        password = test_data["login_data"]["invalid_user"]["password"]
        login_page.login(username,password)

        assert "jobfeed" in login_page.get_title().lower(), "Login-Failed - Job feed not opened"

        login_page.validate_error()

    def test_invalid_pass(self,browser,test_data):
        login_page = LoginPage(browser)

        login_page.open_url(test_data["base_url"])
        username = test_data["login_data"]["invalid_pass"]["email"]
        password = test_data["login_data"]["invalid_pass"]["password"]
        login_page.login(username,password)

        assert "jobfeed" in login_page.get_title().lower(), "Login-Failed - Job feed not opened"

        login_page.validate_error()'''











