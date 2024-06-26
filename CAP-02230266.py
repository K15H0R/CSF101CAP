################################
# KISHOR KUMAR GHALLEY
# MECHANICAL ENGINEERING
# 02230266
################################
# REFERENCES:
# https://www.dataquest.io/blog/read-file-python/#:~:text=Python%20provides%20a%20built%2Din,we%20can%20manipulate%20its%20content
# https://youtu.be/TSHEnfUz6wk?si=D6w-DN9uMU0GxUaV
################################
# SOLUTION
# Your Solution Score:50223
# number: 6
################################
def read_input():
    f = open('CSF101CAP/input_6_cap1.txt', 'r')
    print(f.read())
    f.close()

def reader():
    A= open('CSF101CAP/input_6_cap1.txt', 'r')
    return A

def calculate_score(txt):
   
    totalscore = 0
    scorestore= {'A X': 3, 'A Y': 4, 'A Z': 8, 'B X': 1, 'B Y': 5, 'B Z': 9, 'C X': 2, 'C Y': 6, 'C Z': 7}
    for round in txt: 
        score=round.strip()
        scorevalue=scorestore.get(score,None)
        if scorevalue is not None:
            totalscore+=scorevalue

    print("Total Score:", totalscore)
                
read_input()
calculate_score(reader())
