import pandas as pd

df = pd.DataFrame({'values': [10, 20, 30, 40, 50]})
median_value = df['values'].median()

print("Median:", median_value)  # Output: 30.0

# ວິທີນີ້ເໝາະສຳລັບການວິເຄາະຂໍ້ມູນໃນ DataFrame ຂໍ້ມູນຈາກໄຟລ CSV