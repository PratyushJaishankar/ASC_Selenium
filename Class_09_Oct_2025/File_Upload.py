# File_Upload.py - Demonstrates file upload using Selenium
# Author: Pratyush Jaishankar
# Date: 09-Oct-2025

class FileUploadDemo:
    def __init__(self):
        print("[INIT] Initializing Chrome WebDriver...")
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        import os
        self.driver = webdriver.Chrome()
        self.By = By
        self.os = os
        print("[INIT] WebDriver initialized.")

    def run(self):
        print("[RUN] Starting File Upload demo...")
        try:
            print("[STEP] Navigating to https://the-internet.herokuapp.com/upload ...")
            self.driver.get("https://the-internet.herokuapp.com/upload")
            print("[STEP] Creating test file for upload...")
            with open("test_upload.txt", "w") as f:
                f.write("This is a test file for upload")
            print("[STEP] Uploading file using send_keys...")
            file_input = self.driver.find_element(self.By.ID, "file-upload")
            file_input.send_keys(self.os.path.abspath("test_upload.txt"))
            print("[STEP] Clicking upload button...")
            upload_btn = self.driver.find_element(self.By.ID, "file-submit")
            upload_btn.click()
            import time
            time.sleep(2)
            success_message = self.driver.find_element(self.By.TAG_NAME, "h3").text
            print(f"[RESULT] Upload result: {success_message}")
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
    print("[MAIN] Running FileUploadDemo...")
    demo = FileUploadDemo()
    demo.run()
    print("[MAIN] FileUploadDemo finished.")
