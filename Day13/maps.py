import folium

# Create map centered on Nepal
m = folium.Map(location=[28.0, 84.0], zoom_start=7)

# Add Kathmandu
folium.Marker([27.7172, 85.3240], popup="Kathmandu").add_to(m)

# Add Pokhara
folium.Marker([28.2096, 83.9856], popup="Pokhara").add_to(m)

# Show map
m.save("nepal_map.html")