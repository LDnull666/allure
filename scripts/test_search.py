from base.base_driver import init_driver
from page.page import Page
import pytest
import time


class TestSearch:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)   #添加严重级别
    @pytest.mark.parametrize("args", ["hello1", "xiaoming"])    #参数化
    def test_search(self, args):
        self.page.setting.click_search()
        self.page.search.input_key_word(args)
        time.sleep(3)
        self.page.search.click_back()

    def teardown(self):
        time.sleep(3)
        self.driver.quit()
