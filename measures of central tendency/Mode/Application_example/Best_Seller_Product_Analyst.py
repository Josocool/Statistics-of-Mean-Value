from scipy.stats import mode

sales_data = ["ໜັງສື", "ໜັງສື", "ໜັງສື", "ເສື້ອ", "ໂສ້ງ", "ເກີບ", "ກະເປົາ", "ສະລິບ", "ເສື້ອ", "ໜັງສື"]
most_common_product = mode(sales_data)
print("ສິນຄ້າທີ່ຂາຍດີທີສຸດ:", most_common_product.mode[0])


scores = [85, 90, 88, 90, 85, 90, 92, 88, 85, 85]
most_common_score = mode(scores)
print("ຄະແນນທີ່ເກີດຂື້ນດຸທີສຸດ:", most_common_score.mode[0])

genres = ["Action", "Drama", "Comedy", "Action", "Action", "Comedy", "Drama", "Action"]
popular_genre = mode(genres)
print("ແນວໜັງທີ່ຄົນເບິ່ງຫຼາຍທີ່ສຸດ:", popular_genre.mode[0])


order_channels = ["Online", "Store", "Online", "Store", "Store", "Online", "Online", "Store"]
common_channel = mode(order_channels)
print("ຊ່ອງທາງທີ່ລູກຄ້າເລືອກສັ່ງສິນຄ້າຫຼາຍທີ່ສຸດ:", common_channel.mode[0])


colors = ["Red", "Blue", "Red", "Green", "Blue", "Red", "Blue", "Red", "Green"]
favorite_color = mode(colors)
print("ສີເສື້ອທີລູກຄ້າມັກຊື້ຫຼາຍທີ່ສຸດ:", favorite_color.mode[0])


visit_hours = [10, 12, 14, 12, 14, 14, 16, 12, 14, 10, 12]
common_visit_hour = mode(visit_hours)
print("ເວລາໃດທີ່ລູກຄ້າມັກມາຮ້ານຫຼາຍທີ່ສຸດ:", common_visit_hour.mode[0])

