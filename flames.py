#getting names from the user
#removing sapace characters from the string or name
name_1=input("Enter your name:").replace(" ","")
name_2=input("Enter your crush name:").replace(" ","")
#function to getting the values of the string input
def fre_calculator(list_str):
    frequency_str={}
    for i in list_str:
        if i in frequency_str:
            frequency_str[i]+=1
        else:
            frequency_str[i]=1
    return frequency_str
#flames calculator
def flames_calculator(sum):
    arr=['F','L','A','M','E','S']
    for i in range(1,6):
        val=sum
        if val>len(arr):
                while val>len(arr):
                    val=val-len(arr)
                arr.pop(val-1)      
    #loop for rearrrange the list values
                for i in range(0,(len(arr)-val)+1):
                    swap=arr.pop((len(arr)-1))
                    arr.insert(0,swap)         
        else:
            arr.pop(val-1)
    return arr
#convert string to list
list_str_1=list(name_1)
list_str_2=list(name_2)
#getting the frequency of the values in string 1
frequency_str_1=fre_calculator(list_str_1)
#getting the frequency of the values in string 2
frequency_str_2=fre_calculator(list_str_2)
#getting the common values from the two string
common_keys=frequency_str_1.keys() & frequency_str_2.keys()
#sum is the final value to do flames
sum=0
for i in common_keys:
    val_1=abs(frequency_str_1[i]-frequency_str_2[i])
    sum=sum+val_1 
#pop the common values from the two dictionaries
for i in common_keys:
    frequency_str_1.pop(i)
    frequency_str_2.pop(i)   
#adding the remaining frequence to sum value
for i in frequency_str_1:
    val=frequency_str_1[i]
    sum=sum+val
for i in frequency_str_2:
    val=frequency_str_2[i]
    sum=sum+val
#passing the final value to calculator function
result=flames_calculator(sum)
print(result)

        




