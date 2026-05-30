count = 0
total = 0
largest = None
smallest = None
while True:
    score = input("Enter score:")
    if score == "done":
        print("done")
        break
    try:
        score = float(score)
    except:
        print("Invalid input")
        continue
    count = count + 1
    total = total + score
    if largest is None or score > largest:
        largest = score
    if smallest is None or score < smallest:
        smallest = score
print("Count:", count)
print("Total:", total)
print("Average:", total / count if count > 0 else 0)
print("Largest:", largest)
print("Smallest:", smallest)