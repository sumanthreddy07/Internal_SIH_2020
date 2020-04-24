import pickle


with open ('percent_arr_values.txt', 'rb') as fp:
    itemlist = pickle.load(fp)

print(itemlist)
