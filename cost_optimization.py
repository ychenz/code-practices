def get_cost(n, m, w2, w3, multiplier):
    if n >= m:
        if multiplier == 2:
            return [w2]
        else:
            return [w3]

    list_c2 = get_cost(n * 2, m, w2, w3, 2)
    list_c3 = get_cost(n * 3, m, w2, w3, 3)
    list = list_c2 + list_c3

    if multiplier == 2:
        for i, cost in enumerate(list):
            list[i] += w2
    else:
        for i, cost in enumerate(list):
            list[i] += w3

    return list


def solution(input):
    for line in input:
        numbers = line.split()
        n = int(numbers[0])
        m = int(numbers[1])
        w2 = int(numbers[2])
        w3 = int(numbers[3])

        if n >= m:
            print(0)
            continue

        list1 = get_cost(n*2, m, w2, w3, 2)
        list2 = get_cost(n*3, m, w2, w3, 3)
        list = list1 + list2
        print(min(list))


if __name__ == "__main__":
    input = [
        "1 6 2 3",
        "4 32 3 4",
        "2 1 1 2",
        "1 2147483647 1 4"
    ]
    solution(input)

