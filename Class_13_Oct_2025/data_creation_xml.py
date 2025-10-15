import os
import xml.etree.ElementTree as ET

def create_xml_data():
    os.makedirs("test_data/test_data", exist_ok=True)

    root = ET.Element("LoginTests")

    test_data = [
        ('TC001', 'standard_user', 'secret_sauce', 'Success'),
        ('TC002', 'locked_out_user', 'secret_sauce', 'Error'),
        ('TC003', 'problem_user', 'secret_sauce', 'Success'),
        ('TC004', 'performance_glitch_user', 'secret_sauce', 'Success'),
        ('TC005', 'wrong_user', 'wrong_pass', 'Error'),
        ('TC006', '', 'secret_sauce', 'Error'),
        ('TC007', 'standard_user', '', 'Error')
    ]

    for tc_id, username, password, expected in test_data:
        testcase = ET.SubElement(root, "TestCase")
        ET.SubElement(testcase, "TestCaseID").text = tc_id
        ET.SubElement(testcase, "Username").text = username
        ET.SubElement(testcase, "Password").text = password
        ET.SubElement(testcase, "ExpectedResult").text = expected

    tree = ET.ElementTree(root)
    file_path = 'test_data/login_data.xml'
    tree.write(file_path, encoding="utf-8", xml_declaration=True)
    print(f"Login test data created successfully at: {file_path}")

if __name__ == "__main__":
    create_xml_data()
