class Estudante:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.eng_quiz = 0
        self.math_quiz = 0
        self.science_quiz = 0
aaaaaa
    def __str__(self):
        return (f"Nome : {self.name}, ID : {self.student_id}\n"
                f"Nota no quiz em inglês: {self.eng_quiz}, Nota no quiz em matemática: {self.math_quiz}\n"
                f"Resultado do quiz científico: {self.science_quiz},\n"
                f"Total : {self.get_total_score()}, Média : {self.get_avg_score():.1f}")

    def set_eng_quiz(self, score):
        self.eng_quiz = score

    def set_math_quiz(self, score):
        self.math_quiz = score

    def set_science_quiz(self, score):
        self.science_quiz = score

    def get_name(self):
        return self.name

    def get_student_id(self):
        return self.student_id

    def get_eng_quiz(self):
        return self.eng_quiz

    def get_math_quiz(self):
        return self.math_quiz

    def get_science_quiz(self):
        return self.science_quiz

    def get_total_score(self):
        return self.eng_quiz + self.math_quiz + self.science_quiz

    def get_avg_score(self):
        return self.get_total_score() / 3

# Solicitação dos dados do estudante
nome = input("Digite o nome do estudante: ")
id_estudante = int(input("Digite o ID do estudante: "))
pontuacao_eng = int(input("Digite a pontuação do aluno no quiz de inglês: "))
pontuacao_math = int(input("Digite a pontuação do estudante no quiz de matemática: "))
pontuacao_science = int(input("Digite a pontuação do estudante no quiz de ciências: "))

# Criação da instância do estudante
my_student = Estudante(nome, id_estudante)

# Definindo as pontuações dos quizzes
my_student.set_eng_quiz(pontuacao_eng)
my_student.set_math_quiz(pontuacao_math)
my_student.set_science_quiz(pontuacao_science)

# Exibindo os resultados
print(my_student)
