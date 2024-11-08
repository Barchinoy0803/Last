colours = [colour for colour in input("Enter the colours: ").split(" ")]
time = 0
for i in range(1, len(colours)):
    if colours[i] != colours[i-1]:    
        time += 1
time += len(colours) * 2   
print(time)     