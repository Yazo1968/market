# Component Library Reference

Comprehensive library of reusable HTML/CSS components for building assessment reports. All components are self-contained, production-ready, and styled according to the design system.

---

## Quick Index

| Component | Purpose | Mobile Friendly | Interactivity |
|-----------|---------|-----------------|----------------|
| Determination Badge | Hero determination display | Yes | Static |
| Score Ring | Circular progress indicator | Yes | Static |
| Domain Heatmap Grid | 10-domain overview | Yes | Hover + Click |
| Gap Card | Individual gap item | Yes | Expand/Collapse |
| Tab Navigation | Multi-section navigation | Yes | Click + Keyboard |
| Collapsible Section | Expandable detail panels | Yes | Click to expand |
| Module Score Row | Domain module detail | Yes | Static |
| Source Citation | Research source display | Yes | Static |
| Alert Banner | Warning/info messages | Yes | Static |
| Data Table | Sortable data display | Yes | Sort + Filter |
| Phase Progress Bar | 4-phase workflow indicator | Yes | Static |
| Cover Page | PDF title page section | No (print only) | Static |
| QA/QC Entry | Quality check log item | Yes | Static |
| Session Audit Entry | Activity log item | Yes | Static |

---

## 1. Determination Badge (Large Hero)

Large, centered badge displaying the assessment determination with color coding and icon.

### HTML

```html
<div class="determination-badge determination-{{DETERMINATION_LOWERCASE}}">
  <div class="determination-badge__icon">
    <!-- Icon will be rendered via CSS -->
  </div>
  <div class="determination-badge__text">
    <div class="determination-badge__label">{{DETERMINATION}}</div>
    <div class="determination-badge__subtext">Assessment Date: {{DATE}}</div>
    <div class="determination-badge__company">{{COMPANY_NAME}}</div>
  </div>
</div>
```

### CSS

```css
.determination-badge {
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 32px 40px;
  border-radius: 12px;
  border: 3px solid currentColor;
  gap: 20px;
  margin: 20px 0;
  font-family: 'Inter', sans-serif;
  text-align: center;
  flex-direction: column;
}

.determination-badge__icon {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 48px;
  background: currentColor;
  color: white;
}

.determination-badge__label {
  font-size: 32px;
  font-weight: 700;
  margin-bottom: 8px;
}

.determination-badge__subtext {
  font-size: 13px;
  opacity: 0.85;
  margin-bottom: 4px;
}

.determination-badge__company {
  font-size: 16px;
  font-weight: 600;
}

/* Determination-specific styling */
.determination-badge.determination-go {
  color: #22c55e;
  background: rgba(34, 197, 94, 0.08);
}

.determination-badge.determination-conditional-go {
  color: #3b82f6;
  background: rgba(59, 130, 246, 0.08);
}

.determination-badge.determination-conditional-hold {
  color: #f59e0b;
  background: rgba(245, 158, 11, 0.08);
}

.determination-badge.determination-no-go {
  color: #ef4444;
  background: rgba(239, 68, 68, 0.08);
}

/* Responsive design */
@media (max-width: 768px) {
  .determination-badge {
    padding: 24px 20px;
    gap: 16px;
  }

  .determination-badge__icon {
    width: 60px;
    height: 60px;
    font-size: 36px;
  }

  .determination-badge__label {
    font-size: 24px;
  }
}
```

### Usage Notes

- Variable `{{DETERMINATION_LOWERCASE}}` should be: `go`, `conditional-go`, `conditional-hold`, or `no-go`
- Icon automatically changes based on determination type via CSS pseudo-elements (if using icon font)
- Center alignment and padding scale responsively
- Suitable as hero section of Executive Dashboard tab

---

## 2. Score Ring (SVG-Based Progress Circle)

Circular progress indicator showing a percentage score (0–100%) with color interpolation.

### HTML

