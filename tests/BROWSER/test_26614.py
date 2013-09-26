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

class test_main(GaiaTestCase):
    
    def setUp(self):
        #
        # Set up child objects...
        #
        GaiaTestCase.setUp(self)
        self.UTILS      = UTILS(self)
        self.Browser    = Browser(self)
        self.actions    = Actions(self.marionette)
        

    def tearDown(self):
        self.UTILS.reportResults()
        
    def test_run(self):
    
        self.UTILS.getNetworkConnection()
        
        #
        # Open the browser app. and search for 'something'.
        #
        self.Browser.launch()
        
        x = self.Browser.getAwesomeList("top sites")
        x = self.Browser.getAwesomeList("bookmarks")
        x = self.Browser.getAwesomeList("history")
        
