# File_Upload_Diff.py - Demonstrates file upload on a different site using Selenium
# Author: Pratyush Jaishankar
# Date: 09-Oct-2025

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


class FileUploadDiffDemo:
    def __init__(self):
        print("[INIT] Initializing Chrome WebDriver...")
        self.driver = webdriver.Chrome()
        print("[INIT] WebDriver initialized.")

    def run(self):
        print("[RUN] Starting File Upload Diff demo...")
        try:
            print("[STEP] Navigating to https://practice.expandtesting.com/upload ...")
            self.driver.get("https://practice.expandtesting.com/upload")
            print("[STEP] Uploading file using send_keys...")
            file_input = self.driver.find_element(By.ID, "fileInput")
            file_input.send_keys(os.path.abspath("Alerts.py"))
            print("[STEP] Clicking upload button...")
            upload_btn = self.driver.find_element(By.ID, "fileSubmit")
            upload_btn.click()
            time.sleep(2)
            file_name = "Alerts.py"
            success_message = self.driver.find_element(By.ID, "uploaded-files").text
            if file_name in success_message:
                print("[RESULT] File Uploaded Successfully")
            else:
                print("[RESULT] File Upload Failed")
            print(f"[RESULT] Upload result: {success_message}")
            print("[STEP] Cleaning up test file if exists...")
            if os.path.exists("test_upload.txt"):
                os.remove("test_upload.txt")
        except Exception as e:
            print(f"[ERROR] Exception occurred: {e}")
        finally:
            print("[END] Quitting browser...")
            self.driver.quit()
            print("[END] Browser closed.")


if __name__ == "__main__":
    print("[MAIN] Running FileUploadDiffDemo...")
    demo = FileUploadDiffDemo()
    demo.run()
    print("[MAIN] FileUploadDiffDemo finished.")
