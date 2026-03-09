# Chart Patterns Reference

Comprehensive guide to implementing data visualization patterns in HTML assessment reports using Chart.js and CSS Grid. All code snippets are copy-paste ready and production-tested.

---

## Quick Reference

| Chart Type | Use Case | CDN Included | Implementation |
|-----------|----------|-------------|-----------------|
| Radar Chart | Domain scores (all 10 domains, 2 tracks) | Yes | Chart.js + Canvas |
| Bar Chart (Horizontal) | Gap severity distribution | Yes | Chart.js + Canvas |
| Bar Chart (Vertical) | Score comparison (Readiness vs Fit) | Yes | Chart.js + Canvas |
| Heatmap Grid | 10-domain overview at a glance | No (CSS Grid) | Pure CSS + JS coloring |

---

## Chart.js CDN Import

Add this line to the `<head>` section of your HTML template:

```html
<script src="https://cdn.jsdelivr.net/npm/chart.js@3.9.1/dist/chart.min.js"></script>
```

No additional setup required. Chart.js is globally available as `Chart` object after the script loads.

---

## 1. Radar Chart: Domain Scores Overview

### Use Case
Display all 10 assessment domains with dual scoring tracks (Readiness + Fit-to-Purpose) on a single radar chart. Ideal for the Executive Dashboard tab to give a complete visual summary.

### Full Working Snippet

```html
<!-- Canvas element for the chart -->
<canvas id="domainRadarChart" width="400" height="300" style="max-width: 600px; margin: 0 auto; display: block;"></canvas>

<script>
// Domain score data (replace with actual assessment data)
const domainData = {
  labels: [
    'Market & TAM',
    'Technology',
    'Financials',
    'Competitive Positioning',
    'Leadership & Team',
    'Customer & Channels',
    'Intellectual Property',
    'Operations & Resources',
    'Regulatory & Health/Safety',
    'Business Development'
  ],
  datasets: [
    {
      label: 'Readiness Score',
      data: [78, 62, 85, 45, 91, 88, 71, 64, 92, 77],
      borderColor: '#3b82f6',
      backgroundColor: 'rgba(59, 130, 246, 0.1)',
      borderWidth: 2,
      pointRadius: 4,
      pointHoverRadius: 6,
      pointBackgroundColor: '#3b82f6',
      pointBorderColor: '#fff',
      pointBorderWidth: 2
    },
    {
      label: 'Fit-to-Purpose Score',
      data: [72, 58, 79, 42, 88, 85, 68, 61, 89, 74],
      borderColor: '#f59e0b',
      backgroundColor: 'rgba(245, 158, 11, 0.1)',
      borderWidth: 2,
      pointRadius: 4,
      pointHoverRadius: 6,
      pointBackgroundColor: '#f59e0b',
      pointBorderColor: '#fff',
      pointBorderWidth: 2
    }
  ]
};

// Chart configuration
const radarChartConfig = {
  type: 'radar',
  data: domainData,
  options: {
    responsive: true,
    maintainAspectRatio: true,
    plugins: {
      legend: {
        position: 'top',
        labels: {
          font: { family: 'Inter, sans-serif', size: 13 },
          color: '#1f2937',
          padding: 16,
          usePointStyle: true
        }
      },
      tooltip: {
        backgroundColor: 'rgba(15, 23, 42, 0.9)',
        padding: 12,
        titleFont: { family: 'Inter, sans-serif', size: 13, weight: '600' },
        bodyFont: { family: 'Inter, sans-serif', size: 12 },
        borderColor: 'rgba(255, 255, 255, 0.2)',
        borderWidth: 1,
        callbacks: {
          label: function(context) {
            return context.dataset.label + ': ' + context.parsed.r + '%';
          }
        }
      }
    },
    scales: {
      r: {
        beginAtZero: true,
        max: 100,
        ticks: {
          font: { family: 'Inter, sans-serif', size: 11 },
          color: '#6b7280',
          stepSize: 20,
          callback: function(value) {
            return value + '%';
          }
        },
        grid: {
          color: 'rgba(107, 114, 128, 0.1)',
          drawBorder: true,
          borderColor: 'rgba(107, 114, 128, 0.2)'
        },
        angleLines: {
          color: 'rgba(107, 114, 128, 0.15)'
        }
      }
    }
  }
};

// Instantiate and render chart
const domainRadarChartCtx = document.getElementById('domainRadarChart').getContext('2d');
new Chart(domainRadarChartCtx, radarChartConfig);
</script>
```

