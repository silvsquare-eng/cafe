import json

with open('khobar_packaging_leads.json', encoding='utf-8') as f:
    master_leads = json.load(f)

with open('classified_visits.json', encoding='utf-8') as f:
    classified_visits = json.load(f)

print(f"Master leads: {len(master_leads)}, Classified visits: {len(classified_visits)}")

# Save a CSV for the rep activity analysis
import csv

rep_analysis_headers = [
    "الرقم", "الطابع الزمني", "المندوب", "اسم الكوفي", "الحي",
    "رقم الجوال", "حالة الزيارة", "الملاحظات المسجلة", "إجراء الإدارة المطلوب"
]

with open('rep_activity_report.csv', 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(rep_analysis_headers)
    for v in classified_visits:
        action = ""
        if v['status'] == 'hot_lead':
            action = "🚨 عاجل: إرسال عرض سعر وعينات بوكسات فوراً"
        elif v['status'] == 'has_phone':
            action = "📞 اتصال هاتفي بمسؤول المشتريات لتقديم كتالوج التغليف"
        elif v['status'] == 'revisit':
            action = "⏳ جدولة زيارة ثانية لمتابعة التوريد"
        elif v['status'] == 'rejected':
            action = "استبعاد حالياً"
        else:
            action = "متابعة دورية"
            
        writer.writerow([
            v['id'], v['timestamp'], v['rep'], v['name'], v['district'],
            v['phone'], v['status_label'], v['notes'], action
        ])

print("Saved rep_activity_report.csv")
