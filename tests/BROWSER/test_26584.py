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
        
        #
        # Wifi needs to be off for this test to work.
        #
        self.UTILS.getNetworkConnection()
        
        #
        # Open the browser app. and search for 'something'.
        #
        self.Browser.launch()
        self.Browser.searchUsingUrlField("dilbert cartoons")
        
        #
        # Open our URL.
        #
        self.UTILS.switchToFrame(*DOM.Browser.browser_page_frame, p_viaRootFrame=False)
        
        x = self.UTILS.getElements(DOM.Browser.search_result_links, "Search results")[0]
        self.actions.press(x).wait(2).release().perform()
        
        #
        # Click the 'open in new tab' button.
        #
        self.UTILS.switchToFrame(*DOM.Browser.frame_locator)
        x = self.UTILS.getElement(DOM.Browser.open_in_new_tab_button, "Open link in new tab")
        x.tap()
        
        #
        # Now open the tabs list and check our tab is there.
        #
        self.UTILS.TEST(self.Browser.trayCounterValue() == "2", "Tab tray counter is '2'.", False)
        
        x = self.UTILS.getElement(DOM.Browser.tab_tray_open, "Tab tray open button")
        x.tap()

        time.sleep(2)
        self.UTILS.TEST(self.UTILS.waitForNoNetworkActivity(p_timeout=30), "Finished loading page within 30 seconds.", False)
        self.UTILS.switchToFrame(*DOM.Browser.frame_locator)
        
        x = self.UTILS.getElements(DOM.Browser.tab_tray_tab_list, "Tab list")
        _displayed = x[0].find_element("tag name", "span").text.lower()
        self.UTILS.TEST("dilbert cartoons" in _displayed, 
                        "The first tab is for the 'dilbert cartoons' search (it was \"%s\")" % _displayed, False)

        _displayed = x[1].find_element("tag name", "span").text.lower()
        self.UTILS.TEST("dilbert website" in _displayed, 
                        "The second tab is for the dilbert website (it was \"%s\")" % _displayed, False)

        
        x = self.UTILS.screenShotOnErr()
        self.UTILS.logResult("debug", "Final screenshot:", x)
        