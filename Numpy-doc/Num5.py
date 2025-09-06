#How to get unique items and counts
import numpy as np

#You can find the unique elements in an array easily with np.unique
data_set = ['Hung', 'Minh', 'Phuc', 'David', 'David', 'Minh', 'Bao', 'Bao', 'Hung']
mix = np.unique(data_set)
print(mix)

#To get the indices of unique values in a NumPy array(an array of first index positions of unique values in the array)
mix, indices_list = np.unique(data_set, return_index=True)      #pass return_index
print(mix, indices_list)

#You can pass the return_counts argument in np.unique() along with your array to get the frequency count
mix, occurrence_count = np.unique(data_set, return_counts=True)  #pass return_count
print(mix, occurrence_count)     #Đếm số lần xuất hiện

data_set2 = np.array([['Minh', 'Phat', 'Phu', 'Nguyen'],
                      [8, 5, 7, 10],
                      ['B+', 'C', 'B', 'A'],
                      [8, 5, 7, 10]])
mix2 = np.unique(data_set2, axis=0)
print(mix2)
mix2, indices, occurrence_count = np.unique(
     data_set2, axis=0, return_counts=True, return_index=True)
print(indices)
print(occurrence_count)

