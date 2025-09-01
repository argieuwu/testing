from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

options = Options()
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=options)
driver.get('')

wait = WebDriverWait(driver, 10)

# REGISTER SIDE
driver.find_element(By.LINK_TEXT, 'Register').click()
username = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[2]/form/div[2]/input')))
username.send_keys('argieuwu')

driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/form/div[3]/input').send_keys('argiepard@gmail.com')
driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/form/div[4]/input').send_keys('argie123')
driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/form/div[5]/input').send_keys('argie123')

driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
wait.until(EC.presence_of_element_located((By.LINK_TEXT, 'Login')))
driver.find_element(By.LINK_TEXT, 'Login').click()

# LOGIN SIDE
driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/form/div[1]/input').send_keys('argiepard@gmail.com')
driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/form/div[2]/input').send_keys('argie123')
driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

# Assert Login Success (check URL or Overview text)
wait.until(EC.url_contains("/overview"))
assert "overview" in driver.current_url, "Login failed, not redirected to overview"

# OVERVIEW PAGE DROPDOWNS
def select_dropdown(value, label):
    dropdown = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "_selectInput_vsfh7_28")))
    dropdown.click()
    option = wait.until(EC.element_to_be_clickable((By.XPATH, f"//option[@value='{value}'] | //li[normalize-space()='{label}']")))
    option.click()
    time.sleep(2)
    print(f" Selected {label}")

select_dropdown("thisWeek", "This Week")
select_dropdown("thisMonth", "This Month")
select_dropdown("thisQuarter", "This Quarter")

driver.execute_script("window.scrollBy(500, document.body.scrollHeight);")
print(driver.execute_script("return document.body.scrollHeight;"))

# NAVIGATE TO MAP
driver.find_element(By.XPATH, '//*[@id="root"]/div/div/aside/div[1]/ul/li[2]/a').click()
wait.until(EC.url_contains("/map"))
assert "map" in driver.current_url, "Failed to navigate to Map page"
print(" Navigated to Map Page")

# MAP PAGE DATE RANGE
dropdown = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "_selectInput_1uazd_45")))
dropdown.click()
option = wait.until(EC.element_to_be_clickable((By.XPATH, "//option[@value='quarter'] | //li[normalize-space()='This Quarter']")))
option.click()
time.sleep(2)

driver.execute_script("window.scrollBy(500, document.body.scrollHeight);")
print(driver.execute_script("return document.body.scrollHeight;"))
print(" Map filter set to This Quarter")

# setting page

print("Test Flow Completed Successfully!")

