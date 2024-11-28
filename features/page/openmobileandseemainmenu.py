import os
import yaml
from appium.webdriver.common.appiumby import AppiumBy
from features.resource.element.elements_Android import Elements
from src.mobile_functions import MobileAutomation


class Mobiledevice:

    def openmobile(self):
        # Obtener la ruta absoluta del archivo YAML
        base_dir = os.path.dirname(os.path.abspath(__file__))
        yaml_path = os.path.join(base_dir, "..", "resource", "config", "config.yaml")
        # Cargar el archivo YAML
        if not os.path.exists(yaml_path):
            raise FileNotFoundError(f"Archivo YAML no encontrado en: {yaml_path}")
        with open(yaml_path, "r") as file:
            config = yaml.safe_load(file)
            # Obtener las capabilities desde el YAML
        capabilities = config['desired_caps']
        appium_server_url = 'http://localhost:4723'
        MobileAutomation.init_driver(self, appium_server_url, capabilities, 'Pixel_7_API_UpsideDownCakePrivacySandbox')
        MobileAutomation.click(self,AppiumBy.XPATH,Elements['MockUp'])