#ex1
def binarysearch(list1,key):
    start=0
    end=len(list1)-1
    while start< end :
        mid=(start+end)//2
        if list1[mid]==key:
            return True
        elif list1[mid]<key:
            start=mid+1
        else:
            end=mid-1
    return False
binarysearch([5,9,8,3],4)
#Charcters = [“a”, ”b”, ”c”], n = 2
def combination(characters,num,l1):
    if len(l1)==num:
        print(l1)
        return

    for element in characters:
        temp_list1=l1[:]
        temp_list1.append(element)
        combination(characters,num,temp_list1)

characters=["a", "b", "c"]
combination(characters,2,l1=[])

#Exercise 4: Adding a number to a sorted list

def add_num(list3,value):
    value=int(input("enter an integer" ))
    for i in range(0,len(list3)):
        if value<= list3[i]:
            list3.insert(i,value)
            i+=1
        print(list3)

list3=[3,5,9]
add_num(list3,value=4)
#Exercise 3: POS for aamo el dekanje
def posSystem(items_name,barcodeIT,priceIT,avIT):
    new_receipt=input("Do you want new receipt ?  y/n")
    while new_receipt==n:
        break
 #If he chooses yes, he will be prompted for an item barcode and the quantity the client
#purchased. If he answers no, the system exits.
 def receipt(total_cost,total_amount):
       total_cost=priceIT*quantity
       total_amount=sum(total_cost)
    if add_item== "n":
          return receipt(total_cost,total_amount)
      else:
          items = {}
          items[(items_name, barcodeIT)] = priceIT
          quantity = int(input("Enter the quantity "))
          add_item: input("Do you want to add items?  y/n")

#After choosing “yes” and then inputting the barcode and the quantity, aamo l dekanje is asked if
#he would like to add another item to the list.