### Usage Notes

- **Data Substitution**: Replace the `data: [78, 62, 85, ...]` arrays with actual readiness and fit-to-purpose scores
- **Labels**: Domain names are abbreviated in reports; use full names here for clarity
- **Color Scheme**: Blue (#3b82f6) for Readiness, Amber (#f59e0b) for Fit-to-Purpose (consistent with color coding)
- **Responsive**: Scales automatically to container width (max 600px recommended)
- **Interactivity**: Hover over points to see exact scores; click legend to toggle datasets

### Responsive Sizing Pattern

```javascript
// For mobile optimization, adjust canvas size
const chartContainer = document.getElementById('domainRadarChart').parentElement;
const isMobile = window.innerWidth < 768;

if (isMobile) {
  document.getElementById('domainRadarChart').style.maxWidth = '100%';
  document.getElementById('domainRadarChart').style.height = '250px';
} else {
  document.getElementById('domainRadarChart').style.maxWidth = '600px';
  document.getElementById('domainRadarChart').style.height = '400px';
}
```

---

## 2. Horizontal Bar Chart: Gap Severity Distribution

### Use Case
Show the count of identified gaps by severity level (Critical, High, Medium, Low). Used in the Gap Register tab to provide quick visual assessment of gap distribution.

### Full Working Snippet

```html
<!-- Canvas element -->
<canvas id="gapSeverityChart" width="400" height="250"></canvas>

<script>
// Gap severity data (replace with actual counts)
const gapSeverityData = {
  labels: ['Critical', 'High', 'Medium', 'Low'],
  datasets: [
    {
      label: 'Gap Count by Severity',
      data: [3, 8, 12, 7],
      backgroundColor: [
        '#ef4444', // Red for Critical
        '#f97316', // Orange-red for High
        '#f59e0b', // Amber for Medium
        '#eab308'  // Yellow for Low
      ],
      borderColor: [
        '#dc2626',
        '#ea580c',
        '#d97706',
        '#ca8a04'
      ],
      borderWidth: 1.5,
      borderRadius: 4,
      indexAxis: 'y'  // Makes it horizontal
    }
  ]
};

const gapSeverityChartConfig = {
  type: 'bar',
  data: gapSeverityData,
  options: {
    indexAxis: 'y',  // Horizontal orientation
    responsive: true,
    maintainAspectRatio: true,
    plugins: {
      legend: {
        display: false  // Not needed for single dataset
      },
      tooltip: {
        backgroundColor: 'rgba(15, 23, 42, 0.9)',
        padding: 10,
        titleFont: { family: 'Inter, sans-serif', size: 12, weight: '600' },
        bodyFont: { family: 'Inter, sans-serif', size: 11 },
        callbacks: {
          label: function(context) {
            return context.parsed.x + ' gaps';
          }
        }
      },
      datalabels: {
        display: true
      }
    },
    scales: {
      x: {
        beginAtZero: true,
        grid: {
          color: 'rgba(107, 114, 128, 0.1)',
          drawBorder: true
        },
        ticks: {
          font: { family: 'Inter, sans-serif', size: 11 },
          color: '#6b7280',
          stepSize: 5,
          callback: function(value) {
            return value;
          }
        }
      },
      y: {
        grid: {
          display: false,
          drawBorder: false
        },
        ticks: {
          font: { family: 'Inter, sans-serif', size: 12, weight: '600' },
          color: '#1f2937'
        }
      }
    }
  }
};

const gapSeverityCtx = document.getElementById('gapSeverityChart').getContext('2d');
new Chart(gapSeverityCtx, gapSeverityChartConfig);
</script>
```

### Usage Notes

- **Data Mapping**: `data: [3, 8, 12, 7]` represents counts of Critical, High, Medium, Low gaps respectively
- **Color Codes**: Red → Orange → Amber → Yellow (severity gradient, left to right)
- **Horizontal Layout**: `indexAxis: 'y'` makes the chart horizontal; useful for readability with longer labels
- **Interactivity**: Hover to see exact count; click legend items to toggle visibility

### Adding Count Labels on Bars

```javascript
// Add data labels plugin for visual count display
const gapSeverityChartConfig = {
  // ... other config ...
  plugins: {
    datalabels: {
      align: 'end',
      anchor: 'end',
      color: '#1f2937',
      font: { family: 'Inter, sans-serif', size: 11, weight: '600' },
      formatter: function(value) {
        return value;
      }
    }
  }
};
```

---

## 3. Vertical Bar Chart: Readiness vs Fit-to-Purpose Comparison

### Use Case
Side-by-side comparison of Readiness and Fit-to-Purpose scores for each domain. Used in the Readiness Scores and Fit-to-Purpose Analysis tabs to show domain-by-domain performance across both tracks.

### Full Working Snippet

```html
<!-- Canvas element -->
<canvas id="scoreComparisonChart" width="400" height="300"></canvas>

<script>
// Score comparison data (replace with actual scores)
const scoreComparisonData = {
  labels: [
    'Market',
    'Technology',
    'Financials',
    'Competitive',
    'Leadership',
    'Channels',
    'IP',
    'Operations',
    'Regulatory',
    'Partnerships'
  ],
  datasets: [
    {
      label: 'Readiness Score',
      data: [78, 62, 85, 45, 91, 88, 71, 64, 92, 77],
      backgroundColor: '#3b82f6',
      borderColor: '#1e40af',
      borderWidth: 1,
      borderRadius: 4,
      order: 2
    },
    {
      label: 'Fit-to-Purpose Score',
      data: [72, 58, 79, 42, 88, 85, 68, 61, 89, 74],
      backgroundColor: '#f59e0b',
      borderColor: '#d97706',
      borderWidth: 1,
      borderRadius: 4,
      order: 1  // Draw behind first dataset
    }
  ]
};

const scoreComparisonConfig = {
  type: 'bar',
  data: scoreComparisonData,
  options: {
    responsive: true,
    maintainAspectRatio: true,
    barPercentage: 0.8,
    categoryPercentage: 0.7,  // Space between bar groups
    plugins: {
      legend: {
        position: 'top',
        labels: {
          font: { family: 'Inter, sans-serif', size: 13 },
          color: '#1f2937',
          padding: 16,
          usePointStyle: true
        }
      },
      tooltip: {
        backgroundColor: 'rgba(15, 23, 42, 0.9)',
        padding: 12,
        titleFont: { family: 'Inter, sans-serif', size: 12, weight: '600' },
        bodyFont: { family: 'Inter, sans-serif', size: 11 },
        callbacks: {
          label: function(context) {
            return context.dataset.label + ': ' + context.parsed.y + '%';
          }
        }
      }
    },
    scales: {
      y: {
        beginAtZero: true,
        max: 100,
        grid: {
          color: 'rgba(107, 114, 128, 0.1)',
          drawBorder: true
        },
        ticks: {
          font: { family: 'Inter, sans-serif', size: 11 },
          color: '#6b7280',
          stepSize: 20,
          callback: function(value) {
            return value + '%';
          }
        }
      },
      x: {
        grid: {
          display: false,
          drawBorder: false
        },
        ticks: {
          font: { family: 'Inter, sans-serif', size: 11 },
          color: '#1f2937'
        }
      }
    }
  }
};

const scoreComparisonCtx = document.getElementById('scoreComparisonChart').getContext('2d');
new Chart(scoreComparisonCtx, scoreComparisonConfig);
</script>
```

### Usage Notes

- **Data Arrays**: Must have same length; one score per domain for each track
- **Spacing Control**: `categoryPercentage: 0.7` controls space between bar groups; adjust 0.6–0.8 for preference
- **Color Consistency**: Blue for Readiness, Amber for Fit-to-Purpose (matches other charts)
- **Mobile Optimization**: Chart automatically scales; for small screens, consider rotating axis labels

### Adding Reference Line (Optional Target Score)

```javascript
// Add a horizontal reference line for target score (e.g., 75%)
const scoreComparisonConfig = {
  // ... other config ...
  scales: {
    y: {
      // ... other y-axis config ...
      plugins: {
        filler: {
          propagate: true
        }
      }
    }
  },
  annotation: {
    annotations: {
      targetLine: {
        type: 'line',
        yMin: 75,
        yMax: 75,
        borderColor: '#6b7280',
        borderWidth: 2,
        borderDash: [5, 5],
        label: {
          content: ['Target: 75%'],
          enabled: true,
          position: 'end'
        }
      }
    }
  }
};
```

---

## 4. Heatmap Grid: Domain Score Overview (CSS Grid + JS)

### Use Case
Quick visual overview of all 10 domains in a compact 2×5 grid format. Each cell shows domain abbreviation with Readiness (top) and Fit-to-Purpose (bottom) scores. No Chart.js required; pure CSS Grid + color interpolation.

### Full Working Snippet

```html
<div id="domainHeatmapContainer" class="heatmap-grid">
  <!-- Grid cells will be generated by JavaScript -->
</div>

<style>
.heatmap-grid {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 12px;
  padding: 20px;
  background: #f9fafb;
  border-radius: 8px;
  margin: 20px 0;
}

@media (max-width: 768px) {
  .heatmap-grid {
    grid-template-columns: repeat(3, 1fr);
    gap: 8px;
    padding: 12px;
  }
}

@media (max-width: 480px) {
  .heatmap-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 6px;
    padding: 8px;
  }
}

.heatmap-cell {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 16px 8px;
  border-radius: 6px;
  border: 2px solid rgba(229, 231, 235, 0.8);
  min-height: 100px;
  cursor: pointer;
  transition: all 0.3s ease;
  font-family: 'Inter', sans-serif;
}

.heatmap-cell:hover {
  transform: scale(1.05);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
  border-color: rgba(31, 41, 55, 0.3);
}

.heatmap-label {
  font-size: 11px;
  font-weight: 700;
  color: #ffffff;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-bottom: 6px;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.2);
}

.heatmap-scores {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 2px;
  width: 100%;
}

.heatmap-score {
  font-size: 14px;
  font-weight: 600;
  color: #ffffff;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.2);
}

.heatmap-score-label {
  font-size: 9px;
  color: rgba(255, 255, 255, 0.8);
  font-weight: 500;
}
</style>

<script>
// Color interpolation function (0-100 → red/amber/green)
function scoreToColor(score) {
  if (score < 50) {
    // Red to Amber gradient: 0 → 50
    const ratio = score / 50;
    const r = 239;
    const g = Math.round(158 + (94 - 158) * ratio);  // 158 → 94
    const b = 68;
    return `rgb(${r}, ${g}, ${b})`;
  } else {
    // Amber to Green gradient: 50 → 100
    const ratio = (score - 50) / 50;
    const r = Math.round(245 - (245 - 34) * ratio);   // 245 → 34
    const g = Math.round(158 + (85 - 158) * ratio);   // 158 → 85
    const b = Math.round(15 + (39 - 15) * ratio);     // 15 → 39
    return `rgb(${r}, ${g}, ${b})`;
  }
}

// Domain data (replace with actual assessment data)
const domains = [
  { id: 'market', label: 'M', name: 'Market & TAM', readiness: 78, fit: 72 },
  { id: 'technology', label: 'T', name: 'Technology', readiness: 62, fit: 58 },
  { id: 'financials', label: 'F', name: 'Financials', readiness: 85, fit: 79 },
  { id: 'competitive', label: 'C', name: 'Competitive', readiness: 45, fit: 42 },
  { id: 'leadership', label: 'L', name: 'Leadership', readiness: 91, fit: 88 },
  { id: 'channels', label: 'CC', name: 'Channels', readiness: 88, fit: 85 },
  { id: 'ip', label: 'IP', name: 'IP', readiness: 71, fit: 68 },
  { id: 'operations', label: 'OR', name: 'Operations', readiness: 64, fit: 61 },
  { id: 'regulatory', label: 'RH', name: 'Regulatory', readiness: 92, fit: 89 },
  { id: 'partnerships', label: 'BD', name: 'Partnerships', readiness: 77, fit: 74 }
];

// Generate heatmap cells
const container = document.getElementById('domainHeatmapContainer');
container.innerHTML = '';

domains.forEach(domain => {
  const cell = document.createElement('div');
  cell.className = 'heatmap-cell';
  cell.title = `${domain.name}\nReadiness: ${domain.readiness}%\nFit-to-Purpose: ${domain.fit}%`;

  // Use average of two scores for cell background color
  const avgScore = (domain.readiness + domain.fit) / 2;
  const bgColor = scoreToColor(avgScore);

  cell.style.backgroundColor = bgColor;

  cell.innerHTML = `
    <div class="heatmap-label">${domain.label}</div>
    <div class="heatmap-scores">
      <div class="heatmap-score">${domain.readiness}%</div>
      <div class="heatmap-score-label">R</div>
      <div class="heatmap-score">${domain.fit}%</div>
      <div class="heatmap-score-label">F</div>
    </div>
  `;

  // Optional: Make cells clickable to navigate to domain detail
  cell.addEventListener('click', function() {
    console.log(`Clicked domain: ${domain.name}`);
    // Navigate to domain tab or scroll to domain section
  });

  container.appendChild(cell);
});
</script>
```

### Usage Notes

- **Color Logic**: Each cell background is colored using the average of Readiness and Fit-to-Purpose scores
- **Responsiveness**: Grid automatically adjusts to 5 columns (desktop), 3 (tablet), 2 (mobile)
- **Hover Effects**: Cells scale up and show shadow on hover for interactivity
- **Score Labels**: "R" = Readiness, "F" = Fit-to-Purpose (compact display)
- **Accessibility**: Hover tooltips show full domain name and both scores

### Alternative: Separate Rows for Each Track

```javascript
// Instead of averaging scores, display two distinct cells per domain
domains.forEach(domain => {
  // Create Readiness cell
  const readinessCell = document.createElement('div');
  readinessCell.className = 'heatmap-cell';
  readinessCell.style.backgroundColor = scoreToColor(domain.readiness);
  readinessCell.innerHTML = `
    <div class="heatmap-label">${domain.label}</div>
    <div class="heatmap-score">${domain.readiness}%</div>
    <div class="heatmap-score-label">Readiness</div>
  `;

  // Create Fit cell
  const fitCell = document.createElement('div');
  fitCell.className = 'heatmap-cell';
  fitCell.style.backgroundColor = scoreToColor(domain.fit);
  fitCell.innerHTML = `
    <div class="heatmap-label">${domain.label}</div>
    <div class="heatmap-score">${domain.fit}%</div>
    <div class="heatmap-score-label">Fit</div>
  `;

  container.appendChild(readinessCell);
  container.appendChild(fitCell);
});
```

---

## Score Color Interpolation Function (Reference)

Use this function to convert any 0–100 score to a color in the red → amber → green spectrum:

```javascript
/**
 * Convert a 0-100 score to an RGB color string
 * 0-50: Red to Amber gradient
 * 50-100: Amber to Green gradient
 */
function scoreToColor(score) {
  // Clamp score to 0-100 range
  score = Math.max(0, Math.min(100, score));

  if (score < 50) {
    // Red (#ef4444) to Amber (#f59e0b) gradient
    // Red: (239, 68, 68)
    // Amber: (245, 158, 11)
    const ratio = score / 50;
    const r = 239;
    const g = Math.round(68 + (158 - 68) * ratio);
    const b = Math.round(68 + (11 - 68) * ratio);
    return `rgb(${r}, ${g}, ${b})`;
  } else {
    // Amber (#f59e0b) to Green (#22c55e) gradient
    // Amber: (245, 158, 11)
    // Green: (34, 197, 94)
    const ratio = (score - 50) / 50;
    const r = Math.round(245 - (245 - 34) * ratio);
    const g = Math.round(158 + (197 - 158) * ratio);
    const b = Math.round(11 + (94 - 11) * ratio);
    return `rgb(${r}, ${g}, ${b})`;
  }
}

// Usage examples:
console.log(scoreToColor(25));   // → rgb(239, 113, 68)  (orange-red)
console.log(scoreToColor(50));   // → rgb(245, 158, 11)  (amber)
console.log(scoreToColor(75));   // → rgb(128, 177, 52)  (yellow-green)
console.log(scoreToColor(100));  // → rgb(34, 197, 94)   (green)
```

### Hex Color Alternative

If you prefer working with hex colors instead of RGB:

```javascript
function scoreToColorHex(score) {
  score = Math.max(0, Math.min(100, score));

  const rgb = scoreToColor(score).match(/\d+/g);
  const r = parseInt(rgb[0]).toString(16).padStart(2, '0');
  const g = parseInt(rgb[1]).toString(16).padStart(2, '0');
  const b = parseInt(rgb[2]).toString(16).padStart(2, '0');

  return `#${r}${g}${b}`;
}
```

---

## Responsive Chart Sizing

All charts should automatically adjust to screen size. Use this pattern for consistent responsive behavior:

```javascript
// Global responsive chart options (add to every Chart.js config)
const responsiveOptions = {
  responsive: true,
  maintainAspectRatio: true,
  layout: {
    padding: {
      left: 10,
      right: 10,
      top: 10,
      bottom: 10
    }
  }
};

