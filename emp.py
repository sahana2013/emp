import pytest
from emp import format_employee_info
def test_get_employee_info():
    name = "John Doe"
    emp_id = "181"
    department ="XY"
    salary = 6789
    expected_output =(
        "Employee Name: John Doe\n"
        "Employee ID: 181\n"
        "Department: XY\n"
        "Salary: 6789"
    )
    assert format_employee_info(name,emp_id,department,salary) == expected_output