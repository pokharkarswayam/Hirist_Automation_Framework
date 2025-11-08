import pytest
from pages.jobfeed_page import Jobfeed


class Test_Apply:

    def test_job_apply(self,browser):
        obj_jobfeed = Jobfeed(browser)
        obj_jobfeed.select_checkboxes()
        obj_jobfeed.click_apply_btn()


