import time

timer = 0
isbreak = False

def timer2():
    global timer, isbreak
    try:
        timer = input('時間')
        if timer == 0:
            isbreak = True
    except TypeError:
        print('錯誤')
        timer2()

def countdown():
    for i in range(timer):
        time.sleep(1)
        print(timer - i)
    print('')

while True:
    timer2()
    if isbreak == True:
        break
    countdown()