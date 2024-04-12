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
# Your Solution Score:46637
# number: 6
################################
# Read the input.txt file
def read_input():
    f = open('CSF101CAP/input_6_cap1.txt', 'r')
    print(f.read())
    f.close()

def reader():
    return open('CSF101CAP/input_6_cap1.txt', 'r')

def calculate_score(txt):
   
    totalscore = 0
    store= {'A X': 2, 'A Y': 4, 'A Z': 9, 'B X': 1, 'B Y': 5, 'B Z': 7, 'C X': 1, 'C Y': 6, 'C Z': 7}
    for round in txt: 
        score=round.strip()
        value=store.get(score,None)
        if value is not None:
            totalscore+=value

    print("Total Score:", totalscore)
                
read_input()
calculate_score(reader())




