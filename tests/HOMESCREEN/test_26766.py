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
        
        self.UTILS.switchToFrame(*DOM.Home.frame_locator)
        try:
            self.wait_for_element_present(*DOM.Home.docked_apps, timeout=1)
        except:
            self.UTILS.logResult(False, "Warning: no apps in dock! Restart device to default settings ...")
            return
        
        #
        # Get the name of the first app and move it.
        #            
        x     = self.UTILS.getElements(DOM.Home.docked_apps, "Dock apps")
        _name = x[0].get_attribute("aria-label")
        self.UTILS.TEST( self.UTILS.moveAppFromDock(_name) != False, 
                         "App '%s' was successfully moved from the dock." % _name)

