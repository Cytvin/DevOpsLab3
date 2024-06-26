import sys

sys.path.insert(0, '/home/runner/work/DevOpsLab3/DevOpsLab3/src/')

import pytest
from typing import Tuple
from Types import DataType
from YamlDataReader import YamlDataReader


class TestTextDataReader:
    @pytest.fixture()
    def file_and_data_content(self) -> Tuple[str, DataType]:
        text = "Иванов Константин Дмитриевич:\n" + \
            "- математика: 91\n" + "- химия: 100\n" + \
            "Петров Петр Семенович:\n" + \
            "- русский язык: 87\n" + "- литература: 78\n"
        data = {
            "Иванов Константин Дмитриевич": [
                ("математика", 91), ("химия", 100)
            ],
            "Петров Петр Семенович": [
                ("русский язык", 87), ("литература", 78)
            ]
        }
        return text, data

    @pytest.fixture()
    def filepath_and_data(self,
                          file_and_data_content: Tuple[str,
                                                       DataType],
                          tmpdir) -> Tuple[str,
                                           DataType]:
        p = tmpdir.mkdir("datadir").join("my_data.txt")
        with open(p, "w", encoding="utf-8") as test_file:
            test_file.write(file_and_data_content[0])
        return str(p), file_and_data_content[1]
    
    def test_read(self, filepath_and_data:
                  Tuple[str, DataType]) -> None:
        file_content = YamlDataReader().read(filepath_and_data[0])
        assert file_content == filepath_and_data[1]
