import time
from selenium.webdriver.support.wait import WebDriverWait
from datetime import datetime, timedelta
from pages.locators import Locators


class Homepage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
    def login(self,username,password):
        self.driver.find_element(*Locators.username).send_keys(username)
        self.driver.find_element(*Locators.password).send_keys(password)
        self.driver.find_element(*Locators.login).click()
    def createLead(self, firstname, lastname, company):
        time.sleep(5)
        self.driver.execute_script('arguments[0].click();', self.driver.find_element(*Locators.lead_header))
        time.sleep(10)
        self.driver.find_element(*Locators.lead_dropdown).click()
        time.sleep(5)
        self.driver.execute_script('arguments[0].click();', self.driver.find_element(*Locators.new_lead_icon))
        time.sleep(5)
        self.driver.find_element(*Locators.salutation).click()
        self.driver.execute_script('arguments[0].click();', self.driver.find_element(*Locators.salutation_option))
        time.sleep(5)
        self.driver.find_element(*Locators.firstname).send_keys(firstname)
        self.driver.find_element(*Locators.lastname).send_keys(lastname)
        self.driver.find_element(*Locators.company).send_keys(company)
        self.driver.find_element(*Locators.saveedit).click()

    def convertLead(self):
        time.sleep(10)
        self.driver.execute_script('arguments[0].click();', self.driver.find_element(*Locators.convert_dropdown))
        time.sleep(5)
        self.driver.execute_script('arguments[0].click();', self.driver.find_element(*Locators.convert_text))
        time.sleep(5)
        self.driver.find_element(*Locators.convert_button).click()
        time.sleep(5)
        self.driver.find_element(*Locators.close_window).click()

    def verifyConvertedLead(self,first_name,last_name,company):
        time.sleep(5)
        self.driver.find_element(*Locators.accounts_dropdown).click()
        time.sleep(5)

        self.driver.execute_script(
            'arguments[0].click();',
            self.driver.find_element(*Locators.recent_method(company))
        )
        time.sleep(5)
        name = self.driver.find_element(*Locators.account_name).text

        # Compare the retrieved name with the generated name
        assert name == f"{first_name} {last_name}", \
            f"Expected {first_name} {last_name}, but got {name}"
        print(f"Verified lead: {name}")

    def createAccount(self,account_name):
        time.sleep(10)
        self.driver.find_element(*Locators.accounts_dropdown).click()
        time.sleep(10)
        self.driver.execute_script('arguments[0].click();',self.driver.find_element(*Locators.new_account_icon))
        time.sleep(5)
        self.driver.find_element(*Locators.account_name_field).send_keys(account_name)
        self.driver.find_element(*Locators.saveedit).click()

    def createContact(self,contact_name,last_name):
        time.sleep(5)
        self.driver.find_element(*Locators.contact_dropdown).click()
        time.sleep(5)
        self.driver.execute_script('arguments[0].click();',self.driver.find_element(*Locators.new_contact_icon))
        time.sleep(5)
        self.driver.find_element(*Locators.search_icon).click()
        time.sleep(5)
        self.driver.find_element(*Locators.recentAccountName(contact_name)).click()
        time.sleep(5)
        self.driver.find_element(*Locators.lastname).send_keys(last_name)
        self.driver.find_element(*Locators.saveedit).click()

    def createOpportunity(self,account_name,opportunity_name):
        time.sleep(5)
        self.driver.find_element(*Locators.opportunity_dropdown).click()
        time.sleep(5)
        self.driver.execute_script('arguments[0].click();',self.driver.find_element(*Locators.new_opportunity_icon))
        time.sleep(5)
        self.driver.find_element(*Locators.search_icon).click()
        time.sleep(10)
        self.driver.find_element(*Locators.recentAccountName(account_name)).click()
        time.sleep(5)
        self.driver.find_element(*Locators.opportunity_name_field).send_keys(opportunity_name)
        current_date_plus_10 = (datetime.now() + timedelta(days=10)).strftime("%d/%m/%Y")
        self.driver.find_element(*Locators.opportunity_date_field).send_keys(current_date_plus_10)
        time.sleep(5)
        self.driver.execute_script('arguments[0].click();',self.driver.find_element(*Locators.stage_dropdown))
        time.sleep(10)
        self.driver.find_element(*Locators.qualification_option).click()
        self.driver.find_element(*Locators.saveedit).click()

    def verifyContact(self,account_name,contact_name):
        time.sleep(5)
        self.driver.find_element(*Locators.accounts_dropdown).click()
        time.sleep(5)
        self.driver.execute_script('arguments[0].click();',self.driver.find_element(*Locators.recent_method(account_name)))
        time.sleep(5)
        actual_contact_name=self.driver.find_element(*Locators.contactOrOpportunity(contact_name)).text

        assert contact_name == actual_contact_name,f"Expected {contact_name} , but got {actual_contact_name}"

    def verifyOpportunity(self,opportunity):
        time.sleep(10)
        actual_opportunity_name = self.driver.find_element(*Locators.contactOrOpportunity(opportunity)).text

        assert actual_opportunity_name == opportunity, f"Expected {opportunity} , but got {actual_opportunity_name}"






























