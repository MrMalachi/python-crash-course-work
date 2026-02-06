def user_profile(first_name, last_name, **info):
    """Return dictionary 'user_dict' containing information about user."""
    user_dict = {
        "first_name": first_name.title(),
        "last_name": last_name.title(),
    }
    if info:
        user_dict["info"] = info

    return user_dict

print(user_profile(
    "malachi",
    "brown",
    hair_color="black",
    eye_color="brown",
    height="5'10"
))