```html
<div class="score-ring-container">
  <svg class="score-ring" width="140" height="140" viewBox="0 0 140 140">
    <!-- Background circle -->
    <circle cx="70" cy="70" r="60" fill="none" stroke="#e5e7eb" stroke-width="6"/>

    <!-- Progress circle (use scoreToColor() function to determine stroke-dasharray) -->
    <circle
      id="progressRing"
      cx="70"
      cy="70"
      r="60"
      fill="none"
      stroke="#22c55e"
      stroke-width="6"
      stroke-dasharray="0 376.99"
      stroke-linecap="round"
      style="transition: stroke-dasharray 0.5s ease;"
    />

    <!-- Center text -->
    <text x="70" y="70" text-anchor="middle" dy="-6" font-size="32" font-weight="700" fill="#1f2937">{{SCORE}}</text>
    <text x="70" y="70" text-anchor="middle" dy="14" font-size="16" fill="#6b7280">%</text>
  </svg>
</div>

<script>
// Score ring initialization
function initScoreRing(score) {
  const ring = document.getElementById('progressRing');
  const circumference = 2 * Math.PI * 60;  // 376.99
  const strokeDasharray = (score / 100) * circumference;

  // Determine color based on score
  function scoreToColor(score) {
    if (score < 50) {
      const ratio = score / 50;
      const r = 239;
      const g = Math.round(68 + (158 - 68) * ratio);
      const b = Math.round(68 + (11 - 68) * ratio);
      return `rgb(${r}, ${g}, ${b})`;
    } else {
      const ratio = (score - 50) / 50;
      const r = Math.round(245 - (245 - 34) * ratio);
      const g = Math.round(158 + (197 - 158) * ratio);
      const b = Math.round(11 + (94 - 11) * ratio);
      return `rgb(${r}, ${g}, ${b})`;
    }
  }

  ring.setAttribute('stroke-dasharray', `${strokeDasharray} ${circumference}`);
  ring.setAttribute('stroke', scoreToColor(score));
}

// Call on page load: initScoreRing(78);
</script>
```

### CSS

```css
.score-ring-container {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 140px;
  height: 140px;
  margin: 0 auto;
}

.score-ring {
  transform: rotate(-90deg);
  max-width: 100%;
}

/* Responsive sizing */
@media (max-width: 768px) {
  .score-ring-container {
    width: 100px;
    height: 100px;
  }

  .score-ring text:first-of-type {
    font-size: 24px;
  }

  .score-ring text:last-of-type {
    font-size: 12px;
  }
}
```

### Usage Notes

- Circumference calculation: `2 * π * radius = 2 * π * 60 ≈ 376.99`
- Stroke dasharray represents: (score / 100) * circumference
- Color interpolates from red (0%) → amber (50%) → green (100%)
- Smooth transition when score updates
- Compact size suitable for metric cards

### Integration with Actual Scores

```javascript
// When populating page with assessment data:
document.addEventListener('DOMContentLoaded', function() {
  const readinessScore = {{READINESS_SCORE}};  // e.g., 76.5
  const fitScore = {{FIT_SCORE}};              // e.g., 72.3

  initScoreRing(readinessScore);
  // If second ring exists:
  // document.getElementById('fitScoreRing').init(fitScore);
});
```

---

## 3. Domain Heatmap Grid

See **`references/chart-patterns.md`** → "4. Heatmap Grid: Domain Score Overview" for complete implementation.

---

## 4. Gap Card (Expandable)

Individual gap item with severity badge, domain, description, and expandable detail section.

### HTML

```html
<div class="gap-card" data-severity="{{SEVERITY}}">
  <div class="gap-card__header">
    <div class="gap-card__badge gap-severity-{{SEVERITY_LOWERCASE}}">
      {{SEVERITY}}
    </div>
    <div class="gap-card__title">
      <span class="gap-card__domain">{{DOMAIN_NAME}}</span>
      <span class="gap-card__description">{{GAP_DESCRIPTION}}</span>
    </div>
    <button class="gap-card__toggle" aria-expanded="false">
      <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
        <path d="M6 8l4 4 4-4" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
      </svg>
    </button>
  </div>

  <div class="gap-card__details" hidden>
    <div class="gap-card__detail-group">
      <label>Full Description</label>
      <p>{{FULL_DESCRIPTION}}</p>
    </div>
    <div class="gap-card__detail-group">
      <label>Impact</label>
      <p>{{IMPACT_DESCRIPTION}}</p>
    </div>
    <div class="gap-card__detail-group">
      <label>Suggested Remediation</label>
      <p>{{REMEDIATION_SUGGESTION}}</p>
    </div>
    <div class="gap-card__detail-group">
      <label>Status</label>
      <span class="gap-card__status">{{STATUS}}</span>
    </div>
  </div>
</div>

<script>
// Gap card toggle behavior
document.querySelectorAll('.gap-card__toggle').forEach(button => {
  button.addEventListener('click', function() {
    const card = this.closest('.gap-card');
    const details = card.querySelector('.gap-card__details');
    const isExpanded = details.hidden;

    details.hidden = !isExpanded;
    this.setAttribute('aria-expanded', isExpanded);
  });
});
</script>
```

### CSS

