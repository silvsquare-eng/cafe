import urllib.request
import json
import re

# Expanded bounding box covering Al Khobar, Dhahran, Aziziyah, Half Moon, Rakah, Doha
bbox = "26.10,50.00,26.45,50.30"

query = f"""
[out:json][timeout:90];
(
  node["amenity"~"cafe|restaurant|fast_food|ice_cream|food_court"]({bbox});
  way["amenity"~"cafe|restaurant|fast_food|ice_cream|food_court"]({bbox});
  node["shop"~"bakery|coffee|tea|confectionery|pastry|chocolate|beverages"]({bbox});
  way["shop"~"bakery|coffee|tea|confectionery|pastry|chocolate|beverages"]({bbox});
  node["cuisine"]({bbox});
  way["cuisine"]({bbox});
);
out center tags;
"""

print("Fetching broader dataset...")
req = urllib.request.Request(
    'https://overpass-api.de/api/interpreter',
    data=query.encode('utf-8'),
    headers={'User-Agent': 'KhobarPackagingMaster/2.0'}
)

try:
    with urllib.request.urlopen(req, timeout=90) as resp:
        res = json.loads(resp.read().decode('utf-8'))
        elements = res.get('elements', [])
        print(f"Total elements retrieved: {len(elements)}")
        
        seen = set()
        clean_list = []
        
        for el in elements:
            tags = el.get('tags', {})
            name = tags.get('name') or tags.get('name:ar') or tags.get('name:en')
            if not name or len(name.strip()) < 2:
                continue
            
            lat = el.get('lat') or (el.get('center', {}).get('lat'))
            lng = el.get('lon') or (el.get('center', {}).get('lon'))
            if not lat or not lng:
                continue
                
            # Deduplicate by approximate coord & name
            key = (round(lat, 4), round(lng, 4), name.strip().lower())
            if key in seen:
                continue
            seen.add(key)
            
            clean_list.append({
                'name': name.strip(),
                'name_en': tags.get('name:en', '').strip(),
                'name_ar': tags.get('name:ar', '').strip(),
                'amenity': tags.get('amenity', ''),
                'shop': tags.get('shop', ''),
                'cuisine': tags.get('cuisine', ''),
                'lat': lat,
                'lng': lng,
                'phone': tags.get('phone') or tags.get('contact:phone') or tags.get('mobile', ''),
                'website': tags.get('website') or tags.get('contact:website', ''),
                'street': tags.get('addr:street', ''),
                'district': tags.get('addr:suburb') or tags.get('addr:district', tags.get('addr:city', '')),
                'brand': tags.get('brand', '')
            })
            
        print(f"Total unique named packaging targets: {len(clean_list)}")
        with open('osm_expanded_businesses.json', 'w', encoding='utf-8') as f:
            json.dump(clean_list, f, ensure_ascii=False, indent=2)
except Exception as e:
    print(f"Error: {e}")
