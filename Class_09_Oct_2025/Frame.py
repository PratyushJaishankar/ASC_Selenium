# Frame.py - Demonstrates frame handling in Selenium
# Author: Pratyush Jaishankar
# Date: 09-Oct-2025

class FrameHandlingDemo:
    def __init__(self):
        print("[INIT] Initializing Chrome WebDriver...")
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        self.driver = webdriver.Chrome()
        self.By = By
        print("[INIT] WebDriver initialized.")

    def run(self):
        print("[RUN] Starting Frame Handling demo...")
        try:
            print("[STEP] Navigating to https://demoqa.com/frames ...")
            self.driver.get("https://demoqa.com/frames")
            print("[STEP] Switching to frame by ID 'frame1' ...")
            f1 = self.driver.find_element(self.By.ID, "frame1")
            self.driver.switch_to.frame(f1)
            print("[STEP] Switched to frame f1.")
            frame_text = self.driver.find_element(self.By.ID, "sampleHeading").text
            print(f"[RESULT] Frame text: {frame_text}")
            self.driver.switch_to.default_content()
            print("[STEP] Switched back to main content.")
            print("[STEP] Switching to frame by element (ID 'frame2') ...")
            frame_element = self.driver.find_element(self.By.ID, "frame2")
            self.driver.switch_to.frame(frame_element)
            print("[STEP] Switched to frame by element.")
            frame_text = self.driver.find_element(self.By.ID, "sampleHeading").text
            print(f"[RESULT] Frame text: {frame_text}")
            self.driver.switch_to.default_content()
            print("[STEP] Switched back to main content.")
        except Exception as e:
            print(f"[ERROR] Exception occurred: {e}")
        finally:
            print("[END] Quitting browser...")
            self.driver.quit()
            print("[END] Browser closed.")

if __name__ == "__main__":
    print("[MAIN] Running FrameHandlingDemo...")
    demo = FrameHandlingDemo()
    demo.run()
    print("[MAIN] FrameHandlingDemo finished.")
