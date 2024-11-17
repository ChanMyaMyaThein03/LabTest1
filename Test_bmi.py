import bmi

def test_bmi_normal_weight():
    bmi_result = bmi.calculate_bmi(height=1.75, weight = 70)
    assert ( bmi_result == 0)


def test_bmi_over_weight():
     bmi_result = bmi.calculate_bmi(1.75,80)
     assert ( bmi_result == 1)


def test_bmi_under_weight():
      bmi_result = bmi.calculate_bmi(1.75,50)
      assert ( bmi_result == -1)