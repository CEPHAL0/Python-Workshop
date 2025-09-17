from datetime import datetime
import matplotlib.pyplot as plt
from meteostat import Point, Daily

# Set time period
start = datetime(2024, 1, 1)
end = datetime(2024, 12, 30)

# Kathmandu
# location = Point(27.7172, 85.3240, 1400)

# Pokhara
location = Point(28.2096, 83.9856, 822)


data = Daily(location, start, end)
data = data.fetch()

# data.plot(y=["tavg", "tmin", "tmax"])

data.plot(y=["prcp", "wspd"])
plt.ylabel("mm")
plt.title("Windspeed and Precipitation of Pokhara")
plt.show()