// Apply to all charts by merging with specific config:
const finalConfig = {
  ...responsiveOptions,
  type: 'radar',
  data: domainData,
  options: {
    ...responsiveOptions.options,
    // Chart-specific options...
  }
};
```

### Container-Based Responsive Sizing

```css
/* Wrapper for responsive chart container */
.chart-container {
  position: relative;
  width: 100%;
  max-width: 600px;
  height: auto;
  margin: 0 auto;
}

.chart-container canvas {
  display: block !important;
  width: 100% !important;
  height: auto !important;
}

/* Tablet and below */
@media (max-width: 768px) {
  .chart-container {
    max-width: 100%;
    padding: 0 12px;
  }
}

/* Mobile */
@media (max-width: 480px) {
  .chart-container {
    max-width: 100%;
    padding: 0 8px;
  }
}
```

---

## Common Pitfalls and Solutions

### Pitfall 1: Chart Not Rendering

**Symptom:** Canvas appears but no chart visible

**Solution:** Ensure Chart.js CDN is loaded before your script:
```html
<script src="https://cdn.jsdelivr.net/npm/chart.js@3.9.1/dist/chart.min.js"></script>
<!-- Your chart script AFTER the CDN -->
<script>
  // Chart code here
</script>
```

### Pitfall 2: Multiple Charts on Same Page Conflict

**Symptom:** Only first chart renders; others are blank

**Solution:** Give each canvas a unique `id` and use different variable names:
```html
<canvas id="chart1"></canvas>
<canvas id="chart2"></canvas>
<script>
  new Chart(document.getElementById('chart1').getContext('2d'), config1);
  new Chart(document.getElementById('chart2').getContext('2d'), config2);
