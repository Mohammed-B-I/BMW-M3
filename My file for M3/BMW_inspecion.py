print("===============================")
print(" BMW M3 2026 FACTORY INSPECTION ")
print("===============================")


vehicle = input("Enter vehicle model: ")

battery = int(input("Enter battery percentage: "))


door_closed = True
engine_fault = False


print()
print("vehicle:", vehicle)

print("Battery: ", battery, "%")

print()

if battery >= 80:
    print("Battery test: PASSED")

else:
    print("Battery test: FAILED")


if battery >= 80 and engine_fault == False:
    print('Vehicle status: APPROVED FOR DELIVERY')

else:
    print('Vehicle status: NEEDS INSPECTION')






    


