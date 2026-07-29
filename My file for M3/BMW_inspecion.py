print(" BMW FACTORY INSPECTION SYSTEM ")
print("===============================")


def battery_check():
    battery = int(input("Enter battery percentage: "))

    if battery >= 80:
        print("Battery Passed")
        return True
    else:
        print("Battery Failed")
        return False

def engine_check():
    engine = input("Enter engine status (good/bad): ")

    if engine.lower() == "good":
        print("Engine Passed")
        return True
    else:
        print("Engine Failed")
        return False

battery_ok = battery_check()
engine_ok = engine_check()

if battery_ok and engine_ok:
    print("Vehicle Approved")
else:
    print("Vehicle Failed Inspection")
