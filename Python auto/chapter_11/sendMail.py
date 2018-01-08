from selenium import webdriver

browser = webdriver.Safari()
browser.get('https://qiye.163.com/login/?from=ym')
mailElem = browser.find_element_by_id('accname')
mailElem.send_keys('huyuan@ech-med.com')
mailElem = browser.find_element_by_id('accpwd')
mailElem.send_keys('Hy770914')
mailElem=browser.find_element_by_class_name('loginbtn')
mailElem.click()
browser.switch_to.frame('folder')
mailElem=browser.find_element_by_class_name('aXieXIN')
mailElem.click()
