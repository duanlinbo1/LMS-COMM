# coding = utf - 8
from selenium import webdriver
from time import sleep
# 团队添加作品集
def tjzpj():
    driver = webdriver.Chrome()
    driver.get('https://learn.dev.longan.eliteu.xyz/manage/team/')
    driver.maximize_window()
    sleep(1)
    driver.find_element_by_xpath('//*[@id="normal_login_username"]').send_keys('abc')
    sleep(1)
    driver.find_element_by_xpath('//*[@id="normal_login_password"]').send_keys('123456')
    sleep(1)
    driver.find_element_by_xpath('//*[@id="normal_login"]/div[4]/div/div/div/button').click()
    sleep(2)
    driver.find_element_by_xpath(
        '//*[@id="team"]/div[1]/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[2]/button').click()
    sleep(2)
    driver.find_element_by_xpath('//*[@id="name"]').send_keys("自动化添加作品集0")
    sleep(1)
    driver.find_element_by_xpath(
        '//*[@id="portfolio"]/div[2]/div[2]/div/div[2]/div[1]/div[3]/form/div[3]/div[2]/div/div/div/div').click()
    sleep(1)
    driver.find_element_by_xpath('//*[@id="team"]').click()
    sleep(1)
    driver.find_element_by_xpath('//*[@id="portfolio"]/div[2]/div[2]/div/div[2]/div[2]/div/button[2]').click()
    sleep(2)
    driver.back()
    sleep(1)
    driver.refresh()
    sleep(2)
    driver.find_element_by_xpath(
        '//*[@id="team"]/div[1]/div[2]/div/div/div/div/div/div/table/tbody/tr[2]/td[2]/button').click()
    sleep(2)
    driver.find_element_by_xpath('//*[@id="name"]').send_keys("自动化添加作品集1")
    sleep(1)
    driver.find_element_by_xpath(
        '//*[@id="portfolio"]/div[2]/div[2]/div/div[2]/div[1]/div[3]/form/div[3]/div[2]/div/div/div/div').click()
    sleep(1)
    driver.find_element_by_xpath('//*[@id="team"]').click()
    sleep(1)
    driver.find_element_by_xpath('//*[@id="portfolio"]/div[2]/div[2]/div/div[2]/div[2]/div/button[2]').click()
    sleep(2)
    driver.back()
    sleep(1)
    driver.refresh()
    sleep(2)
    driver.find_element_by_xpath(
        '//*[@id="team"]/div[1]/div[2]/div/div/div/div/div/div/table/tbody/tr[3]/td[2]/button').click()
    sleep(2)
    driver.find_element_by_xpath('//*[@id="name"]').send_keys("自动化添加作品集2")
    sleep(1)
    driver.find_element_by_xpath(
        '//*[@id="portfolio"]/div[2]/div[2]/div/div[2]/div[1]/div[3]/form/div[3]/div[2]/div/div/div/div').click()
    sleep(1)
    driver.find_element_by_xpath('//*[@id="team"]').click()
    sleep(1)
    driver.find_element_by_xpath('//*[@id="portfolio"]/div[2]/div[2]/div/div[2]/div[2]/div/button[2]').click()
    sleep(2)
    driver.back()
    sleep(1)
    driver.refresh()
    sleep(2)
    driver.find_element_by_xpath(
        '//*[@id="team"]/div[1]/div[2]/div/div/div/div/div/div/table/tbody/tr[4]/td[2]/button').click()
    sleep(2)
    driver.find_element_by_xpath('//*[@id="name"]').send_keys("自动化添加作品集3")
    sleep(1)
    driver.find_element_by_xpath(
        '//*[@id="portfolio"]/div[2]/div[2]/div/div[2]/div[1]/div[3]/form/div[3]/div[2]/div/div/div/div').click()
    sleep(1)
    driver.find_element_by_xpath('//*[@id="team"]').click()
    sleep(1)
    driver.find_element_by_xpath('//*[@id="portfolio"]/div[2]/div[2]/div/div[2]/div[2]/div/button[2]').click()
    sleep(2)
    driver.back()
    sleep(1)
    driver.refresh()
    sleep(2)
    driver.find_element_by_xpath(
        '//*[@id="team"]/div[1]/div[2]/div/div/div/div/div/div/table/tbody/tr[5]/td[2]/button').click()
    sleep(2)
    driver.find_element_by_xpath('//*[@id="name"]').send_keys("自动化添加作品集4")
    sleep(1)
    driver.find_element_by_xpath(
        '//*[@id="portfolio"]/div[2]/div[2]/div/div[2]/div[1]/div[3]/form/div[3]/div[2]/div/div/div/div').click()
    sleep(1)
    driver.find_element_by_xpath('//*[@id="team"]').click()
    sleep(1)
    driver.find_element_by_xpath('//*[@id="portfolio"]/div[2]/div[2]/div/div[2]/div[2]/div/button[2]').click()
    sleep(2)
    driver.back()
    sleep(1)
    driver.refresh()
    sleep(2)
    driver.find_element_by_xpath(
        '//*[@id="team"]/div[1]/div[2]/div/div/div/div/div/div/table/tbody/tr[6]/td[2]/button').click()
    sleep(2)
    driver.find_element_by_xpath('//*[@id="name"]').send_keys("自动化添加作品集5")
    sleep(1)
    driver.find_element_by_xpath(
        '//*[@id="portfolio"]/div[2]/div[2]/div/div[2]/div[1]/div[3]/form/div[3]/div[2]/div/div/div/div').click()
    sleep(1)
    driver.find_element_by_xpath('//*[@id="team"]').click()
    sleep(1)
    driver.find_element_by_xpath('//*[@id="portfolio"]/div[2]/div[2]/div/div[2]/div[2]/div/button[2]').click()
    sleep(2)
    driver.back()
    sleep(1)
    driver.refresh()
    sleep(2)
    driver.find_element_by_xpath(
        '//*[@id="team"]/div[1]/div[2]/div/div/div/div/div/div/table/tbody/tr[7]/td[2]/button').click()
    sleep(2)
    driver.find_element_by_xpath('//*[@id="name"]').send_keys("自动化添加作品集6")
    sleep(1)
    driver.find_element_by_xpath(
        '//*[@id="portfolio"]/div[2]/div[2]/div/div[2]/div[1]/div[3]/form/div[3]/div[2]/div/div/div/div').click()
    sleep(1)
    driver.find_element_by_xpath('//*[@id="team"]').click()
    sleep(1)
    driver.find_element_by_xpath('//*[@id="portfolio"]/div[2]/div[2]/div/div[2]/div[2]/div/button[2]').click()
    sleep(2)
    driver.back()
    sleep(1)
    driver.refresh()
    sleep(2)
    driver.find_element_by_xpath(
        '//*[@id="team"]/div[1]/div[2]/div/div/div/div/div/div/table/tbody/tr[8]/td[2]/button').click()
    sleep(2)
    driver.find_element_by_xpath('//*[@id="name"]').send_keys("自动化添加作品集7")
    sleep(1)
    driver.find_element_by_xpath(
        '//*[@id="portfolio"]/div[2]/div[2]/div/div[2]/div[1]/div[3]/form/div[3]/div[2]/div/div/div/div').click()
    sleep(1)
    driver.find_element_by_xpath('//*[@id="team"]').click()
    sleep(1)
    driver.find_element_by_xpath('//*[@id="portfolio"]/div[2]/div[2]/div/div[2]/div[2]/div/button[2]').click()
    sleep(2)
    driver.back()
    sleep(1)
    driver.refresh()
    sleep(2)
    driver.find_element_by_xpath('//*[@id="team"]/div[1]/div[2]/div/div/div/ul/li[4]/a').click()
    sleep(2)
    driver.find_element_by_xpath(
        '//*[@id="team"]/div[1]/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[2]/button').click()
    sleep(2)
    driver.find_element_by_xpath('//*[@id="name"]').send_keys("自动化添加作品集8")
    sleep(1)
    driver.find_element_by_xpath(
        '//*[@id="portfolio"]/div[2]/div[2]/div/div[2]/div[1]/div[3]/form/div[3]/div[2]/div/div/div/div').click()
    sleep(1)
    driver.find_element_by_xpath('//*[@id="team"]').click()
    sleep(1)
    driver.find_element_by_xpath('//*[@id="portfolio"]/div[2]/div[2]/div/div[2]/div[2]/div/button[2]').click()
    sleep(2)
    driver.back()
    sleep(1)
    driver.refresh()
    sleep(2)
    driver.find_element_by_xpath(
        '//*[@id="team"]/div[1]/div[2]/div/div/div/div/div/div/table/tbody/tr[2]/td[2]/button').click()
    sleep(2)
    driver.find_element_by_xpath('//*[@id="name"]').send_keys("自动化添加作品集9")
    sleep(1)
    driver.find_element_by_xpath(
        '//*[@id="portfolio"]/div[2]/div[2]/div/div[2]/div[1]/div[3]/form/div[3]/div[2]/div/div/div/div').click()
    sleep(1)
    driver.find_element_by_xpath('//*[@id="team"]').click()
    sleep(1)
    driver.find_element_by_xpath('//*[@id="portfolio"]/div[2]/div[2]/div/div[2]/div[2]/div/button[2]').click()
    sleep(2)
    driver.back()
    sleep(1)
    driver.refresh()
    sleep(2)
    driver.quit()