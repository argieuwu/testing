
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

# --------------Login input credentials---------------------------------------------
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

# ----------------User Page-----------------------------------------------------------
# -----------------------------------------------------------------------------------------
user = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Users')))
user.click()
print(' ✔ Navigating to Users page')
time.sleep(2)
assert user.is_displayed(), "❌ Users page did not load"

adminTab = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="radix-_r_0_-trigger-admins"]')))
adminTab.click()
time.sleep(2)
# -----------------------ADD NEW ADMIN------------------------------------------------------------
addAdmin = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="radix-_r_0_-content-admins"]/div[1]/button')))
addAdmin.click()

adminEmail = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="admin-email"]')))
adminEmail.send_keys('testing1BaA2@gmail.com')
adminUsername = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="admin-username"]')))
adminUsername.send_keys('testing12345')
adminPassword = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="admin-password"]')))
adminPassword.send_keys('admin123')
addAdminButton = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="radix-_r_6_"]/form/div[5]/button[1]')))
addAdminButton.click()
time.sleep(5)
print(' ✔ Create admin acct successfully')



# ------------------------Booking Page------------------------------------------------------
# -----------------------------------------------------------------------------------------
bookings = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Bookings')))
bookings.click()
print(' ✔ Navigating to Booking page')
time.sleep(3)
assert bookings.is_displayed(), '❌ Booking page did not load'


# -------------------------Filter Status Button--------------------------------------------------
allStatusButton = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[2]/main/div/div/div[2]/div[1]/select')))
allStatusButton.click()

select = Select(allStatusButton)

select.select_by_value('all')
print(" --- ☆ Selected: All Status")
time.sleep(1)

select.select_by_value("pending")
print(" --- ☆ Selected: Pending")
time.sleep(1)

select.select_by_value("rescheduled")
print(" --- ☆ Selected: Rescheduled")
time.sleep(1)

select.select_by_value("confirmed")
print(" --- ☆ Selected: Confirmed")
time.sleep(1)

select.select_by_value("cancelled")
print(" --- ☆ Selected: Cancelled")
time.sleep(1)

select.select_by_value("completed")
print(" --- ☆ Selected: Completed")
time.sleep(1)

select.select_by_value('all')
print(" --- ☆ Selected: All Status")
time.sleep(1)


# -------------------------Accepting Bookings---------------------------------------------
# -----------------------------------------------------------------------------------------
acceptBooking = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[2]/main/div/div/div[2]/div[2]/table/tbody/tr[1]/td[7]/div/button[1]')))
acceptBooking.click()
assert acceptBooking.is_displayed(), '❌ Accept button not click'


responseMessage = driver.find_element(By.XPATH, '//textarea[@placeholder="Enter your response message..."]')
responseMessage.send_keys('tessssssssssssssssssssssssssst')

assert responseMessage.is_displayed(), '❌  Message not working'
time.sleep(3)


confirmBooking = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.bg-green-600')))
confirmBooking.click()
print("✔ Confirm Booking clicked")
time.sleep(3)

conflict_buttons = driver.find_elements(By.XPATH, '//*[@id="radix-_r_f_"]/div[3]/button')
if conflict_buttons:
    conflict_buttons[0].click()
    print("✔ Resolve Booking Conflict clicked")
    time.sleep(2)
else:
    print("ℹ No conflict dialog appeared, continuing...")

# -------------------------History Bookings---------------------------------------------
wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "div[data-state='open']")))

historyButton = wait.until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, "button:has(svg.lucide-history)")
))
historyButton.click()
print("✔ History button clicked")
time.sleep(4)



dialog = wait.until(EC.visibility_of_element_located(
    (By.CSS_SELECTOR, "div[data-state='open']"))
)


closeButton = wait.until(EC.element_to_be_clickable((
    By.CSS_SELECTOR, "div[data-state='open'] button:has(svg.lucide-x)"
)))

try:
    closeButton.click()
    print('✔ History dialog closed')
except:
    driver.execute_script(driver.execute_script("arguments[0].click();", closeButton))
    print('✔ History dialog closed')

wait.until(EC.invisibility_of_element_located(
    (By.CSS_SELECTOR, "div[data-state='open']"))
)
time.sleep(2)

# ------------------------------Program Page--------------------------
# -----------------------------------------------------------------------------------------
programs = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Programs')))
programs.click()
print(' ✔ Navigating to Programs page')
time.sleep(3)

dietSection = wait.until(EC.presence_of_element_located(
    (By.XPATH, "//button[contains(normalize-space(.), 'Diet')]")))
driver.execute_script("arguments[0].scrollIntoView(true);", dietSection)
wait.until(EC.element_to_be_clickable(dietSection)).click()
print(" --- ☆ Selected diet section")
time.sleep(2)




# ------------------------------Resources Page-------------------------
# -----------------------------------------------------------------------------------------
resources = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Resources')))
resources.click()
print(' ✔ Navigating to Resources page')
time.sleep(3)

# Click Testimonials button
testimonialsButton = wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//button[.//span[text()='Testimonials']] | //button[contains(., 'Testimonials')]")))
testimonialsButton.click()
print("✔ Testimonials button clicked")
time.sleep(2)

# Click Others button
othersButton = wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//button[.//span[text()='Others']] | //button[contains(., 'Others')]")))
othersButton.click()
print("✔ Others button clicked")
time.sleep(2)


# ------------------------------Chat Support Page-------------------------
# -----------------------------------------------------------------------------------------
chatSupport = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/chat']")))
chatSupport.click()
print(' ✔ Navigating to Chat Support page')
time.sleep(2)

# click the latest user who chat
targetFirstMessage = wait.until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, "div.cursor-pointer.p-3")))
targetFirstMessage.click()

time.sleep(1)

# TEST MESSAGE
chatInput = wait.until(EC.presence_of_element_located(
    (By.CSS_SELECTOR, "input[placeholder='Type your message...']")))
chatInput.send_keys("test message ra ta ra ta ra ta ra ta ra ta ra ta ra ta")
print("✔ Message typed into chat")
time.sleep(1)

# send button
sendButton = wait.until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, "button[data-slot='button'][type='submit']")))
sendButton.click()
print("✔ Message sent")
time.sleep(2)

# ------------------------------Settings Page--------------------------
# -----------------------------------------------------------------------------------------
settings = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Settings')))
settings.click()
print(' ✔ Navigating to Settings page')
time.sleep(2)

dashboard = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Dashboard')))
dashboard.click()
print(' ✔ Navigating to Dashboard page')
time.sleep(2)


print("────── ★⋆☆⋆★ ──── ✨ SUMAKSIS! ✨──── ★⋆☆⋆★ ──────")