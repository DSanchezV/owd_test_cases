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
        self.Browser.open_url("www.google.com")
        
        x = self.UTILS.screenShotOnErr()
        self.UTILS.logResult("info", "Screenshot of web page:", x)
        
        self.UTILS.switchToFrame(*DOM.Browser.frame_locator)
        
        x = self.UTILS.getElement(DOM.Browser.url_input, "Search input field")
        x.clear()

        x = self.UTILS.waitForElements(DOM.Browser.awesome_cancel_btn, "Awesome screen")

        x = self.UTILS.screenShotOnErr()
        self.UTILS.logResult("info", "Screenshot after clearing the text in the address bar:", x)
        