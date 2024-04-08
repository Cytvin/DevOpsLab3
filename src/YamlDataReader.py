import yaml
from Types import DataType
from DataReader import DataReader

class YamlDataReader(DataReader):
    def __init__(self) -> None:
        self.key: str = ""
        self.students: DataType = {}

    def read(self, path: str) -> DataType:
        with open(path, encoding='utf-8') as stream:
            data = yaml.safe_load(stream)
            for key, value in data.items():
                self.key = key
                self.students[self.key] = []
                for subj in value:
                    for key, value in subj.items():
                        self.students[self.key].append(
                            (key, int(value)))
                    
        return self.students
            
            
