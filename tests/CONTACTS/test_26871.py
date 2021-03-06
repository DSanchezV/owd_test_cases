#
# Imports which are standard for all test cases.
#
import sys
sys.path.insert(1, "./")
from gaiatest   import GaiaTestCase
from OWDTestToolkit import *

#
# Imports particular to this test case.
#
from tests._mock_data.contacts import MockContacts
import time

class test_main(GaiaTestCase):

    def setUp(self):
        #
        # Set up child objects...
        #
        GaiaTestCase.setUp(self)
        self.UTILS      = UTILS(self)
        self.contacts   = Contacts(self)
    
        #
        # Get details of our test contacts.
        #
        self.cont1 = MockContacts().Contact_1
        self.cont2 = MockContacts().Contact_2
        self.cont3 = MockContacts().Contact_3
        
        self.cont3["givenName"]="Rnameer"
        self.cont3["familyName"]="Tnameir"
        self.midWord="name"
        
        self.data_layer.insert_contact(self.cont1)
        self.data_layer.insert_contact(self.cont2)
        self.data_layer.insert_contact(self.cont3)
        
        
    def tearDown(self):
        self.UTILS.reportResults()
        
    def test_run(self):
        #
        # Launch contacts app.
        #
        self.contacts.launch()

        #
        # Search for the sought contact.
        #
        self.contacts.search(self.midWord)
        
        #
        # Verify our contact is listed.
        #
        self.contacts.checkSearchResults(self.cont3["givenName"])
        
        #
        # Verify the other contact is NOT listed.
        #
        self.contacts.checkSearchResults(self.cont2["givenName"],False)
        self.contacts.checkSearchResults(self.cont1["givenName"],False)
        