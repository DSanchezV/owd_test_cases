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
        self.lockscreen.lock()
        x = self.UTILS.screenShotOnErr()
        self.UTILS.logResult("info", "Locked screen:", x)
        self.UTILS.waitForElements( ("id", "lockscreen-area-handle"), "Lockscreen area", True, 1, False)

        self.lockscreen.unlock()
        x = self.UTILS.screenShotOnErr()
        self.UTILS.logResult("info", "unlocked screen:", x)
        
        self.UTILS.waitForNotElements( ("id", "lockscreen-area-handle"), "Lockscreen area", True, 1, False)
