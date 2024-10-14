#1- Write the recursive version of binary search.
def binarysearch(list1,key):
 start==0
 end==len(list1)-1
 while start<=end:
    mid=(start +end)//2
    if mid==key:
        return True

    elif mid<key:
        start=mid +1
    else:
        end=mid-1
 return False
#Exercise 2
#Given a list of characters and an integer n, generate, using recursion, all possible combinations of length n that contain the characters in the list.





def generate_combinations(characters, n, current_combination="", index=0):
  """Generates all possible combinations of length n using recursion.

  Args:
    characters: A list of characters.
    n: The desired length of the combinations.
    current_combination: The current combination being built.
    index: The current index in the characters list.

  Returns:
    A list of all possible combinations.
  """

  if len(current_combination) == n:
    return [current_combination]

  combinations = []
  for i in range(index, len(characters)):
    new_combination = current_combination + characters[i]
    combinations.extend(generate_combinations(characters, n, new_combination, i))

  return combinations

# Example usage
characters = ["a", "b", "c"]
n = 2
combinations = generate_combinations(characters, n)
print(combinations)


#Exercise 4 : Adding a number to a sorted list
#Given a sorted list of integers, and an integer value, add value to the correct position of the list.
def insert_number(list1, val):
    if not list1 or val <= list1[0]:
        return [val] + list1
left, right == 0, len(list1) - 1
while left <= right:
    mid = (left + right) // 2
    if list1[mid] == val:
      # If val is already in the list, insert it after the existing occurrences
      while mid < len(list1) and list1[mid] == val:
        mid += 1
      break
    elif list1[mid] < val:
      left = mid + 1
    else:
      right = mid - 1

  # Insert val at the appropriate position
list1.insert(left, val)
return list1

# Example usage:
list1 = [1, 34, 56, 78, 89]
val = 77


#Exercise 3: POS for aamo el dekanje

def receipt1(receipt[],items[], quantity):
receipt==receipt[]
items==items[]

while True:
    start_new_receipt = input("Do you want to start a new receipt? (yes/no): ")
    if start_new_receipt.lower() =="no":
        break

    receipt = Receipt()
    while True:
        barcode = input("Enter the barcode of the item: ")
        if barcode not in items:
            print("Invalid barcode. Please try again.")
            continue
        quantity = int(input("Enter the quantity: "))
        item = items[barcode]
        receipt.add_item(item, quantity)

        add_another_item = input("Do you want to add another item? (yes/no): ")
        if add_another_item.lower()== "no":
            break
    receipt.print_receipt()
