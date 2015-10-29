import time
from functional_tests.base import FunctionalTest 

class AuthenticationTest(FunctionalTest):
	fixtures = ['data_small.json', 'users.json']

	def test_user_can_login_and_logout(self):
		#Clayton is looking for dirty photos, specifically the 'private collection'
		self.browser.get(self.live_server_url)

		#He clicks the 'Log in' link which takes him to the login form
		login_link = self.browser.find_element_by_id('login')
		login_link.click()
		time.sleep(.5) 

		#He enters his username and password and clicks the 'Log in' submission button
		self.browser.find_element_by_id('id_username').send_keys('test_user')
		self.browser.find_element_by_id('id_password').send_keys('test_password')
		login_button = self.browser.find_element_by_id('submit')
		login_button.click()
		time.sleep(.5) 

		#He is redirected back to the homepage but now sees his username
		#and Log out button in the header. The login button is no longer present 
		header_text = self.browser.find_element_by_tag_name('header').text 
		self.assertIn('test_user', header_text)
		self.assertIn('Logout', header_text)
		self.assertNotIn('Login', header_text)

		#Clayton has looked at enough dirty pictures, so he clicks the 'Log out' button
		logout_link = self.browser.find_element_by_id('logout')
		logout_link.click()
		time.sleep(.5)

		#The homepage reloads and he can no longer see his username
		#or Log out in the header. The login button is again present 
		header_text = self.browser.find_element_by_tag_name('header').text 
		self.assertNotIn('test_user', header_text)
		self.assertNotIn('Logout', header_text)
		self.assertIn('Login', header_text)

		self.fail('Finish the auth test!')