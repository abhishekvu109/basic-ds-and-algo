import argparse


class Solution:
    def count_of_digits(self, n: int) -> int:
        if n <= 0:
            return 0
        else:
            return 1 + self.count_of_digits(n // 10)


def main(n: int):
    solution = Solution()
    result = solution.count_of_digits(n=n)
    print(f'Result:{result}')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='put your arguments')
    parser.add_argument('--n', type=str, help='A string argument')
    args = parser.parse_args()
    n = args.n
    n = int(n)
    main(n=n)
