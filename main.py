import pickle


lending_list = list(pickle.load(open("lending_data.bin", "rb")))
print(lending_list)
