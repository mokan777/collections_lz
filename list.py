from statistics import median
n = int(input("ведите количество элементов в ряду фибоначи:"))

sequence = [0,1]
if n <= 2:
    print(f"ряд фибоначи до {n} элементов:{sequence[:n]}")
else:
    for i in range(2,n):
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)
    for i in range(len(sequence)):
        if sequence[i] % 2 == 0:
            sequence[i] *= 2
        else:
            sequence[i] **= 2
    print(f"ряд фибоначи до {n} эл-тов:{sequence}")


min_value=min(sequence)
max_value=max(sequence)
list_length=len(sequence)
num_elements=len(sequence)
med = median(sequence)
print("минимальный элемент",min_value)
print("максимальный элемент",max_value)
print("длина списка", list_length)
print("количество элементов",num_elements)
print("медианное значение",med)