import argparse


class Solution:
    def powerset_util(self, s: str, i: int, h: str, output: []) -> []:
        if i >= len(s):
            output.append(h)
            return output
        include = self.powerset_util(s, i + 1, (h + s[i]), output)
        exclude = self.powerset_util(s, i + 1, h, include)
        return exclude

    def powerset(self, s: str):
        list = self.powerset_util(s, 0, "", [])
        list.sort()
        for s in list:
            print(s, end=" ")


def main(s: str):
    solution = Solution()
    solution.powerset(s=s)


if __name__ == "__main__":
    n = "abc"
    main(s=n)
