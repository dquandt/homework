import unittest
from selenium import webdriver

class HomepageTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def test_homepage_layout(self):
		#Clayton opens his browser and goes to the photo album homepage 
		self.browser.get('http://localhost:8000')

		#He sees a link called "The Private Album"
		links = self.browser.find_element_by_css_selector('li.link a')
		self.assertEqual(len(links), 5)

if __name__ == '__main__':
	unittest.main(warnings='ignore')


