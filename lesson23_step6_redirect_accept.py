from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(x))))

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/redirect_accept.html')

try:
    button1 = browser.find_element_by_tag_name('button')
    button1.click()

    browser.switch_to.window(browser.window_handles[1])

    x_element = int(browser.find_element_by_id('input_value').text)
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(calc(x_element))

    button2 = browser.find_element_by_tag_name('button')
    button2.click()

finally:
    time.sleep(10)
    browser.quit()
