import time

timer = 0
isbreak = False

def timer2():
    global timer, isbreak
    try:
        timer = input('時間')
        if timer == 0:
            isbreak = True
    except SyntaxError:
        print('錯誤')
        timer2()

def countdown():
    for i in range(timer):
        time.sleep(1)
        print(timer - i)
    print('時間到了')

while True:
    timer2()
    if isbreak == True:
        break
    countdown()