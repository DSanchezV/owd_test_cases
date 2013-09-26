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
        x = self.UTILS.getElement(DOM.Browser.browser_iframe_xpath, "Web page")
        _src_orig = x.get_attribute("src")
        
        x = self.UTILS.getElement(DOM.Browser.url_input, "Search input field")
        x.tap()

        x = self.UTILS.screenShotOnErr()
        self.UTILS.logResult("info", "Screenshot before cancelling 'awesomeScreen':", x)
        
        x = self.UTILS.getElement(DOM.Browser.awesome_cancel_btn, "Awesome screen cancel button")
        x.tap()

        self.UTILS.waitForNotElements(DOM.Browser.awesome_cancel_btn, "Awesome screen cancel button")

        x = self.UTILS.getElement(DOM.Browser.browser_iframe_xpath, "Web page")
        _src_new = x.get_attribute("src")
        
        self.UTILS.switchToFrame(*DOM.Browser.browser_page_frame, p_viaRootFrame=False)
        
        x = self.UTILS.screenShotOnErr()
        self.UTILS.logResult("info", "Screenshot of web page after cancelling 'awesomeScreen':", x)
        
        self.UTILS.TEST(_src_orig == _src_new, 
                        "Web page source before ('%s') == web page source after ('%s')." %\
                        (_src_orig, _src_new))
        
        
        
        