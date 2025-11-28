import pytest
from pages.jobfeed_page import Jobfeed
import logging
from utils.logger import get_logger


class Test_Apply:
    git
    push
    origin
    main
    def test_job_apply(self,browser):
        obj_jobfeed = Jobfeed(browser)
        obj_jobfeed.select_checkboxes()
        obj_jobfeed.click_apply_btn()


