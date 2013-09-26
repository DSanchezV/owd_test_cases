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
    
        self.UTILS.getNetworkConnection()
        
        #
        # Open the browser app. and search for 'something'.
        #
        self.Browser.launch()
        self.Browser.open_url("www.wikipedia.com")
        self.Browser.open_url("www.google.com")
        
        x = self.Browser.getAwesomeList("top sites")
        self.UTILS.TEST(len(x) >= 2, "There are at least 2 sites listed here (there were %s)." % len(x))
        
        x = self.Browser.getAwesomeList("bookmarks")
        
        x = self.Browser.getAwesomeList("history")
        self.UTILS.TEST(len(x) >= 2, "There are at least 2 sites listed here")
        self.UTILS.TEST("google"    in x[0].get_attribute("href"), "The 1st history item is for google.")
        self.UTILS.TEST("wikipedia" in x[1].get_attribute("href"), "The 2nd history item is for wikipedia.")
        
