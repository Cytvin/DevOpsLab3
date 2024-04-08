import pandas as pd

class StudentRating:
    def __init__(self, student_ratings):
        self.df = pd.DataFrame(list(student_ratings.items()), columns=['student', 'rating'])

    def get_second_quartile_students(self):
        Q1 = self.df['rating'].quantile(0.25)
        Q2 = self.df['rating'].quantile(0.50)

        second_quartile_students = self.df[(self.df['rating'] > Q1) & (self.df['rating'] <= Q2)]

        students = {}
        for index, row in second_quartile_students.iterrows():
            students[row['student']] = row['rating']
        
        return students
