# ==========================================
# 1. Linear Search (Сызықтық іздеу)
# ==========================================

numbers = [10, 20, 30, 40, 50]
target = 30

print("=== Linear Search ===")

found = False

for i in range(len(numbers)):
    if numbers[i] == target:
        print(f"{target} элементі {i}-индексте табылды.")
        found = True
        break

if not found:
    print("Элемент табылмады.")

# ==========================================
# 2. Binary Search (Бинарлық іздеу)
# ==========================================

print("\n=== Binary Search ===")

numbers = [10, 20, 30, 40, 50]

target = 30

left = 0
right = len(numbers) - 1

found = False

while left <= right:
    mid = (left + right) // 2

    if numbers[mid] == target:
        print(f"{target} элементі {mid}-индексте табылды.")
        found = True
        break

    elif numbers[mid] < target:
        left = mid + 1

    else:
        right = mid - 1

if not found:
    print("Элемент табылмады.")

# ==========================================
# 3. Палиндромды тексеру
# ==========================================

print("\n=== Палиндромды тексеру ===")

word = input("Сөз енгізіңіз: ")

if word == word[::-1]:
    print("Бұл палиндром.")
else:
    print("Бұл палиндром емес.")

# ==========================================
# 4. 1-ден 10-ға дейінгі сандардың қосындысы
# ==========================================

print("\n=== Қосындыны есептеу ===")

summa = 0

for i in range(1, 11):
    summa += i

print("1-ден 10-ға дейінгі сандардың қосындысы:", summa)