import temperature



def test_find_min_max():
    num_list = [5,67,58]
    result = temperature.find_min_max(num_list)
    assert result == 1

def test_calc_average():
    num_list = [5,67,58]
    result = temperature.calc_average(num_list)
    assert result == 0

def test_calc_median_temperature():
    num_list = [5,58,67]
    result = temperature.calc_median_temperature(num_list)
    assert result == 2




