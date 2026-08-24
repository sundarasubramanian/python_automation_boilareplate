def assert_equal(actual, expected, message=None):
    if message is None:
        message = f'Expected: {expected} but got: {actual}'
    assert actual == expected, message
