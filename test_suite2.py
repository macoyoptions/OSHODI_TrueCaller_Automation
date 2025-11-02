import time
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from LoginPageTest.LoginPage import LoginPage

capabilities = {
    "platformName": "Android",
    "deviceName": "R5CRB32M98N",
    "automationName": "uiautomator2",
    "platformVersion": "15",
    "appPackage": "com.truecaller",
    "appActivity": "com.truecaller.ui.TruecallerInit",
    "noReset": True
}

appium_server_url = "http://127.0.0.1:4723/wd/hub"


@pytest.fixture(scope="function")
def driver():
    options = UiAutomator2Options().load_capabilities(capabilities)
    driver = webdriver.Remote(appium_server_url, options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


# LOGIN FLOW
def test_login_page_for_truecaller(driver):
    login = LoginPage(driver)
    login.get_started_button()
    login.click_truecaller_button()
    login.set_truecaller_as_default_caller_button()
    login.click_continue_button()
    login.click_allow_truecaller_to_access_call_button()
    login.click_allow_truecaller_to_access_contact_button()
    login.click_allow_truecaller_to_make_phone_calls_button()
    login.click_allow_truecaller_to_send_messages_button()
    login.set_truecaller_button()
    login.set_truecaller_as_default_sms_button()
    login.click_choose_your_number_button()
    login.continue_for_ads_button()
    login.close_premium_button()
    login.consent_button()
