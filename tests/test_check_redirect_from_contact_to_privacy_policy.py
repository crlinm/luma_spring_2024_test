from pages.locators import *
from data.links import *
from selene import browser, by, be, have, support


def test_redirect_from_contact_to_privacy_policy():
    browser.open(PRIVACY_POLICY_LINK)
    browser.element(ContactUsLocators.CONTACT_US_LINK).click()
    browser.element(PrivacyPolicy.GO_BACK_LINK).click()
    browser.element(PrivacyPolicy.PRIVACY_POLICY_TITLE).should(have.text('Privacy Policy'))
