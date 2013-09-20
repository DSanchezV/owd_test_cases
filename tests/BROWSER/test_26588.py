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
        
        self.Browser.addNewTab()                
        self.Browser.searchUsingUrlField("two")

        self.Browser.addNewTab()
        self.Browser.searchUsingUrlField("three")
        
        _t = self.getTabTitle(3)
        self.UTILS.logResult("info", "Title of tab to be closed: \"%s\"." % _t)
        self.UTILS.logResult("info", "Number of tab with this title: \"%s\"." % self.getTabNumber(_t))
        
        self.closeTab(3)
        
        self.UTILS.TEST(not self.getTabNumber(_t), "Tab no longer exists with title \"%s\"." % _t)
        
    def getTabNumber(self, p_titleContains):
        #
        # Returns the number of the browser tab with a title that contains
        # p_titleContains, or False if it's not found.
        # <br>
        # Assumes we're in the main browser frame.
        #
        x = self.UTILS.getElement(DOM.Browser.tab_tray_open, "Tab tray open button")
        x.tap()
        x = self.UTILS.getElements(DOM.Browser.tab_tray_tab_list, "Tab list")
        boolOK = False
        for i in range(0,len(x)):
            _title = x[i].find_element(*DOM.Browser.tab_tray_tab_item_title)
            _title = _title.text.encode('ascii', 'ignore')
            if p_titleContains.lower() in _title.lower():
                boolOK = True
                break
            
        self.marionette.execute_script("document.getElementById('%s').click()" % DOM.Browser.tab_tray_close_btn[1])
        return boolOK
        
        
    def getTabTitle(self, p_num):
        #
        # Returns the title of tab p_num (assume we are in the main browser frame).
        #
        x = self.UTILS.getElement(DOM.Browser.tab_tray_open, "Tab tray open button")
        x.tap()

        x      = self.UTILS.getElements(DOM.Browser.tab_tray_tab_list, "Tab list")
        _title = x[p_num-1].find_element(*DOM.Browser.tab_tray_tab_item_title)
        
        self.marionette.execute_script("document.getElementById('%s').click()" % DOM.Browser.tab_tray_close_btn[1])
        return _title.text.encode('ascii', 'ignore')

    def closeTab(self, p_num):
        #
        # Closes the browser tab p_num (starting at '1').
        # Assumes we are in the main Browser iframe.
        #
        _before = self.Browser.trayCounterValue()
        x = self.UTILS.getElement(DOM.Browser.tab_tray_open, "Tab tray open button")
        x.tap()

        x = self.UTILS.getElements(DOM.Browser.tab_tray_tab_list, "Tab list")
        self.UTILS.TEST(len(x) >= p_num, "Tab %s exists." % p_num)

        _close = x[p_num-1].find_element(*DOM.Browser.tab_tray_tab_item_close)
        _close.tap()
        
        _after  = self.Browser.trayCounterValue()
        _expect = _before - 1
        self.UTILS.TEST(_expect == _after, "Tray counter was %s before closing one, now it is %s." % (_before, _after))
        
        self.marionette.execute_script("document.getElementById('%s').click()" % DOM.Browser.tab_tray_close_btn[1])
        