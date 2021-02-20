

A = [1, 7, 2, 8, 223, 23, 123, 98, 3, 5, 2, 65]


def bubble_sort(A):
    # TODO: dopisz implementację sortowania bąbelkowego (BubbleSort)

    return A



# tests
A_sorted = sorted(A)

A_bubble_sorted = bubble_sort(A)

for i in range(len(A)):
    if A_sorted[i] != A_bubble_sorted[i]:
        print("List is not sorted correctly")
        break
else:
    print("Congrats! List is sorted!")

