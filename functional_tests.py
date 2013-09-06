import unittest
from selenium import webdriver
from django.core.urlresolvers import reverse

class HomePageTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def test_index(self):
		self.browser.get('http://localhost:8000/')
		title = self.browser.title
		for i in dir(self.browser.title):
			print i
		self.assertIn('Index', title)

	def test_login(self):
		self.browser.get('http://localhost:8000/')
		try:
			login = self.browser.find_element_by_name('username')
			password = self.browser.find_element_by_name('password')
		except:
			self.fail()
		self.assertEqual(True,False)

if __name__ == '__main__':
		unittest.main()