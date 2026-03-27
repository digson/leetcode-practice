class Solution:
    def myAtoi(self, s: str) -> int:
        isnegative = False
        sol =""
        result = 0
        for char in s.replace(" ",""):
            if char == '-':
                isnegative = True
            elif not s.isdigit():
                break
            else:
                sol += char
        result = -1*int(sol) if isnegative else int(sol)
        return result