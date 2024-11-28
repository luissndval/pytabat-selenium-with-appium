from selenium.webdriver.common.by import By
from features.resource.element.elements_Android import Elements
from src.functions_selenium import Functions


class dropdown(Functions):

    def dropdownselect(self, Option):
        self.driver.swipe(start_x=1000, start_y=1443, end_x=223, end_y=1431, duration=800)
        Functions.click_field(self, By.XPATH, Elements["dropDown Select"])
        # Functions.Iframe(self, By.XPATH, Elements["Iframe Options"])
        option_xpath=Elements.get(Option)
        if option_xpath:
            Functions.click_action(self, By.XPATH, option_xpath)

    def dropdownvalidate(self, Option):
        get_text = Functions.validates(self, By.XPATH, Elements[Option])
        if Option == get_text:
            Functions.take_screenshot(self, f"Option Validate {get_text}")
