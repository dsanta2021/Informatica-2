def makeIncrementer() -> int:
    def addOne(n: int) -> int:
        return n + 1
    return addOne

incrementer = makeIncrementer()
print(incrementer(41))