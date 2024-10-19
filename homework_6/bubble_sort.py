def bubble_sort(unsorted_list):

  n = len(unsorted_list)

  for i in range(n-1):
    for j in range(0, n-i-1):
      if unsorted_list[j] > unsorted_list[j+1] :
        unsorted_list[j], unsorted_list[j+1] = unsorted_list[j+1], unsorted_list[j]
  return unsorted_list

my_list = [64, 34, 25, 12, 0, 22, 11, 90, 1000]
sorted_list = bubble_sort(my_list)
print("Отсортированный список :", sorted_list)