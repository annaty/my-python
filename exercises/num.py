
i = 0   
while i < 5:
    nmber = int(input())
    if nmber <= 10:
        continue
    if nmber >= 100:
        break
    else:
        print(nmber)
    i += 1