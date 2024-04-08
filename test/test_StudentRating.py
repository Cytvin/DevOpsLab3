import sys

sys.path.insert(0, '/home/runner/work/DevOpsLab3/DevOpsLab3/src/')

from CalcRating import CalcRating
from Types import DataType
from StudentRating import StudentRating
import pytest


class TestRatingFilter:

    @pytest.fixture()
    def input_data(self) -> tuple[DataType, {}]:
        data: DataType = {
            "Абрамов Петр Сергеевич":
                [
                    ("математика", 100),
                    ("русский язык", 100),
                    ("программирование", 100)
                ],
            "Петров Игорь Владимирович":
                [
                    ("математика", 75),
                    ("русский язык", 75),
                    ("программирование", 75),
                    ("литература", 75)
                ],
            "Тестовый Тест Тестович":
                [
                    ("математика", 50),
                    ("русский язык", 50),
                    ("ОБЖ", 50),
                    ("литература", 50)
                ],
            "Несуществующий студент эвм":
                [
                    ("NotFound", 0),
                    ("NotFound", 0),
                    ("NotFound", 0),
                    ("NotFound", 0)
                ],
            "Существующий студент ивт":
                [
                    ("МЗЯ", 25),
                    ("АрхЭВМ", 25),
                    ("ООП", 25),
                    ("Физика", 25)
                ],
        }

        filtered_rating = {
            "Тестовый Тест Тестович": 50
        }

        return data, filtered_rating

    def test_init_filter_rating(self, input_data: tuple[DataType,
                                {}]) -> None:
        calc_rating = CalcRating(input_data[0]).calc()
        filter_rating = StudentRating(calc_rating).get_second_quartile_students()
        assert input_data[1] == filter_rating

    def test_filter_second_quantile(self, input_data: tuple[DataType,
                                    {}]) -> None:
        calc_rating = CalcRating(input_data[0]).calc()
        filter_rating = StudentRating(calc_rating).get_second_quartile_students()

        assert pytest.approx(filter_rating) == input_data[1]
