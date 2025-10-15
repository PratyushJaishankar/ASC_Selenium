# ASC_Selenium

A collection of hands-on Python Selenium automation scripts for demonstrating core browser automation concepts and data handling tasks.

## Overview

This repository contains practical examples of using Selenium WebDriver with Python to automate browser actions, interact with web elements, and handle different data formats. Each script is self-contained and demonstrates a specific automation scenario, making this repo ideal for learning and experimenting with Selenium.

## Key Features

- **Web Table Automation**: Extract, search, and print data from web tables.
- **Drag and Drop**: Perform drag-and-drop actions and verify results.
- **Double Click & Right Click**: Demonstrate double and right-click interactions on web elements.
- **File Uploads**: Automate uploading files through browser interfaces.
- **Handling Alerts**: Interact with browser alerts (simple, confirmation, prompt).
- **Multiple Window Handling**: Manage multiple browser windows/tabs.
- **JavaScript Execution**: Run custom JavaScript in the browser context using Selenium.
- **Title Verification**: Check and verify webpage titles for automated testing.
- **Data Creation**: Generate sample data in CSV, XLSX, and XML formats for testing purposes.

## Directory Structure

```
ASC_Selenium/
│
├── Class_06_Oct_2025/
│   └── main.py
├── Class_07_Oct_2025/
│   └── webTableDemo.py
├── Class_09_Oct_2025/
│   ├── Alerts.py
│   ├── File_Upload.py
│   └── MultipleWindowHandling.py
├── Class_10_Oct_2025/
│   └── src/title.py
├── Class_13_Oct_2025/
│   ├── data_creation_csv.py
│   ├── data_creation_xlsx.py
│   └── data_creation_xml.py
├── Lab_07_Oct_2025/
│   ├── Drag_Drop.py
│   ├── DoubleClick.py
│   ├── JavaScript_Executor.py
│   ├── Right_Click.py
│   └── webTable.py
└── ...
```

## Getting Started

1. **Clone the repository**
   ```sh
   git clone https://github.com/PratyushJaishankar/ASC_Selenium.git
   ```
2. **Install dependencies**
   - Python 3.x
   - Selenium (`pip install selenium`)
   - openpyxl (for XLSX data scripts: `pip install openpyxl`)

3. **Run example scripts**
   - Each script can be run independently, for example:
     ```sh
     python Lab_07_Oct_2025/Drag_Drop.py
     ```
   - Make sure the correct web driver for your browser (e.g., ChromeDriver) is installed and available in your PATH.

## Author

- [Pratyush Jaishankar](https://github.com/PratyushJaishankar)

## License

This repository currently does not specify a license.
