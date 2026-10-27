import json

with open('khobar_packaging_leads.json', encoding='utf-8') as f:
    leads = json.load(f)

print(f"Embedding {len(leads)} leads into index.html...")

leads_json_str = json.dumps(leads, ensure_ascii=False)

html_template = f'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>دليل شركات التغليف لكافيهات ومطاعم الخبر والظهران | Packaging Sales Directory</title>
  <meta name="description" content="قاعدة بيانات 348 كافيه ومطعم ومخبز في الخبر والظهران لشركات التغليف والكرتون والبوكسات والأكواب، مرتبة بالمسافة ومسارات الجولات الميدانية.">
  
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@300;400;500;700;800;900&family=Outfit:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">

  <style>
    :root {{
      --bg-primary: #0b0908;
      --bg-secondary: #14100e;
      --bg-card: rgba(26, 20, 18, 0.94);
      --bg-card-hover: rgba(36, 28, 24, 0.98);
      --accent-gold: #d4a373;
      --accent-gold-light: #faedcd;
      --accent-copper: #c86d51;
      --accent-green: #2ecc71;
      --accent-blue: #3498db;
      --accent-amber: #f39c12;
      --accent-purple: #9b59b6;
      --text-main: #f8f6f0;
      --text-muted: #b7ada4;
      --border-color: rgba(212, 163, 115, 0.22);
      --border-color-hover: rgba(212, 163, 115, 0.55);
      --shadow-card: 0 10px 30px -10px rgba(0, 0, 0, 0.7);
      --shadow-hover: 0 20px 40px -10px rgba(0, 0, 0, 0.85), 0 0 25px rgba(212, 163, 115, 0.2);
      --radius-sm: 8px;
      --radius-md: 14px;
      --radius-lg: 20px;
      --radius-full: 9999px;
      --transition: all 0.25s cubic-bezier(0.25, 0.8, 0.25, 1);
      --font-arabic: 'Tajawal', sans-serif;
      --font-latin: 'Outfit', sans-serif;
    }}

    * {{ margin: 0; padding: 0; box-sizing: border-box; }}

    body {{
      font-family: var(--font-arabic);
      background-color: var(--bg-primary);
      color: var(--text-main);
      line-height: 1.6;
      direction: rtl;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      overflow-x: hidden;
      background-image: 
        radial-gradient(circle at 10% 12%, rgba(200, 109, 81, 0.12) 0%, transparent 45%),
        radial-gradient(circle at 90% 88%, rgba(212, 163, 115, 0.1) 0%, transparent 45%);
      background-attachment: fixed;
    }}

    .container {{
      width: 100%;
      max-width: 1380px;
      margin: 0 auto;
      padding: 0 1.5rem;
    }}

    /* Hero */
    .hero-section {{
      position: relative;
      padding: 3.5rem 0 2.5rem;
      background: linear-gradient(180deg, #1e1511 0%, var(--bg-primary) 100%);
      border-bottom: 1px solid var(--border-color);
      text-align: center;
    }}

    .badge-sales {{
      display: inline-flex;
      align-items: center;
      gap: 0.6rem;
      padding: 0.45rem 1.4rem;
      background: rgba(200, 109, 81, 0.18);
      border: 1px solid rgba(200, 109, 81, 0.45);
      border-radius: var(--radius-full);
      color: #ff9e80;
      font-size: 0.95rem;
      font-weight: 700;
      margin-bottom: 1rem;
      backdrop-filter: blur(10px);
    }}

    .main-title {{
      font-size: 2.8rem;
      font-weight: 900;
      color: #fff;
      letter-spacing: -0.5px;
      margin-bottom: 0.8rem;
      background: linear-gradient(135deg, #ffffff 40%, var(--accent-gold) 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }}

    .subtitle {{
      max-width: 840px;
      margin: 0 auto 1.8rem;
      font-size: 1.15rem;
      color: var(--text-muted);
      line-height: 1.8;
    }}

    /* Sales HUD */
    .sales-hud {{
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-lg);
      padding: 1.25rem;
      margin: 0 auto 1.8rem;
      max-width: 1000px;
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
      gap: 1rem;
      backdrop-filter: blur(12px);
      text-align: center;
    }}

    .hud-card {{
      display: flex;
      flex-direction: column;
      gap: 0.25rem;
    }}

    .hud-title {{
      font-size: 0.82rem;
      color: var(--text-muted);
      font-weight: 600;
    }}

    .hud-value {{
      font-family: var(--font-latin);
      font-size: 1.7rem;
      font-weight: 800;
      color: var(--accent-gold);
    }}

    /* Buttons */
    .hero-actions {{
      display: flex;
      gap: 0.75rem;
      flex-wrap: wrap;
      justify-content: center;
    }}

    .btn {{
      display: inline-flex;
      align-items: center;
      gap: 0.55rem;
      padding: 0.75rem 1.4rem;
      border-radius: var(--radius-md);
      font-family: var(--font-arabic);
      font-size: 0.95rem;
      font-weight: 700;
      cursor: pointer;
      border: none;
      transition: var(--transition);
      text-decoration: none;
    }}

    .btn-gps {{
      background: linear-gradient(135deg, #27ae60, #2ecc71);
      color: #fff;
      box-shadow: 0 4px 18px rgba(46, 204, 113, 0.4);
    }}
    .btn-gps:hover {{
      transform: translateY(-2px);
      box-shadow: 0 6px 25px rgba(46, 204, 113, 0.6);
    }}

    .btn-secondary {{
      background: rgba(255, 255, 255, 0.06);
      color: var(--text-main);
      border: 1px solid var(--border-color);
    }}
    .btn-secondary:hover {{
      background: rgba(212, 163, 115, 0.18);
      border-color: var(--accent-gold);
      color: var(--accent-gold-light);
      transform: translateY(-2px);
    }}

    /* Controls Panel */
    .main-content {{
      flex: 1;
      padding: 2.2rem 1.5rem;
    }}

    .controls-panel {{
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-lg);
      padding: 1.75rem;
      margin-bottom: 2rem;
      box-shadow: var(--shadow-card);
      backdrop-filter: blur(15px);
    }}

    /* Origin row */
    .origin-row {{
      display: flex;
      align-items: center;
      gap: 1rem;
      padding: 0.9rem 1.25rem;
      background: rgba(212, 163, 115, 0.08);
      border: 1px dashed var(--border-color);
      border-radius: var(--radius-md);
      margin-bottom: 1.35rem;
      flex-wrap: wrap;
    }}

    .origin-label {{
      font-weight: 700;
      color: var(--accent-gold-light);
      display: flex;
      align-items: center;
      gap: 0.5rem;
      font-size: 0.95rem;
      white-space: nowrap;
    }}

    .origin-select {{
      flex: 1;
      min-width: 260px;
      padding: 0.65rem 1rem;
      background: #15110f;
      border: 1px solid var(--border-color);
      color: #fff;
      border-radius: var(--radius-sm);
      font-family: inherit;
      font-size: 0.95rem;
      cursor: pointer;
    }}

    .search-box {{
      position: relative;
      display: flex;
      align-items: center;
      margin-bottom: 1.35rem;
    }}

    .search-icon {{
      position: absolute;
      right: 1.35rem;
      color: var(--accent-gold);
      font-size: 1.15rem;
    }}

    .search-box input {{
      width: 100%;
      padding: 0.95rem 3.4rem 0.95rem 3.2rem;
      background: rgba(12, 10, 9, 0.85);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-md);
      color: #fff;
      font-family: inherit;
      font-size: 1.05rem;
      transition: var(--transition);
    }}

    .search-box input:focus {{
      outline: none;
      border-color: var(--accent-gold);
      box-shadow: 0 0 18px rgba(212, 163, 115, 0.3);
      background: rgba(12, 10, 9, 0.95);
    }}

    .clear-btn {{
      position: absolute;
      left: 1.2rem;
      background: transparent;
      border: none;
      color: var(--text-muted);
      cursor: pointer;
      font-size: 1.1rem;
    }}

    /* Categories / Packaging Needs Pills */
    .filter-section {{
      margin-bottom: 1.25rem;
    }}

    .section-label {{
      font-size: 0.88rem;
      color: var(--text-muted);
      font-weight: 700;
      margin-bottom: 0.5rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}

    .filter-pills {{
      display: flex;
      gap: 0.5rem;
      flex-wrap: wrap;
    }}

    .pill {{
      display: inline-flex;
      align-items: center;
      gap: 0.45rem;
      padding: 0.5rem 1.05rem;
      border-radius: var(--radius-full);
      background: rgba(255, 255, 255, 0.04);
      color: var(--text-muted);
      border: 1px solid rgba(255, 255, 255, 0.08);
      font-family: inherit;
      font-size: 0.88rem;
      font-weight: 600;
      cursor: pointer;
      transition: var(--transition);
    }}

    .pill:hover {{
      background: rgba(212, 163, 115, 0.12);
      color: var(--accent-gold-light);
      border-color: var(--border-color);
    }}

    .pill.active {{
      background: var(--accent-gold);
      color: #171311;
      font-weight: 800;
      border-color: var(--accent-gold);
      box-shadow: 0 3px 12px rgba(212, 163, 115, 0.35);
    }}

    .pill-route.active {{
      background: var(--accent-copper);
      color: #fff;
      border-color: var(--accent-copper);
    }}

    /* Meta bar */
    .results-meta {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 0.95rem;
      color: var(--text-muted);
      padding-top: 1rem;
      border-top: 1px solid rgba(255, 255, 255, 0.06);
      flex-wrap: wrap;
      gap: 0.75rem;
    }}

    .results-meta strong {{
      color: var(--accent-gold);
      font-size: 1.1rem;
    }}

    .btn-sm {{
      padding: 0.45rem 0.9rem;
      font-size: 0.85rem;
      border-radius: var(--radius-sm);
      background: rgba(255, 255, 255, 0.05);
      color: var(--text-muted);
      border: 1px solid var(--border-color);
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      font-family: inherit;
    }}
    .btn-sm:hover, .btn-sm.active {{
      background: var(--accent-gold);
      color: #171311;
      border-color: var(--accent-gold);
      font-weight: 700;
    }}

    /* Cards Grid */
    .cafes-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
      gap: 1.5rem;
    }}

    .cafe-card {{
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-lg);
      padding: 1.5rem;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      transition: var(--transition);
      box-shadow: var(--shadow-card);
      backdrop-filter: blur(12px);
    }}

    .cafe-card:hover {{
      background: var(--bg-card-hover);
      border-color: var(--border-color-hover);
      transform: translateY(-4px);
      box-shadow: var(--shadow-hover);
    }}

    .card-top {{
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      margin-bottom: 0.6rem;
      gap: 0.5rem;
    }}

    .card-title-group h3 {{
      font-size: 1.3rem;
      font-weight: 800;
      color: #fff;
      margin-bottom: 0.15rem;
    }}

    .card-title-en {{
      font-family: var(--font-latin);
      font-size: 0.82rem;
      color: var(--accent-gold);
      font-weight: 500;
    }}

    .distance-badge {{
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
      padding: 0.35rem 0.8rem;
      border-radius: var(--radius-full);
      font-size: 0.85rem;
      font-weight: 800;
      background: rgba(46, 204, 113, 0.18);
      color: #5ef09b;
      border: 1px solid rgba(46, 204, 113, 0.35);
      white-space: nowrap;
    }}
    .distance-badge.far {{
      background: rgba(212, 163, 115, 0.15);
      color: var(--accent-gold-light);
      border-color: var(--border-color);
    }}

    .tag-row {{
      display: flex;
      gap: 0.4rem;
      flex-wrap: wrap;
      margin-bottom: 0.85rem;
    }}

    .badge-cat {{
      font-size: 0.78rem;
      padding: 0.2rem 0.7rem;
      border-radius: var(--radius-full);
      background: rgba(52, 152, 219, 0.15);
      color: #60a5fa;
      border: 1px solid rgba(52, 152, 219, 0.3);
      font-weight: 600;
    }}

    .badge-pack {{
      font-size: 0.78rem;
      padding: 0.2rem 0.7rem;
      border-radius: var(--radius-full);
      background: rgba(200, 109, 81, 0.18);
      color: #ffaa91;
      border: 1px solid rgba(200, 109, 81, 0.35);
      font-weight: 700;
    }}

    .badge-route {{
      font-size: 0.75rem;
      padding: 0.2rem 0.6rem;
      border-radius: var(--radius-full);
      background: rgba(255, 255, 255, 0.05);
      color: var(--text-muted);
      border: 1px solid rgba(255, 255, 255, 0.08);
    }}

    .card-info-list {{
      display: flex;
      flex-direction: column;
      gap: 0.5rem;
      font-size: 0.9rem;
      color: var(--text-muted);
      margin-bottom: 1rem;
    }}

    .card-info-item {{
      display: flex;
      align-items: flex-start;
      gap: 0.6rem;
    }}

    .card-info-item i {{
      color: var(--accent-gold);
      width: 16px;
      margin-top: 3px;
      flex-shrink: 0;
    }}

    /* Packaging pitch box */
    .pitch-box {{
      background: rgba(212, 163, 115, 0.08);
      border-right: 3px solid var(--accent-gold);
      padding: 0.65rem 0.85rem;
      border-radius: var(--radius-sm);
      font-size: 0.84rem;
      color: var(--accent-gold-light);
      margin-bottom: 1.1rem;
      line-height: 1.5;
    }}

    .pitch-box strong {{
      color: #fff;
      display: block;
      margin-bottom: 0.2rem;
      font-size: 0.82rem;
    }}

    /* Visit status selector */
    .status-row {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 0.5rem;
      background: rgba(0, 0, 0, 0.35);
      padding: 0.55rem 0.75rem;
      border-radius: var(--radius-sm);
      margin-bottom: 1.1rem;
      border: 1px solid rgba(255, 255, 255, 0.05);
    }}

    .status-select {{
      background: #181311;
      border: 1px solid var(--border-color);
      color: #fff;
      padding: 0.35rem 0.6rem;
      border-radius: var(--radius-sm);
      font-family: inherit;
      font-size: 0.85rem;
      cursor: pointer;
    }}

    /* Card Actions */
    .card-actions {{
      display: grid;
      grid-template-columns: repeat(2, 1fr) auto;
      gap: 0.5rem;
      padding-top: 0.9rem;
      border-top: 1px solid rgba(255, 255, 255, 0.08);
    }}

    .action-btn {{
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 0.4rem;
      padding: 0.55rem 0.6rem;
      border-radius: var(--radius-sm);
      font-size: 0.85rem;
      font-weight: 700;
      text-decoration: none;
      cursor: pointer;
      border: none;
      transition: var(--transition);
    }}

    .action-call {{
      background: rgba(46, 204, 113, 0.18);
      color: #4ade80;
      border: 1px solid rgba(74, 222, 128, 0.3);
    }}
    .action-call:hover {{ background: #27ae60; color: #fff; }}

    .action-map {{
      background: rgba(52, 152, 219, 0.18);
      color: #60a5fa;
      border: 1px solid rgba(96, 165, 250, 0.3);
    }}
    .action-map:hover {{ background: #2563eb; color: #fff; }}

    .action-more {{
      background: rgba(255, 255, 255, 0.07);
      color: var(--text-muted);
      border: 1px solid var(--border-color);
      width: 40px;
    }}
    .action-more:hover {{ background: var(--accent-gold); color: #171311; }}

    /* Table View */
    .table-container {{
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-lg);
      overflow-x: auto;
      box-shadow: var(--shadow-card);
      display: none;
    }}

    .directory-table {{
      width: 100%;
      border-collapse: collapse;
      text-align: right;
      font-size: 0.92rem;
    }}

    .directory-table th {{
      background: rgba(212, 163, 115, 0.15);
      color: var(--accent-gold-light);
      padding: 1rem;
      font-weight: 700;
      border-bottom: 2px solid var(--border-color);
      white-space: nowrap;
    }}

    .directory-table td {{
      padding: 0.9rem 1rem;
      border-bottom: 1px solid rgba(255, 255, 255, 0.06);
      color: var(--text-main);
      vertical-align: middle;
    }}

    .directory-table tr:hover td {{
      background: rgba(255, 255, 255, 0.03);
    }}

    /* Load more bar */
    .load-more-bar {{
      text-align: center;
      padding: 2rem 0;
    }}

    /* Modal */
    .modal-backdrop {{
      position: fixed;
      inset: 0;
      background: rgba(0, 0, 0, 0.88);
      backdrop-filter: blur(12px);
      z-index: 1000;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 1.5rem;
    }}

    .modal-card {{
      position: relative;
      background: #181412;
      border: 1px solid var(--border-color-hover);
      border-radius: var(--radius-lg);
      width: 100%;
      max-width: 640px;
      box-shadow: 0 25px 70px -15px rgba(0, 0, 0, 0.95);
      padding: 2rem;
      animation: modalEnter 0.25s ease-out;
      max-height: 90vh;
      overflow-y: auto;
    }}

    @keyframes modalEnter {{
      from {{ opacity: 0; transform: scale(0.95) translateY(15px); }}
      to {{ opacity: 1; transform: scale(1) translateY(0); }}
    }}

    .modal-close {{
      position: absolute;
      top: 1.35rem;
      left: 1.35rem;
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-full);
      color: var(--text-muted);
      width: 36px;
      height: 36px;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
    }}

    .rep-notes-textarea {{
      width: 100%;
      min-height: 80px;
      padding: 0.7rem;
      background: #110e0d;
      border: 1px solid var(--border-color);
      border-radius: var(--radius-sm);
      color: #fff;
      font-family: inherit;
      font-size: 0.92rem;
      margin-top: 0.4rem;
    }}

    /* Toast */
    .toast-notification {{
      position: fixed;
      bottom: 2rem;
      left: 50%;
      transform: translateX(-50%) translateY(100px);
      background: #231b17;
      border: 1px solid var(--accent-gold);
      border-radius: var(--radius-md);
      padding: 0.85rem 1.8rem;
      color: #fff;
      display: flex;
      align-items: center;
      gap: 0.75rem;
      box-shadow: 0 12px 35px rgba(0, 0, 0, 0.8);
      z-index: 2000;
      transition: transform 0.3s cubic-bezier(0.25, 0.8, 0.25, 1), opacity 0.3s ease;
      opacity: 0;
      pointer-events: none;
      font-weight: 700;
    }}
    .toast-notification.show {{
      transform: translateX(-50%) translateY(0);
      opacity: 1;
    }}

    /* Footer */
    .footer {{
      background: #090807;
      border-top: 1px solid var(--border-color);
      padding: 2.2rem 0;
      margin-top: auto;
      text-align: center;
      font-size: 0.95rem;
      color: var(--text-muted);
    }}

    .footer-links {{
      display: flex;
      gap: 1.5rem;
      justify-content: center;
      margin-top: 0.8rem;
    }}

    .footer-links button {{
      color: var(--accent-gold);
      background: transparent;
      border: none;
      font-family: inherit;
      font-size: inherit;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
    }}

    @media (max-width: 768px) {{
      .main-title {{ font-size: 2.1rem; }}
      .cafes-grid {{ grid-template-columns: 1fr; }}
      .sales-hud {{ grid-template-columns: 1fr 1fr; }}
      .origin-row {{ flex-direction: column; align-items: stretch; }}
    }}
  </style>
</head>
<body>

  <!-- هيدر التطبيق ولوحة مؤشرات التغليف -->
  <header class="hero-section">
    <div class="container hero-content">
      <div class="badge-sales">
        <i class="fa-solid fa-boxes-packing"></i> قاعدة بيانات مبيعات التغليف والكرتون والأكواب (الخبر والظهران)
      </div>
      <h1 class="main-title">دليل مشاريع الخبر والظهران لشركات التغليف</h1>
      <p class="subtitle">
        دليل ميداني شامل يضم <strong>348 كافيه ومطعم ومخبز ومحل شاي</strong> مرتبة جغرافياً بالمسافة لمندوبي مبيعات التغليف (البوكسات، فلاتر القهوة، الأكواب، وأكياس التيك أواي) مع التوجيه الملاحي المباشر.
      </p>

      <!-- مؤشرات سريعة -->
      <div class="sales-hud">
        <div class="hud-card">
          <span class="hud-title">إجمالي المشاريع المستهدفة</span>
          <span class="hud-value" id="total-count">{len(leads)}</span>
        </div>
        <div class="hud-card">
          <span class="hud-title">كافيهات ومحامص القهوة</span>
          <span class="hud-value" style="color: #d4a373;">99</span>
        </div>
        <div class="hud-card">
          <span class="hud-title">مطاعم برجر ووجبات سريعة</span>
          <span class="hud-value" style="color: #ff9e80;">76</span>
        </div>
        <div class="hud-card">
          <span class="hud-title">الزيارات المنجزة</span>
          <span class="hud-value" id="completed-visits-count" style="color: #2ecc71;">0</span>
        </div>
        <div class="hud-card">
          <span class="hud-title">حالة المسافة (GPS)</span>
          <span class="hud-value" id="gps-status-text" style="font-size: 1.05rem; color: #60a5fa;">محدد مسبقاً</span>
        </div>
      </div>

      <!-- أزرار الإجراءات -->
      <div class="hero-actions">
        <button id="get-gps-btn" class="btn btn-gps">
          <i class="fa-solid fa-location-crosshairs"></i> ترتيب حسب موقعي الحالي (GPS)
        </button>
        <button id="download-sales-csv" class="btn btn-secondary">
          <i class="fa-solid fa-file-excel"></i> تصدير كل المشاريع (Excel)
        </button>
        <button onclick="window.print()" class="btn btn-secondary">
          <i class="fa-solid fa-print"></i> طباعة خطة الزيارة
        </button>
      </div>
    </div>
  </header>

  <!-- جسم التطبيق -->
  <main class="container main-content">
    
    <section class="controls-panel">
      <!-- تحديد نقطة الانطلاق لحساب المسافة -->
      <div class="origin-row">
        <span class="origin-label">
          <i class="fa-solid fa-compass"></i> حساب المسافة من نقطة انطلاق المندوب:
        </span>
        <select id="origin-select" class="origin-select">
          <option value="matal">1. مجمع المطل وكورنيش الخبر (الواجهة البحرية)</option>
          <option value="branda">2. مجمع برندة والحزام الأخضر (شارع البيبسي)</option>
          <option value="patio">3. باتيو سنتر والخبر الشمالية</option>
          <option value="bandariyah">4. حي البندرية والعقربية (طريق الأمير تركي)</option>
          <option value="rakah">5. حي الراكة الجنوبية (طريق الأمير سلطان)</option>
          <option value="ithra">6. الظهران ومركز إثراء وحي الدوحة</option>
          <option value="tahlia">7. حي التحلية وجنوب الخبر</option>
        </select>
        <button id="apply-origin-btn" class="btn-sm active">
          <i class="fa-solid fa-calculator"></i> إعادة حساب المسافات
        </button>
      </div>

      <!-- البحث الفوري -->
      <div class="search-box">
        <i class="fa-solid fa-magnifying-glass search-icon"></i>
        <input 
          type="text" 
          id="search-input" 
          placeholder="ابحث باسم المشروع (برجر، قهوة، شاي، بيتزا...)، الحي، أو نوع التغليف (فلاتر، بوكسات، أكواب...)"
          autocomplete="off"
        >
        <button id="clear-search-btn" class="clear-btn" style="display: none;">
          <i class="fa-solid fa-xmark"></i>
        </button>
      </div>

      <!-- فلترة نوع المشروع واحتياج التغليف -->
      <div class="filter-section">
        <div class="section-label"><i class="fa-solid fa-boxes-stacked"></i> تصنيف المشروع ونوع التغليف المطلوب:</div>
        <div class="filter-pills" id="category-pills">
          <button class="pill active" data-cat="all"><i class="fa-solid fa-border-all"></i> الكل ({len(leads)})</button>
          <button class="pill" data-cat="كافيهات ومحامص قهوة مختصة"><i class="fa-solid fa-coffee"></i> كافيهات ومحامص (أكواب وفلاتر) (99)</button>
          <button class="pill" data-cat="مطاعم برجر ووجبات سريعة"><i class="fa-solid fa-burger"></i> مطاعم برجر ووجبات (بوكسات وورق) (76)</button>
          <button class="pill" data-cat="مطاعم ومأكولات متنوعة"><i class="fa-solid fa-utensils"></i> مطاعم ومشويات (علب وتوصيل) (131)</button>
          <button class="pill" data-cat="مخابز وحلويات وكيك"><i class="fa-solid fa-cake-candles"></i> مخابز وحلويات (بوكسات كيك) (24)</button>
          <button class="pill" data-cat="مطاعم بيتزا ومعجنات"><i class="fa-solid fa-pizza-slice"></i> بيتزا وفطاير (كراتين بيتزا) (10)</button>
          <button class="pill" data-cat="كافيهات ومحلات شاي وكرك"><i class="fa-solid fa-mug-hot"></i> كافيهات شاي وكرك وبوبا (6)</button>
        </div>
      </div>

      <!-- فلترة المسارات الميدانية -->
      <div class="filter-section">
        <div class="section-label"><i class="fa-solid fa-route"></i> مسار الجولة الميدانية اليومية:</div>
        <div class="filter-pills" id="route-pills">
          <button class="pill pill-route active" data-route="all">كل المسارات</button>
          <button class="pill pill-route" data-route="مسار 1: الكورنيش وأجدان والمطل">الكورنيش وأجدان (103)</button>
          <button class="pill pill-route" data-route="مسار 6: الظهران والدوحة وإثراء">الظهران وإثراء (81)</button>
          <button class="pill pill-route" data-route="مسار عام: الخبر المركزية">الخبر المركزية (50)</button>
          <button class="pill pill-route" data-route="مسار 4: الحزام والعليا والبستان">الحزام والعليا (38)</button>
          <button class="pill pill-route" data-route="مسار 3: البندرية والعقربية">البندرية والعقربية (33)</button>
          <button class="pill pill-route" data-route="مسار 7: التحلية وجنوب الخبر">التحلية والجنوبية (28)</button>
          <button class="pill pill-route" data-route="مسار 5: الراكة والصفا">الراكة والصفا (13)</button>
        </div>
      </div>

      <!-- شريط الحالة والتحكم -->
      <div class="results-meta">
        <span id="results-count-text">مرتب حسب <strong>الأقرب لموقع الانطلاق</strong></span>
        <div class="view-controls">
          <button id="view-cards-btn" class="btn-sm active" title="عرض البطاقات"><i class="fa-solid fa-table-cells-large"></i> بطاقات</button>
          <button id="view-table-btn" class="btn-sm" title="عرض جدول"><i class="fa-solid fa-table-list"></i> جدول</button>
          <button id="sort-distance-btn" class="btn-sm" title="عكس ترتيب المسافة"><i class="fa-solid fa-arrow-down-short-wide"></i> المسافة</button>
        </div>
      </div>
    </section>

    <!-- شبكة البطاقات -->
    <section class="cafes-grid" id="cafes-grid"></section>

    <!-- عرض الجدول المنظم -->
    <section class="table-container" id="table-view">
      <table class="directory-table">
        <thead>
          <tr>
            <th>#</th>
            <th>اسم المشروع</th>
            <th>المسافة</th>
            <th>التصنيف</th>
            <th>احتياج التغليف الرئيسي</th>
            <th>الحي / العنوان</th>
            <th>الهاتف</th>
            <th>حالة الزيارة</th>
            <th>GPS وملاحة</th>
          </tr>
        </thead>
        <tbody id="table-body"></tbody>
      </table>
    </section>

    <!-- زر تحميل المزيد -->
    <div class="load-more-bar" id="load-more-container" style="display: none;">
      <button id="load-more-btn" class="btn btn-secondary">
        <i class="fa-solid fa-angles-down"></i> عرض المزيد من المشاريع (<span id="remaining-count">0</span> متبقي)
      </button>
    </div>

    <!-- حالة فارغة -->
    <div class="empty-state" id="empty-state" style="display: none;">
      <i class="fa-solid fa-box-open" style="font-size: 3.5rem; color: var(--accent-gold); margin-bottom: 1rem; opacity: 0.6;"></i>
      <h3>لا توجد نتائج مطابقة لبحثك</h3>
      <p>جرّب اختيار تصنيف آخر أو مسار مختلف.</p>
    </div>

  </main>

  <!-- نافذة التفاصيل والملاحظات -->
  <div class="modal-backdrop" id="details-modal" style="display: none;">
    <div class="modal-card">
      <button class="modal-close" id="modal-close-action"><i class="fa-solid fa-xmark"></i></button>

      <div style="margin-bottom: 1.5rem; padding-bottom: 1rem; border-bottom: 1px solid var(--border-color);">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; gap: 0.5rem;">
          <div>
            <h2 id="modal-name" style="font-size: 1.7rem; color: #fff;">اسم المشروع</h2>
            <span id="modal-en" style="font-family: var(--font-latin); color: var(--accent-gold); font-size: 0.95rem;"></span>
          </div>
          <span class="distance-badge" id="modal-dist"></span>
        </div>
        <div style="display: flex; gap: 0.4rem; margin-top: 0.6rem;">
          <span class="badge-cat" id="modal-cat"></span>
          <span class="badge-pack" id="modal-pack"></span>
        </div>
      </div>

      <div style="display: flex; flex-direction: column; gap: 1.1rem; margin-bottom: 1.5rem;">
        <div>
          <strong style="color: var(--text-muted); font-size: 0.85rem;"><i class="fa-solid fa-location-dot"></i> العنوان:</strong>
          <p id="modal-loc" style="color: #fff; margin-top: 0.2rem;"></p>
        </div>
        <div>
          <strong style="color: var(--text-muted); font-size: 0.85rem;"><i class="fa-solid fa-phone"></i> رقم الهاتف:</strong>
          <p id="modal-tel" style="color: #fff; margin-top: 0.2rem;"></p>
        </div>
        <div>
          <strong style="color: var(--accent-copper); font-size: 0.85rem;"><i class="fa-solid fa-bullseye"></i> منتجات التغليف المستهدفة للبيع:</strong>
          <p id="modal-items" style="color: #faedcd; margin-top: 0.2rem; line-height: 1.5;"></p>
        </div>
        <div>
          <strong style="color: var(--text-muted); font-size: 0.85rem;"><i class="fa-solid fa-clipboard-user"></i> حالة الزيارة وملاحظات المندوب:</strong>
          <div style="margin-top: 0.4rem;">
            <select id="modal-status-select" class="status-select" style="padding: 0.45rem; width: 100%; margin-bottom: 0.5rem;">
              <option value="none">⚪ لم تتم الزيارة</option>
              <option value="done">🟢 تم البيع / مهتم بالتعاقد</option>
              <option value="followup">🟡 يحتاج متابعة (Follow-up)</option>
              <option value="rejected">🔴 غير مهتم</option>
            </select>
            <textarea id="modal-rep-note" class="rep-notes-textarea" placeholder="اكتب ملاحظتك: اسم مسؤول المشتريات، حجم الاستهلاك، موعد إرسال عينات التغليف..."></textarea>
            <button id="save-note-btn" class="btn-sm active" style="margin-top: 0.5rem;"><i class="fa-solid fa-floppy-disk"></i> حفظ الملاحظة</button>
          </div>
        </div>
      </div>

      <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.75rem;">
        <a href="#" id="modal-call-btn" class="btn" style="background: #1b5e20; color: #fff; justify-content: center;"><i class="fa-solid fa-phone"></i> اتصال</a>
        <a href="#" id="modal-maps-btn" target="_blank" rel="noopener noreferrer" class="btn" style="background: #1565c0; color: #fff; justify-content: center;"><i class="fa-solid fa-diamond-turn-right"></i> ملاحة GPS</a>
      </div>
    </div>
  </div>

  <div class="toast-notification" id="toast-notif">
    <i class="fa-solid fa-circle-check" style="color: #4ade80;"></i>
    <span id="toast-text"></span>
  </div>

  <footer class="footer">
    <div class="container footer-content">
      <p>دليل كافيهات ومطاعم ومشاريع الخبر والظهران لشركات التغليف &copy; 2026. قاعدة بيانات 348 مشروعاً ميدانياً.</p>
      <div class="footer-links">
        <button id="download-csv-footer"><i class="fa-solid fa-file-excel"></i> تنزيل قاعدة البيانات Excel</button>
        <button onclick="window.print()"><i class="fa-solid fa-print"></i> طباعة القائمة</button>
      </div>
    </div>
  </footer>

  <!-- كود الجافاسكربت وقاعدة البيانات المدمجة بالكامل -->
  <script>
    const ALL_LEADS = {leads_json_str};

    const ORIGINS = {{
      matal: {{ name: "مجمع المطل والكورنيش", lat: 26.2975, lng: 50.2190 }},
      branda: {{ name: "مجمع برندة والحزام الأخضر", lat: 26.3055, lng: 50.1982 }},
      patio: {{ name: "باتيو سنتر والخبر الشمالية", lat: 26.3078, lng: 50.2072 }},
      bandariyah: {{ name: "البندرية والعقربية", lat: 26.2890, lng: 50.2048 }},
      rakah: {{ name: "الراكة الجنوبية (طريق الأمير سلطان)", lat: 26.3552, lng: 50.1882 }},
      ithra: {{ name: "مركز إثراء والظهران", lat: 26.3352, lng: 50.1245 }},
      tahlia: {{ name: "التحلية وجنوب الخبر", lat: 26.2355, lng: 50.2105 }}
    }};

    let currentOrigin = {{ ...ORIGINS.matal }};
    let activeCategory = 'all';
    let activeRoute = 'all';
    let searchQuery = '';
    let currentView = 'cards';
    let sortDistanceAsc = true;
    let selectedLead = null;
    let displayLimit = 40; // Pagination batch

    let visitStatuses = JSON.parse(localStorage.getItem('khobar_pack_visits') || '{{}}');
    let visitNotes = JSON.parse(localStorage.getItem('khobar_pack_notes') || '{{}}');

    function calculateDistance(lat1, lon1, lat2, lon2) {{
      const R = 6371;
      const dLat = (lat2 - lat1) * Math.PI / 180;
      const dLon = (lon2 - lon1) * Math.PI / 180;
      const a = Math.sin(dLat / 2) * Math.sin(dLat / 2) + Math.cos(lat1 * Math.PI / 180) * Math.cos(lat2 * Math.PI / 180) * Math.sin(dLon / 2) * Math.sin(dLon / 2);
      return R * (2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a)));
    }}

    function formatDistance(distKm) {{
      if (distKm < 1) return `${{Math.round(distKm * 1000)}} متر`;
      return `${{distKm.toFixed(1)}} كم`;
    }}

    function showToast(msg) {{
      const notif = document.getElementById('toast-notif');
      document.getElementById('toast-text').textContent = msg;
      notif.classList.add('show');
      setTimeout(() => notif.classList.remove('show'), 2400);
    }}

    function updateCompletedVisits() {{
      let count = 0;
      Object.values(visitStatuses).forEach(s => {{ if (s === 'done') count++; }});
      const el = document.getElementById('completed-visits-count');
      if (el) el.textContent = `${{count}} من ${{ALL_LEADS.length}}`;
    }}

    function getProcessedLeads() {{
      const processed = ALL_LEADS.map(lead => {{
        const dist = calculateDistance(currentOrigin.lat, currentOrigin.lng, lead.lat, lead.lng);
        return {{
          ...lead,
          distanceKm: dist,
          distanceFormatted: formatDistance(dist),
          status: visitStatuses[lead.id] || 'none',
          note: visitNotes[lead.id] || ''
        }};
      }});

      let filtered = processed.filter(l => {{
        if (activeCategory !== 'all' && l.category !== activeCategory) return false;
        if (activeRoute !== 'all' && l.route_zone !== activeRoute) return false;

        if (searchQuery.trim() !== '') {{
          const q = searchQuery.toLowerCase().trim();
          const matchName = l.name.toLowerCase().includes(q) || (l.name_en && l.name_en.toLowerCase().includes(q));
          const matchArea = l.area.toLowerCase().includes(q) || l.address.toLowerCase().includes(q);
          const matchItems = l.pack_items.toLowerCase().includes(q);
          const matchPitch = l.sales_notes.toLowerCase().includes(q);
          if (!matchName && !matchArea && !matchItems && !matchPitch) return false;
        }}
        return true;
      }});

      filtered.sort((a, b) => sortDistanceAsc ? (a.distanceKm - b.distanceKm) : (b.distanceKm - a.distanceKm));
      return filtered;
    }}

    function render() {{
      const filtered = getProcessedLeads();
      const countText = document.getElementById('results-count-text');
      countText.innerHTML = `يتم عرض <strong>${{Math.min(displayLimit, filtered.length)}}</strong> من أصل <strong>${{filtered.length}}</strong> مشروع (الأقرب لـ <strong>${{currentOrigin.name}}</strong>)`;

      const grid = document.getElementById('cafes-grid');
      const table = document.getElementById('table-view');
      const empty = document.getElementById('empty-state');
      const loadMoreContainer = document.getElementById('load-more-container');

      if (filtered.length === 0) {{
        grid.style.display = 'none';
        table.style.display = 'none';
        empty.style.display = 'block';
        loadMoreContainer.style.display = 'none';
        return;
      }}

      empty.style.display = 'none';
      const visibleData = filtered.slice(0, displayLimit);

      if (currentView === 'cards') {{
        grid.style.display = 'grid';
        table.style.display = 'none';
        renderCards(visibleData);
      }} else {{
        grid.style.display = 'none';
        table.style.display = 'block';
        renderTable(visibleData);
      }}

      if (filtered.length > displayLimit) {{
        loadMoreContainer.style.display = 'block';
        document.getElementById('remaining-count').textContent = filtered.length - displayLimit;
      }} else {{
        loadMoreContainer.style.display = 'none';
      }}

      updateCompletedVisits();
    }}

    function renderCards(data) {{
      const grid = document.getElementById('cafes-grid');
      grid.innerHTML = data.map((item, idx) => {{
        const cleanPhone = (item.phone || '').replace(/[^0-9+]/g, '');
        const isClose = item.distanceKm <= 2.5;

        return `
          <article class="cafe-card">
            <div>
              <div class="card-top">
                <div class="card-title-group">
                  <h3><span style="color:var(--accent-gold); font-size:1.1rem; margin-left:0.3rem;">#${{idx + 1}}</span> ${{item.name}}</h3>
                  ${{item.name_en ? `<span class="card-title-en">${{item.name_en}}</span>` : ''}}
                </div>
                <div class="distance-badge ${{isClose ? '' : 'far'}}">
                  <i class="fa-solid fa-person-walking"></i> ${{item.distanceFormatted}}
                </div>
              </div>

              <div class="tag-row">
                <span class="badge-cat"><i class="fa-solid ${{item.icon || 'fa-store'}}"></i> ${{item.category}}</span>
                <span class="badge-pack"><i class="fa-solid fa-box"></i> ${{item.pack_type}}</span>
                <span class="badge-route">${{item.route_zone}}</span>
              </div>

              <div class="card-info-list">
                <div class="card-info-item">
                  <i class="fa-solid fa-location-dot"></i>
                  <span>${{item.address}}</span>
                </div>
                ${{cleanPhone ? `
                  <div class="card-info-item">
                    <i class="fa-solid fa-phone"></i>
                    <a href="tel:${{cleanPhone}}" style="color:var(--accent-gold); font-weight:700;">${{item.phone}}</a>
                  </div>
                ` : ''}}
              </div>

              <div class="pitch-box">
                <strong><i class="fa-solid fa-cart-shopping"></i> احتياجات التغليف المقترح بيعها:</strong>
                ${{item.pack_items}}
              </div>

              <div class="status-row">
                <span style="font-size:0.85rem; font-weight:700;"><i class="fa-solid fa-clipboard-user"></i> الزيارة:</span>
                <select class="status-select" onchange="changeVisitStatus(${{item.id}}, this.value)">
                  <option value="none" ${{item.status === 'none' ? 'selected' : ''}}>⚪ لم تتم</option>
                  <option value="done" ${{item.status === 'done' ? 'selected' : ''}}>🟢 تم البيع / مهتم</option>
                  <option value="followup" ${{item.status === 'followup' ? 'selected' : ''}}>🟡 متابعة</option>
                  <option value="rejected" ${{item.status === 'rejected' ? 'selected' : ''}}>🔴 غير مهتم</option>
                </select>
              </div>
            </div>

            <div class="card-actions">
              ${{cleanPhone ? `
                <a href="tel:${{cleanPhone}}" class="action-btn action-call"><i class="fa-solid fa-phone"></i> اتصال</a>
              ` : `
                <a href="${{item.maps_url}}" target="_blank" class="action-btn action-call" style="background:rgba(212,163,115,0.15); color:var(--accent-gold-light);"><i class="fa-solid fa-building"></i> زيارة</a>
              `}}
              <a href="${{item.maps_url}}" target="_blank" rel="noopener noreferrer" class="action-btn action-map"><i class="fa-solid fa-diamond-turn-right"></i> ملاحة GPS</a>
              <button class="action-btn action-more" onclick="openDetails(${{item.id}})" title="تفاصيل وملاحظة"><i class="fa-solid fa-pen-to-square"></i></button>
            </div>
          </article>
        `;
      }}).join('');
    }}

    function renderTable(data) {{
      const tbody = document.getElementById('table-body');
      tbody.innerHTML = data.map((item, idx) => {{
        const cleanPhone = (item.phone || '').replace(/[^0-9+]/g, '');
        return `
          <tr>
            <td><strong>#${{idx + 1}}</strong></td>
            <td>
              <div style="font-weight:800; color:#fff;">${{item.name}}</div>
              <small style="color:var(--accent-gold);">${{item.name_en || ''}}</small>
            </td>
            <td><span class="distance-badge" style="font-size:0.8rem;">${{item.distanceFormatted}}</span></td>
            <td><span class="badge-cat">${{item.category}}</span></td>
            <td><span class="badge-pack">${{item.pack_type}}</span></td>
            <td><small>${{item.address}}</small></td>
            <td>${{cleanPhone ? `<a href="tel:${{cleanPhone}}" style="color:var(--accent-gold); font-weight:700;">${{item.phone}}</a>` : '<span style="color:#777;">ميداني</span>'}}</td>
            <td>
              <select class="status-select" onchange="changeVisitStatus(${{item.id}}, this.value)" style="font-size:0.8rem;">
                <option value="none" ${{item.status === 'none' ? 'selected' : ''}}>⚪ لم تتم</option>
                <option value="done" ${{item.status === 'done' ? 'selected' : ''}}>🟢 تم البيع</option>
                <option value="followup" ${{item.status === 'followup' ? 'selected' : ''}}>🟡 متابعة</option>
                <option value="rejected" ${{item.status === 'rejected' ? 'selected' : ''}}>🔴 غير مهتم</option>
              </select>
            </td>
            <td>
              <a href="${{item.maps_url}}" target="_blank" class="btn-sm" style="color:#60a5fa;"><i class="fa-solid fa-diamond-turn-right"></i> GPS</a>
            </td>
          </tr>
        `;
      }}).join('');
    }}

    window.changeVisitStatus = function(id, val) {{
      visitStatuses[id] = val;
      localStorage.setItem('khobar_pack_visits', JSON.stringify(visitStatuses));
      showToast('تم تحديث حالة الزيارة ✅');
      updateCompletedVisits();
    }};

    window.openDetails = function(id) {{
      const item = ALL_LEADS.find(l => l.id === id);
      if (!item) return;

      selectedLead = item;
      const dist = calculateDistance(currentOrigin.lat, currentOrigin.lng, item.lat, item.lng);

      document.getElementById('modal-name').textContent = item.name;
      document.getElementById('modal-en').textContent = item.name_en || '';
      document.getElementById('modal-dist').innerHTML = `<i class="fa-solid fa-person-walking"></i> تبعد ${{formatDistance(dist)}}`;
      document.getElementById('modal-cat').textContent = item.category;
      document.getElementById('modal-pack').textContent = item.pack_type;
      document.getElementById('modal-loc').textContent = item.address;
      document.getElementById('modal-tel').innerHTML = item.phone ? `<a href="tel:${{item.phone.replace(/[^0-9+]/g, '')}}" style="color:var(--accent-gold); font-weight:700;">${{item.phone}}</a>` : 'غير متوفر - زيارة ميدانية للموقع';
      document.getElementById('modal-items').textContent = item.pack_items;

      document.getElementById('modal-status-select').value = visitStatuses[item.id] || 'none';
      document.getElementById('modal-rep-note').value = visitNotes[item.id] || '';

      const cleanPhone = (item.phone || '').replace(/[^0-9+]/g, '');
      const callBtn = document.getElementById('modal-call-btn');
      if (cleanPhone) {{
        callBtn.href = `tel:${{cleanPhone}}`;
        callBtn.style.display = 'inline-flex';
      }} else {{
        callBtn.style.display = 'none';
      }}
      document.getElementById('modal-maps-btn').href = item.maps_url;

      document.getElementById('details-modal').style.display = 'flex';
    }};

    document.getElementById('save-note-btn').addEventListener('click', () => {{
      if (!selectedLead) return;
      const id = selectedLead.id;
      visitStatuses[id] = document.getElementById('modal-status-select').value;
      visitNotes[id] = document.getElementById('modal-rep-note').value;
      localStorage.setItem('khobar_pack_visits', JSON.stringify(visitStatuses));
      localStorage.setItem('khobar_pack_notes', JSON.stringify(visitNotes));
      showToast('تم حفظ ملاحظات العميل 💾');
      document.getElementById('details-modal').style.display = 'none';
      render();
    }});

    document.getElementById('modal-close-action').addEventListener('click', () => {{
      document.getElementById('details-modal').style.display = 'none';
    }});

    document.getElementById('apply-origin-btn').addEventListener('click', () => {{
      const key = document.getElementById('origin-select').value;
      currentOrigin = {{ ...ORIGINS[key] }};
      document.getElementById('gps-status-text').textContent = currentOrigin.name;
      document.getElementById('gps-status-text').style.color = 'var(--accent-gold)';
      showToast(`تم تحديث الانطلاق: ${{currentOrigin.name}}`);
      render();
    }});

    document.getElementById('get-gps-btn').addEventListener('click', () => {{
      if (!navigator.geolocation) return alert('GPS غير مدعوم');
      document.getElementById('gps-status-text').textContent = 'جارٍ التحديد...';
      navigator.geolocation.getCurrentPosition(
        (pos) => {{
          currentOrigin = {{ name: "موقعك الحالي (GPS)", lat: pos.coords.latitude, lng: pos.coords.longitude }};
          document.getElementById('gps-status-text').textContent = "📍 موقعك الحي (GPS)";
          document.getElementById('gps-status-text').style.color = "#2ecc71";
          showToast('تم تحديد موقعك بدقة وترتيب 348 مشروعاً حسب الأقرب لك فوراً!');
          render();
        }},
        () => showToast('تعذر جلب موقعك، تم استخدام النقطة المحددة.')
      );
    }});

    // Pills Events
    document.getElementById('category-pills').addEventListener('click', (e) => {{
      const pill = e.target.closest('.pill');
      if (!pill) return;
      document.querySelectorAll('#category-pills .pill').forEach(p => p.classList.remove('active'));
      pill.classList.add('active');
      activeCategory = pill.dataset.cat;
      displayLimit = 40;
      render();
    }});

    document.getElementById('route-pills').addEventListener('click', (e) => {{
      const pill = e.target.closest('.pill-route');
      if (!pill) return;
      document.querySelectorAll('#route-pills .pill-route').forEach(p => p.classList.remove('active'));
      pill.classList.add('active');
      activeRoute = pill.dataset.route;
      displayLimit = 40;
      render();
    }});

    // Search
    const searchInput = document.getElementById('search-input');
    const clearSearch = document.getElementById('clear-search-btn');
    searchInput.addEventListener('input', (e) => {{
      searchQuery = e.target.value;
      clearSearch.style.display = searchQuery ? 'block' : 'none';
      displayLimit = 40;
      render();
    }});

    clearSearch.addEventListener('click', () => {{
      searchInput.value = '';
      searchQuery = '';
      clearSearch.style.display = 'none';
      render();
    }});

    // View Toggles
    document.getElementById('view-cards-btn').addEventListener('click', function() {{
      currentView = 'cards';
      this.classList.add('active');
      document.getElementById('view-table-btn').classList.remove('active');
      render();
    }});

    document.getElementById('view-table-btn').addEventListener('click', function() {{
      currentView = 'table';
      this.classList.add('active');
      document.getElementById('view-cards-btn').classList.remove('active');
      render();
    }});

    document.getElementById('sort-distance-btn').addEventListener('click', () => {{
      sortDistanceAsc = !sortDistanceAsc;
      render();
      showToast(sortDistanceAsc ? 'الترتيب: الأقرب أولاً' : 'الترتيب: الأبعد أولاً');
    }});

    // Load More
    document.getElementById('load-more-btn').addEventListener('click', () => {{
      displayLimit += 40;
      render();
    }});

    // Export CSV
    function exportCSV() {{
      window.location.href = 'khobar_packaging_leads.csv';
      showToast('جارٍ تحميل قاعدة بيانات 348 مشروعاً للإكسل...');
    }}
    document.getElementById('download-sales-csv').addEventListener('click', exportCSV);
    document.getElementById('download-csv-footer').addEventListener('click', exportCSV);

    render();
  </script>
</body>
</html>
'''

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_template)

print("Generated complete index.html successfully with all 348 packaging leads!")
