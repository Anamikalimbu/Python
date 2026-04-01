 def counts(word):
     volews="aeiouAEIOU"
     num_count = 0
     c_count = 0
    
     for char in word:
         if char.isdigit():
             num_count +=1
         elif char.isalpha() and char not in volews:
             c_count +=1
     return num_count, c_count
 num_count, c_count = counts("Python123456")
 print("Number of digits:", num_count)
 print("Number of consonants:", c_count)
