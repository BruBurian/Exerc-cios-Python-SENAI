def func1(a):
    def func2(a):
        result1 = []
        for i in a:
            if i % 5 == 0:
                result1.append(i)
        return result1
a
    def func3(a):
        result2 = []
        for i in a:
            if i % 7 == 0:
                result2.append(i)
        return result2

    result1 = func2(a)
    result2 = func3(a)
    
    result = list(set(result1 + result2))  # Combina e remove duplicatas
    result = sorted(result)
    
    return result

lst = [i for i in range(101)]
result = func1(lst)
print(result)
