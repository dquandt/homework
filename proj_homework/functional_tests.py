from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:8000')

page_body = browser.find_element_by_tag_name('body')

assert 'this is my album, yo' in page_body.text 

browser.quit()

