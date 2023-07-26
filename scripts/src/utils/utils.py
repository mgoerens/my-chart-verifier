def add_output(key,value):
    """This function prints the key/value pair to stdout in a "key=value" format.

    This is intended to be piped to GITHUB_OUTPUT so that values can be reused in
    subsequent tasks.
    """

    print(f'{key}={value}')
