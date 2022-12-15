import turtle

t = turtle.Turtle()

t.color("red")

t.speed(0)                      # 그려지는 속도 조절 



for i in range(1, 10):

    for j in range(1, 6):       # 5개의 선을 이용해서 별을 그린다.

        t.left(144)             # 각도 144도 

        t.forward(200)          # 선 길이 200

    t.left(10)                  # 각 별들 사이에 10도씩 이동해서 그리기 



