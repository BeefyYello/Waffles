import pytest

from main import victory_message

def test_victory_message_has_been_changed():
    '''This test is meant to ensure that you've changed the message in the function in main.py. Right now it will fail.'''
    what_nate_wrote = "You brought the turtle home safely."
    assert victory_message() != what_nate_wrote
