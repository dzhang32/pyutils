import pytest
import os
from pyutils import here

def test_here_default():
    assert here(__file__) == os.path.dirname(__file__)

def test_here_appends_paths():
    assert here(__file__, "a", "path") == os.path.join(os.path.dirname(__file__), "a", "path")

def test_here_gets_abs_path():
    assert here(__file__, "..") == os.path.abspath(os.path.dirname(__file__) + "/..")

def test_here_keeps_final_backslash():
    assert here(__file__, "..", "dir/") == os.path.abspath(os.path.dirname(__file__) + "/../dir") + "/"

# catching user input errors
def test_here_catches_type_error():
    with pytest.raises(TypeError):
        here(__file__, 1)

def test_here_requires_script_path():
    with pytest.raises(TypeError):
        here()