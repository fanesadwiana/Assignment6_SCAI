from Math_function import add, multiply, divide


def main():

    data_1 = int(input("masukkan input 1 :"))
    data_2 = int(input("masukkan input 2 :"))
    operator = input("masukkan operator :")

    if operator == "+":
        result = add(data_1, data_2)

    print("{} {} {} = {} ".format(data_1, operator, data_2, result))


if __name__ == "__main__":
    print("Hello Main !")
    main()
    

result_mul = multiply(5, 3)
result_div = divide(10, 2)

print("Hasil perkalian:", result_mul)
print("Hasil pembagian:", result_div)
