with open("study.txt","w",encoding="utf8")as study_file:
    study_file.write("주니어 개발자 김희주")
with open("study.txt","r",encoding="utf8")as study_file:
    print(study_file.read())