```css
.gap-card {
  border: 1px solid #e5e7eb;
  border-radius: 8px;
  overflow: hidden;
  margin: 12px 0;
  background: white;
  transition: all 0.3s ease;
}

.gap-card:hover {
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
  border-color: #d1d5db;
}

.gap-card__header {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 16px;
  cursor: pointer;
  user-select: none;
}

.gap-card__badge {
  padding: 4px 10px;
  border-radius: 16px;
  font-size: 12px;
  font-weight: 600;
  white-space: nowrap;
  color: white;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.gap-severity-critical { background: #ef4444; }
.gap-severity-high { background: #f97316; }
.gap-severity-medium { background: #f59e0b; }
.gap-severity-low { background: #eab308; }

.gap-card__title {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.gap-card__domain {
  font-weight: 600;
  color: #1f2937;
  font-size: 14px;
}

.gap-card__description {
  font-size: 13px;
  color: #6b7280;
}

.gap-card__toggle {
  background: none;
  border: none;
  cursor: pointer;
  color: #6b7280;
  padding: 4px;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: transform 0.3s ease;
}

.gap-card__toggle[aria-expanded="true"] {
  transform: rotate(180deg);
  color: #1f2937;
}

.gap-card__details {
  background: #f9fafb;
  padding: 16px;
  border-top: 1px solid #e5e7eb;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.gap-card__detail-group {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.gap-card__detail-group label {
  font-size: 12px;
  font-weight: 600;
  color: #1f2937;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.gap-card__detail-group p {
  font-size: 13px;
  color: #4b5563;
  line-height: 1.5;
  margin: 0;
}

.gap-card__status {
  display: inline-block;
  padding: 4px 8px;
  background: #dbeafe;
  color: #1e40af;
  border-radius: 4px;
  font-size: 12px;
  font-weight: 500;
}

/* Responsive */
@media (max-width: 640px) {
  .gap-card__header {
    flex-direction: column;
    align-items: flex-start;
  }

  .gap-card__title {
    width: 100%;
  }
}
```

### Usage Notes

- Severity levels: Critical (red), High (orange-red), Medium (amber), Low (yellow)
- Expandable detail section hidden by default
- Arrow icon rotates 180° when expanded
- Hover effects provide visual feedback
- Suitable for Gap Register tab

---

## 5. Tab Navigation Component

Multi-tab navigation bar with content switching and keyboard support.

### HTML

```html
<nav class="tab-nav" role="tablist">
  <button class="tab-nav__item" role="tab" aria-selected="true" aria-controls="panel-executive">
    Executive Dashboard
  </button>
  <button class="tab-nav__item" role="tab" aria-selected="false" aria-controls="panel-framework">
    Framework
  </button>
  <button class="tab-nav__item" role="tab" aria-selected="false" aria-controls="panel-readiness">
    Readiness Scores
  </button>
  <button class="tab-nav__item" role="tab" aria-selected="false" aria-controls="panel-fit">
    Fit-to-Purpose
  </button>
  <button class="tab-nav__item" role="tab" aria-selected="false" aria-controls="panel-gaps">
    Gap Register
  </button>
  <!-- Additional tabs... -->
</nav>

<div class="tab-content">
  <div id="panel-executive" class="tab-panel" role="tabpanel" aria-labelledby="tab-executive">
    <!-- Executive dashboard content -->
  </div>
  <div id="panel-framework" class="tab-panel" role="tabpanel" aria-labelledby="tab-framework" hidden>
    <!-- Framework content -->
  </div>
  <!-- Additional panels... -->
</div>

<script>
// Tab navigation behavior
class TabNavigation {
  constructor() {
    this.tabs = document.querySelectorAll('[role="tab"]');
    this.panels = document.querySelectorAll('[role="tabpanel"]');

    this.tabs.forEach(tab => {
      tab.addEventListener('click', () => this.selectTab(tab));
      tab.addEventListener('keydown', (e) => this.handleKeydown(e));
    });
  }

  selectTab(selectedTab) {
    // Hide all panels
    this.panels.forEach(panel => panel.hidden = true);

    // Deselect all tabs
    this.tabs.forEach(tab => {
      tab.setAttribute('aria-selected', 'false');
      tab.classList.remove('is-active');
    });

    // Show selected panel
    const panelId = selectedTab.getAttribute('aria-controls');
    document.getElementById(panelId).hidden = false;

    // Select clicked tab
    selectedTab.setAttribute('aria-selected', 'true');
    selectedTab.classList.add('is-active');
  }

  handleKeydown(e) {
    let targetTab = null;

    switch(e.key) {
      case 'ArrowRight':
        targetTab = this.getNextTab(e.target);
        break;
      case 'ArrowLeft':
        targetTab = this.getPrevTab(e.target);
        break;
      case 'Home':
        targetTab = this.tabs[0];
        break;
      case 'End':
        targetTab = this.tabs[this.tabs.length - 1];
        break;
      default:
        return;
    }

    if (targetTab) {
      e.preventDefault();
      targetTab.focus();
      this.selectTab(targetTab);
    }
  }

  getNextTab(currentTab) {
    const index = Array.from(this.tabs).indexOf(currentTab);
    return this.tabs[index + 1] || this.tabs[0];
  }

  getPrevTab(currentTab) {
    const index = Array.from(this.tabs).indexOf(currentTab);
    return this.tabs[index - 1] || this.tabs[this.tabs.length - 1];
  }
}

new TabNavigation();
</script>
```

