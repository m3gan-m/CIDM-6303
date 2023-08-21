#Follow the instructions for what to code in this file. 
# Megan Moore
#table1 = [18.1,15.4,19.0,13.4,10.2,13.1,18.1,14.4,15.0,10.8,5.4,12.2,0.7,0.0,0.7,1.0.1.1,0.4,0.0,1.0,2.3,2.9,1.3]
before_wash= [18.1,15.4,19.0,13.4,10.2,13.1,18.1,14.4,15.0,10.8,5.4,12.2]
after_wash= [0.7,0.0,0.7,1.0,1.1,0.4,0.0,1.0,2.3,2.9,1.3]

def cal_average(num1):
    sum_num1 = 0
    for t in num1:
        sum_num1 = sum_num1 + t
    avg=sum_num1/len(num1)
    return avg
        
print("Average mortality rate before hand washing policy: ", cal_average(before_wash))
print("Average mortality rate after hand washing policy: ", cal_average(after_wash))

