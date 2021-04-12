#type이 set
알바계={"희철씨","언니","스승님","희주"}
print(알바계,type(알바계))
#type이 list
알바계=list(알바계)
print(알바계,type(알바계))
#type이 tuple
알바계=tuple(알바계)
print(알바계,type(알바계))

알바계=set(알바계)
print(알바계,type(알바계))

from random import *
users=range(1,21)
#print(type(users))
users=list(users)
#print(type(users))
print(users)
shuffle(users)
print(users)
winners=sample(users,4)
print("--당첨자발표--")
print("치킨당첨자:{0}".format(winners[0]))
print("커피당첨자:{0}".format(winners[1:]))
print("--축하합니다--")



print("<알바계 조개구이 날짜 정하기>")
from random import*
id=range(1,31)
#print(type(id))
id=list(id)
#print(type(id))
shuffle(id)
#print(id)
당첨일=sample(id,4)
print("--11월 알바계 회식 날짜 랜덤 발표---")
print("가능성이 높은 날:{0}".format(당첨일[0]))
print("가능성이 다음으로 높은 날:{0}".format(당첨일[1:]))
print("----11월엔 꼭 조개구이를 먹읍시다---")

