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
        x = self.UTILS.getElement(DOM.Browser.tab_tray_open, "Tab tray open button")
        x.tap()

        time.sleep(2)
        self.UTILS.TEST(self.UTILS.waitForNoNetworkActivity(p_timeout=30), "Finished loading page within 30 seconds.", False)
        self.UTILS.switchToFrame(*DOM.Browser.frame_locator)
        time.sleep(10)
        
        x = self.UTILS.getElements(DOM.Browser.tab_tray_tab_list, "Tab list")
        for i in range(0,len(x)):
            try:
                _img = x[i].find_element(*DOM.Browser.tab_tray_tab_item_image)
            except:
                _img = False
            self.UTILS.TEST(_img, "Tab %s has a preview image area." % (i+1), False)
            self.UTILS.TEST("background-image" in _img.get_attribute("style"), 
                            "Tab %s has a preview image which actually contains an image." % (i+1), False) 
        
            try:
                _title = x[i].find_element(*DOM.Browser.tab_tray_tab_item_title)
            except:
                _title = False
            self.UTILS.TEST(_title, "Tab %s has a title." % (i+1), False)
        
            try:
                _close = x[i].find_element(*DOM.Browser.tab_tray_tab_item_close)
            except:
                _close = False
            self.UTILS.TEST(_close, "Tab %s has a close button." % (i+1), False)
        
        
        