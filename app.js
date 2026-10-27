// Khobar Cafes Directory Logic
let cafesData = [];
let activeFilter = 'all';
let searchQuery = '';
let showFavoritesOnly = false;
let favorites = JSON.parse(localStorage.getItem('khobar_cafes_favs') || '[]');

// DOM Elements
const cafesGrid = document.getElementById('cafes-grid');
const searchInput = document.getElementById('search-input');
const clearSearchBtn = document.getElementById('clear-search-btn');
const filterPills = document.querySelectorAll('.filter-pill');
const resultsCountText = document.getElementById('results-count-text');
const totalCafesCount = document.getElementById('total-cafes-count');
const emptyState = document.getElementById('empty-state');
const resetSearchBtn = document.getElementById('reset-search-btn');
const sortNameBtn = document.getElementById('sort-name-btn');
const downloadCsvBtn = document.getElementById('download-csv-btn');
const downloadJsonBtn = document.getElementById('download-json-btn');
const favoriteFilterBtn = document.getElementById('favorite-filter-btn');
const favCountEl = document.getElementById('fav-count');
const toastNotification = document.getElementById('toast-notification');
const toastMessage = document.getElementById('toast-message');

// Modal Elements
const cafeModal = document.getElementById('cafe-modal');
const modalCloseBtn = document.getElementById('modal-close-btn');
const modalCafeName = document.getElementById('modal-cafe-name');
const modalCafeEn = document.getElementById('modal-cafe-en');
const modalCategory = document.getElementById('modal-category');
const modalAddress = document.getElementById('modal-address');
const modalPhone = document.getElementById('modal-phone');
const modalHours = document.getElementById('modal-hours');
const modalHighlights = document.getElementById('modal-highlights');
const modalTags = document.getElementById('modal-tags');
const modalCallLink = document.getElementById('modal-call-link');
const modalMapsLink = document.getElementById('modal-maps-link');
const modalIgLink = document.getElementById('modal-ig-link');

// Initialize
document.addEventListener('DOMContentLoaded', async () => {
  try {
    const res = await fetch('khobar_cafes_data.json');
    cafesData = await res.json();
  } catch (err) {
    console.error('Failed to load JSON data, falling back to static array', err);
  }

  if (totalCafesCount) totalCafesCount.textContent = cafesData.length;
  updateFavCount();
  renderCafes();
  setupEventListeners();
});

function updateFavCount() {
  if (favCountEl) favCountEl.textContent = favorites.length;
}

function showToast(message) {
  toastMessage.textContent = message;
  toastNotification.classList.add('show');
  setTimeout(() => {
    toastNotification.classList.remove('show');
  }, 2600);
}

