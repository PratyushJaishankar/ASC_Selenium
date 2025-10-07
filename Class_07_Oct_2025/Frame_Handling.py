from selenium import webdriver

from selenium.webdriver.common.by import By

import time


def frame_handling_demo():
    driver = webdriver.Chrome()

    try:

        driver.get("https://demoqa.com/frames")

        # Switch to frame by index

        driver.switch_to.frame(0)

        print("Switched to frame 0")

        # Get text from frame

        frame_text = driver.find_element(By.ID, "sampleHeading").text

        print(f"Frame text: {frame_text}")

        # Switch back to main content

        driver.switch_to.default_content()

        print("Switched back to main content")

        # Switch to frame by ID/Name (if available)

        # driver.switch_to.frame("frame1")

        # Switch to frame by WebElement

        frame_element = driver.find_element(By.ID, "frame1")

        driver.switch_to.frame(frame_element)

        print("Switched to frame by element")

        frame_text = driver.find_element(By.ID, "sampleHeading").text

        print(f"Frame text: {frame_text}")

        # Always switch back to default content

        driver.switch_to.default_content()



    finally:

        driver.quit()


frame_handling_demo()