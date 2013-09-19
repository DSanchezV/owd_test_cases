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
        self.actions    = Actions(self.marionette)
        
        #
        # Don't prompt me for geolocation (this was broken recently in Gaia, so 'try' it).
        #
        try:
            self.apps.set_permission('Homescreen', 'geolocation', 'deny')
        except:
            self.UTILS.logComment("(Just FYI) Unable to automatically set Homescreen geolocation permission.")

        
    def tearDown(self):
        self.UTILS.reportResults()
        
    def test_run(self):
        
        self._page1 = (DOM.Home.app_icon_pages[0], DOM.Home.app_icon_pages[1] + "[1]")
        
        self.UTILS.goHome()
        self.UTILS.scrollHomescreenRight()
        time.sleep(1)

        self.UTILS.logResult("info", "<u><b><i>BEFORE</i> EDIT MODE ACTIVATED ...</b></u>")
        x = self.UTILS.screenShotOnErr()
        self.UTILS.waitForElements(self._page1, "Icon page 1", True, 1, False)

        self._scrollLeft()
        x = self.UTILS.screenShotOnErr()
        self.UTILS.logResult("info", "Scroll back to home page:", x)
        self.UTILS.waitForNotElements(self._page1, "Icon page 1", True, 1, False)
        

        
        #
        # Go back to first icon page and put homescreen in edit mode.
        #
        self.UTILS.putHomeInEditMode()
        
        self.UTILS.logResult("info", "<u><b><i>AFTER</i> EDIT MODE ACTIVATED ...</b></u>")

        x = self.UTILS.screenShotOnErr()
        self.UTILS.waitForElements(self._page1, "Icon page 1", True, 1, False)
        
        self._scrollLeft()
        x = self.UTILS.screenShotOnErr()
        self.UTILS.logResult("info", "Scroll back to home page:", x)
        self.UTILS.waitForElements(self._page1, "Icon page 1 is still displayed", True, 1, False)
        

        #
        # Take it out of edit mode.
        #
        self.UTILS.touchHomeButton()
        
        
    def _scrollLeft(self):
        x = self.UTILS.getElement(self._page1, "Icon pages on homescreen")
        _icon1 = x.find_elements("xpath", "./ol/li[@class='icon']")[0]
        _icon2 = x.find_elements("xpath", "./ol/li[@class='icon']")[3]
        self.actions.press(_icon1).move(_icon2).release().perform()
        time.sleep(1)
