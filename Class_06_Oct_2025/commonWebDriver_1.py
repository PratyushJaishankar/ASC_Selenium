from selenium import webdriver



print("Starting commonWebDriver_1 demo...")
driver = webdriver.Chrome()


# 1. get() - Navigate to URL

print("Navigating to Google...")

driver.get("https://www.google.com")


# 2. get_title() - Get page title

title = driver.title

print(f"Page Title: {title}")


# 3. current_url - Get current URL

current_url = driver.current_url

print(f"Current URL: {current_url}")


# 4. page_source - Get page source

page_source = driver.page_source

print(f"Page Source Length: {len(page_source)}")

print(f"Page Source (first 500 chars): {page_source[:500]}")


# 5. maximize_window() - Maximize browser window

print("Maximizing browser window...")

driver.maximize_window()


# 6. set_window_size() - Set window size

print("Setting window size to 1024x768...")

driver.set_window_size(1024, 768)


# 7. set_window_position() - Set window position

print("Setting window position to (100, 100)...")

driver.set_window_position(100, 100)


# 8. back() - Navigate back

print("Navigating back...")

driver.back()


# 9. forward() - Navigate forward

print("Navigating forward...")

driver.forward()


# 10. refresh() - Refresh page

print("Refreshing page...")

driver.refresh()


# 11. close() - Close current window

print("Closing current window...")

driver.close()


# 12. quit() - Close all windows

print("Quitting browser...")

driver.quit()

print("commonWebDriver_1 demo completed.")
