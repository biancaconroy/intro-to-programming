import json
import requests
import webbrowser
from pathlib import Path

# Replace with your actual Google Maps API key
from config import api_key

def get_city_coordinates(city, api_key):
    url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {"address": city, "key": api_key}
    response = requests.get(url, params=params).json()
    if response.get("status") == "OK":
        loc = response["results"][0]["geometry"]["location"]
        return loc["lat"], loc["lng"]
    return 41.3851, 2.1734  # fallback to Barcelona

print("Welcome to ClubTime!")
city = input("What city are you looking for? ").strip()
city_lat, city_lng = get_city_coordinates(city, api_key)

with open("clubs_data.json", "r", encoding="utf-8") as f:
    clubs = json.load(f)

days = list(clubs[0]["schedule"].keys())
time_slots = list(clubs[0]["schedule"][days[0]].keys())
day_selector = ''.join(f'<option value="{d}">{d}</option>' for d in days)
time_selector = ''.join(f'<option value="{t}">{t}</option>' for t in time_slots)

def icon_url(color):
    return f"http://maps.google.com/mapfiles/ms/icons/{color}-dot.png"

colors = {
    "green": icon_url("green"),
    "yellow": icon_url("yellow"),
    "orange": icon_url("orange"),
    "red": icon_url("red"),
    "blue": icon_url("blue")
}

html = f"""
<!DOCTYPE html>
<html>
<head><meta charset="utf-8"><title>ClubTime</title></head>
<body>
<div style="margin:10px 0;">
  <label for="day">Day:</label>
  <select id="day">{day_selector}</select>
  <label for="slot" style="margin-left:12px;">Time:</label>
  <select id="slot">{time_selector}</select>
</div>

<div id="map" style="height:600px; width:100%;"></div>

<script>
  const clubs = {json.dumps(clubs)};
  const icons = {json.dumps(colors)};
  let map, markers = [], selectedClubLocation = null, directionsRenderer = null, selectedMarker = null;
  let infoWindow;

  function initMap() {{
    map = new google.maps.Map(document.getElementById('map'), {{
      zoom: 14,
      center: {{lat: {city_lat}, lng: {city_lng}}}
    }});
    directionsRenderer = new google.maps.DirectionsRenderer({{ preserveViewport: true }});
    infoWindow = new google.maps.InfoWindow();
    updateMarkers();
    document.getElementById('slot').addEventListener('change', updateMarkers);
    document.getElementById('day').addEventListener('change', updateMarkers);
  }}

  function clearMarkers() {{
    markers.forEach(m => m.setMap(null));
    markers = [];
    if (directionsRenderer) directionsRenderer.setMap(null);
    if (selectedMarker) selectedMarker.setIcon(icons[selectedMarker.originalColor]);
    selectedMarker = null;
    document.getElementById('routeInfo').innerText = '';
  }}

  function updateMarkers() {{
    const day = document.getElementById('day').value;
    const slot = document.getElementById('slot').value;
    clearMarkers();
    clubs.forEach(c => {{
      let color = c.schedule?.[day]?.[slot] || "green";
      if (color !== "black") {{
        const marker = new google.maps.Marker({{
          position: {{lat: c.lat, lng: c.lng}},
          map: map,
          title: `${{c.name}} - ${{day}} ${{slot}}`,
          icon: icons[color],
          originalColor: color
        }});
        markers.push(marker);

        marker.addListener('click', () => {{
          if (selectedMarker) selectedMarker.setIcon(icons[selectedMarker.originalColor]);
          selectedClubLocation = {{lat: c.lat, lng: c.lng}};
          selectedMarker = marker;
          marker.setIcon(icons["blue"]);

          infoWindow.setContent(`<strong>${{c.name}}</strong>`);
          infoWindow.open(map, marker);
        }});
      }}
    }});
  }}

  function calculateRoutes() {{
    const origin = document.getElementById('userAddress').value;
    const mode = document.getElementById('travelMode').value;

    if (!selectedClubLocation || !origin) {{
      alert("Please select a club and enter your address.");
      return;
    }}

    const service = new google.maps.DirectionsService();
    const request = {{
      origin: origin,
      destination: selectedClubLocation,
      travelMode: google.maps.TravelMode[mode]
    }};

    directionsRenderer = new google.maps.DirectionsRenderer({{ preserveViewport: true }});
    directionsRenderer.setMap(map);

    service.route(request, (response, status) => {{
      if (status === 'OK') {{
        directionsRenderer.setDirections(response);
        const leg = response.routes[0]?.legs?.[0];
        if (leg) {{
          const duration = leg.duration?.text || "";
          const distance = leg.distance?.text || "";
          document.getElementById('routeInfo').innerText =
            `Estimated: ${{duration}} (${{distance}}) via ${{mode.toLowerCase()}}`;
        }}
      }} else if (status === 'ZERO_RESULTS' && mode === 'TRANSIT') {{
        alert("Transit directions not available at this time or location.");
      }} else {{
        alert("Directions failed: " + status);
      }}
    }});
  }}
</script>

<script async
  src="https://maps.googleapis.com/maps/api/js?key={api_key}&callback=initMap">
</script>

<div style="margin-top:15px; padding:10px; border:1px solid #ccc;">
  <label>Starting address:</label>
  <input id="userAddress" size="40" placeholder="e.g. Plaça Catalunya">
  <label style="margin-left:10px;">Mode:</label>
  <select id="travelMode">
    <option value="WALKING">Walking</option>
    <option value="TRANSIT">Transit</option>
    <option value="DRIVING">Driving</option>
  </select>
  <button onclick="calculateRoutes()">Get Directions</button>
</div>

<div id="routeInfo" style="margin-top:10px; font-weight:bold; font-size:14px;"></div>
</body>
</html>
"""

# Save and open the HTML file in browser
html_path = Path("club_map.html")
html_path.write_text(html, encoding="utf-8")
webbrowser.open(html_path.absolute().as_uri())
