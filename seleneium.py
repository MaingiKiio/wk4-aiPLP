# Task 2: Automated Testing with AI
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Setup
driver = webdriver.Chrome()
driver.maximize_window()

# Target login page
url = "https://practicetestautomation.com/practice-test-login/"
driver.get(url)

# Function to test login
def test_login(username, password):
    driver.find_element(By.ID, "username").clear()
    driver.find_element(By.ID, "username").send_keys(username)

    driver.find_element(By.ID, "password").clear()
    driver.find_element(By.ID, "password").send_keys(password)

    driver.find_element(By.ID, "submit").click()
    time.sleep(2)

# Test with valid credentials
test_login("student", "Password123")
if "Logged In Successfully" in driver.page_source:
    print("✅ Valid Login Test Passed")
else:
    print("❌ Valid Login Test Failed")

driver.back()
time.sleep(2)

# Test with invalid credentials
test_login("student", "WrongPassword")
if "Your password is invalid!" in driver.page_source:
    print("✅ Invalid Login Test Passed")
else:
    print("❌ Invalid Login Test Failed")

# Capture screenshot
driver.save_screenshot("login_test_results.png")
driver.quit()
