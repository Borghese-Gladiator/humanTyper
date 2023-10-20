from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from typer import Typer


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://write-box.appspot.com/")

text = """
    The quick brown fox jumps over the lazy dog.
    The quick brown fox jumps over the lazy dog.
    The quick brown fox jumps over the lazy dog.
    The quick brown fox jumps over the lazy dog.
    The quick brown fox jumps over the lazy dog.
    """
element = driver.find_element(By.ID, 'editor')
element.clear()
ty = Typer(accuracy = 0.90, correction_chance = 0.50, typing_delay = (0.04, 0.08), distance = 2)
ty.send(element, text)