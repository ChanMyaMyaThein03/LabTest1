import employee_info

def test_get_employees_by_age_range():
    age_lower_limit = 23
    age_upper_limit = 30

    result = []
    result = employee_info.get_employees_by_age_range(age_lower_limit, age_upper_limit)
    test = [ {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000}]
    assert(result == test)

def test_calculate_average_salary():
    test = 60166.666666666664
    result = employee_info.calculate_average_salary()

    assert(result == test)

def test_get_employees_by_dept():
    department = "Sales"
    test = [{"name": "John", "age": 30, "department": "Sales", "salary": 50000},
            {"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}]
    result = employee_info.get_employees_by_dept(department)

    assert( result == test)

