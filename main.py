import os
import time

# Fayl orqali oxirgi commit raqamini saqlaymiz
num_file = "num.txt"

# Agar fayl mavjud bo'lsa, ichidagi sonni o'qiymiz, aks holda 1 dan boshlaymiz
if os.path.exists(num_file):
    with open(num_file, "r") as f:
        num = int(f.read().strip())
else:
    num = 1

# 35 marta commit qilish uchun sikl
for i in range(35):
    print(f"Commit qilinmoqda: {num}")  # Terminalga chiqadi
    
    # Git buyruqlarini terminalda bajarish
    os.system("git add .")
    os.system(f'git commit -m "simile-{num}"')
    os.system("git push")

    # Yangi commit raqamini oshiramiz
    num += 1

    # Faylga yangi commit raqamini yozamiz
    with open(num_file, "w") as f:
        f.write(str(num))
    
    # Har bir commit orasida 1 soniya kutish (ixtiyoriy)
    time.sleep(1)  

print("✅ 35 ta commit bajarildi!")
