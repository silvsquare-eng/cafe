import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('rep_visits_log.json', encoding='utf-8') as f:
    visits = json.load(f)

with open('khobar_packaging_leads.json', encoding='utf-8') as f:
    master_leads = json.load(f)

# Clean rep names
reps = {}
districts = {}
statuses = {
    'hot_lead': [],     # طلب بوكسات / مهتم
    'has_phone': [],    # تم تحصيل رقم جوال
    'revisit': [],      # زيارة مرة أخرى
    'rejected': [],     # امتنع
    'normal': []        # تمت الزيارة بدون ملاحظات سلبية
}

for v in visits:
    rep = v['المندوب'].strip()
    reps[rep] = reps.get(rep, 0) + 1
    
    dist = (v['الحي'] or 'غير محدد').strip()
    districts[dist] = districts.get(dist, 0) + 1
    
    notes = (v['ملاحظات'] or '').strip()
    phone = (v['رقم الجوال'] or '').strip()
    cafe_name = v['اسم الكوفي'].strip()
    
    lead_obj = {
        'cafe': cafe_name,
        'rep': rep,
        'district': dist,
        'phone': phone,
        'notes': notes,
        'timestamp': v['طابع زمني']
    }
    
    if any(k in notes.lower() for k in ['يبي بوكسات', 'يبون بكسات', 'بوكسات']):
        statuses['hot_lead'].append(lead_obj)
    elif 'امتنع' in phone or 'امتنع' in notes:
        statuses['rejected'].append(lead_obj)
    elif 'زيار' in notes:
        statuses['revisit'].append(lead_obj)
    elif phone and len(phone) >= 9:
        statuses['has_phone'].append(lead_obj)
    else:
        statuses['normal'].append(lead_obj)

print(f"Total Visits Recorded: {len(visits)}")
print("Reps Performance:")
for r, c in reps.items():
    print(f"  - {r}: {c} زيارة ({round(c/len(visits)*100, 1)}%)")

print("\nOutcomes Breakdown:")
print(f"  - 🔥 فرص بيع ساخنة (طلبوا بوكسات وتغليف): {len(statuses['hot_lead'])}")
print(f"  - 📞 تم تحصيل رقم هاتف المسؤول: {len(statuses['has_phone'])}")
print(f"  - ⏳ مطلوب إعادة زيارة ومتابعة: {len(statuses['revisit'])}")
print(f"  - ❌ امتنعوا / غير مهتمين: {len(statuses['rejected'])}")
print(f"  - 📋 زيارات عامة تمت بنجاح: {len(statuses['normal'])}")

print("\nDistricts Visited:")
for d, c in sorted(districts.items(), key=lambda x: x[1], reverse=True):
    print(f"  - {d}: {c} زيارة")

# Match with Master Database to see unvisited
visited_names = set(v['اسم الكوفي'].strip().lower() for v in visits)
unvisited = []
for lead in master_leads:
    ln = lead['name'].strip().lower()
    # Check if exact match or substring
    is_visited = False
    for vn in visited_names:
        if vn in ln or ln in vn or (len(vn) > 4 and vn[:5] in ln):
            is_visited = True
            break
    if not is_visited:
        unvisited.append(lead)

print(f"\nMaster Database Coverage:")
print(f"  - Total In Master DB: {len(master_leads)}")
print(f"  - Remaining Unvisited in DB: {len(unvisited)}")
print(f"  - Coverage Rate: {round((len(master_leads) - len(unvisited)) / len(master_leads) * 100, 1)}%")

with open('rep_activity_summary.json', 'w', encoding='utf-8') as f:
    json.dump({
        'total_visits': len(visits),
        'reps': reps,
        'districts': districts,
        'statuses': {k: len(v) for k, v in statuses.items()},
        'hot_leads': statuses['hot_lead'],
        'revisit_leads': statuses['revisit'],
        'rejected_leads': statuses['rejected'],
        'has_phone_leads': statuses['has_phone'],
        'unvisited_count': len(unvisited)
    }, f, ensure_ascii=False, indent=2)
