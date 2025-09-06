const $ = (sel, root = document) => root.querySelector(sel);
const $$ = (sel, root = document) => Array.from(root.querySelectorAll(sel));

const escapeHTML = (str) => String(str)
  .replaceAll("&", "&amp;")
  .replaceAll("<", "&lt;")
  .replaceAll(">", "&gt;")
  .replaceAll('"', "&quot;")
  .replaceAll("'", "&#039;");

const state = {
  data: [],
  filtered: [],
  query: "",
  type: "",
  license: "",
};

function bySipAsc(a, b) {
  return Number(a.sip) - Number(b.sip);
}

function buildOptions(select, values) {
  const current = select.value;
  select.innerHTML = '<option value="">All</option>' +
    Array.from(values)
      .sort((a, b) => a.localeCompare(b))
      .map(v => `<option value="${escapeHTML(v)}">${escapeHTML(v)}</option>`) 
      .join("");
  select.value = current;
}

function renderMeta() {
  const meta = $("#meta");
  const total = state.data.length;
  const shown = state.filtered.length;
  meta.textContent = shown === total ? `${shown} SIPs` : `${shown} of ${total} SIPs`;
}

function renderGrid() {
  const grid = $("#grid");
  grid.setAttribute("aria-busy", "false");
  grid.innerHTML = state.filtered.map(item => renderCard(item)).join("");

  const empty = $("#empty");
  empty.hidden = state.filtered.length !== 0;
}

function renderCard(item) {
  const authors = (item.authors && item.authors.length)
    ? escapeHTML(item.authors.join(" • "))
    : "";
  const emails = (item.emails && item.emails.length)
    ? item.emails.map(e => `<a href="mailto:${escapeHTML(e)}">${escapeHTML(e)}</a>`).join(" · ")
    : "";
  const copyright = item.copyright ? `<div class="copyright">${escapeHTML(item.copyright)}</div>` : "";
  const typeChip = item.type ? `<span class="chip" title="Type"><span class="dot"></span>${escapeHTML(item.type)}</span>` : "";
  const licenseChip = item.license ? `<span class="chip" title="License">${escapeHTML(item.license)}</span>` : "";

  return `
    <article class="card" tabindex="0" aria-label="SIP ${escapeHTML(item.sip)}: ${escapeHTML(item.title || "Untitled")}">
      <div class="sip">SIP ${escapeHTML(item.sip)}</div>
      <h2 class="title">${escapeHTML(item.title || "Untitled")}</h2>
      <div class="meta">${typeChip}${licenseChip}</div>
      ${authors ? `<div class="authors">${authors}</div>` : ""}
      ${emails ? `<div class="emails">${emails}</div>` : ""}
      ${copyright}
    </article>
  `;
}

function applyFilters() {
  const q = state.query.toLowerCase().trim();
  const match = (s) => (s || "").toLowerCase().includes(q);
  const type = state.type;
  const license = state.license;

  state.filtered = state.data.filter(item => {
    if (type && item.type !== type) return false;
    if (license && item.license !== license) return false;
    if (!q) return true;
    return (
      match(item.sip) ||
      match(item.title) ||
      (Array.isArray(item.authors) && item.authors.some(match)) ||
      (Array.isArray(item.emails) && item.emails.some(match))
    );
  }).sort(bySipAsc);

  renderMeta();
  renderGrid();
}

function debounce(fn, ms = 180) {
  let t = null;
  return (...args) => {
    clearTimeout(t);
    t = setTimeout(() => fn(...args), ms);
  };
}

async function init() {
  try {
    const res = await fetch('./sips.json', { cache: 'no-store' });
    if (!res.ok) throw new Error(`Failed to load sips.json: ${res.status}`);
    const data = await res.json();

    if (!Array.isArray(data)) throw new Error('Invalid JSON shape');
    state.data = data.sort(bySipAsc);
    state.filtered = state.data.slice();

    // Build filter options
    const types = new Set();
    const licenses = new Set();
    for (const it of state.data) {
      if (it.type) types.add(it.type);
      if (it.license) licenses.add(it.license);
    }
    buildOptions($("#type-filter"), types);
    buildOptions($("#license-filter"), licenses);

    renderMeta();
    renderGrid();
  } catch (err) {
    const grid = $("#grid");
    grid.setAttribute("aria-busy", "false");
    grid.innerHTML = `<div class="empty">${escapeHTML(err.message || 'Failed to load data')}</div>`;
  }

  // Wire interactions
  const onQuery = debounce((e) => { state.query = e.target.value; applyFilters(); }, 120);
  $("#q").addEventListener("input", onQuery);
  $("#type-filter").addEventListener("change", (e) => { state.type = e.target.value; applyFilters(); });
  $("#license-filter").addEventListener("change", (e) => { state.license = e.target.value; applyFilters(); });
}

init();


