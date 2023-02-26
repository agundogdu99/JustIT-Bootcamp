weight = 10
cost_premium = 125

# Ground Shipping
if weight <= 2:
    cost_ground = 20 + (weight * 1.50)
elif weight <= 6:
    cost_ground = 20 + (weight * 3)
elif weight <= 10:
    cost_ground = 20 + (weight * 4)
else:
    cost_ground = 20 + (weight * 4.75)

print("Ground: " + str(cost_ground))
print("Ground Premium: " + str(cost_premium))

# Drone
if weight <= 2:
    cost_drone = weight * 4.50
elif weight <= 6:
    cost_drone = weight * 9
elif weight <= 10:
    cost_drone = weight * 12
else:
    cost_drone = weight * 14.25

print("Drone: " + str(cost_drone))
