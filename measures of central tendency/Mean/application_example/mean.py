import pandas as pd

def calc_mean(series):
    return series.mean() if not series.empty else None

# 1 ຄຳນວນຫາຄະແນນສະເລ່ຍຂອງນັກຮຽນ.
students_scores = pd.Series([ 85 , 90 , 78 , 92 , 88 ])
print("Average Scores:", calc_mean(students_scores))