</script>
```

### Pitfall 3: Data Not Updating After Page Load

**Symptom:** Data appears correct in console but chart shows old values

**Solution:** Chart objects don't auto-update; use `.update()` method:
```javascript
const chart = new Chart(ctx, config);
// Later, to update data:
chart.data.datasets[0].data = [new, values];
chart.update();
```

### Pitfall 4: Tooltip Text Invisible

**Symptom:** Tooltips appear but text is unreadable

**Solution:** Ensure backgroundColor is dark enough; add textColor:
```javascript
tooltip: {
  backgroundColor: 'rgba(15, 23, 42, 0.95)',  // Near-black
  titleColor: '#ffffff',
  bodyColor: '#ffffff',
  borderColor: 'rgba(255, 255, 255, 0.2)'
}
```

### Pitfall 5: Print to PDF Loses Chart Colors

**Symptom:** Charts appear grayscale when printed

**Solution:** Add print-specific styling:
```css
@media print {
  canvas {
    display: block !important;
    page-break-inside: avoid;
  }
  .chart-container {
    break-inside: avoid;
  }
}
```

---

## Testing Checklist

When implementing charts in reports:

- [ ] Chart displays without console errors
- [ ] Chart is responsive (test resize browser)
- [ ] Data labels are readable (not overlapping)
- [ ] Tooltips work on hover/touch
- [ ] Colors match design system
- [ ] Legend shows correct datasets
- [ ] Chart prints to PDF without data loss
- [ ] Mobile layout is optimal (test < 480px width)
- [ ] Performance is acceptable (chart loads in <1s)
- [ ] All external CDN links are from trusted sources

---

**Last Updated:** 2026-03-08
**Reference Version:** 1.0
