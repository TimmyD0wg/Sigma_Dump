import random
import time

def ans(cnt):
    if int(cnt) == 0:
        a = input("Wanna Play? Y/N ")
    if int(cnt) > 0:
        a = input("Play Again? Y/N ")

    if a == 'Y':
        print("Yippee! Let's Play!")
        print("Rock...")
        time.sleep(1.5)
        print("Paper...")
        time.sleep(1.5)
        print("Scissors...")
        time.sleep(1.5)
        print("SHOOT!")
        return True
    if a == 'N':
        print("Ok! See U Next Time!")
        return False
    else:
        "Pick A Valid Answer"
        return ans(cnt)
    
cnt = 0
pscore = 0
cscore = 0
answer = ans(cnt)

while(answer):
    c = ["Rock", "Paper", "Scissors"]

    d = input()

    cd = random.choice(c)

    match d:
        case "Rock":
            if cd == "Scissors":
                print(f"{cd}. U Win :)")
                pscore+=1
            if cd == "Paper":
                print(f"{cd}. I Win :)")
                cscore+=1
            if cd == d:
                print(f"{cd}. Tie")


        case "Paper":
            if cd == "Rock":
                print(f"{cd}. U Win :)")
                pscore+=1
            if cd == "Scissors":
                print(f"{cd}. I Win :)")
                cscore+=1
            if cd == d:
                print(f"{cd}. Tie")

    
        case "Scissors":
            if cd == "Paper":
                print(f"{cd}. U Win :)")
                pscore+=1
            if cd == "Rock":
                print(f"{cd}. I Win :)")
                cscore+=1
            if cd == d:
                print(f"{cd}. Tie")

        case default:
            print("Invalid Decision")
    
    cnt+=1

    answer = ans(cnt)

print(f"Final Score: {pscore}:{cscore}. Hope U Had Fun!")




