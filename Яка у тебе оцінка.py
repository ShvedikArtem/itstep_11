grade = int(input("Введіть чесно свою оцінку: "))
if grade >=0 and grade<=49:
    print("Незадовільно")
elif grade >=50 and grade<=69:
    print("Задовільно")
elif grade >=70 and grade<=89:
    print("Добре")
elif grade >= 90 and grade <= 100:
    print("Відмінно")