### CSS

```css
.tab-nav {
  display: flex;
  border-bottom: 2px solid #e5e7eb;
  background: white;
  position: sticky;
  top: 0;
  z-index: 100;
  overflow-x: auto;
  -webkit-overflow-scrolling: touch;
}

.tab-nav__item {
  flex: 1;
  min-width: 120px;
  padding: 16px 20px;
  border: none;
  background: none;
  cursor: pointer;
  font-family: 'Inter', sans-serif;
  font-size: 14px;
  font-weight: 500;
  color: #6b7280;
  border-bottom: 3px solid transparent;
  transition: all 0.3s ease;
  white-space: nowrap;
  text-align: center;
}

.tab-nav__item:hover {
  color: #1f2937;
  background: #f9fafb;
}

.tab-nav__item[aria-selected="true"],
.tab-nav__item.is-active {
  color: #1f2937;
  border-bottom-color: #3b82f6;
  font-weight: 600;
  background: white;
}

.tab-nav__item:focus {
  outline: 2px solid #3b82f6;
  outline-offset: -2px;
}

.tab-content {
  background: white;
}

.tab-panel {
  padding: 24px;
  display: block;
}

.tab-panel[hidden] {
  display: none;
}

/* Responsive: Stack tabs on mobile */
@media (max-width: 640px) {
  .tab-nav {
    flex-wrap: wrap;
    border-bottom: 1px solid #e5e7eb;
  }

  .tab-nav__item {
    flex: 0 1 50%;
    min-width: auto;
    padding: 12px 16px;
    font-size: 12px;
  }

  .tab-panel {
    padding: 16px;
  }
}
```

### Usage Notes

- Keyboard navigation: Arrow keys (left/right), Home (first tab), End (last tab)
- Active tab marked with blue underline
- Sticky positioning keeps nav visible while scrolling content
- ARIA roles ensure screen reader accessibility
- Horizontal scroll on mobile for many tabs

---

## 6. Collapsible Section Component

Expandable detail panel for domain findings, frameworks, etc.

### HTML

```html
<div class="collapsible" data-id="{{SECTION_ID}}">
  <button class="collapsible__trigger" aria-expanded="false">
    <span class="collapsible__title">{{SECTION_TITLE}}</span>
    <svg class="collapsible__icon" width="20" height="20" viewBox="0 0 20 20" fill="none">
      <path d="M6 8l4 4 4-4" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
    </svg>
  </button>

  <div class="collapsible__content" hidden>
    {{SECTION_CONTENT_HTML}}
  </div>
</div>

<script>
// Collapsible functionality
document.querySelectorAll('.collapsible__trigger').forEach(trigger => {
  trigger.addEventListener('click', function() {
    const collapsible = this.closest('.collapsible');
    const content = collapsible.querySelector('.collapsible__content');
    const isExpanded = !content.hidden;

    content.hidden = isExpanded;
    this.setAttribute('aria-expanded', !isExpanded);
  });
});
</script>
```

### CSS

```css
.collapsible {
  border: 1px solid #e5e7eb;
  border-radius: 8px;
  margin: 12px 0;
  background: white;
}

.collapsible__trigger {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 16px;
  border: none;
  background: white;
  cursor: pointer;
  font-family: 'Inter', sans-serif;
  font-size: 14px;
  font-weight: 600;
  color: #1f2937;
  transition: background 0.3s ease;
}

.collapsible__trigger:hover {
  background: #f9fafb;
}

.collapsible__trigger:focus {
  outline: 2px solid #3b82f6;
  outline-offset: -2px;
}

.collapsible__icon {
  color: #6b7280;
  flex-shrink: 0;
  transition: transform 0.3s ease;
  margin-left: 12px;
}

.collapsible__trigger[aria-expanded="true"] .collapsible__icon {
  transform: rotate(180deg);
}

.collapsible__content {
  padding: 16px;
  border-top: 1px solid #e5e7eb;
  background: #f9fafb;
}

.collapsible__content[hidden] {
  display: none;
}

/* Nested collapsibles */
.collapsible .collapsible {
  border-left: 2px solid #e5e7eb;
  border-right: none;
  border-top: none;
  border-bottom: none;
  margin: 8px 0 8px 16px;
}
```

