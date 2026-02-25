from eva_data_analysis import text_to_duration, calculate_crew_size
import pytest

#def test_text_to_duration_integer():
#    input_value = "10:00"
#    test_result = text_to_duration(input_value) == 10
#    print(f"text_to_duration('10:00') == 10? {test_result}")

def test_text_to_duration_integer():
    """
    Test that text_to_duration returns expected values for typical durations with a zero minutes component
    """

    assert text_to_duration("10:00") == 10
# Expect no output if everything went well


def test_text_to_duration_float():
    """
    Test that text_to_duration returns expected ground truth values for typical durations with a non zero minutes component
    """
#    assert text_to_duration("10:20") == 10.3333333333333333
#    assert abs(text_to_duration("10:20") - 10.3333333333333333) < 1e-5
    assert text_to_duration("10:20") == pytest.approx(10.33333)

#test_text_to_duration_integer()
#test_text_to_duration_float()

def test_calculate_crew_size():
    """
    Test that calculate_crew_size returns expected size for typical crew values
    """
    actual_result = calculate_crew_size("Dafni Lettos;")
    expected_result = 1
    assert actual_result == expected_result

    actual_result = calculate_crew_size("Dafni Lettos; Alex Taylor;")
    expected_result = 2
    assert actual_result == expected_result


def test_calculate_crew_size_edge_cases():
    """
    Test that calculate_crew_size returns expected size for atypical crew values (edge case were crew is empty string)
    """
    actual_result = calculate_crew_size("")
    assert actual_result == None
