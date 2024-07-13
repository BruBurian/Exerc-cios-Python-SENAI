student_tuple = [('211101', 'David Doe', '010-123-1111'), ('211102', 'John Smith', '010-123-2222'), ('211103', 'Jane Carter', '010-123-3333')]

student_dict = {student[0]: student[1] for student in student_tuple}

print("Dicionário de estudantes:")
for id_student, name in student_dict.items():
    print(f"{id_student} : {name}")

while True:
    student_id = input("\nDigite o número de identificação do estudante: ")
    if student_id in student_dict:
        student_name = student_dict[student_id]
        student_phone = [student[2] for student in student_tuple if student[0] == student_id][0]
        print(f"O aluno {student_id} é {student_name} e o número de telefone é {student_phone}.")
        break
    else:
        print("Número de identificação de estudante inválido. Tente novamente.")