### Usage Notes

- Click to expand/collapse
- Icon rotates 180° when expanded
- Suitable for domain detail sections, framework notes, methodology explanations
- Can be nested for multi-level hierarchies

---

## 7. Module Score Row

Compact row displaying a module with scores and status indicators.

### HTML

```html
<div class="module-row">
  <div class="module-row__module">
    <span class="module-row__name">{{MODULE_NAME}}</span>
    <span class="module-row__status module-status-{{STATUS_LOWERCASE}}">{{STATUS}}</span>
  </div>
  <div class="module-row__scores">
    <div class="module-row__score">
      <span class="module-row__score-label">Readiness</span>
      <span class="module-row__score-value">{{READINESS}}</span>
    </div>
    <div class="module-row__score">
      <span class="module-row__score-label">Fit</span>
      <span class="module-row__score-value">{{FIT}}</span>
    </div>
  </div>
  <div class="module-row__indicators">
    <div class="score-indicator" style="background: {{READINESS_COLOR}};" title="Readiness: {{READINESS}}%"></div>
    <div class="score-indicator" style="background: {{FIT_COLOR}};" title="Fit: {{FIT}}%"></div>
  </div>
</div>
```

### CSS

```css
.module-row {
  display: grid;
  grid-template-columns: 1fr auto auto;
  gap: 16px;
  align-items: center;
  padding: 12px;
  border-bottom: 1px solid #e5e7eb;
  background: white;
}

.module-row:last-child {
  border-bottom: none;
}

.module-row__module {
  display: flex;
  align-items: center;
  gap: 8px;
}

.module-row__name {
  font-size: 13px;
  font-weight: 500;
  color: #1f2937;
}

.module-row__status {
  padding: 2px 6px;
  border-radius: 4px;
  font-size: 10px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  color: white;
}

.module-status-complete { background: #22c55e; }
.module-status-incomplete { background: #f59e0b; }
.module-status-pending { background: #9ca3af; }

.module-row__scores {
  display: flex;
  gap: 16px;
  text-align: center;
  min-width: 100px;
}

.module-row__score {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.module-row__score-label {
  font-size: 10px;
  color: #6b7280;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.module-row__score-value {
  font-size: 14px;
  font-weight: 700;
  color: #1f2937;
}

.module-row__indicators {
  display: flex;
  gap: 6px;
  min-width: 30px;
}

.score-indicator {
  width: 12px;
  height: 12px;
  border-radius: 2px;
  transition: opacity 0.3s ease;
}

.module-row:hover .score-indicator {
  opacity: 0.8;
}

/* Responsive */
@media (max-width: 640px) {
  .module-row {
    grid-template-columns: 1fr;
    gap: 8px;
  }

  .module-row__scores {
    width: 100%;
    justify-content: space-around;
  }
}
```

### Usage Notes

- Compact display suitable for module-level detail tables
- Colors for score indicators use `scoreToColor()` function
- Status badges indicate completion (Complete/Incomplete/Pending)
- Hover effects provide visual feedback

---

## 8. Source Citation Component

Research source reference with confidence level badge.

### HTML

```html
<div class="source-citation">
  <div class="source-citation__main">
    <span class="source-citation__id">{{SOURCE_ID}}</span>
    <span class="source-citation__name">{{SOURCE_NAME}}</span>
    <span class="source-citation__type">{{SOURCE_TYPE}}</span>
  </div>
  <div class="source-citation__metadata">
    <span class="source-citation__date">Accessed: {{DATE}}</span>
    <span class="source-citation__confidence confidence-{{CONFIDENCE_LEVEL_LOWERCASE}}">
      {{CONFIDENCE_LEVEL}} Confidence
    </span>
  </div>
</div>
```

### CSS

```css
.source-citation {
  padding: 12px;
  border-left: 3px solid #3b82f6;
  background: #eff6ff;
  border-radius: 4px;
  margin: 8px 0;
  font-family: 'Inter', sans-serif;
}

.source-citation__main {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 8px;
}

.source-citation__id {
  font-size: 11px;
  font-weight: 700;
  color: #1e40af;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.source-citation__name {
  font-size: 13px;
  font-weight: 500;
  color: #1f2937;
  flex: 1;
}

.source-citation__type {
  padding: 2px 6px;
  background: #dbeafe;
  border-radius: 3px;
  font-size: 10px;
  color: #1e40af;
  font-weight: 600;
  text-transform: capitalize;
}

.source-citation__metadata {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  font-size: 12px;
  color: #6b7280;
}

.source-citation__date {
  font-size: 11px;
}

.source-citation__confidence {
  padding: 2px 6px;
  border-radius: 3px;
  font-weight: 600;
  font-size: 11px;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  color: white;
}

.confidence-high { background: #22c55e; }
.confidence-medium { background: #f59e0b; }
.confidence-low { background: #ef4444; }

/* Responsive */
@media (max-width: 640px) {
  .source-citation__metadata {
    flex-direction: column;
    align-items: flex-start;
  }
}
```

