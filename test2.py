
from itertools import count


def start_tests():
    print("------- List tests ------")

    nums = [1, 2, 3, 4, 5, 6]

    # read from the list
    print(nums[0])
    print(nums[1])

    # add elements to the list
    nums.append(9)
    print(nums)

    # for loop
    for n in nums:
        print(n)

    # for loop from 0 to 20
    for number in range(0, 21):
        print(number)


def test1():
    print("test 1")

    prices = [123, 3, 23, 6475, 58, 89, 45, 34, 87,
              34, -12, 23, 123, -23, -123, 0, 123, 0, -29, 10]

    count = 0
    sum = 0
    sum_non_zero = 0
    zeros = 0
    for n in prices:
        sum += n

        if n > 0:
            sum_non_zero += n

        if n == 0:
            zeros += 1

        if n < 50:
            print(n)
            count += 1

    print(f"there are {count} prices lower than $50")


def test2():
    print("------- Test 2 --------")

    users = [
        {
            "gender": "F",
            "name": "Louis",
            "color": "Green"
        },
        {
            "gender": "M",
            "name": "Manuel",
            "color": "Gray"
        },
        {
            "gender": "F",
            "name": "Rossy",
            "color": "Pink"
        },
        {
            "gender": "F",
            "name": "Renny",
            "color": "pink"
        },
        {
            "gender": "M",
            "name": "Roman",
            "color": "Purple"
        },
        {
            "gender": "m",
            "name": "John",
            "color": "Pink"
        },
        {
            "gender": "F",
            "name": "Susan",
            "color": "Black"
        },
    ]

    print(len(users))

    for user in users:
        print(user["name"])

    print("users who like pink")
    for user in users:
        if user["color"] .lower() == "pink":
            print(user["name"])


def test3():
    print("-------- Test 3 --------")

    prices = [123, 3, 23, 6475, 58, 89, 45, 34, 87,
              34, -12, 23, 123, -23, -123, 0, 123, 0, -29, 10]

    # find the most expensive product price
    # soulution = prices []
    # for price is prices
    # if price is greater than your solution
    # your solution is equal to price

    # outside the loop, prices the result

    solution = prices[0]
    for num in prices:
        if num > solution:
            solution = num

    print("The biggest number is " + str(solution))


start_tests()
test1()
test2()
test3()
