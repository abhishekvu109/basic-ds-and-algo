import argparse


class Solution:
    def power(self, N: int, R: int) -> int:
        MOD = 1000000007
        if R == 1:
            return N
        half = self.power(N, R // 2)
        if R % 2 != 0:
            return (N * half * half) % MOD
        else:
            return (half ** 2) % MOD


def main(N: int, R: int):
    solution = Solution()
    result = solution.power(N=N, R=R)
    print(f'Result:{result}')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='put your arguments')
    parser.add_argument('--N', type=str, help='A string argument')
    parser.add_argument('--R', type=str, help='A string argument')
    args = parser.parse_args()
    N = args.N
    R = args.R
    R = N[::-1]
    N = int(N)
    R = int(R)
    main(N=N, R=R)
