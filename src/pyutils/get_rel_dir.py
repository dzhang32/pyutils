import os

def get_rel_dir(path: str, rel_dir: str) -> str:
    """Obtain the relative path to (by default), the current script.
    Useful for making paths in projects self-contained.

    @type path: str
    @param path: path to script. The path of the current, executed
    script can be obtained through "__file__".
    @type rel_dir: str
    @param rel_dir: Relative path from script_path to directory of
    interest. This must be to a directory, i.e. not a file as
    os.path.abspath() drops the final "/"
    @rtype: str
    @returns: Absolute path to a directory of interest.
    """

    script_dir = os.path.dirname(path)
    rel_dir = os.path.join(script_dir, rel_dir)

    # convert this back to absolute path for printing
    rel_dir = os.path.abspath(rel_dir)

    # add "/" that would be potentially dropped by
    # os.path.abspath
    rel_dir = rel_dir + "/"

    return rel_dir
