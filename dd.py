def openstack ():
    print("새로운 주식이 발행되었습니다.")
openstack()

def deposit(balance, money):
    print ("입금완료, 잔액은{0}원입니다.".format(balance + money))
    return balance + money
balance = 0 #잔액
balance = deposit(balance,1000)
print(balance)


def profile(name,age,main_lang):
    print("이름:{0}\t나이:{1}\t주사용언어:{2}"\
        .format(name,age,main_lang))
profile("김희주",26,"파이썬")
profile("김희주닉",26,"자바")

#같은반,같은학년일때

def profile(name,age=17,main_lang="파이썬"):
    print("이름:{0}\t나이:{1}\t주사용언어:{2}".format(name,age,main_lang))
profile("김희주")
profile("김희주닉")

def profile(name,age,main_lang):
    print(name,age,main_lang)
profile(name="김희주",main_lang="파이썬",age=20)
profile(main_lang="파이썬",age=20,name="유재석")


def profile(name,age,lang1,lang2,lang3,lang4,lang5):
    print("이름:{0}\t나이:{1}\t".format(name,age),end=" ")
    print(lang1,lang2,lang3,lang4,lang5)
profile("김희주",26,"python","java","c","c++","c#")
profile("유재석",27,"swith","java","","","")


def profile(name,age,*language):
    print("이름:{0}\t나이:{1}\t".format(name,age),end=" ")
    for lang in language:
        print(lang,end=" ")
profile("김희주",26,"python","java","c","c++","c#")
profile("유재석",27,"swith","java")

gun = 10
def checkpoint(soldiers):
 gun=20
 gun=gun-soldiers
 print("[함수내]남은총:{0}".format(gun))

print("전체 총:{0}".format(gun))
checkpoint(2)
print("남은 총 :{0}".format(gun))
