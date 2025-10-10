# WindowHandling.py - Demonstrates single window handling in Selenium
# Author: Pratyush Jaishankar
# Date: 09-Oct-2025

class WindowHandlingDemo:
    def __init__(self):
        print("[INIT] Initializing Chrome WebDriver...")
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        import time
        self.driver = webdriver.Chrome()
        self.By = By
        self.time = time
        print("[INIT] WebDriver initialized.")

    def run(self):
        print("[RUN] Starting Window Handling demo...")
        try:
            print("[STEP] Navigating to https://demoqa.com/browser-windows ...")
            self.driver.get("https://demoqa.com/browser-windows")
            parent_window = self.driver.current_window_handle
            print(f"[STEP] Parent window: {parent_window}")
            print("[STEP] Clicking button to open new window...")
            new_window_btn = self.driver.find_element(self.By.ID, "windowButton")
            new_window_btn.click()
            self.time.sleep(2)
            all_windows = self.driver.window_handles
            print(f"[STEP] Total windows: {len(all_windows)}")
            for window in all_windows:
                if window != parent_window:
                    print(f"[STEP] Switching to: {window}")
                    self.driver.switch_to.window(window)
                    print(f"[STEP] New window title: {self.driver.title}")
                    print(f"[STEP] New window URL: {self.driver.current_url}")
                    text_element = self.driver.find_element(self.By.TAG_NAME, "body")
                    print(f"[RESULT] Text in new window: {text_element.text}")
                    print("[STEP] Closing new window...")
                    self.driver.close()
            print("[STEP] Switching back to parent window...")
            self.driver.switch_to.window(parent_window)
        except Exception as e:
            print(f"[ERROR] Exception occurred: {e}")
        finally:
            print("[END] Quitting browser...")
            self.driver.quit()
            print("[END] Browser closed.")

if __name__ == "__main__":
    print("[MAIN] Running WindowHandlingDemo...")
    demo = WindowHandlingDemo()
    demo.run()
    print("[MAIN] WindowHandlingDemo finished.")
