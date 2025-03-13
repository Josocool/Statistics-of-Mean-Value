import numpy as np

# sale month analyst 

monthly_sales = [1000,1200,1100,1300, 1500]
variance_sales = np.var(monthly_sales)
std_deviation_sales = np.std(monthly_sales)


print("ຍອດຂາຍເດືອນ Variance :", variance_sales)
print("ຍອດຂາຍເດືອນ standard deviation :", std_deviation_sales)



# estimate costs

monthly_expenses = [1200, 1500 , 1650 ,1400, 1550 , 1800] 
variance_expenses = np.var(monthly_expenses)

std_deviation_expenses = np.std(monthly_expenses)

print ("ຄ່າໃ້ຊຈ່າຍປະຈຳເດືອນ : ", variance_expenses)
print ("ຄ່າໃ້ຊຈ່າຍປະຈຳເດືອນ : ", std_deviation_expenses)
