def rev_vowels(word):
 string = list()
i=0  
j= len("word")-1
while i < j :
           if [i] not in "aeiouAEIOU":
               i+=1
           elif [j] not in "aeiouAEIOU":
               j-=1
           else:
               [i],[j] = [j] ,[i]
               i+=1
               j-=1
            
        





    
    
   