### Usage Notes

- Blue left border indicates research source
- Confidence badges color-coded: green (high), amber (medium), red (low)
- Suitable for Research Provenance tab
- Can be repeated for each source in assessment

---

## 9. Alert/Flag Banner Component

Warning, info, critical, or success alert messages.

### HTML

```html
<div class="alert alert-{{ALERT_TYPE}}">
  <div class="alert__icon">
    <!-- Icon via CSS or emoji -->
  </div>
  <div class="alert__content">
    <div class="alert__title">{{TITLE}}</div>
    <div class="alert__message">{{MESSAGE}}</div>
  </div>
  <button class="alert__close" aria-label="Close alert">
    <svg width="16" height="16" viewBox="0 0 16 16" fill="none">
      <path d="M2 2l12 12M14 2L2 14" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
    </svg>
  </button>
</div>

<script>
// Alert dismiss behavior
document.querySelectorAll('.alert__close').forEach(button => {
  button.addEventListener('click', function() {
    this.closest('.alert').remove();
  });
});
</script>
```

### CSS

```css
.alert {
  display: flex;
  align-items: flex-start;
  gap: 12px;
  padding: 14px 16px;
  border-radius: 6px;
  border-left: 4px solid;
  margin: 16px 0;
  font-family: 'Inter', sans-serif;
}

.alert__icon {
  flex-shrink: 0;
  font-size: 18px;
}

.alert__content {
  flex: 1;
}

.alert__title {
  font-weight: 600;
  font-size: 13px;
  margin-bottom: 4px;
}

.alert__message {
  font-size: 12px;
  line-height: 1.5;
}

.alert__close {
  background: none;
  border: none;
  cursor: pointer;
  color: currentColor;
  padding: 4px;
  flex-shrink: 0;
  transition: opacity 0.3s ease;
}

.alert__close:hover {
  opacity: 0.7;
}

/* Alert type variants */
.alert-critical {
  background: #fef2f2;
  border-left-color: #ef4444;
  color: #991b1b;
}

.alert-warning {
  background: #fffbeb;
  border-left-color: #f59e0b;
  color: #92400e;
}

.alert-info {
  background: #eff6ff;
  border-left-color: #3b82f6;
  color: #1e40af;
}

.alert-success {
  background: #f0fdf4;
  border-left-color: #22c55e;
  color: #166534;
}
```

### Usage Notes

- Four alert types: critical (red), warning (amber), info (blue), success (green)
- Dismissable with close button
- Suitable for framework notes, QA issues, important notices
- Stack multiple alerts for multiple messages

---

## 10. Data Table Component

Sortable, filterable table for displaying structured data (domains, modules, gaps, sources).

### HTML

```html
<div class="data-table">
  <table>
    <thead>
      <tr>
        <th class="data-table__header sortable" data-column="domain">Domain</th>
        <th class="data-table__header sortable" data-column="score">Score</th>
        <th class="data-table__header sortable" data-column="status">Status</th>
        <th class="data-table__header">Actions</th>
      </tr>
    </thead>
    <tbody>
      <tr class="data-table__row">
        <td class="data-table__cell">{{DOMAIN_NAME}}</td>
        <td class="data-table__cell numeric">{{SCORE}}%</td>
        <td class="data-table__cell"><span class="status-badge">{{STATUS}}</span></td>
        <td class="data-table__cell"><button class="data-table__action">View</button></td>
      </tr>
      <!-- Additional rows... -->
    </tbody>
  </table>
</div>

<script>
// Sort functionality
class DataTable {
  constructor(tableElement) {
    this.table = tableElement;
    this.headers = tableElement.querySelectorAll('.sortable');
    this.headers.forEach(header => {
      header.addEventListener('click', () => this.sortTable(header));
    });
  }

  sortTable(header) {
    const column = header.dataset.column;
    const rows = Array.from(this.table.querySelectorAll('tbody tr'));
    const isAsc = header.classList.contains('sort-asc');

    rows.sort((a, b) => {
      const aValue = a.querySelector(`[data-column="${column}"]`)?.textContent || '';
      const bValue = b.querySelector(`[data-column="${column}"]`)?.textContent || '';

      if (isAsc) {
        return aValue.localeCompare(bValue);
      } else {
        return bValue.localeCompare(aValue);
      }
    });

    this.table.classList.toggle('sort-asc');
    this.table.classList.toggle('sort-desc');

    rows.forEach(row => this.table.querySelector('tbody').appendChild(row));
  }
}

new DataTable(document.querySelector('.data-table'));
</script>
```

