import os

def here(script_path: str = None, *args: str) -> str:
    """Obtain the relative path to directory of the executed script.

    Useful for making projects self-contained, for example by making
    results path relative to the script where they are generated.

    Args:
        script_path (str): path to the current executed script.
        args (str): relative paths to the file or directory of interest.

    Returns:
        str: Absolute path to file/directory of interest.
    """

    if script_path is None:
        raise ValueError("script_path should be set to '__file__'. E.g. ",
                         "here(__file__, 'path', 'to', 'somewhere')")

    script_dir = os.path.dirname(script_path)

    # if args entered, check whether last one ends with "/"
    if len(args) == 0:
        return script_dir
    else:
        last_arg = args[len(args) - 1]
        ends_with_slash = last_arg[len(last_arg) - 1] == "/"

    rel_path = os.path.join(script_dir, *args)
    abs_path = os.path.abspath(rel_path)

    # os.path.abspath() drops last "/"
    # if last arg ended with slash, append this to the end
    if ends_with_slash:
        abs_path = abs_path + "/"

    return abs_path
