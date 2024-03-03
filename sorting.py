# Функція сортування бульбашкою
def bubble_sort(arr):
    
    n = len(arr)
    for i in range(n):

        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


if __name__ == "__main__":
    unsorted_list = [64, 34, 25, 12, 22, 11, 90]
    sorted_list = bubble_sort(unsorted_list)
    print("Отсортований список:", sorted_list)
