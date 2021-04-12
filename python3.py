#weather="맑아요"
#if weather =="비":
    #print("우산을 챙기세요")
#elif weather == "미세먼지":
   #print("마스크를 챙기세요")
#else:
  #print("준비물이 필요없어요")

#input

#weather=input(" 오늘 날씨 어때요 ")
#if weather == "비" or weather=="눈":
    #print("우산을 챙기세요")
#elif weather== "미세먼지":
    #print("마스크를 챙기세요")
#else:
    #print("준비물이 필요없어요")

#temp = int(input("기온은 어때요?"))
#if 30<= temp:
    #print("너무 더워요. 나가지 마세요")
#elif 10<=temp and temp<30 :
    #print("괜찮은 날씨에요")
#elif 0<= temp<10:
    #print("외투를 챙기세요")
#else:
    #print("너무 추워요. 나가지 마세요")

for 희주식당대기번호 in range(5):
    print("대기번호:{0}".format(희주식당대기번호))

starbucks =["희주","희촐씨","언니","스승님"]
for customers in starbucks:
    print ( "{0}님 커피가 준비 되었습니다.".format(customers,[0]))
    print ( "{0}님 프라푸치노가 준비 되었습니다.".format(customers[:3]))

#while
customer="희주닉"
index=5
while index >= 1:
    print("{0}님 커피가 준비되었습니다.{1}번 남았어요.".format(customer,index))
    index -= 1
    if index == 0:
        print("커피는 폐기처분되었습니다.")

customer="희주닉"
종업원="unknown"
while 종업원 != customer:
    print("{0}님 커피가 준비되었습니다".format(customer))
    종업원=input("이름이 어떻게 되세요")


absent = [2, 5]
no_book =[7]
for student in range(1, 11):
    if student in absent:
     continue
    elif student in no_book:
        print("오늘 수업 여기까지. {0}는 교무실로 따라와."format (student))
        break
print("{0}번,책읽어봐".format(student))


student=[1,2,3,4,5]
print(student)
student=[i+100 for i in student]