class Solution:
    def lcmAndGcd(self, a: int, b: int) -> List[int]:
        def gcd(x, y):
            while y:
                x, y = y, x % y
            return x

        g = gcd(a, b)
        l = (a * b) // g   # LCM formula: (a*b) / gcd
        return [l, g]
