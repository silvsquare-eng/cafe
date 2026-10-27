import json
import math

# Load OSM raw data
with open('osm_raw_businesses.json', encoding='utf-8') as f:
    osm_items = json.load(f)

# Load existing 32 verified cafes to merge and enrich
try:
    with open('khobar_cafes_data.json', encoding='utf-8') as f:
        existing_cafes = json.load(f)
except Exception:
    existing_cafes = []

print(f"OSM Raw: {len(osm_items)}, Existing verified: {len(existing_cafes)}")

# Helper to determine district and route based on lat/lng
def get_location_info(lat, lng, street=''):
    # Dhahran
    if lng <= 50.165:
        if 26.330 <= lat <= 26.345 and 50.115 <= lng <= 50.135:
            district = "الظهران - مركز إثراء"
        elif 26.315 <= lat <= 26.335:
            district = "الظهران - حي الدوحة"
        elif 26.300 <= lat < 26.315:
            district = "الظهران - حي الدانة / الجامعة"
        else:
            district = "الظهران"
        route = "مسار 6: الظهران والدوحة وإثراء"
        return district, route

    # Rakah
    if lat >= 26.340:
        district = "الراكة الجنوبية"
        route = "مسار 5: الراكة والصفا"
        return district, route

    # Corniche & Waterfront
    if lng >= 50.210:
        if lat >= 26.295:
            district = "كورنيش الخبر (المطل والشاطئ)"
        elif 26.285 <= lat < 26.295:
            district = "أجدان ووك والواجهة البحرية"
        elif 26.265 <= lat < 26.285:
            district = "كورنيش الخبر الجنوبي"
        else:
            district = "كورنيش الخبر"
        route = "مسار 1: الكورنيش وأجدان والمطل"
        return district, route

    # Hizam, Olaya, Rawabi, Bustan
    if 50.180 <= lng < 50.202 and lat >= 26.302:
        if 26.315 <= lat:
            district = "حي العليا / الروابي"
        elif 26.308 <= lat < 26.315:
            district = "حي الحزام الذهبي / البستان"
        else:
            district = "حي الحزام الأخضر"
        route = "مسار 4: الحزام والعليا والبستان"
        return district, route

    # Aqrabiyah & Bandariyah
    if 50.185 <= lng < 50.210 and 26.280 <= lat < 26.305:
        if 26.295 <= lat:
            district = "حي العقربية"
        else:
            district = "حي البندرية"
        route = "مسار 3: البندرية والعقربية"
        return district, route

    # Khobar North & Yarmouk
    if lat >= 26.290 and 50.200 <= lng < 26.315:
        if lng >= 50.208:
            district = "حي اليرموك"
        else:
            district = "الخبر الشمالية"
        route = "مسار 2: الخبر الشمالية واليرموك"
        return district, route

    # South Khobar, Bayoniah, Tahlia, Khozama
    if lat < 26.280:
        if lat < 26.250:
            district = "حي التحلية / العزيزية"
            route = "مسار 7: التحلية وجنوب الخبر"
        elif lng <= 50.200:
            district = "حي الخزامى / الجسر"
            route = "مسار 7: التحلية وجنوب الخبر"
        else:
            district = "الخبر الجنوبية (البايونية)"
            route = "مسار 2: الخبر الشمالية والجنوبية"
        return district, route

    # Default
    return "الخبر", "مسار عام: الخبر المركزية"

