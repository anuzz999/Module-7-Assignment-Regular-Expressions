import pytest
from assignment4 import ConcertAnalysis 

# Defining the test inputs and expected outputs
test_data = [
    ("*****Artist1---CAPACITY---:1000 -- $ATTENDANCE: 900--GATE:--$45,000;", 
     {"Artist1": {"average_ticket_price": "$50.00", "multi_word_name": True, "venue_fill_percentage": "90%"}}),
     
    ("*****Artist2---CAPACITY---:2000 -- $ATTENDANCE: 1800--GATE:--$36,000;", 
     {"Artist2": {"average_ticket_price": "$20.00", "multi_word_name": True, "venue_fill_percentage": "90%"}})
    # Add more test cases as needed
]

@pytest.mark.parametrize("text,expected", test_data)
def test_task_four(text, expected):
    """This tests that our task_four returns the correct outputs for different inputs."""
    analysis = ConcertAnalysis(text)  # Initialize your class with the test text
    output = analysis.task_four()  # Execute the method to get the output

    # Assertions to check if the output matches the expected results
    assert isinstance(output, dict), f"For input '{text}', expected a dictionary but got {type(output)}"
    assert output == expected, f"For input '{text}', expected {expected} but got {output}"
