from django.test import TestCase
from selenium import webdriver
browser=webdriver.Firefox(executable_path=r'C:\Users\saeedpc\workspace\gecko\geckodriver.exe')
browser.get("http://localhost:8000")
assert browser.page_source.find('install')

# Create your tests here.
class f_test(TestCase):
    def setUp(self):
        self.browser=webdriver.Firefox(executable_path=r'C:\Users\saeedpc\workspace\gecko\geckodriver.exe')

    def test_home_page(self):
        self.browser.get("http://localhost:8000")
        self.assertIn('install',browser.page_source)


    def tearDown(self):
        self.browser.quit()


