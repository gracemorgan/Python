n=int(input("Enter the number of students:"))
scores=[]
highest_score=0
second_highest=0
i=0
while i<n:
    print("Enter scores",i+1,":")
    score=int(input())
    scores.append(score)
    i+=1
    if score>highest_score:
        second_highest=highest_score
        highest_score=score
    
print("The second highest score was",second_highest)



    
