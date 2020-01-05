def quick_sort(i, l, r):
    start = numbers[l]
    end = r
    if(start > end):
        return
    while(numbers[start] < numbers[i]):
        start+1
    while(numbers[r] > numbers[i]):
        end-1
    k = numbers[start]
    numbers[start] = numbers[end]
    numbers[end] = k

    return quick_sort()

if __name__ == '__main__':
    numbers = [3, 1, 9, 7, 2, 5]
    print(quick_sort(numbers, 0, 4))

abc = 1
b = 2
