def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info

print(build_profile(
    "malachi",
    "brown",
    hair_color="brown",
    height="5'10",
    age="27",
    ))




