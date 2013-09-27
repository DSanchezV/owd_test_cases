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
    
    _RESTART_DEVICE = True

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
        
        self.UTILS.switchToFrame(*DOM.Home.frame_locator)
        x = self.UTILS.getElements(DOM.Home.docked_apps, "Dock apps (before)")
        self.UTILS.TEST(len(x) < 7, "There are less than 7 apps in the dock before we start (or we can't add another one).", True)

        #
        # Get the name of the first app listed and add it to the dock.
        #
        self.UTILS.scrollHomescreenRight()
        x = self.UTILS.getElements(DOM.Home.apps, "Homepage apps")[0]
        _appName = x.get_attribute("aria-label")
        self.UTILS.logResult("info", "Adding app '%s' ..." % _appName)

        self.UTILS.addAppToDock(_appName)
