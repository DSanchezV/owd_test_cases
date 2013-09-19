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
        self._page2 = (DOM.Home.app_icon_pages[0], DOM.Home.app_icon_pages[1] + "[2]")
                
        self.UTILS.goHome()

        self.UTILS.logResult("info", "Scrolling to icon page 1 ...")
        self.UTILS.scrollHomescreenRight()
        self.UTILS.waitForElements(self._page1, "Icon page 1", True, 1, False)
        
        self._hitHome()
        
        self.UTILS.logResult("info", "Scrolling to icon page 1 ...")
        self.UTILS.scrollHomescreenRight()
        self.UTILS.waitForElements(self._page1, "Icon page 1", True, 1, False)
        
        self.UTILS.logResult("info", "Scrolling to icon page 2 ...")
        self.UTILS.scrollHomescreenRight()
        self.UTILS.waitForElements(self._page2, "Icon page 2", True, 1, False)
        
        self._hitHome()
                
    def _hitHome(self):
        x = self.UTILS.screenShotOnErr()
        self.UTILS.logResult("info", "Before tapping the home button:", x)
        self.UTILS.logResult("info", "Hitting home button ...")
        self.UTILS.touchHomeButton()
        
        self.UTILS.switchToFrame(*DOM.Home.frame_locator)
        x = self.UTILS.screenShotOnErr()
        self.UTILS.logResult("info", "After tapping the home button:", x)
        
        self.UTILS.waitForNotElements(self._page1, "Icon page 1", True, 1, False)
        self.UTILS.waitForNotElements(self._page2, "Icon page 2", True, 1, False)
        
