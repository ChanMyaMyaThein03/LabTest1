import employee_info

def test_get_employees_by_age_range():
    age_lower_limit = 23
    age_upper_limit = 30

    result = []
    result = employee_info.get_employees_by_age_range(age_lower_limit, age_upper_limit)
    test = [ {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000}]
    assert(result == test)