# Helper to classify business and deduce packaging needs
def classify_packaging(name, amenity, shop, cuisine):
    n_lower = name.lower()
    combined = f"{n_lower} {amenity} {shop} {cuisine}".lower()

    # 1. Tea / Boba / Karak
    if any(k in combined for k in ['tea', 'شاي', 'كرك', 'karak', 'boba', 'بوبا', 'chai', 'شاي وكرك']):
        category = "كافيهات ومحلات شاي وكرك"
        pack_type = "أكواب شاي وبوبا"
        pack_items = "أكواب كرك ورقية سميكة، بوكسات شاي جمعات (سخانات 2-3 لتر)، كاسات بوبا بلاستيك مع غشاء تغليف حراري، مصاصات عريضة، حوامل أكواب"
        target_pitch = "سخانات شاي كرتون، أكواب دبل وول عازلة للحرارة، ستيكرات لوجو"
        icon = "fa-mug-hot"

    # 2. Specialty Coffee & Roasteries
    elif any(k in combined for k in ['cafe', 'coffee', 'قهوة', 'كافيه', 'محمصة', 'roaster', 'espresso', 'roastery', 'باريستا', 'specialty']):
        category = "كافيهات ومحامص قهوة مختصة"
        pack_type = "أكواب وفلاتر قهوة"
        pack_items = "أكواب ورقية 4/7/8/12/16 أونص دبل وسنجل، كاسات بلاستيك شفافة PET، فلاتر V60 وكيمكس، أكياس بن بصمام وسحاب، أغطية كاسات، هولدرات، أكياس كرافت"
        target_pitch = "أكواب قهوة مطبوعة، فلاتر V60 جملة، أكياس بن كرافت مع صمام، بوكسات قهوة اليوم"
        icon = "fa-coffee"

    # 3. Burger & Fast Food
    elif any(k in combined for k in ['burger', 'برجر', 'fast_food', 'chicken', 'دجاج', 'شواية', 'وجبات سريعة', 'fries', 'ساندوتش', 'sandwich']):
        category = "مطاعم برجر ووجبات سريعة"
        pack_type = "بوكسات برجر ووجبات"
        pack_items = "بوكسات برجر كرتون، علب بطاطس مقلية، ورق ساندوتش مقاوم للزيوت، علب صوصات 1-2 أونص مع أغطية، أكياس تيك أواي ورقية بمقبض، أطقم شوك وملاعق ومناديل"
        target_pitch = "علب برجر كرتونية مقواة بشعار المطعم، ورق لف برجر زبدة، بوكسات وجبات كومبو"
        icon = "fa-burger"

    # 4. Pizza & Italian & Pies
    elif any(k in combined for k in ['pizza', 'بيتزا', 'فطاير', 'معجنات', 'pie', 'pasta', 'إيطالي']):
        category = "مطاعم بيتزا ومعجنات"
        pack_type = "كراتين بيتزا ومعجنات"
        pack_items = "كراتين بيتزا مقاسات 9/11/13/15 إنش، فواصل بيتزا بلاستيك ثلاثية، أكياس توصيل حرارية، علب فطاير كرتونية، أكياس كرافت ورقية"
        target_pitch = "كراتين بيتزا مخصصة عالية التحمل، فواصل بيتزا، كراتين فطاير طويلة"
        icon = "fa-pizza-slice"

    # 5. Bakeries, Pastry & Sweets
    elif any(k in combined for k in ['bakery', 'مخبز', 'حلى', 'sweet', 'حلويات', 'cake', 'كيك', 'pastry', 'confectionery', 'donut', 'دونات', 'chocolate', 'شوكولاتة', 'cookies', 'كوكيز', 'تارت']):
        category = "مخابز وحلويات وكيك"
        pack_type = "بوكسات كيك وحلويات"
        pack_items = "بوكسات كيك بنافذة شفافة، علب حلى وتارت وتشيز كيك، قواعد كيك ذهبية، أكياس مخبوزات ورقية، أشرطة تغليف ستان، أطباق تقديم فاخرة"
        target_pitch = "بوكسات كيك أنيقة، أكياس كرواسون ومخبوزات نافذة، علب حلى مربعة"
        icon = "fa-cake-candles"

    # 6. Ice cream & Juices
    elif any(k in combined for k in ['ice_cream', 'آيسكريم', 'ايسكريم', 'juice', 'عصير', 'عصائر', 'smoothie', 'gelato']):
        category = "آيسكريم وعصائر ومشروبات"
        pack_type = "كاسات وعلب مثلجات"
        pack_items = "أكواب آيسكريم كرتونية مطبوعة، قوارير عصير بلاستيكية، أغطية قبة، ملاعق آيسكريم ملونة، مصاصات عريضة، حوامل كاسات"
        target_pitch = "أكواب آيسكريم كرتون، زجاجات عصير PET، ملاعق حلى خشبية وبلاستيكية"
        icon = "fa-ice-cream"

    # 7. General Restaurant / Shawarma / Traditional
    else:
        category = "مطاعم ومأكولات متنوعة"
        pack_type = "علب وجبات وتوصيل"
        pack_items = "بوكسات وجبات كرتونية، صحون ألمنيوم وقصدير، علب ميكروويف بلاستيكية محكمة، أكياس توصيل ورقية وبلاستيكية، أطقم سفرة وملاعق"
        target_pitch = "أكياس ورقية متينة للتوصيل، علب طعام مقاومة للحرارة، علب صوصات"
        icon = "fa-utensils"

    return category, pack_type, pack_items, target_pitch, icon

# Process All Businesses
merged_list = []
seen_names = set()

