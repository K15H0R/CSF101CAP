################################
# KISHOR KUMAR GHALLEY
# MECHANICAL ENGINEERING
# 02230266
################################
# REFERENCES
# https://www.dataquest.io/blog/read-file-python/#:~:text=Python%20provides%20a%20built%2Din,we%20can%20manipulate%20its%20content
# https://youtu.be/TSHEnfUz6wk?si=D6w-DN9uMU0GxUaV
################################
# SOLUTION
# Your Solution Score:50023
# number: 6
################################
# Read the input.txt file
def read_input():
    f = open('CSF101CAP/input_6_cap1.txt', 'r')
    round=f.read()
    print(round)
    f.close()

def calculate_score():
    print("\n calculation:")
    print("\nmarking system:\n win=6 \n lose=0 \n draw=3")
    print("score will be added by\n 1 if rock\n 2 if paper \n 3 if sissor")
    print("representaion:\n A is rock \n B is paper \n C is sissor \n x =lose \n y= draw \n z= win")

    f = open('CSF101CAP/input_6_cap1.txt', 'r')
    rounds=f.read()
    totalscore = 0
    for round in rounds: 
        opponentchoice =round  #appointing round to opponentchoice
        
        
        if opponentchoice == "A":
            totalscore += 1  #1 for rock
        elif opponentchoice == "B":
            totalscore += 2  #2 for paper
        elif opponentchoice == "C":
            totalscore += 3  #3 for sissors
        elif opponentchoice == "X":
            totalscore += 0 # 0 for losing
        elif opponentchoice == "Y":
            totalscore += 3  # 3 for draw 
        elif opponentchoice == "Z":
            totalscore += 6  # 6 for winning 
       

    print("Total Score:", totalscore)
        
read_input()
calculate_score()




