class Solution:
    def calPoints(self, operations: List[str]) -> int:
        newarry = []
        for n in operations:
            if n == 'D':
                newarry.append(2*newarry[-1])
            elif n == '+':
                newarry.append(newarry[-1]+newarry[-2])
            elif n =='C':
                newarry.pop()
            else:
                newarry.append(int(n))
        return sum(newarry)
        