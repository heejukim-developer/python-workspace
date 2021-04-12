print("<나야나>")

def std_weight(height,gender,std_weight):
    print("키 {0}cm {1}의 표준체중은 {2}kg입니다.".format(height,gender,std_weight))
std_weight(175,"남자",round(175*175*0.0022))


def std_weight(height,gender,std_weight):
    print("키 {0}cm {1}의 표준체중은 {2}kg입니다.".format(height,gender,std_weight))
std_weight(170,"여자",round(170*170*0.0021))

print("<유튜브>")
def std_weight(height,gender):
    if gender =="남자":
        return height*height*22
    else:
        return height*height*21
height=175
gender="남자"
weight=round(std_weight(height/100,gender),2)
print("키 {0}cm {1}의 표준체중은 {2}kg입니다.".format(height,gender,weight))

print("희주","희주닉",sep="vs", end=" ?")
print("무엇이 더 재밌을까요 ?")