import subprocess
import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import logging

# Configuración del logger
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("mobile_automation.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class MobileAutomation:
    def __init__(self,driver=None):
        self.driver = driver

    def init_driver(self, appium_server_url, capabilities, avd_name):
        """
        Inicia el emulador Android y configura el driver de Appium.
        """
        try:
            logger.info(f"Iniciando el emulador: {avd_name}")
            subprocess.Popen(["emulator", "-avd", avd_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            time.sleep(15)  # Esperar a que el emulador esté listo
            logger.info(f"Conectando al servidor Appium en: {appium_server_url}")
            self.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))
            time.sleep(15)
            logger.info("Driver inicializado con éxito.")
            return self.driver
        except Exception as e:
            logger.error(f"Error al iniciar el driver: {e}")
            raise

    def quit_driver(self):
        """
        Cierra el driver de Appium.
        """
        if self.driver is not None:
            logger.info("Cerrando el driver de Appium.")
            self.driver.quit()

    def find_element(self, locator_type, locator_value):
        """
        Busca un elemento en la pantalla.
        """
        try:
            logger.info(f"Buscando elemento: {locator_type} = {locator_value}")
            element = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((locator_type, locator_value))
            )

            # Validar que el elemento esté habilitado y visible
            if element.is_displayed() and element.is_enabled():
                logger.info(f"Elemento encontrado y disponible: {locator_type} = {locator_value}")
            else:
                logger.warning(f"Elemento encontrado, pero no está disponible: {locator_type} = {locator_value}")

            return element
        except Exception as e:
            logger.error(f"Error al buscar el elemento {locator_type} = {locator_value}: {e}")
            raise

    def click(self, locator_type, locator_value):
        """
        Hace clic en un elemento.
        """
        try:
            logger.info(f"Haciendo clic en: {locator_type} = {locator_value}")
            element = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((locator_type, locator_value)))
            element.click()
        except Exception as e:
            logger.error(f"Error al hacer clic en {locator_type} = {locator_value}: {e}")
            raise

    def enter_text(self, locator_type, locator_value, text):
        """
        Ingresa texto en un campo de texto.
        """
        try:
            logger.info(f"Escribiendo texto en: {locator_type} = {locator_value}")
            element = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((locator_type, locator_value)))
            element.clear()
            element.send_keys(text)

            # Confirmar que el texto fue ingresado correctamente
            entered_text = element.get_attribute("text")
            if entered_text == text:
                logger.info(f"Texto '{text}' ingresado correctamente en {locator_type} = {locator_value}")
            else:
                logger.warning(f"El texto ingresado no coincide: '{entered_text}' (esperado: '{text}')")
        except Exception as e:
            logger.error(f"Error al ingresar texto en {locator_type} = {locator_value}: {e}")
            raise

    def swipe(self, start_x, start_y, end_x, end_y, duration=1000):
        """
        Realiza un gesto de deslizamiento en la pantalla.
        """
        try:
            logger.info(f"Deslizando desde ({start_x}, {start_y}) hasta ({end_x}, {end_y}) con duración {duration}ms")
            self.driver.swipe(start_x, start_y, end_x, end_y, duration)
        except Exception as e:
            logger.error(f"Error al deslizar: {e}")
            raise

    def get_text(self, locator_type, locator_value):
        """
        Obtiene el texto de un elemento.
        """
        try:
            logger.info(f"Obteniendo texto de: {locator_type} = {locator_value}")
            element = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((locator_type, locator_value)))
            return element.text
        except Exception as e:
            logger.error(f"Error al obtener texto de {locator_type} = {locator_value}: {e}")
            raise

    def send_keys(self, keycode):
        """
        Envía teclas específicas al dispositivo (por ejemplo, ENTER, BACKSPACE).
        """
        try:
            logger.info(f"Enviando tecla: {keycode}")
            self.driver.press_keycode(keycode)
        except Exception as e:
            logger.error(f"Error al enviar tecla {keycode}: {e}")
            raise


    def switch_to_context(self, context_name=None):
        """
        Cambia al contexto especificado (por ejemplo, 'WEBVIEW' o 'NATIVE_APP').
        Si no se proporciona un nombre, lista los contextos disponibles.
        """
        try:
            # Obtener contextos disponibles
            available_contexts = self.driver.contexts
            logger.info(f"Contextos disponibles: {available_contexts}")

            if not context_name:
                logger.info("No se proporcionó un contexto. Permaneciendo en el contexto actual.")
                return

            # Validar que el contexto deseado esté disponible
            if context_name in available_contexts:
                self.driver.switch_to.context(context_name)
                logger.info(f"Cambiado al contexto: {context_name}")
            else:
                logger.warning(f"El contexto '{context_name}' no está disponible. Permaneciendo en el contexto actual.")
        except Exception as e:
            logger.error(f"Error al cambiar al contexto '{context_name}': {e}")
            raise