// Render Cafes
function renderCafes() {
  let filtered = cafesData.filter(cafe => {
    // Favorites check
    if (showFavoritesOnly && !favorites.includes(cafe.id)) {
      return false;
    }

    // Category filter check
    if (activeFilter !== 'all') {
      if (activeFilter === 'corniche') {
        const isCorniche = cafe.area.includes('كورنيش') || cafe.area.includes('أجدان') || cafe.address.includes('الكورنيش') || cafe.address.includes('أجدان');
        if (!isCorniche) return false;
      } else if (activeFilter === 'specialty') {
        const isSpecialty = cafe.category.includes('مختصة') || cafe.category.includes('محمصة') || cafe.tags.includes('قهوة مختصة');
        if (!isSpecialty) return false;
      } else if (activeFilter === 'hizam') {
        const isHizam = cafe.area.includes('الحزام') || cafe.area.includes('العليا') || cafe.area.includes('البستان') || cafe.area.includes('البندرية') || cafe.area.includes('الروابي');
        if (!isHizam) return false;
      } else if (activeFilter === 'bakery') {
        const isBakery = cafe.category.includes('مخبز') || cafe.tags.includes('فطور') || cafe.tags.includes('مخبز');
        if (!isBakery) return false;
      } else if (activeFilter === 'dhahran') {
        const isDhahran = cafe.area.includes('الظهران') || cafe.address.includes('الظهران') || cafe.tags.includes('الظهران') || cafe.tags.includes('إثراء');
        if (!isDhahran) return false;
      } else if (activeFilter === '24hours') {
        const is24h = cafe.working_hours.includes('24') || cafe.tags.includes('24 ساعة');
        if (!is24h) return false;
      }
    }

    // Search query check
    if (searchQuery.trim() !== '') {
      const q = searchQuery.toLowerCase().trim();
      const matchName = cafe.name.toLowerCase().includes(q) || cafe.name_en.toLowerCase().includes(q);
      const matchArea = cafe.area.toLowerCase().includes(q) || cafe.address.toLowerCase().includes(q);
      const matchHighlights = cafe.highlights.toLowerCase().includes(q);
      const matchTags = cafe.tags && cafe.tags.some(t => t.toLowerCase().includes(q));
      if (!matchName && !matchArea && !matchHighlights && !matchTags) {
        return false;
      }
    }

    return true;
  });

  resultsCountText.innerHTML = `يتم عرض <strong>${filtered.length}</strong> كافيه`;

  if (filtered.length === 0) {
    cafesGrid.innerHTML = '';
    emptyState.style.display = 'block';
    return;
  }

  emptyState.style.display = 'none';
  cafesGrid.innerHTML = filtered.map(cafe => {
    const isFav = favorites.includes(cafe.id);
    const tagsHtml = (cafe.tags || []).slice(0, 3).map(t => `<span class="tag-badge">${t}</span>`).join('');
    const cleanPhone = cafe.phone.replace(/[^0-9+]/g, '');

    return `
      <article class="cafe-card" data-id="${cafe.id}">
        <div class="card-header-content">
          <div class="card-top">
            <div class="card-title-group">
              <h3>${cafe.name}</h3>
              <span class="card-title-en">${cafe.name_en}</span>
            </div>
            <button class="card-fav-btn ${isFav ? 'favorited' : ''}" data-id="${cafe.id}" title="${isFav ? 'إزالة من المفضلة' : 'إضافة للمفضلة'}">
              <i class="fa-${isFav ? 'solid' : 'regular'} fa-heart"></i>
            </button>
          </div>

          <span class="card-category-badge">${cafe.category}</span>

          <div class="card-info-list">
            <div class="card-info-item">
              <i class="fa-solid fa-location-dot"></i>
              <span><strong>${cafe.area}</strong> - ${cafe.address}</span>
            </div>
            <div class="card-info-item">
              <i class="fa-solid fa-phone"></i>
              <a href="tel:${cleanPhone}" class="phone-link" title="اتصل الآن">${cafe.phone}</a>
            </div>
            <div class="card-info-item">
              <i class="fa-solid fa-clock"></i>
              <span>${cafe.working_hours}</span>
            </div>
            <div class="card-info-item">
              <i class="fa-brands fa-instagram"></i>
              <a href="${cafe.instagram_url}" target="_blank" rel="noopener noreferrer">${cafe.instagram}</a>
            </div>
          </div>

          <div class="card-tags">
            ${tagsHtml}
          </div>
        </div>

        <div class="card-actions">
          <a href="tel:${cleanPhone}" class="action-btn action-call" title="اتصال">
            <i class="fa-solid fa-phone"></i> اتصال
          </a>
          <a href="${cafe.maps_url}" target="_blank" rel="noopener noreferrer" class="action-btn action-map" title="الموقع في خرائط جوجل">
            <i class="fa-solid fa-map-location-dot"></i> الموقع
          </a>
          <a href="${cafe.instagram_url}" target="_blank" rel="noopener noreferrer" class="action-btn action-ig" title="حساب الإنستغرام">
            <i class="fa-brands fa-instagram"></i> إنستقرام
          </a>
          <button class="action-btn action-more open-details-btn" data-id="${cafe.id}" title="عرض التفاصيل كاملة">
            <i class="fa-solid fa-circle-info"></i>
          </button>
        </div>
      </article>
    `;
  }).join('');
}

