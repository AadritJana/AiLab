from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


def ai_agent(requirement: str, expected_output: str) -> bool:
    """
    AI Agent to navigate a webpage, perform an action, and validate output.
    :param requirement: Action to perform (e.g., click a button)
    :param expected_output: Expected URL or page element to validate success
    :return: True if test passes, False otherwise
    """
    # Set up the Selenium WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.calfus.com/")
    time.sleep(3)

    try:
        # Locate the element and perform the action
        element = driver.find_element(By.CSS_SELECTOR, "#comp-lkb6bgja > nav > ul > li:nth-child(1) > a > div > span")
        ActionChains(driver).move_to_element(element).click().perform()
        time.sleep(3)  # Allow navigation to complete

        # Validate expected output
        if driver.current_url == expected_output:
            print("Test Passed: Navigation successful")
            return True
        else:
            print(f"Test Failed: Expected {expected_output}, but got {driver.current_url}")
            return False

    except Exception as e:
        print(f"Test Failed due to exception: {e}")
        return False

    finally:
        driver.quit()


# Example Usage
requirement = "Click on Products & Platforms"
expected_output = "https://www.calfus.com/products-platforms"
ai_agent(requirement, expected_output)
