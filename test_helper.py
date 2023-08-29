import pytest
import helper
import datetime


def test_add():
    # Given: I want to add a to-do with a date
    text = "Lorem ipsum"
    date = "2023-12-25"

    # When: I add the item
    helper.add(text, datetime.datetime.strptime(date, "%Y-%m-%d"))

    # Then: The to-do should have a date
    item = helper.items[-1]
    assert isinstance(item.date, datetime.date)
