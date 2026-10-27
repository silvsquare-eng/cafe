import urllib.request
import urllib.parse
import json
import time

# Al Khobar, Dhahran, and Suburbs bounding box
# Lat: 26.15 to 26.42, Lon: 50.05 to 50.28
bbox = "26.15,50.05,26.42,50.28"

query = f"""
[out:json][timeout:60];
(
  node["amenity"="cafe"]({bbox});
  way["amenity"="cafe"]({bbox});
  node["amenity"="restaurant"]({bbox});
  way["amenity"="restaurant"]({bbox});
  node["amenity"="fast_food"]({bbox});
  way["amenity"="fast_food"]({bbox});
  node["shop"="bakery"]({bbox});
  way["shop"="bakery"]({bbox});
  node["shop"="coffee"]({bbox});
  way["shop"="coffee"]({bbox});
  node["shop"="tea"]({bbox});
  way["shop"="tea"]({bbox});
  node["shop"="confectionery"]({bbox});
  way["shop"="confectionery"]({bbox});
);
out center tags;
"""

print("Querying Overpass API for Khobar, Dhahran & suburbs...")
req = urllib.request.Request(
    'https://overpass-api.de/api/interpreter',
    data=query.encode('utf-8'),
    headers={'User-Agent': 'KhobarPackagingDirectory/1.0'}
)

try:
    with urllib.request.urlopen(req, timeout=60) as resp:
        res = json.loads(resp.read().decode('utf-8'))
        elements = res.get('elements', [])
        print(f"Total OSM elements retrieved: {len(elements)}")
        
        valid = []
        for el in elements:
            tags = el.get('tags', {})
            name = tags.get('name') or tags.get('name:ar') or tags.get('name:en')
            if not name:
                continue
            
            lat = el.get('lat') or (el.get('center', {}).get('lat'))
            lng = el.get('lon') or (el.get('center', {}).get('lon'))
            if not lat or not lng:
                continue
                
            valid.append({
                'name': name,
                'name_en': tags.get('name:en', ''),
                'name_ar': tags.get('name:ar', ''),
                'amenity': tags.get('amenity', ''),
                'shop': tags.get('shop', ''),
                'cuisine': tags.get('cuisine', ''),
                'lat': lat,
                'lng': lng,
                'phone': tags.get('phone') or tags.get('contact:phone') or tags.get('mobile', ''),
                'website': tags.get('website') or tags.get('contact:website', ''),
                'street': tags.get('addr:street', ''),
                'district': tags.get('addr:suburb') or tags.get('addr:district', ''),
                'opening_hours': tags.get('opening_hours', '')
            })
            
        print(f"Total named businesses with coordinates: {len(valid)}")
        with open('osm_raw_businesses.json', 'w', encoding='utf-8') as f:
            json.dump(valid, f, ensure_ascii=False, indent=2)
        print("Saved raw businesses to osm_raw_businesses.json")
except Exception as e:
    print(f"Error: {e}")