// Event Listeners
function setupEventListeners() {
  // Search input
  searchInput.addEventListener('input', (e) => {
    searchQuery = e.target.value;
    clearSearchBtn.style.display = searchQuery ? 'block' : 'none';
    renderCafes();
  });

  clearSearchBtn.addEventListener('click', () => {
    searchInput.value = '';
    searchQuery = '';
    clearSearchBtn.style.display = 'none';
    searchInput.focus();
    renderCafes();
  });

  resetSearchBtn.addEventListener('click', () => {
    searchInput.value = '';
    searchQuery = '';
    activeFilter = 'all';
    showFavoritesOnly = false;
    favoriteFilterBtn.classList.remove('active');
    filterPills.forEach(p => p.classList.toggle('active', p.dataset.filter === 'all'));
    renderCafes();
  });

  // Filter Pills
  filterPills.forEach(pill => {
    pill.addEventListener('click', () => {
      filterPills.forEach(p => p.classList.remove('active'));
      pill.classList.add('active');
      activeFilter = pill.dataset.filter;
      showFavoritesOnly = false;
      favoriteFilterBtn.classList.remove('active');
      renderCafes();
    });
  });

  // Favorites Filter
  favoriteFilterBtn.addEventListener('click', () => {
    showFavoritesOnly = !showFavoritesOnly;
    favoriteFilterBtn.classList.toggle('active', showFavoritesOnly);
    renderCafes();
  });

  // Grid Interactions (Delegation)
  cafesGrid.addEventListener('click', (e) => {
    // Favorite toggle
    const favBtn = e.target.closest('.card-fav-btn');
    if (favBtn) {
      const id = parseInt(favBtn.dataset.id, 10);
      toggleFavorite(id);
      return;
    }

    // Open Details Modal
    const detailsBtn = e.target.closest('.open-details-btn');
    if (detailsBtn) {
      const id = parseInt(detailsBtn.dataset.id, 10);
      openDetailsModal(id);
      return;
    }
  });

  // Sort by Name
  let sortAsc = true;
  sortNameBtn.addEventListener('click', () => {
    sortAsc = !sortAsc;
    cafesData.sort((a, b) => {
      return sortAsc ? a.name.localeCompare(b.name, 'ar') : b.name.localeCompare(a.name, 'ar');
    });
    renderCafes();
    showToast(sortAsc ? 'تم الترتيب تصاعدياً (أ-ي)' : 'تم الترتيب تنازلياً (ي-أ)');
  });

  // Modal Close
  modalCloseBtn.addEventListener('click', closeModal);
  cafeModal.addEventListener('click', (e) => {
    if (e.target === cafeModal) closeModal();
  });

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && cafeModal.style.display === 'flex') {
      closeModal();
    }
  });

  // Download CSV
  downloadCsvBtn.addEventListener('click', downloadCSV);

  // Download JSON
  downloadJsonBtn.addEventListener('click', downloadJSON);
}

// Toggle Favorite
function toggleFavorite(id) {
  const index = favorites.indexOf(id);
  if (index > -1) {
    favorites.splice(index, 1);
    showToast('تمت إزالة الكافيه من المفضلة');
  } else {
    favorites.push(id);
    showToast('تمت إضافة الكافيه إلى المفضلة ❤️');
  }
  localStorage.setItem('khobar_cafes_favs', JSON.stringify(favorites));
  updateFavCount();
  renderCafes();
}

// Modal open
function openDetailsModal(id) {
  const cafe = cafesData.find(c => c.id === id);
  if (!cafe) return;

  modalCafeName.textContent = cafe.name;
  modalCafeEn.textContent = cafe.name_en;
  modalCategory.textContent = cafe.category;
  modalAddress.textContent = `${cafe.area} - ${cafe.address}`;
  modalPhone.innerHTML = `${cafe.phone} ${cafe.toll_free ? `| الرقم البديل: ${cafe.toll_free}` : ''} 
    <button class="btn-sm" style="margin-right: 0.5rem;" onclick="copyPhone('${cafe.phone}')"><i class="fa-regular fa-copy"></i> نسخ</button>`;
  modalHours.textContent = cafe.working_hours;
  modalHighlights.textContent = cafe.highlights;

  modalTags.innerHTML = (cafe.tags || []).map(t => `<span class="tag-badge">${t}</span>`).join('');

  const cleanPhone = cafe.phone.replace(/[^0-9+]/g, '');
  modalCallLink.href = `tel:${cleanPhone}`;
  modalMapsLink.href = cafe.maps_url;
  modalIgLink.href = cafe.instagram_url;

  cafeModal.style.display = 'flex';
}

function closeModal() {
  cafeModal.style.display = 'none';
}

window.copyPhone = function(phone) {
  navigator.clipboard.writeText(phone);
  showToast(`تم نسخ رقم الهاتف: ${phone}`);
};

// Export to CSV
function downloadCSV() {
  window.location.href = 'khobar_cafes_directory.csv';
  showToast('جارٍ تحميل ملف CSV / Excel...');
}

// Export to JSON
function downloadJSON() {
  const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(cafesData, null, 2));
  const dlAnchor = document.createElement('a');
  dlAnchor.setAttribute("href", dataStr);
  dlAnchor.setAttribute("download", "khobar_cafes_data.json");
  document.body.appendChild(dlAnchor);
  dlAnchor.click();
  dlAnchor.remove();
  showToast('جارٍ تحميل ملف JSON...');
}
