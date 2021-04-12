scores={"희철":100,"희주":90,"은정":95}
for subject,score in scores.items():
   #print(subject,score)
    print(subject.ljust(8),str(score).rjust(4),sep=":")

answer = input("언제쯤 개발자가 될까요?")
print("당신은"+answer+"판교에 입성합니다.")

score_file=open("희주월드.txt","w",encoding="utf8")
print("파이썬:20",file=score_file)
print("자바:100",file=score_file)
score_file.close()

score_file=open("희주월드.txt","a",encoding="utf8")
score_file.write("과학:80")
score_file.write("\n코딩:80")
score_file.close()

score_file=open("희주월드.txt","r",encoding="utf8")
print(score_file.read())
score_file=close()

with open("study.txt","w",encoding="utf8")as study_file:
    study_file.write("주니어 개발자 김희주")