### CSS

```css
.data-table {
  width: 100%;
  overflow-x: auto;
  border: 1px solid #e5e7eb;
  border-radius: 8px;
  margin: 16px 0;
}

.data-table table {
  width: 100%;
  border-collapse: collapse;
  font-family: 'Inter', sans-serif;
  font-size: 13px;
}

.data-table__header {
  padding: 12px 16px;
  text-align: left;
  font-weight: 600;
  background: #f3f4f6;
  color: #1f2937;
  border-bottom: 2px solid #e5e7eb;
  white-space: nowrap;
}

.data-table__header.sortable {
  cursor: pointer;
  user-select: none;
}

.data-table__header.sortable:hover {
  background: #e5e7eb;
}

.data-table__header.sort-asc::after {
  content: ' ▲';
  font-size: 10px;
}

.data-table__header.sort-desc::after {
  content: ' ▼';
  font-size: 10px;
}

.data-table__row {
  border-bottom: 1px solid #e5e7eb;
  transition: background 0.2s ease;
}

.data-table__row:hover {
  background: #f9fafb;
}

.data-table__row:last-child {
  border-bottom: none;
}

.data-table__cell {
  padding: 12px 16px;
  color: #1f2937;
}

.data-table__cell.numeric {
  text-align: right;
  font-variant-numeric: tabular-nums;
}

.data-table__action {
  padding: 4px 8px;
  background: #3b82f6;
  color: white;
  border: none;
  border-radius: 4px;
  font-size: 12px;
  cursor: pointer;
  transition: background 0.3s ease;
}

.data-table__action:hover {
  background: #2563eb;
}

/* Responsive: Scroll on mobile */
@media (max-width: 640px) {
  .data-table {
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
  }

  .data-table table {
    font-size: 12px;
  }

  .data-table__cell {
    padding: 8px 12px;
  }
}
```

### Usage Notes

- Click header (if sortable) to sort column
- Hover rows for visual feedback
- Numeric columns right-aligned
- Responsive scroll on mobile
- Suitable for domain lists, module tables, gap registers, source logs

---

## 11. Phase Progress Bar

4-step workflow progress indicator showing current phase position.

### HTML

```html
<div class="phase-progress">
  <div class="phase-progress__step phase-progress__step--active">
    <div class="phase-progress__circle">1</div>
    <div class="phase-progress__label">Pre-Assessment</div>
  </div>
  <div class="phase-progress__connector"></div>

  <div class="phase-progress__step phase-progress__step--active">
    <div class="phase-progress__circle">2</div>
    <div class="phase-progress__label">Assessment</div>
  </div>
  <div class="phase-progress__connector"></div>

  <div class="phase-progress__step">
    <div class="phase-progress__circle">3</div>
    <div class="phase-progress__label">Sensitivity</div>
  </div>
  <div class="phase-progress__connector"></div>

  <div class="phase-progress__step">
    <div class="phase-progress__circle">4</div>
    <div class="phase-progress__label">Recommendations</div>
  </div>
</div>
```

### CSS

```css
.phase-progress {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  padding: 24px;
  background: #f9fafb;
  border-radius: 8px;
  margin: 16px 0;
}

.phase-progress__step {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
  flex: 1;
  text-align: center;
}

.phase-progress__circle {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  font-size: 16px;
  background: #e5e7eb;
  color: #6b7280;
  border: 2px solid transparent;
  transition: all 0.3s ease;
}

.phase-progress__step--active .phase-progress__circle {
  background: #3b82f6;
  color: white;
  border-color: #1e40af;
}

.phase-progress__label {
  font-size: 12px;
  font-weight: 500;
  color: #6b7280;
}

.phase-progress__step--active .phase-progress__label {
  color: #1f2937;
  font-weight: 600;
}

.phase-progress__connector {
  flex: 0 0 40px;
  height: 2px;
  background: #e5e7eb;
}

.phase-progress__step--active ~ .phase-progress__connector {
  background: #3b82f6;
}

/* Responsive: Stack on mobile */
@media (max-width: 640px) {
  .phase-progress {
    gap: 8px;
    padding: 16px;
  }

  .phase-progress__circle {
    width: 32px;
    height: 32px;
    font-size: 14px;
  }

  .phase-progress__label {
    font-size: 10px;
  }

  .phase-progress__connector {
    flex: 0 0 16px;
  }
}
```

### Usage Notes

- Active steps marked with blue circle and solid connector
- Numbered 1–4 for four assessment phases
- Responsive layout adapts to mobile
- Suitable for report header or phase navigation section

