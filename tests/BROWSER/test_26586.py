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
        
        #
        # Now open the tabs list and check our tab is there.
        #
        self.UTILS.TEST(self.Browser.trayCounterIs(2), "Tab tray counter is '1'.", False)
        
        x = self.UTILS.getElement(DOM.Browser.tab_tray_open, "Tab tray open button")
        x.tap()

        