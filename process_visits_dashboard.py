import json

# Load files
with open('rep_visits_log.json', encoding='utf-8') as f:
    rep_visits = json.load(f)

with open('khobar_packaging_leads.json', encoding='utf-8') as f:
    master_leads = json.load(f)

# Classify visits
classified_visits = []
visited_names_set = set()

for idx, v in enumerate(rep_visits):
    rep = v['المندوب'].strip()
    dist = (v['الحي'] or 'غير محدد').strip()
    notes = (v['ملاحظات'] or '').strip()
    phone = (v['رقم الجوال'] or '').strip()
    cafe_name = v['اسم الكوفي'].strip()
    
    visited_names_set.add(cafe_name.lower())
    
    # Status detection
    if any(k in notes.lower() for k in ['يبي بوكسات', 'يبون بكسات', 'بوكسات']):
        status = "hot_lead"
        status_label = "🔥 طلب بوكسات وتغليف (فرصة ساخنة)"
        badge_color = "#e74c3c"
    elif 'امتنع' in phone or 'امتنع' in notes:
        status = "rejected"
        status_label = "❌ امتنع / غير مهتم"
        badge_color = "#7f8c8d"
    elif 'زيار' in notes:
        status = "revisit"
        status_label = "⏳ مطلوب إعادة زيارة"
        badge_color = "#f39c12"
    elif phone and len(phone) >= 9:
        status = "has_phone"
        status_label = "📞 تم تحصيل رقم هاتف"
        badge_color = "#2ecc71"
    else:
        status = "completed"
        status_label = "📋 تمت الزيارة بنجاح"
        badge_color = "#3498db"
        
    classified_visits.append({
        "id": idx + 1,
        "timestamp": v['طابع زمني'],
        "rep": rep,
        "name": cafe_name,
        "district": dist,
        "phone": phone if 'امتنع' not in phone else '',
        "notes": notes,
        "status": status,
        "status_label": status_label,
        "badge_color": badge_color
    })

# Compute unvisited master leads
unvisited_leads = []
for lead in master_leads:
    ln = lead['name'].strip().lower()
    match = False
    for vn in visited_names_set:
        if vn in ln or ln in vn or (len(vn) > 4 and vn[:5] in ln):
            match = True
            break
    if not match:
        unvisited_leads.append(lead)

print(f"Total Visits Classified: {len(classified_visits)}")
print(f"Total Master Leads: {len(master_leads)}")
print(f"Total Unvisited Leads: {len(unvisited_leads)}")

with open('classified_visits.json', 'w', encoding='utf-8') as f:
    json.dump(classified_visits, f, ensure_ascii=False, indent=2)

print("Saved classified_visits.json")
