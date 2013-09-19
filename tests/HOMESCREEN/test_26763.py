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
        self.UTILS.scrollHomescreenRight()
        
        #
        # Get the number of icons in the dock.
        #
        x = self.UTILS.getElements(DOM.Home.docked_apps, "Dock apps (before)")
        _i1 = len(x)
            
        self.UTILS.logResult("info", "<b>There are %s apps in the dock before we begin.</b>" % _i1)
        
        #
        # Now loop enough times to have (potentially) more than 7 apps to the dock.
        #
        for i in range(_i1, 9):
            #
            # Get the name of the first app listed (changes each loop so we have to keep getting it).
            #
            x = self.UTILS.getElements(DOM.Home.apps, "Homepage apps")[0]
            _appName = x.get_attribute("aria-label")
            self.UTILS.logResult("info", "Adding app '%s' ..." % _appName)
            self.UTILS.addAppToDock(_appName)

        x = self.UTILS.getElements(DOM.Home.docked_apps, "Dock apps (after)")
        _i2 = len(x)
        
        self.UTILS.TEST(_i2 == 7, "<b>There are only 7 apps in the dock after trying to add more than this.</b>")
