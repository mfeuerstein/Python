from Time import Time

time = Time()

print("The attributes of time are: ")
print("time.hour: ", time.hour)
print("time.minute: ", time.minute)
print("time.second: ", time.second)

print("\nCalling method printMilitary: ")
time.printMilitary()

print("\nCalling method printStandard: ")
time.printStandard()

print("\nChanging time's hour attribute in a lazy manner")
time.hour = 25
print("\nCalling method printMilitary after alteration: ")
time.printMilitary()
