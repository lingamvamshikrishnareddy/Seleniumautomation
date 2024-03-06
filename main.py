from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import random
import time
import re

# Function to generate a random mobile number
def generate_mobile_number():
    # Start with the fixed starting digit 6
    mobile_number = "6"
    # Generate 9 random digits
    for _ in range(9):
        digit = random.randint(0, 9)
        mobile_number += str(digit)
    return mobile_number

def extract_name(username):
    # Remove any non-alphabetic characters from the username
    username_alpha = re.sub(r'[^a-zA-Z]', '', username)
    # Take the first 7 characters as the first name
    first_name = username_alpha[:7]
    # Take the remaining characters as the last name
    last_name = username_alpha[7:]
    return first_name, last_name


# Function to extract username from email
def extract_username(email):
    return email.split('@')[0]

# Configure Chrome options for incognito mode
chrome_options = Options()
chrome_options.add_argument("--incognito")

# Start a Selenium WebDriver session with incognito mode
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://unstop.com/auth/signup?utm_source=Herody&utm_medium=Affiliates&utm_campaign=signup&ref=HR29")

# Wait for the page to load (You may need to wait for specific elements to be visible)


# Generate random email
email = "venugopal36832@gmail.com"#Enter Manually"

username = extract_username(email)

first_name, last_name = extract_name(username)

first_name_input = driver.find_element(By.ID, "first_name")
first_name_input.send_keys(first_name)

last_name_input = driver.find_element(By.ID, "last_name")
last_name_input.send_keys(last_name)


# Extract username from email


username_input = driver.find_element(By.ID,"username")
username_input.send_keys(username);

# Locate the email input field by class name and enter the generated email
email_input = driver.find_element(By.ID, "email_address")
email_input.send_keys(email)

# Locate the mobile number input field by class name and enter the generated mobile number
mobile_number = generate_mobile_number()
mobile_number_input = driver.find_element(By.CLASS_NAME, "mat-input-element")
mobile_number_input.send_keys(mobile_number)

# Locate the password input field and enter the password
password_input = driver.find_element(By.NAME, "password")
password_input.send_keys("Abcd@123")

# Locate the password confirmation input field and enter the same password
password_confirmation_input = driver.find_element(By.NAME, "password_confirmation")
password_confirmation_input.send_keys("Abcd@123")

# Locate the checkbox and click on it
checkbox = driver.find_element(By.CLASS_NAME, "checkbox_type")
checkbox.click()

# Wait for 10 seconds after clicking the checkbox


# Click on the next button using class name
next_button = driver.find_element(By.CLASS_NAME, "gtm_step1.waves-effect")
next_button.click()


# Wait for 90 seconds (as in your previous code)

# Fill in the first name field with the first 7 characters of the username

# Wait for 5 seconds
time.sleep(60)

# Quit the browser
driver.quit()
