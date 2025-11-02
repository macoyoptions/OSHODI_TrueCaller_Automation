import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from TrueCallerLocators.LoginLocator import LoginLocators


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    # This test is conducted to validate that user
    # can successfully log in to their account when they fill in all valid information

    # CLICK ON THE "GET STARTED BUTTON"
    def get_started_button(self):
        get_started_btn = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LoginLocators.click_get_started_button))
        get_started_btn.click()
        time.sleep(5)

    # CLICK ON TRUECALLER RADIO BUTTON IN OTHER TO CHOOSE IT AS YOUR DEFAULT CALLER ID & SPAM APP
    def click_truecaller_button(self):
        click_truecaller_as_option = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LoginLocators.click_truecaller_as_option))
        click_truecaller_as_option.click()
        time.sleep(5)

    # CLICK ON "SET AS DEFAULT BUTTON"
    def set_truecaller_as_default_caller_button(self):
        set_truecaller_as_default_caller = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LoginLocators.click_set_truecaller_as_default_caller))
        set_truecaller_as_default_caller.click()
        time.sleep(5)

    # YOUR DEVICE WILL SEND PERMISSION TO ENABLE CALLER ID AND SPAM DETECTION ON IT, CLICK "CONTINUE BUTTON"
    def click_continue_button(self):
        click_continue_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LoginLocators.click_continue_button))
        click_continue_button.click()
        time.sleep(5)

    # ALLOW TRUECALLER TO ACCESS YOUR CALL LOG, "CLICK ALLOW BUTTON"
    def click_allow_truecaller_to_access_call_button(self):
        click_allow_truecaller_to_access_call_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LoginLocators.click_allow_truecaller_to_access_call_button))
        click_allow_truecaller_to_access_call_button.click()
        time.sleep(5)

    # ALLOW TRUECALLER TO ACCESS YOUR CONTACTS, "CLICK ALLOW BUTTON"
    def click_allow_truecaller_to_access_contact_button(self):
        click_allow_truecaller_to_access_contact_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LoginLocators.click_allow_truecaller_to_access_contact_button))
        click_allow_truecaller_to_access_contact_button.click()
        time.sleep(5)

    # CLICK "ALLOW BUTTON" IN OTHER FOR TRUECALLER TO MAKE AND MANAGE PHONE CALLS
    def click_allow_truecaller_to_make_phone_calls_button(self):
        allow_truecaller_to_make_phone_calls_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LoginLocators.click_allow_truecaller_to_make_phone_calls_button))
        allow_truecaller_to_make_phone_calls_button.click()
        time.sleep(5)

    # CLICK "ALLOW BUTTON" IN OTHER FOR TRUECALLER TO SEND AND VIEW SMS MESSAGES
    def click_allow_truecaller_to_send_messages_button(self):
        send_message_btn = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LoginLocators.click_allow_truecaller_to_send_messages_button))
        send_message_btn.click()
        time.sleep(5)

    # CLICK ON "TRUECALLER RADIO BUTTON" IN OTHER TO SET IT AS YOUR DEFAULT SMS APP
    def set_truecaller_button(self):
        truecaller_as_default_sms_app = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LoginLocators.click_truecaller_as_default_sms_app))
        truecaller_as_default_sms_app.click()
        time.sleep(5)

    # CLICK ON "SET AS DEFAULT BUTTON"
    def set_truecaller_as_default_sms_button(self):
        set_as_default_sms_app = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LoginLocators.click_truecaller_set_as_default))
        set_as_default_sms_app.click()
        time.sleep(5)

    # CLICK ON YOUR PHONE NUMBER THAT IS ALREADY THERE
    def click_choose_your_number_button(self):
        number_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LoginLocators.click_choose_your_number_button))
        number_button.click()
        time.sleep(5)

    # ON HOW ADS WILL APPEAR TO YOU, "CLICK CONTINUE BUTTON"
    def continue_for_ads_button(self):
        continue_for_ads_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LoginLocators.click_continue_for_ads_button))
        continue_for_ads_button.click()
        time.sleep(5)

    # CLICK ON "NOT NOW BUTTON" TO CLOSE THE MODAL FOR SUBSCRIPTION PAGE
    def close_premium_button(self):
        close_premium_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LoginLocators.click_close_premium_button))
        close_premium_button.click()
        time.sleep(5)

    # CLICK ON "CONSENT BUTTON" FOR YOU TO ACCEPT TRUECALLER TO USER YOUR PERSONAL DATA
    def consent_button(self):
        consent_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LoginLocators.click_consent_button))
        consent_button.click()
        time.sleep(5)

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
