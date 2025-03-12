from scipy.stats import mode
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 6, 7, 8, 9]

mode_result = mode(data , keepdims = True)

print("Mode : ", mode_result.mode[0])
print("Frequency : ", mode_result.count[0])