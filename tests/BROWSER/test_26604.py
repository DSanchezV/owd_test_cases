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
        x = self.UTILS.getElement(DOM.Browser.url_input, "Search input field")
        x.tap()

        self.UTILS.waitForElements(DOM.Browser.awesome_cancel_btn, "Awesome screen cancel button")

        x.send_keys("weather")
        x = self.UTILS.getElement(DOM.Browser.url_go_button, "'Go' button")
        x.tap()
        self.Browser.waitForPageToFinishLoading()
        
        self.UTILS.switchToFrame(*DOM.Browser.browser_page_frame, p_viaRootFrame=False)

        x = self.UTILS.getElements(DOM.Browser.search_result_links, "Search results")[0]
        x.tap()

        self.UTILS.switchToFrame(*DOM.Browser.frame_locator)
        self.UTILS.waitForNotElements(DOM.Browser.awesome_cancel_btn, "Awesome screen cancel button")
        
        
        
        