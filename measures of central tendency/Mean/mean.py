def calc_mean(data):
    return sum(data) / len(data) if len(data) > 0 else None
#Exa
data = [10, 15, 20, 25, 30]
mean_value = calc_mean(data)
print(f"Mean: {mean_value}")