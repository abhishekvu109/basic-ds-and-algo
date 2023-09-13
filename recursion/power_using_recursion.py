import argparse


class Solution:
    def RecursivePower(self, n: int, p: int) -> int:
        if p == 1:
            return n
        half = self.RecursivePower(n, p // 2)
        if p % 2 != 0:
            return n * half * half
        else:
            return half ** 2


def main(n: int, p: int):
    solution = Solution()
    result = solution.RecursivePower(n=n, p=p)
    print(f'Result:{result}')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='put your arguments')
    parser.add_argument('--n', type=str, help='A string argument')
    parser.add_argument('--p', type=str, help='A string argument')
    args = parser.parse_args()
    n = args.n
    p = args.p
    n = int(n)
    p = int(p)
    main(n=n, p=p)
