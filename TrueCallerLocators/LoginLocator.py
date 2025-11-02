from appium.webdriver.common.appiumby import AppiumBy


class LoginLocators:
    click_get_started_button = (AppiumBy.ID, "com.truecaller:id/nextButton")
    click_truecaller_as_option = (AppiumBy.XPATH, '//android.widget.TextView[@content-desc="Truecaller"]')
    click_set_truecaller_as_default_caller = (AppiumBy.ID, "android:id/button1")
    click_continue_button = (AppiumBy.ID, "android:id/button1")
    click_allow_truecaller_to_access_call_button = (AppiumBy.XPATH,
                                                    '//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_allow_button"]')
    click_allow_truecaller_to_access_contact_button = (AppiumBy.XPATH,
                                                       '//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_allow_button"]')
    click_allow_truecaller_to_make_phone_calls_button = (AppiumBy.XPATH,
                                                         '//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_allow_button"]')
    click_allow_truecaller_to_send_messages_button = (AppiumBy.XPATH,
                                                      '//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_allow_button"]')
    click_truecaller_as_default_sms_app = (
        AppiumBy.XPATH, '//android.widget.TextView[@content-desc="Truecaller"]')
    click_truecaller_set_as_default = (AppiumBy.XPATH, '//android.widget.Button[@resource-id="android:id/button1"]')
    click_choose_your_number_button = (AppiumBy.ID, "com.truecaller:id/wizard_subscription_name")
    click_continue_for_ads_button = (AppiumBy.ID, "com.truecaller:id/nextButton")
    click_close_premium_button = (
        AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.truecaller:id/seeOtherPlans"]')
    click_consent_button = (AppiumBy.XPATH, "//android.webkit.WebView")
