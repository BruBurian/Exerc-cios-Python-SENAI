frutas_dic = {
    "maça" : 6000,
    "melão" : 3000,
    "banana" : 5000,
    "laranja" : 4000
}
aaaaaaa
chaves_list = list(frutas_dic.keys())
print("Chaves do dicionário: ", chaves_list)

tem_maca = "maça" in frutas_dic
tem__manga = "manga" in frutas_dic

print("A chave maça está no dicionário?", tem_maca)
print("A chave manga está no dicionário?", tem__manga)
