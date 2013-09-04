import unittest
from selenium import webdriver
from django.core.urlresolvers import reverse

class HomePageTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def test_frontpage(self):
		self.browser.get('http://localhost:8000/')
		#from IPython import embed
		#embed()
		title = self.browser.content
		self.assertEqual(title, True)

if __name__ == '__main__':
		unittest.main()