from pages.homepage import Homepage
from utilities.BaseClass import Baseclass


class Test(Baseclass):
    confirm = None

    def setup_method(self, method):
        self.home = Homepage(self.driver)

    def test_login(self, browser_setup):
        self.driver = browser_setup
        self.home = Homepage(self.driver)
        self.home.login("dhamodharanvemula-mal0@force.com","Dhamuvemula@123")

    def test_create_lead(self):
        self.home.create_lead("Dhamu","Vemula","Tiger")

    def test_convert_lead(self):
        self.home.convert_lead()

    def test_verify_recent_account(self):
        self.home.verify_converted_lead("Dhamu","Vemula","Tiger")

    def test_create_account(self):
        self.home.createAccount("Dhamodharan1")

    def test_create_contact(self):
        self.home.createContact("Dhamodharan1","Vemula")

    def test_create_opportunity(self):
        self.home.createOpportunity("Dhamodharan1","XYZ")

    def test_verify_contact_and_opportunity(self):
        self.home.verify_contact("Dhamodharan1","Vemula")


