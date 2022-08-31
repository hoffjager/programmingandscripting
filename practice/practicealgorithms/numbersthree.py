def has_one(n):
    def isDigitPresent(n, d):
        while (n > 0):
            if (n % 10 == d):
                break
            n = n / 10
            return False
            else:
                return True