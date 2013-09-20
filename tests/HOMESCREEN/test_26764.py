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
            self.apps.set_permission('Camera', 'geolocation', 'deny')
        except:
            self.UTILS.logComment("(Just FYI) Unable to automatically set Homescreen geolocation permission.")

        
    def tearDown(self):
        self.UTILS.reportResults()
        
    def test_run(self):
        
        #
        # Go to the first icon page.
        #
        self.UTILS.switchToFrame(*DOM.Home.frame_locator)
        
        #
        # Get the number of icons in the dock.
        #
        x = self.UTILS.getElements(DOM.Home.docked_apps, "Dock apps (before)")
        _i1 = len(x)
        
        #
        # Add an item to the dock that we can move.
        #
        self.UTILS.scrollHomescreenRight()
        if _i1 < 5:
            x = self.UTILS.getElements(DOM.Home.apps, "Homepage apps")[0]
            _appName = x.get_attribute("aria-label")
            self.UTILS.logResult("info", "Adding app '%s' ..." % _appName)
            self.UTILS.addAppToDock(_appName)
        
        #
        # Try to add the icon to the main home page while in edit mode.
        #
        self.UTILS.goHome()
        x = self.UTILS.getElements(DOM.Home.docked_apps, "Dock apps (before)")
        self.actions.press(x[0]).wait(2).release().perform()
        
        boolOK = True
        try:
            del_icon = x[0].find_element("xpath", ".//span[@class='options']")
            if del_icon.is_displayed():
                boolOK = False
        except:
            pass
        
        self.UTILS.TEST(boolOK, "Screen will not go into edit mode from main homescreen page.")

        #
        # Try to (forceably) scroll homescreen to main page while in edit mode.
        #
        self.UTILS.putHomeInEditMode()
        x = self.UTILS.getElement((DOM.Home.app_icon_pages[0], DOM.Home.app_icon_pages[1] + "[1]"), 
                                  "First icon pages on homescreen")
        _icon1 = x.find_elements("xpath", "./ol/li[@class='icon']")[0]
        _icon2 = x.find_elements("xpath", "./ol/li[@class='icon']")[3]
        self.actions.press(_icon1).move(_icon2).release().perform()
        time.sleep(1)

        boolOK = True
        try:
            self.wait_for_element_displayed(DOM.Home.app_icon_pages[0], DOM.Home.app_icon_pages[1] + "[1]")
            boolOK = False
        except:
            pass
        
        if not boolOK:
            self.UTILS.logResult("info", "Could not 'cheat' and move screen to main homepage while in edit mode.")
            return
        
        #
        # Try to drag the icon out of the dock.
        #
        x = self.UTILS.getElements(DOM.Home.docked_apps, "Dock apps (before trying to drag one out of the dock)")
        _i1 = len(x)
        self.actions.press(x[0]).move_by_offset(0,-500).release().perform()
        
        x = self.UTILS.getElements(DOM.Home.docked_apps, "Dock apps (after trying to drag one out of the dock)")
        _i2 = len(x)
        
        self.UTILS.TEST(_i1 == _i2, "The icon could not be removed from the dock onto the main homepage.")