# coding = utf - 8
from selenium import webdriver
from time import sleep
# 删除十条作品
def sczp():
        driver = webdriver.Chrome()
        url='https://learn.dev.longan.eliteu.xyz/manage/project/'
        driver.get(url)
        driver.maximize_window()
        driver.find_element_by_xpath('//*[@id="normal_login_username"]').send_keys('abc')
        sleep(1)
        driver.find_element_by_xpath('//*[@id="normal_login_password"]').send_keys('123456')
        sleep(1)
        driver.find_element_by_xpath('//*[@id="normal_login"]/div[4]/div/div/div/button').click()
        sleep(2)
        driver.find_element_by_xpath('//*[@id="manageProject"]/div[1]/section/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[4]/div/button[2]').click()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="manageProject"]/div[2]/div[2]/div/div[2]/div/div[2]/button[2]').click()
        sleep(1)
        driver.refresh()
        sleep(3)
        driver.find_element_by_xpath(
                '//*[@id="manageProject"]/div[1]/section/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[4]/div/button[2]').click()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="manageProject"]/div[2]/div[2]/div/div[2]/div/div[2]/button[2]').click()
        sleep(1)
        driver.refresh()
        sleep(3)
        driver.find_element_by_xpath('//*[@id="manageProject"]/div[1]/section/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[4]/div/button[2]').click()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="manageProject"]/div[2]/div[2]/div/div[2]/div/div[2]/button[2]').click()
        sleep(1)
        driver.refresh()
        sleep(3)
        driver.find_element_by_xpath(
                '//*[@id="manageProject"]/div[1]/section/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[4]/div/button[2]').click()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="manageProject"]/div[2]/div[2]/div/div[2]/div/div[2]/button[2]').click()
        sleep(1)
        driver.refresh()
        sleep(3)
        driver.find_element_by_xpath(
                '//*[@id="manageProject"]/div[1]/section/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[4]/div/button[2]').click()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="manageProject"]/div[2]/div[2]/div/div[2]/div/div[2]/button[2]').click()
        sleep(1)
        driver.refresh()
        sleep(3)
        driver.find_element_by_xpath(
                '//*[@id="manageProject"]/div[1]/section/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[4]/div/button[2]').click()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="manageProject"]/div[2]/div[2]/div/div[2]/div/div[2]/button[2]').click()
        sleep(1)
        driver.refresh()
        sleep(3)
        driver.find_element_by_xpath(
                '//*[@id="manageProject"]/div[1]/section/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[4]/div/button[2]').click()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="manageProject"]/div[2]/div[2]/div/div[2]/div/div[2]/button[2]').click()
        sleep(1)
        driver.refresh()
        sleep(3)
        driver.find_element_by_xpath(
                '//*[@id="manageProject"]/div[1]/section/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[4]/div/button[2]').click()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="manageProject"]/div[2]/div[2]/div/div[2]/div/div[2]/button[2]').click()
        sleep(1)
        driver.refresh()
        sleep(3)
        driver.find_element_by_xpath(
                '//*[@id="manageProject"]/div[1]/section/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[4]/div/button[2]').click()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="manageProject"]/div[2]/div[2]/div/div[2]/div/div[2]/button[2]').click()
        sleep(1)
        driver.refresh()
        sleep(3)
        driver.find_element_by_xpath(
                '//*[@id="manageProject"]/div[1]/section/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[4]/div/button[2]').click()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="manageProject"]/div[2]/div[2]/div/div[2]/div/div[2]/button[2]').click()
        sleep(1)
        driver.refresh()
        sleep(3)
        driver.quit()