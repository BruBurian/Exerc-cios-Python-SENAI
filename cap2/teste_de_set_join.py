s1 = {10, 20, 30, 40}
s2 = {30, 40, 50, 60, 70}

result1 = s1 | s2      # União de s1 e s2
result2 = s1 & s2      # Interseção de s1 e s2
result3 = s1 - s2      # Diferença entre s1 e s2
result4 = s1 ^ s2      # Diferença simétrica entre s1 e s2
result5 = s1.issubset(s2)   # Verifica se s1 é subconjunto de s2
result6 = s1.issuperset(s2) # Verifica se s1 é superconjunto de s2
result7 = s1.isdisjoint(s2) # Verifica se s1 e s2 são disjuntos

print("1) s1 | s2 =", result1)
print("2) s1 & s2 =", result2)
print("3) s1 - s2 =", result3)
print("4) s1 ^ s2 =", result4)
print("5) s1.issubset(s2) =", result5)
print("6) s1.issuperset(s2) =", result6)
print("7) s1.isdisjoint(s2) =", result7)