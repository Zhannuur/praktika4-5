# Бастапқы массив
arr = [64, 34, 25, 12, 22, 11, 90]

print("Бастапқы массив:", arr)

# ----------------------------------
# Bubble Sort (Өсу ретімен)
# ----------------------------------
bubble_asc = arr.copy()
n = len(bubble_asc)

for i in range(n):
    for j in range(0, n - i - 1):
        if bubble_asc[j] > bubble_asc[j + 1]:
            bubble_asc[j], bubble_asc[j + 1] = bubble_asc[j + 1], bubble_asc[j]

print("\nBubble Sort (өсу реті):")
print(bubble_asc)

# ----------------------------------
# Bubble Sort (Кему ретімен)
# ----------------------------------
bubble_desc = arr.copy()
n = len(bubble_desc)

for i in range(n):
    for j in range(0, n - i - 1):
        if bubble_desc[j] < bubble_desc[j + 1]:
            bubble_desc[j], bubble_desc[j + 1] = bubble_desc[j + 1], bubble_desc[j]

print("\nBubble Sort (кему реті):")
print(bubble_desc)

# ----------------------------------
# Selection Sort (Өсу ретімен)
# ----------------------------------
selection_asc = arr.copy()
n = len(selection_asc)

for i in range(n):
    min_index = i

    for j in range(i + 1, n):
        if selection_asc[j] < selection_asc[min_index]:
            min_index = j

    selection_asc[i], selection_asc[min_index] = (
        selection_asc[min_index],
        selection_asc[i],
    )

print("\nSelection Sort (өсу реті):")
print(selection_asc)

# ----------------------------------
# Selection Sort (Кему ретімен)
# ----------------------------------
selection_desc = arr.copy()
n = len(selection_desc)

for i in range(n):
    max_index = i

    for j in range(i + 1, n):
        if selection_desc[j] > selection_desc[max_index]:
            max_index = j

    selection_desc[i], selection_desc[max_index] = (
        selection_desc[max_index],
        selection_desc[i],
    )

print("\nSelection Sort (кему реті):")
print(selection_desc)

# ----------------------------------
# sort() әдісі (Өсу ретімен)
# ----------------------------------
sort_asc = arr.copy()
sort_asc.sort()

print("\nsort() әдісі (өсу реті):")
print(sort_asc)

# ----------------------------------
# sort() әдісі (Кему ретімен)
# ----------------------------------
sort_desc = arr.copy()
sort_desc.sort(reverse=True)

print("\nsort() әдісі (кему реті):")
print(sort_desc)

# ----------------------------------
# Уақыт күрделілігі
# ----------------------------------
print("\nУақыт күрделілігі:")
print("Bubble Sort     -> O(n²)")
print("Selection Sort  -> O(n²)")
print("sort() (Timsort)-> O(n log n)")