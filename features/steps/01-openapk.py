import time

from behave import *

from features.page.validatecountry import validate
from features.page.intobrowser import intobrowser
from features.page.openmobileandseemainmenu import Mobiledevice


@given(u'I am on the browser, on my mobile device and navigate to "https://rahulshettyacademy.com/AutomationPractice/"')
def openmobiledevice(context):
    try:
        Mobiledevice.openmobile(context)
        time.sleep(5)
    except:
        assert False, f"Error in :'{openmobiledevice}'"


@when(u'I enter "{country}" into the suggestion class automcomplete field')
def autocompetefield(context,country):
    try:
        intobrowser.selectcountry(context,country)
    except:
        assert False,f"Error in :'{autocompetefield}'"


@then(u'I should have correctly selected the countries')
def correctlyselected(context):
    try:
        validate.validatecountry(context)
        context.driver.close()
    except:
        assert False,f"Error in :'{correctlyselected}'"

