import pandas as pd

# 1️⃣ โหลดข้อมูลจากไฟล์ CSV
df = pd.read_csv("D:/Data-Science/Statistics/Descriptive Statistics/measures of central tendency/Mean/application_example/DB/Sales_data.csv", sep=";")


# 2️⃣ คำนวณค่าเฉลี่ยยอดขายต่อเดือน
average_sales = df["Sales"].mean()

# 3️⃣ แสดงผลลัพธ์
print(f"ยอดขายเฉลี่ยรายเดือน: {average_sales:,.2f} บาท")
  