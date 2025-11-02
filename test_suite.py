# import time
# import pytest
# from appium import webdriver
# from appium.options.android import UiAutomator2Options
# from appium.options.common import AppiumOptions
# from appium.webdriver.common.appiumby import AppiumBy
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# # Desired Capabilities for Appium
# capabilities = {
#     "platformName": "Android",
#     "deviceName": "R5CRB32M98N",  # Ensure this matches your emulator/device name
#     "automationName": "uiautomator2",
#     "platformVersion": "15",  # Update to match your device/emulator version
#     "app": "com.truecaller",  # Path to your app
#     "appWaitActivity": "ui.TruecallerInit",
#     "uiautomator2ServerInstallTimeout": 6000,
#
# }
#
# appium_server_url = 'http://localhost:4723/wd/hub'  # Appium server URL
#
#
# @pytest.fixture(scope="function")
# def driver():
#     options = UiAutomator2Options()
#     options.load_capabilities(capabilities)  # DO NOT use inline call
#
#     driver = webdriver.Remote(appium_server_url, options=options.load_capabilities(capabilities))
#     driver.implicitly_wait(10)
#
#     yield driver  # Test runs here
#     time.sleep(2)
#     # driver.quit()

#
# def Test_Get_Started_Button(driver):
#     # Step 1: Open the app and click the login button
#     select_login_button = WebDriverWait(driver, 20).until(
#         EC.presence_of_element_located((AppiumBy.ID, 'com.truecaller:id/nextButton')))
#     select_login_button.click()

# # Step 2: Enter username
# enter_username_field = WebDriverWait(driver, 20).until(
#     EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "input-email")))
# enter_username_field.send_keys("chinyere@gmail.com")
#
# # Step 3: Enter password
# enter_password_field = WebDriverWait(driver, 20).until(
#     EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'input-password')))
# enter_password_field.send_keys("adeola93@")
#
# # Step 4: Click the login button
# login_button = WebDriverWait(driver, 20).until(
#     EC.presence_of_element_located((AppiumBy.XPATH, '//android.view.ViewGroup['
#                                                     '@content-desc="button-LOGIN"]/android.view.ViewGroup')))
# login_button.click()

# import time
# import pytest
# from appium import webdriver
# from appium.options.android import UiAutomator2Options
# from appium.webdriver.common.appiumby import AppiumBy
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
# from TrueCallerLocators.LoginLocator import LoginLocators
#
# capabilities = {
#     "platformName": "Android",
#     "deviceName": "R5CRB32M98N",
#     "automationName": "uiautomator2",
#     "platformVersion": "15",
#     "appPackage": "com.truecaller",
#     "appActivity": "com.truecaller.ui.TruecallerInit",
#     "noReset": True
# }
#
# appium_server_url = "http://127.0.0.1:4723/wd/hub"
#
#
# @pytest.fixture(scope="function")
# def driver():
#     options = UiAutomator2Options().load_capabilities(capabilities)
#     driver = webdriver.Remote(appium_server_url, options=options)
#     driver.implicitly_wait(10)
#     yield driver
#     driver.quit()
#
#
# def test_get_started_button(self):
#     get_started_btn = WebDriverWait(self.driver, 10).until(
#         EC.presence_of_element_located(LoginLocators.click_get_started_button))
#     get_started_btn.click()
#
#
# def test_set_truecaller_as_default_caller_button(driver):
#     set_truecaller_as_default_caller = driver.find_element(LoginLocators.click_set_truecaller_as_default_caller)
#     set_truecaller_as_default_caller.click()
#     time.sleep(5)
#
#
# def test_click_truecaller_button(driver):
#     click_truecaller_as_option = driver.find_element(LoginLocators.click_truecaller_as_option)
#     click_truecaller_as_option.click()
#     time.sleep(5)
#
#
# def test_click_continue_button(driver):
#     click_continue_button = driver.find_element(LoginLocators.click_continue_button)
#     click_continue_button.click()
#     time.sleep(5)
#
#
# def test_click_allow_truecaller_to_access_call_button(driver):
#     click_allow_truecaller_to_access_call_button = driver.find_element(LoginLocators.click_allow_truecaller_to_access_call_button)
#     click_allow_truecaller_to_access_call_button.click()
#     time.sleep(5)
#
#
# def test_click_allow_truecaller_to_access_contact_button(driver):
#     click_allow_truecaller_to_access_contact_button = driver.find_element(LoginLocators.click_allow_truecaller_to_access_contact_button)
#     click_allow_truecaller_to_access_contact_button.click()
#     time.sleep(5)
#
#
# def test_click_allow_truecaller_to_make_phone_calls_button(driver):
#     allow_truecaller_to_make_phone_calls_button = driver.find_element(LoginLocators.click_allow_truecaller_to_make_phone_calls_button)
#     allow_truecaller_to_make_phone_calls_button.click()
#     time.sleep(5)
#
#
# def test_click_allow_truecaller_to_make_messages_button(driver):
#     get_started_btn = driver.find_element(LoginLocators.click_allow_truecaller_to_make_messages_button)
#     get_started_btn.click()
#     time.sleep(5)
#
#
# def test_click_choose_your_number_button(driver):
#     get_started_btn = driver.find_element(LoginLocators.click_choose_your_number_button)
#     get_started_btn.click()
#     time.sleep(5)
#
#
# def test_click_continue_for_ads_button(driver):
#     get_started_btn = driver.find_element(AppiumBy.ID, "com.truecaller:id/nextButton")
#     get_started_btn.click()
#     time.sleep(5)
#
#
# def test_click_close_premium_button(driver):
#     click_close_premium_button = driver.find_element(LoginLocators.click_close_premium_button)
#     click_close_premium_button.click()
#     time.sleep(5)
#
#
# def test_click_consent_button(driver):
#     click_consent_button = driver.find_element(LoginLocators.click_consent_button)
#     click_consent_button.click()
#     time.sleep(5)
