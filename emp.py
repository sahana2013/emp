def format_employee_info(name: str, emp_id: int, department: str, salary: float) -> str:
    """
    Accepts employee details and returns a formatted string.
    """
    return (
        f"Employee Name: {name}\n"
        f"Employee ID: {emp_id}\n"
        f"Department: {department}\n"
        f"Salary: ₹{salary:,.2f}"
    )

if __name__ == "__main__":
    print(format_employee_info("John Doe", 181, "XY", 6789))
