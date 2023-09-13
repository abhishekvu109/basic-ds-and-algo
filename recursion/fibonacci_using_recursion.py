import argparse


class Solution:
    def fibonacci(self, n: int) -> int:
        if n == 1 or n == 2:
            return 1
        return self.fibonacci(n - 1) + self.fibonacci(n - 2)


def main(n: int):
    solution = Solution()
    result = solution.fibonacci(n=n)
    print(f'Result:{result}')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='put your arguments')
    parser.add_argument('--n', type=str, help='A string argument')
    args = parser.parse_args()
    n = args.n
    n = int(n)
    main(n=n)
