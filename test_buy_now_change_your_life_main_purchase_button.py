import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_buy_now_button(driver):
    driver.get("https://mind-body-reset.netlify.app/")

    # Unlock the page by clicking “Start Your Reset Today”
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "✨ Start Your Reset Today"))
    ).click()

    # Wait for page to settle
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "button"))
    )

    # Scroll to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Find and click the 🔥 Buy Now button using JavaScript
    buy_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Buy Now & Change Your Life')]"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", buy_btn)
    driver.execute_script("arguments[0].click();", buy_btn)
