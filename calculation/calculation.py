import random


def generate_addition():
    # addition and subtraction generating

    a = random.randint(1, 99)
    b = random.randint(1, 99)
    op = random.randint(0, 1)  # +/-
    question = ""
    answer = ""

    if (op == 0) :
        question += str(a) + " + " + str(b) + " = "
        answer += str(a+b)

    else:
        if (a > b):
            question += str(a) + " - " + str(b) + " = "
            answer += str(a - b) 
        else:
            question += str(b) + " - " + str(a) + " = "
            answer += str(b - a)
    
    print(question)
    print(answer)
    #questions.append(question)
    #answers.append(answer)

    return

if __name__ == "__main__":
    generate_addition()






