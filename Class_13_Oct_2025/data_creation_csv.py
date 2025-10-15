import csv
import os

def create_csv_data():
    os.makedirs("test_data", exist_ok=True)
    file_path = 'test_data/login_data.csv'

    headers = ['TestCaseID', 'Username', 'Password', 'ExpectedResult']
    test_data = [
        ('TC001', 'standard_user', 'secret_sauce', 'Success'),
        ('TC002', 'locked_out_user', 'secret_sauce', 'Error'),
        ('TC003', 'problem_user', 'secret_sauce', 'Success'),
        ('TC004', 'performance_glitch_user', 'secret_sauce', 'Success'),
        ('TC005', 'wrong_user', 'wrong_pass', 'Error'),
        ('TC006', '', 'secret_sauce', 'Error'),
        ('TC007', 'standard_user', '', 'Error')
    ]

    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(test_data)

    print(f"Login test data created successfully at: {file_path}")

if __name__ == "__main__":
    create_csv_data()
