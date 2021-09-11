import os

def get_rel_path(rel_path: str, path: str = __file__) -> str:
    """Obtain the relative path to (by default), the current script.
    Useful for making paths in projects self-contained.

    @type rel_path: str
    @param rel_path: Relative path from script_path to directory of
    interest.
    @type path: str
    @param path: path to script of, by default obtained through
    '__file__'.
    @rtype: str
    @returns: Absolute path to directory of interest.
    """

    script_dir = os.path.dirname(path)
    rel_dir = os.path.join(script_dir, rel_path)

    # convert this back to absolute path for printing
    rel_dir = os.path.abspath(rel_dir)

    return rel_dir
