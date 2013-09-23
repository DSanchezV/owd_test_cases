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
        self.Browser.searchUsingUrlField("search page one")
        
        self.Browser.addNewTab()                
        self.Browser.searchUsingUrlField("search page two")
        
        _t = self.Browser.getTabTitle(2)
        self.UTILS.logResult("info", "Title of tab to be closed: \"%s\"." % _t)
        self.UTILS.logResult("info", "Number of tab with this title: \"%s\"." % (self.Browser.getTabNumber(_t)+1))
        
        self.Browser.closeTab(2)
        
        self.Browser.openTab(1)
        
        self.UTILS.TEST(not self.Browser.getTabNumber(_t), "Tab no longer exists with title \"%s\"." % _t)

        

        