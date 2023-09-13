def tower_of_hanoi(n: int, rod1: int, rod2: int, rod3: int):
    if n == 1:
        print(f'move disk {n} from rod {rod1} to rod {rod3}')
        return
    tower_of_hanoi(n - 1, rod1, rod3, rod2)
    print(f'move disk {n} from rod {rod1} to rod {rod3}')
    tower_of_hanoi(n - 1, rod2, rod1, rod2)



def main():
    tower_of_hanoi(2, 1, 2, 3)


if __name__ == '__main__':
    main()
