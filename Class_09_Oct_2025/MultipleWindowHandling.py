# MultipleWindowHandling.py - Demonstrates handling multiple browser windows in Selenium
# Author: Pratyush Jaishankar
# Date: 09-Oct-2025

class MultipleWindowHandlingDemo:
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
        print("[RUN] Starting Multiple Window Handling demo...")
        try:
            print("[STEP] Navigating to https://vinothqaacademy.com/multiple-windows/ ...")
            self.driver.get("https://vinothqaacademy.com/multiple-windows/")
            parent_window = self.driver.current_window_handle
            print(f"[STEP] Parent window handle: {parent_window}")
            print("[STEP] Opening new window...")
            self.driver.find_element(self.By.NAME, "newbrowserwindow123").click()
            self.time.sleep(1)
            print("[STEP] Opening message window...")
            self.driver.find_element(self.By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div/section[3]/div/div[4]/div/div/div/center/a").click()
            self.time.sleep(1)
            all_windows = self.driver.window_handles
            print(f"[STEP] All window handles: {all_windows}")
            child_windows = [w for w in all_windows if w != parent_window]
            print(f"[STEP] Total child windows opened: {len(child_windows)}")
            for i, window in enumerate(child_windows, 1):
                print(f"[STEP] Switching to child window {i}: {window}")
                self.driver.switch_to.window(window)
                self.time.sleep(1)
                print(f"[STEP] Current window handle: {self.driver.current_window_handle}")
                if self.driver.title == "about:blank":
                    print("[STEP] Blank window detected, skipping further actions.")
                    continue
                print(f"[STEP] Window title: {self.driver.title}")
                print("[STEP] Closing child window...")
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
    print("[MAIN] Running MultipleWindowHandlingDemo...")
    demo = MultipleWindowHandlingDemo()
    demo.run()
    print("[MAIN] MultipleWindowHandlingDemo finished.")
