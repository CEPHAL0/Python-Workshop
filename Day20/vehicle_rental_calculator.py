# Vehicle Rental System
# Initial Tyre Pressure (35 PSI)

# Fuel Consumption < 40L
# Tyre Pressure > 70%
# Maintainence Cost > 5000
# 5000 Per Day

# Fuel Consumption < 50L
# Tyre Pressure > 60%
# Maintainence Cost > 10000
# 8000 Per Day

# Fuel Consumption < 75L
# Maintainence Cost > 15000
# 10000 Per Day

# otherwise
# 15000 Per Day

# Input -> Days used, Fuel Consumption in Litres, Maintainence Cost, Recieved Tyre Pressure
# Output -> Final Amount


days_used = int(input("Enter the number of days used: "))
fuel_consumption = int(input("Enter the fuel consumed in Litres: "))
maintainence_cost = int(input("Enter the maintainence cost: "))
recieved_tyre_pressure = int(input("Enter the recieved tyre pressure: "))

initial_tyre_pressure = 35

case_1 = (fuel_consumption < 40) and (recieved_tyre_pressure > (0.7 * initial_tyre_pressure)) and (maintainence_cost > 5000)

case_2 = (fuel_consumption < 50) and (recieved_tyre_pressure > (0.6 * initial_tyre_pressure)) and (maintainence_cost > 10000)

case_3 = (fuel_consumption < 75) and (maintainence_cost < 15000)

if case_1:
    charge_per_day = 5000
elif case_2:
    charge_per_day = 8000
elif case_3:
    charge_per_day = 10000
else:
    charge_per_day = 15000

total_charge = days_used * charge_per_day

print(
f"""
==============================
INVOICE
==============================
Tyre Pressure       {recieved_tyre_pressure} PSI
Fuel Consumption    {fuel_consumption} Litres
Days Used           {days_used}
-----------------------------
Charge Per Day      Rs. {charge_per_day}
Total Charge        Rs. {total_charge}
==============================
"""
)
