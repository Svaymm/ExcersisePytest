import pytest

def format_user(userdata, format):
    result = ""
    u = userdata["name"]
    if format == "greeting":
        result = "{}, {} {}".format(u["last"], u["first"], u["last"])
    elif format == "short":
        result = "{}{}".format(u["title"], u["last"])
    elif format == "country":
        result = userdata["nat"]
    elif format == "table":
        result = "{} | {} | {} ".format(u["first"], u["last"], u["title"])
    else:
        result = None

    return result


pytest.main(["-v"])