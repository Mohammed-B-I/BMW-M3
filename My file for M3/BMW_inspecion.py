print(" BMW FACTORY INSPECTION SYSTEM ")
print("===============================")


def battery_check(battery):


    if battery >= 80:
        print("Battery is OK")
        return True
    else:
        print("Battery Failed")
        return False


    

def engine_check(engine):


    if engine.lower() == "good":
        print("Engine is OK")
        return True
    else:
        print("Engine Failed")
        return False



inspection = "yes"
inspection_number = 1


while inspection == "yes":


    print(f"Inspection Number: {inspection_number}")

    

    battery = int(input("Enter battery percentage: "))
    battery_ok = battery_check(battery)

    engine = input("Enter engine status (good/bad): ")
    engine_ok = engine_check(engine)

    if battery_ok and engine_ok:
        print("Vehicle Approved")
    else:
        print("Vehicle Failed Inspection")

    inspection = input("Do you want to inspect another vehicle? (yes/no): ").lower()


    inspection_number += 1