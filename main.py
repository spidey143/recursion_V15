def max_c(N):
    if N < 10:
        return N
    x = max_c(N // 10)
    y = N % 10
    if y > x:
        return y
    else:
        return x


if __name__ == '__main__':
    N = int(input('Введите натуральное число: '))
    if N<0:
        print('Введите другое число')
    else:
        print(max_c(N))