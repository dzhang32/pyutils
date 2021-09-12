import os

def here(*args: str) -> str:
    """Obtain the relative path to directory of the executed script
    or the current working directory (in JNBs). Useful for making
    projects self-contained.

    For R users, this will be similar to the here::here() function,
    however the base path used will be the directory of the executed
    script or current working directory (in JNBs), rather than the
    project working directory set by .Rproj.

    @type args: str
    @param args: the paths that denote the relative path to the file
    or directory of interest.
    @rtype: str
    @returns: Absolute path to file/directory of interest.
    """

    # __file__ runs into NameError in JNBs
    try:
        path = __file__
    except NameError:
        path = os.path.abspath("")

    # if args entered, check whether last one ends with "/"
    if len(args) == 0:
        return path
    else:
        last_arg = args[len(args) - 1]
        ends_with_slash = last_arg[len(last_arg) - 1] == "/"

    rel_path = os.path.join(path, *args)
    abs_path = os.path.abspath(rel_path)

    # os.path.abspath() drops last "/"
    # if last arg ended with slash, append this to the end
    if ends_with_slash:
        abs_path = abs_path + "/"

    return abs_path
