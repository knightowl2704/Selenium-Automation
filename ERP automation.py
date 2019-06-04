from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

print("Enter the roll number :")
roll = str(input())
print("Enter the YYYY :")
year = str(input())
driver = webdriver.Chrome()
driver.get("http://14.139.195.241/Result/login.php")
for j in range(1,13):
    for i in range(1, 32):
        Roll_No = driver.find_element_by_xpath(
            "/html/body/div[1]/div[2]/div/section/div/form/table/tbody/tr[1]/td[2]/input")
        Roll_No.send_keys(str(roll))
        DOB = driver.find_element_by_xpath(
            "/html/body/div[1]/div[2]/div/section/div/form/table/tbody/tr[2]/td[2]/input")
        DOB.send_keys(str(year)+"-"+ str(j)+ "-" + str(i))
        wait = WebDriverWait(driver, 10)
        submit = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/section/div/form/input")
        submit.click()
    pass
pass



