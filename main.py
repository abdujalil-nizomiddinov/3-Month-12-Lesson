import os
import time

num_file = "num.txt"

if os.path.exists(num_file):
    with open(num_file, "r") as f:
        num = int(f.read().strip())
else:
    num = 1

for i in range(36):    
    os.system("git add .")
    os.system(f'git commit -m "Run code-{num}"')
    os.system("git push")

    num += 1

    with open(num_file, "w") as f:
        f.write(str(num))
    
    time.sleep(0.5)  

print("Done ✅")