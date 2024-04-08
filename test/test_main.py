import sys

sys.path.insert(0, '/home/runner/work/DevOpsLab3/DevOpsLab3/src/')

from typing import Tuple, List
from main import get_path_from_arguments
import pytest


@pytest.fixture()
def correct_arguments_string() -> Tuple[List[str], str]:
    return ["-p", "/home/user/file.yml"], \
        "/home/user/file.yaml"


@pytest.fixture()
def noncorrect_arguments_string() -> List[str]:
    return ["/home/user/file.yml"]


def test_get_path_from_correct_arguments(
        correct_arguments_string: Tuple[List[str], str]) -> None:
    path = get_path_from_arguments(correct_arguments_string[0])
    assert path == correct_arguments_string[1]


def test_get_path_from_noncorrect_arguments(
        noncorrect_arguments_string: List[str]) -> None:

    with pytest.raises(SystemExit) as e:
        get_path_from_arguments(noncorrect_arguments_string[0])

    assert e.type == SystemExit
