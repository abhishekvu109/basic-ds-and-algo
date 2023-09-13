import argparse


class Solution:
    def display(self, n: int):
        if n == 0:
            return
        else:
            self.display(n - 1)
        print(n, end=" ")


def main(n: int):
    solution = Solution()
    solution.display(n=n)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='put your arguments')
    parser.add_argument('--n', type=str, help='A string argument')
    args = parser.parse_args()
    n = args.n
    n = int(n)
    main(n=n)