# First add the 32 verified cafes with high priority
for c in existing_cafes:
    name_norm = c['name'].strip().lower()
    seen_names.add(name_norm)
    
    cat, p_type, p_items, p_pitch, icon = classify_packaging(c['name'], 'cafe', 'coffee', '')
    
    district, route = get_location_info(c['lat'], c['lng'], c.get('address', ''))
    
    merged_list.append({
        "id": len(merged_list) + 1,
        "name": c['name'],
        "name_en": c.get('name_en', ''),
        "category": cat,
        "pack_type": p_type,
        "pack_items": p_items,
        "target_pitch": p_pitch,
        "icon": icon,
        "area": district,
        "address": c.get('address', f"{district}، الخبر"),
        "phone": c.get('phone', ''),
        "alt_phone": c.get('alt_phone', ''),
        "maps_url": f"https://maps.google.com/?q={c['lat']},{c['lng']}",
        "lat": round(c['lat'], 5),
        "lng": round(c['lng'], 5),
        "route_zone": route,
        "instagram": c.get('instagram', ''),
        "working_hours": c.get('working_hours', 'صباحاً - مساءً'),
        "highlights": c.get('highlights', ''),
        "sales_notes": c.get('sales_notes', p_pitch)
    })

# Now add from OSM dataset
for item in osm_items:
    name = item['name'].strip()
    name_norm = name.lower()
    
    # Simple deduplication
    if name_norm in seen_names or len(name) < 2:
        continue
    
    # Ignore irrelevant non-food places if any
    if any(skip in name_norm for skip in ['صيدلية', 'مغسلة', 'حلاق', 'خياط', 'مستشفى', 'مستوصف', 'بنك', 'صراف', 'مكتبة', 'ورشة', 'فندق']):
        continue
        
    seen_names.add(name_norm)
    
    lat = float(item['lat'])
    lng = float(item['lng'])
    
    district, route = get_location_info(lat, lng, item.get('street', ''))
    cat, p_type, p_items, p_pitch, icon = classify_packaging(
        name, item.get('amenity', ''), item.get('shop', ''), item.get('cuisine', '')
    )
    
    phone = item.get('phone', '')
    # If phone not found in OSM, leave blank or format
    
    address_str = item.get('street', '')
    if address_str:
        full_addr = f"{district}، {address_str}"
    else:
        full_addr = f"{district}، الخبر/الظهران"
        
    merged_list.append({
        "id": len(merged_list) + 1,
        "name": name,
        "name_en": item.get('name_en', ''),
        "category": cat,
        "pack_type": p_type,
        "pack_items": p_items,
        "target_pitch": p_pitch,
        "icon": icon,
        "area": district,
        "address": full_addr,
        "phone": phone,
        "alt_phone": "",
        "maps_url": f"https://maps.google.com/?q={lat},{lng}",
        "lat": round(lat, 5),
        "lng": round(lng, 5),
        "route_zone": route,
        "instagram": "",
        "working_hours": item.get('opening_hours', 'يومياً (صباحاً - مساءً)'),
        "highlights": f"مشروع نشط يحتاج {p_type}",
        "sales_notes": f"استهداف توريد: {p_pitch}"
    })

print(f"Total merged and enriched packaging target projects: {len(merged_list)}")

# Save Master JSON
with open('khobar_packaging_leads.json', 'w', encoding='utf-8') as f:
    json.dump(merged_list, f, ensure_ascii=False, indent=2)

# Save Master CSV for Excel
csv_headers = [
    "الرقم", "اسم المشروع", "الاسم بالإنجليزية", "التصنيف", "نوع التغليف المستهدف",
    "الحي / المنطقة", "العنوان", "رقم الهاتف", "رابط خرائط جوجل (GPS)",
    "خط العرض", "خط الطول", "مسار الجولة الميدانية", "المنتجات المقترح بيعها وتوريدها",
    "أوقات العمل", "حالة الزيارة (للمندوب)", "ملاحظات المندوب الميداني"
]

import csv
with open('khobar_packaging_leads.csv', 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(csv_headers)
    for c in merged_list:
        writer.writerow([
            c['id'], c['name'], c['name_en'], c['category'], c['pack_type'],
            c['area'], c['address'], c['phone'], c['maps_url'],
            c['lat'], c['lng'], c['route_zone'], c['sales_notes'],
            c['working_hours'], "لم تتم الزيارة", ""
        ])

print("Saved khobar_packaging_leads.json and khobar_packaging_leads.csv successfully!")
