print(" BMW FACTORY INSPECTION SYSTEM ")
print("===============================")


def battery_check(battery):


    if battery >= 80:
        print("Battery is OK")
        return True
    else:
        print("Battery Failed")
        return False

battery = int(input("Enter battery percentage: "))

battery_ok = battery_check(battery)
    

def engine_check(engine):


    if engine.lower() == "good":
        print("Engine is OK")
        return True
    else:
        print("Engine Failed")
        return False

engine = input("Enter engine status (good/bad): ")

engine_ok = engine_check(engine)

if battery_ok and engine_ok:
    print("Vehicle Approved")
else:
    print("Vehicle Failed Inspection")
