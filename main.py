s = 'azcbobobegghakl'

long = temp = s[0]                      # this is the answer if there are no alpha substrings longer than 1
for c in s[1:]:
   if c < temp[-1]:                     # the alpha string is broken
       temp = ""
   temp += c                            # adds c to a continuing substring, or starts a new one
   if len(temp) > len(long):
       long = temp
print("Longest substring in alphabetical order is:", long)