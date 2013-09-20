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
        self.Browser.searchUsingUrlField("one")
        
        #
        # Now open the tabs list and check our tab is there.
        #
        self.UTILS.TEST(self.Browser.trayCounterIs(1), "Tab tray counter is '1'.", False)
        
        self.Browser.addNewTab()
                
        self.Browser.searchUsingUrlField("two")
        self.UTILS.TEST(self.Browser.trayCounterIs(2), "Tab tray counter is '2'.", False)

        self.Browser.addNewTab()
        
        self.Browser.searchUsingUrlField("three")
        self.UTILS.TEST(self.Browser.trayCounterIs(3), "Tab tray counter is '3'.", False)

        self.Browser.addNewTab()
        
        self.Browser.searchUsingUrlField("four")
        self.UTILS.TEST(self.Browser.trayCounterIs(4), "Tab tray counter is '4'.", False)

        
        