from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

# -------------------------------------INPUT AREA------------------------------------------- #

# Get the value of the shop.app _pay_session cookie here
SHOPAPP_USER_COOKIE = ""

# Put the value of the cookie from millies pottery after you login here
MILLIES_SECURE_SESSION_ID = ""

# Put the link to the product you want to buy in here
LINK_TO_PRODUCT = ""

# -------------------------------------INPUT AREA------------------------------------------- #

# Create the driver
driver = webdriver.Firefox()
wait = WebDriverWait(driver, 10)

# Load the shop.app website and add the cookie
driver.get('https://shop.app/')
driver.add_cookie({
    "name": "user",
    "value": SHOPAPP_USER_COOKIE,
    "domain": "shop.app",
    "secure": True,
    "httpOnly": True,
    "sameSite": "Lax"
})

# Load the user account
driver.get('https://milliespottery.com')
driver.add_cookie({
    "name": "_secure_session_id",
    "value": MILLIES_SECURE_SESSION_ID,
    "domain": "milliespottery.com",
    "secure": True,
    "httpOnly": True,
    "sameSite": "Lax"
})

# Make it redirect to shopify
driver.delete_cookie("shopify_pay_redirect")
driver.add_cookie({
    "name": "shopify_pay_redirect",
    "value": "true",
    "domain": "milliespottery.com",
    "secure": False,
    "httpOnly": False,
})

# Go to the product page
driver.get(LINK_TO_PRODUCT)

# Click add to cart
while True:
    if wait.until(EC.presence_of_element_located((By.NAME, "add"))).get_property("disabled"):
        driver.refresh()
    else:
        break


# Click Checkout
wait.until(EC.presence_of_element_located((By.NAME, "add"))).click()
time.sleep(0.5)
wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/cart-notification/div/div/div[3]/form/button"))).click()

# Click on Pay now (DELETE # WHEN YOU WANT THE BOT TO ACTUALLY BUY)
wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/section/div[1]/div[2]/div[3]/div/button"))).click()
