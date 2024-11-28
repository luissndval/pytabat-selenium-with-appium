from selenium.webdriver.common.by import By

from features.resource.element.elements_Android import Elements
from src.functions_selenium import Functions


class intobrowser(Functions):
    def selectcountry(self,Country):
        Functions.input_text(self,By.XPATH,Elements["autoComplete_Country"],Country)
        xpath = Elements["select_Country"].get(Country.strip())
        if xpath:
            try:
                Functions.click_field(self,By.XPATH,xpath)
                Functions.take_screenshot(self, "Country selected successfully")
                return "Country selected successfully."
            except Exception as e:
                return f"Failed to interact with the element: {str(e)}"
        else:
            return "Country code not found in the list."