---

## 12. QA/QC Entry Component

Individual quality assurance check log item.

### HTML

```html
<div class="qacc-entry">
  <div class="qacc-entry__header">
    <span class="qacc-entry__id">{{CHECK_ID}}</span>
    <span class="qacc-entry__category">{{CATEGORY}}</span>
    <span class="qacc-entry__status qacc-status-{{STATUS_LOWERCASE}}">{{STATUS}}</span>
  </div>
  <div class="qacc-entry__finding">
    <label>Finding:</label>
    <p>{{FINDING_DESCRIPTION}}</p>
  </div>
  <div class="qacc-entry__resolution">
    <label>Resolution:</label>
    <p>{{RESOLUTION_DESCRIPTION}}</p>
  </div>
  <div class="qacc-entry__footer">
    <span class="qacc-entry__assessor">Assessed by: {{ASSESSOR_NAME}}</span>
    <span class="qacc-entry__date">{{DATE}}</span>
  </div>
</div>
```

### CSS

```css
.qacc-entry {
  border: 1px solid #e5e7eb;
  border-radius: 6px;
  padding: 12px;
  margin: 8px 0;
  background: white;
  font-family: 'Inter', sans-serif;
  font-size: 12px;
}

.qacc-entry__header {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 8px;
  padding-bottom: 8px;
  border-bottom: 1px solid #f3f4f6;
}

.qacc-entry__id {
  font-weight: 700;
  color: #1f2937;
  text-transform: uppercase;
  font-size: 11px;
  letter-spacing: 0.5px;
}

.qacc-entry__category {
  padding: 2px 6px;
  background: #dbeafe;
  color: #1e40af;
  border-radius: 3px;
  font-size: 10px;
  font-weight: 600;
  text-transform: capitalize;
}

.qacc-entry__status {
  padding: 2px 6px;
  border-radius: 3px;
  font-weight: 600;
  text-transform: uppercase;
  font-size: 10px;
  color: white;
  margin-left: auto;
}

.qacc-status-passed { background: #22c55e; }
.qacc-status-failed { background: #ef4444; }
.qacc-status-waived { background: #9ca3af; }

.qacc-entry__finding,
.qacc-entry__resolution {
  margin: 6px 0;
}

.qacc-entry__finding label,
.qacc-entry__resolution label {
  display: block;
  font-weight: 600;
  color: #1f2937;
  margin-bottom: 2px;
}

.qacc-entry__finding p,
.qacc-entry__resolution p {
  margin: 0;
  color: #6b7280;
  line-height: 1.4;
}

.qacc-entry__footer {
  display: flex;
  justify-content: space-between;
  padding-top: 8px;
  border-top: 1px solid #f3f4f6;
  font-size: 11px;
  color: #9ca3af;
}
```

### Usage Notes

- Status color-coded: green (passed), red (failed), gray (waived)
- Suitable for QA/QC Log tab in assessment reports
- Shows check ID, category, assessment date, and assessor name

---

## 13. Session Audit Entry Component

Activity log entry for assessment workflow actions.

### HTML

```html
<div class="audit-entry">
  <div class="audit-entry__timestamp">{{TIMESTAMP}}</div>
  <div class="audit-entry__content">
    <div class="audit-entry__action">{{ACTION}}</div>
    <div class="audit-entry__actor">By: {{ACTOR_NAME}}</div>
    <div class="audit-entry__details">{{DETAILS}}</div>
  </div>
</div>
```

### CSS

```css
.audit-entry {
  display: flex;
  gap: 16px;
  padding: 12px;
  border-left: 2px solid #d1d5db;
  margin: 8px 0;
  background: white;
  font-family: 'Inter', sans-serif;
}

.audit-entry:first-child {
  border-left-color: #3b82f6;
}

.audit-entry__timestamp {
  flex-shrink: 0;
  min-width: 100px;
  font-size: 11px;
  color: #9ca3af;
  font-weight: 500;
  text-align: right;
}

.audit-entry__content {
  flex: 1;
}

.audit-entry__action {
  font-size: 13px;
  font-weight: 600;
  color: #1f2937;
  margin-bottom: 2px;
}

.audit-entry__actor {
  font-size: 11px;
  color: #6b7280;
}

.audit-entry__details {
  font-size: 12px;
  color: #6b7280;
  line-height: 1.4;
  margin-top: 4px;
}
```

### Usage Notes

- Timeline-style display with left border
- Most recent entry at top (optional: reverse order)
- Suitable for Session Audit Trail in Appendix tab
- Shows timestamp, action, actor, and brief details

---

**Last Updated:** 2026-03-08
**Library Version:** 1.0
**Status:** Production ready
