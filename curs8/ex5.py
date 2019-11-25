with open('ex1.txt') as f:
    # print(f.read())
    for l in f.readlines():
        print(l, end="")
    f.close()

with open('ex2.txt', 'w') as f:
    for i in range(10):
        f.write(f'line_{i}\n')
    f.close()
