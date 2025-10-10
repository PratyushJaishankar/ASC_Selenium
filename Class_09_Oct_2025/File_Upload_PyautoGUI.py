# File_Upload_PyautoGUI.py - Demonstrates file upload using PyAutoGUI and Selenium
# Author: Pratyush Jaishankar
# Date: 09-Oct-2025

class FileUploadPyAutoGUIDemo:
    def __init__(self):
        print("[INIT] Initializing Chrome WebDriver...")
        import pyautogui
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        import os
        self.driver = webdriver.Chrome()
        self.By = By
        self.os = os
        self.pyautogui = pyautogui
        print("[INIT] WebDriver initialized.")

    def run(self):
        print("[RUN] Starting File Upload PyAutoGUI demo...")
        try:
            print("[STEP] Navigating to https://the-internet.herokuapp.com/upload ...")
            self.driver.get("https://the-internet.herokuapp.com/upload")
            print("[STEP] Creating test file for upload...")
            with open("test_upload.txt", "w") as f:
                f.write("This is a test file for upload")
            print("[STEP] Clicking file input to open file dialog...")
            file_input = self.driver.find_element(self.By.ID, "file-upload")
            file_input.click()
            import time
            time.sleep(2)
            print("[STEP] Using pyautogui to handle file dialog...")
            self.pyautogui.write(self.os.path.abspath("test_upload.txt"))
            self.pyautogui.press('enter')
            time.sleep(2)
            print("[STEP] Clicking upload button...")
            upload_btn = self.driver.find_element(self.By.ID, "file-submit")
            upload_btn.click()
            time.sleep(2)
            print("[RESULT] Upload completed.")
        except Exception as e:
            print(f"[ERROR] Exception occurred: {e}")
        finally:
            print("[STEP] Cleaning up test file...")
            if self.os.path.exists("test_upload.txt"):
                self.os.remove("test_upload.txt")
            print("[END] Quitting browser...")
            self.driver.quit()
            print("[END] Browser closed.")

if __name__ == "__main__":
    print("[MAIN] Running FileUploadPyAutoGUIDemo...")
    demo = FileUploadPyAutoGUIDemo()
    demo.run()
    print("[MAIN] FileUploadPyAutoGUIDemo finished.")
