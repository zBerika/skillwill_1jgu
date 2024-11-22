import time

with open('sia.py', 'r', encoding='utf-8') as file:
    lines = file.readlines()

Tbilisi = 'Tbilisi'

for line in lines:
    print(line.strip())
    time.sleep(1)

    if Tbilisi in line:
        with open('Tbilisi.py', 'a', encoding='utf-8') as file:
            file.write(line)
        print(f"ganawilda - 'Tbilisi.py'.")
    else:
        with open('Batumi.py', 'a', encoding='utf-8') as file:
            file.write(line)
        print(f"ganawilda - 'Batumi.py'.")