from name_function import get_formatted_name

def test_first_last_name():
    """Do names like 'Malachi Brown' work?"""
    formatted_name = get_formatted_name("malachi", "brown")
    assert formatted_name == "Malachi Brown"

def test_first_last_middle_name():
    """Do names like 'Malachi Nathaniel Brown' work?"""
    formatted_name = get_formatted_name(
        "malachi", "brown", "nathaniel"
    )
    assert formatted_name == "Malachi Nathaniel Brown"