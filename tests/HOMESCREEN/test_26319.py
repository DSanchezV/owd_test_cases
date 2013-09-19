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
        
    def tearDown(self):
        self.UTILS.reportResults()
        
    def test_run(self):
        self.UTILS.switchToFrame(*DOM.Home.frame_locator)
        self.UTILS.scrollHomescreenRight()
        
        x = self.UTILS.getElements(DOM.Home.apps, "App icons")
        _appName = x[0].get_attribute("aria-label")

        _scr = self.UTILS.screenShotOnErr()
        self.UTILS.logResult("info", "Moving '%s' from position 1 to position 3 ..." % _appName, _scr)
        
        self.actions.press(x[0]).wait(2).move(x[2]).wait(1).release().perform()
        
        self.UTILS.touchHomeButton()

        self.UTILS.switchToFrame(*DOM.Home.frame_locator)
        x = self.UTILS.getElements(DOM.Home.apps, "App icons")
        _appName2 = x[0].get_attribute("aria-label")
        self.UTILS.TEST(_appName2 != _appName, "App in position 1 is no longer '%s' (it was '%s')." % (_appName,_appName2), False)
        
        _appName3 = x[2].get_attribute("aria-label")
        self.UTILS.TEST( _appName3 == _appName,
                        "App in position 3 is now '%s' (it was '%s')." % (_appName, _appName3))

        _scr = self.UTILS.screenShotOnErr()        
        self.UTILS.logResult("info", "Screenshot of moved icon:", _scr)
