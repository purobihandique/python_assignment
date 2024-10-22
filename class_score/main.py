file1 = open("classscore.txt", "r")

file2 = open("score2.txt", "w") 
    
for line in file1:
    username, score = line.split()
    new_score = int(score) + 5
        
    file2.write(f"{username} {new_score}\n")
        
file2.close()
file1.close()
    
print("Final output:")
file2 = open("score2.txt", "r")
print(file2.readlines())

file2.close()  
