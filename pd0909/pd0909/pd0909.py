dic1={}
dic2=dict()
dic ={'name':'naeun','phone':'010-1234-5678','birth':'0111'}
a={1:'hi'}
b={'a':[1,2,3]}

#print(dic['name'])
#a['name']='pey'
#print(a)
#b=a.keys()
#print(b)

#a={'name':'spongebob','phone':'01012319872','birth':'0909'}
#b=a.items()
#print(b)

#print(a.get('name'))
#'name' in a
#'school' in a

data={'홍길동':{'베테랑':5.00,'암살':4.70},
      '고길동':{'베테랑':3.90,'뷰티인사이드':4.0}}
score=data.items()
#print(score)

#print(data.get('홍길동'))
#print(data.get('고길동'))
#print(data.get('홍길동').get('암살'))

#제어문

#answer=input("Would you like express shippint?")
#if answer =="yes" :
#    print("That will be an extra $10")

#a=[(1,2),(3,4),(5,6)]
#for (first,last) in a:
#    print(first + last)

#구구단 출력
#for i in range(2,10):
#    for j in range(1,10):      
#        print("%d * %d = %d" %(i, j, i*j))
#    print('')
         
#turtle 예
#import turtle
#for steps in range(4):
#    turtle.forward(100)
#    turtle.right(90)

#import turtle
#for steps in range(4):
#    turtle.forward(100)
#    turtle.right(90)
#    for moresteps in range(4):
#        turtle.forward(50)
#        turtle.right(90)
#사각형 4개 그리기

import turtle
nSides=5
for steps in range(nSides):
    turtle.forward(100)
    turtle.right(360/nSides)
    for moresteps in range(nSides):
        turtle.forward(50)
        turtle.right(360/nSides)         
#오각형 5개 그리기

#import turtle
#for steps in ['red','blue','green','black']:
#    turtle.color(steps)
#    turtle.forward(100)
#    turtle.right(90)
#색깔 변경

