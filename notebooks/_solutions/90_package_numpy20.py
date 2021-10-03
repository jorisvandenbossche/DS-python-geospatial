# Assign the new values according to the classes
b4_data_classified[b4_data < 0.05] = 10
b4_data_classified[(0.05 <= b4_data) & (b4_data < 0.1)] = 20
b4_data_classified[0.1 <= b4_data] = 30