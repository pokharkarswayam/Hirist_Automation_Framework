import pytest
from pages.jobfeed_page import Jobfeed
import logging
from utils.logger import get_logger


class Test_Apply:
        def test_job_apply(self,browser):
        obj_jobfeed = Jobfeed(browser)
        obj_jobfeed.select_checkboxes()
        obj_jobfeed.click_apply_btn()

    def test_verify_posting_dropdown(self,browser):
        obj_jobfeed = Jobfeed(browser)
        length = obj_jobfeed.find_length_posting_dropdown()
        assert length == 5 , "options are not correct"
