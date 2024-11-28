from selenium.webdriver.common.by import By

from features.resource.element.elements_Android import Elements
from src.functions_selenium import Functions


class validate(Functions):


    def validatecountry(self):
        validates={"Mexico",
                   "United States (USA)",
                   "United Arab Emirates"
                   }
        text=Functions.validates(self,By.XPATH,Elements["autoComplete_Country"])

        if text in validates:
            Functions.take_screenshot(self,f"Country Validate {text}")
        else:
            assert False, "The Country does exist."



