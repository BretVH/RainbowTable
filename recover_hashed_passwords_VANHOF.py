from timeit import default_timer as timer

file1 = open("RECOVERED_PASSWORD_HASHES.txt")

recovered_hashes = file1.readlines()

file1.close()

file2 = open("RAINBOW_TABLE.txt")

# https://docs.python.org/3/library/functions.html#enumerate
indexed_hashes = list(enumerate(file2))

file2.close()

file3 = open("10K_PLAINTEXT_PASSWORDS.txt")

plaintext_passwords = file3.readlines()

file3.close()

# for each candidate hash in recovered_hashes
for candidate in recovered_hashes:
   # you'll need some way to stop the inner for loop search
   # maybe use a flag variable (True/False)
   startTime = timer()
   candidateFound = False
   for i,hash in indexed_hashes:
       if candidate.rstrip() == hash.rstrip():
          endTime = timer()
          totalTime = (endTime - startTime)*100000
          print("MATCH: hash # " + hash + " = " + plaintext_passwords[i])
          print("The search took ", totalTime , " microseconds\n")
          candidateFound = True
          break
   if candidateFound == False:       
   # this part of the code is to be executed if there is no match after a search through
   # the entire list of indexed_hashes. maybe condition on your flag variable
       endTime = timer()
       totalTime = (endTime - startTime)*100000
       print("NO MATCH FOUND FOR ", candidate.rstrip())
       print("The search took ", totalTime, " microseconds\n")
