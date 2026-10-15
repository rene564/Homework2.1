height = float(input())/100
weight = float(input())
bmi = weight / (height ** 2)
print(bmi)
if bmi < 16:
    print("выраженный дефицит массы тела")
elif bmi < 18.5:
    print("недостаточная масса тела")
elif bmi < 25:
    print("норма")
elif bmi < 30:
    print("избыточная масса тела")
elif bmi < 35:
    print("ожирение первой степени")
elif bmi < 40:
    print("ожирение второй степени")
else:
    print("ожирение третьей степени")