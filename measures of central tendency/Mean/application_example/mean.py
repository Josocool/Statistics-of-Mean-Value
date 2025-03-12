import pandas as pd

def calc_mean(series):
    return series.mean() if not series.empty else None

# 1 ຄຳນວນຫາຄະແນນສະເລ່ຍຂອງນັກຮຽນ.
students_scores = pd.Series([ 85 , 90 , 78 , 92 , 88 ])
print("Average Scores:", calc_mean(students_scores))

# 2️⃣ ຄຳນວຫາອຸນຫະພູມສະເລ່ຍອາທິດ
weekly_temperatures = pd.Series([30, 32, 31, 29, 28, 35, 33])
print("ອຸນຫະພູມສະເລ່ຍຂອງອາທິດ :", calc_mean(weekly_temperatures))

# 3️⃣ คำนวณเงินเดือนเฉลี่ยของพนักงาน
salaries = pd.Series([25000, 30000, 28000, 50000, 45000])
print("เงินเดือนเฉลี่ยของพนักงาน:", calc_mean(salaries))

# 4️⃣ คำนวณค่าเฉลี่ยของคะแนนรีวิวสินค้า
product_reviews = pd.Series([4.5, 4.7, 3.8, 4.2, 4.9, 5.0])
print("คะแนนรีวิวเฉลี่ยของสินค้า:", calc_mean(product_reviews))

# 5️⃣ คำนวณระยะทางเฉลี่ยที่รถยนต์ใช้เชื้อเพลิง 1 ลิตร
fuel_efficiency = pd.Series([15.2, 14.8, 16.5, 13.9, 14.2])
print("ระยะทางเฉลี่ยที่ใช้เชื้อเพลิง 1 ลิตร:", calc_mean(fuel_efficiency))

# 6️⃣ คำนวณกำไรเฉลี่ยรายเดือนของบริษัท
monthly_profits = pd.Series([120000, 135000, 110000, 95000, 140000])
print("กำไรเฉลี่ยรายเดือนของบริษัท:", calc_mean(monthly_profits))

# 7️⃣ คำนวณเวลาการทำงานเฉลี่ยต่อวันของพนักงาน
work_hours = pd.Series([8.5, 9.0, 7.5, 8.0, 9.5, 8.8])
print("เวลาทำงานเฉลี่ยต่อวันของพนักงาน:", calc_mean(work_hours))

# 8️⃣ คำนวณค่าเฉลี่ยของความเร็วอินเทอร์เน็ตในพื้นที่
internet_speeds = pd.Series([50, 55, 45, 60, 48, 52])
print("ความเร็วอินเทอร์เน็ตเฉลี่ยในพื้นที่:", calc_mean(internet_speeds))

# 9️⃣ คำนวณอายุเฉลี่ยของประชากรในเมือง
population_ages = pd.Series([25, 30, 27, 35, 40, 29, 33])
print("อายุเฉลี่ยของประชากรในเมือง:", calc_mean(population_ages))

# 🔟 คำนวณน้ำหนักเฉลี่ยของนักกีฬาในทีม
athlete_weights = pd.Series([65, 70, 68, 75, 72, 78])
print("น้ำหนักเฉลี่ยของนักกีฬาในทีม:", calc_mean(athlete_weights))

