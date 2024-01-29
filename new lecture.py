import datetime
file=open("output.txt","w+")
file.write("This is python programming")
file.write (f"\tISLAMIC UNIVERSITY IN UGANDA\t\n\t Kampala Campus\t\n Name: \t\t Walukagga lauben\n REG NO:\t 223-063012-27651\n Lecturer:\t ABDULHAKIM\n Date:\t\t {datetime.date.today()} \n Course Unit:\t Introduction to structured programming\n\t\t ***END***\t\t")
print(f"\tISLAMIC UNIVERSITY IN UGANDA\t\n\t Kampala Campus\t\n Name: \t\t Walukagga lauben\n REG NO:\t 223-063012-27651\n Lecturer:\t ABDULHAKIM\n Date:\t\t {datetime.date.today()} \n Course Unit:\t Introduction to structured programming\n\t\t ***END***\t\t")