#find the duplicate number--------------------O(n^2) notation
numbers=[3,6,2,4,3,6,8,9]
for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
      if numbers[i]==numbers[j]:
        print(numbers[i])
        break