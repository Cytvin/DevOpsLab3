from YamlDataReader import YamlDataReader
from CalcRating import CalcRating
from StudentRating import StudentRating
import argparse
import sys


def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p", dest="path", type=str, required=True,
                        help="Path to datafile")
    args = parser.parse_args(args)
    return args.path


def main():
    path = get_path_from_arguments(sys.argv[1:])
    reader = YamlDataReader()
    students = reader.read(path)
    print("Students: ", students)
    rating = CalcRating(students).calc()
    rating = dict(sorted(rating.items(), key=lambda x:x[1]))
    print("Rating: ", rating)
    sr = StudentRating(rating)
    second_quartile_students = sr.get_second_quartile_students()
    print("Student in second quartile: ", second_quartile_students)

if __name__ == "__main__":
    main()
