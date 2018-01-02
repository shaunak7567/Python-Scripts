#Names=input("Enter the participants : - ")
Participants=[]
Participants_items=[]

count1=int(raw_input("Enter total number of members - "))

count = 0
while (count < count1):
    Names=raw_input("Enter the participants : - ")
    Participants.append(Names)
    count = count + 1
print(Participants)

def summation(li):
   
    for x in li:
        st=0
        while (st != 7):
        
            price=raw_input(" Enter the value of items for" + " " +x)
            Participants_items.append(int(price))
            if price == "end":
                break
        y=sum(Participants_items)
        print(y)
            
            
    
        
summation(Participants)