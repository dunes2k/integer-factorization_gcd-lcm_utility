import os


def clear_display():
    os.system('cls' if os.name == 'nt' else 'clear')


def result_display(result_a, result_b, gcd, lcm):
    print(' ...', end = '')
    print('\n Integer factorization:', result_a[0][0])
    for line_a in result_a:
        divisible = str(line_a[0])
        divider = str(line_a[1])
        print(f' {divisible} / {divider}')
    print(' Integer factorization:', result_b[0][0])
    for line_b in result_b:
        divisible = str(line_b[0])
        divider = str(line_b[1])
        print(f' {divisible} / {divider}')
    print(f' gcd({result_a[0][0]} and {result_b[0][0]}) = {gcd}',
          f'| lcm({result_a[0][0]} and {result_b[0][0]}) = {lcm}')


def gcd_process(result_a, result_b):
    num_a = result_a[0][0]
    num_b = result_b[0][0]
    if num_a < num_b:
        num_a, num_b = num_b, num_a
    while num_b != 0:
        num_a, num_b = num_b, num_a % num_b

    return num_a


def lcm_process(result_a, result_b, gcd):
    result_a = result_a[0][0]
    result_b = result_b[0][0]

    return int(result_a * result_b / gcd)


def integer_factorization(integer_lst):
    prime_numbers = [2, 3, 5, 7]
    if integer_lst[0] < 2 and integer_lst[1] < 2:
        print(' Small numbers! ')
    else:
        number_a = integer_lst[0]
        number_b = integer_lst[1]
        result_a, result_b = [], []
        count_a, count_b = 0, 0

        while number_a > 1:
            if number_a % prime_numbers[count_a] == 0:
                result_a.append([int(number_a), int(prime_numbers[count_a])])
                number_a /= prime_numbers[count_a]
            else:
                count_a += 1
                if count_a > 3:
                    result_a.append([int(number_a), int(number_a)])
                    number_a /= number_a

        while number_b > 1:
            if number_b % prime_numbers[count_b] == 0:
                result_b.append([int(number_b), int(prime_numbers[count_b])])
                number_b /= prime_numbers[count_b]
            else:
                count_b += 1
                if count_b > 3:
                    result_b.append([int(number_b), int(number_b)])
                    number_b /= number_b

        result_a.append([1, ' '])
        result_b.append([1, ' '])
        gcd = gcd_process(result_a, result_b)
        lcm = lcm_process(result_a, result_b, gcd)
        result_display(result_a, result_b, gcd, lcm)


def main_start():
    while True:
        try:
            integer_lst = list(map(int, input(' Input separated by space'
                                              '\n Enter two integers: ').split()))
            if len(integer_lst) == 2:
                clear_display()
                integer_factorization(integer_lst)
            else:
                print(' Two integers are needed! ')
        except ValueError:
            print(' Two integers are needed! ')


main_start()