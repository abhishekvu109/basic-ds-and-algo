import argparse


class Solution:
    def sum_of_digits(self, n: int) -> int:
        if n <= 0:
            return 0
        else:
            return n % 10 + self.sum_of_digits(n // 10)


def main(n: int):
    solution = Solution()
    result = solution.sum_of_digits(n=n)
    print(f'Result:{result}')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='put your arguments')
    parser.add_argument('--n', type=str, help='A string argument')
    args = parser.parse_args()
    n = args.n
    n = int(n)
    main(n=n)
