
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
import time

options = Options()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options = options)
driver.get('https://admin--mobile-app.vercel.app/login')

wait = WebDriverWait(driver, 10)

# --------------Login input credentials-----------------------
emailInput = driver.find_element(By.ID, 'email')
emailInput.send_keys('fortest3960@gmail.com')
passwordInput = driver.find_element(By.ID, 'password')
passwordInput.send_keys('admin123')

loginButton = driver.find_element(By.CSS_SELECTOR, 'button[data-slot="button"]')
loginButton.click()
print(' ✔ Login success')


# dashboard = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Dashboard')))
# dashboard.click()
# print('Navigating to Dashboard page')
# time.sleep(3)

# ----------------User Page-------------------------------------
user = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Users')))
user.click()
print(' ✔ Navigating to Users page')
time.sleep(3)
assert user.is_displayed(), "❌ Users page did not load"

adminTab = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="radix-_r_0_-trigger-admins"]')))
adminTab.click()
time.sleep(3)
# -----------------------ADD NEW ADMIN-------------------------
addAdmin = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="radix-_r_0_-content-admins"]/div[1]/button')))
addAdmin.click()

adminEmail = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="admin-email"]')))
adminEmail.send_keys('testing12345@gmail.com')
adminUsername = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="admin-username"]')))
adminUsername.send_keys('testing12345')
adminPassword = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="admin-password"]')))
adminPassword.send_keys('admin123')
addAdminButton = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="radix-_r_6_"]/form/div[5]/button[1]')))
addAdminButton.click()
print(' ✔ Create admin acct successfully')
time.sleep(5)


# ------------------------Booking Page------------------------------
bookings = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Bookings')))
bookings.click()
print(' ✔ Navigating to Booking page')
time.sleep(3)
assert bookings.is_displayed(), '❌ Booking page did not load'

# -------------------------Filter Status Button--------------------------
allStatusButton = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[2]/main/div/div/div[2]/div[1]/select')))
allStatusButton.click()

select = Select(allStatusButton)

select.select_by_value('all')
print(" ☆ Selected: All Status")
time.sleep(3)

select.select_by_value("pending")
print(" ☆ Selected: Pending")
time.sleep(3)

select.select_by_value("rescheduled")
print(" ☆ Selected: Rescheduled")
time.sleep(3)

select.select_by_value("confirmed")
print(" ☆ Selected: Confirmed")
time.sleep(3)

select.select_by_value("cancelled")
print(" ☆ Selected: Cancelled")
time.sleep(3)

select.select_by_value("completed")
print(" ☆ Selected: Completed")
time.sleep(3)

select.select_by_value('all')
print(" ☆ Selected: All Status")
time.sleep(3)

# ------------------------------Program Page--------------------------
programs = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Programs')))
programs.click()
print(' ✔ Navigating to Programs page')
time.sleep(3)

# ------------------------------Resources Page-------------------------
resources = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Resources')))
resources.click()
print(' ✔ Navigating to Resources page')
time.sleep(3)

# ------------------------------Chat Support Page-------------------------
chatSupport = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Chat Support')))
chatSupport.click()
print(' ✔ Navigating to Chat Support page')
time.sleep(3)

# ------------------------------Settings Page--------------------------
settings = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Settings')))
settings.click()
print(' ✔ Navigating to Settings page')
time.sleep(3)

dashboard = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Dashboard')))
dashboard.click()
print(' ✔ Navigating to Dashboard page')
time.sleep(3)


print("────── ★⋆☆⋆★ ──── ✨ SUMAKSIS! ✨──── ★⋆☆⋆★ ──────")