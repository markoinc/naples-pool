# Concrete Site Template Documentation
**Template Version:** 1.0
**Based on:** fayettevilleconcrete-pros.com
**Last Updated:** 2026-02-17

---

## 📁 Site Structure

```
site-root/
├── index.html                      # Homepage
├── css/styles.css                  # All styles (CSS variables for theming)
├── robots.txt                      # Sitemap reference
├── sitemap.xml                     # All URLs
├── favicon.ico                     # Site icon
├── 404.html                        # Error page
│
├── images/                         # All images
│   ├── logo.png                    # Site logo
│   ├── hero-bg.webp                # Hero background
│   ├── [service-images].webp       # Service photos
│   └── ...
│
├── concrete-driveway-contractors/  # Service: Driveways
│   └── index.html
├── concrete-patio-contractors/     # Service: Patios
│   └── index.html
├── concrete-slab-contractors/      # Service: Slabs
│   └── index.html
├── stamped-concrete-contractors/   # Service: Stamped
│   └── index.html
│
├── about/                          # About Us
│   └── index.html
├── contact/                        # Contact page
│   └── index.html
├── thankyou/                       # Form thank you
│   └── index.html
├── locations/                      # Service area hub
│   └── index.html
│
├── lp/                             # PPC Landing pages
│   ├── driveways/
│   ├── patios/
│   ├── slabs/
│   └── stamped/
│
└── [city-slug]/                    # 95+ location pages
    └── index.html
```

---

## 🎨 Design System

### CSS Variables (css/styles.css)

```css
:root {
  /* Primary Colors - CUSTOMIZE PER SITE */
  --primary-orange: #f97316;        /* CTA buttons, accents */
  --primary-orange-dark: #ea580c;   /* Hover states */
  --primary-dark: #1e3a5f;          /* Brand color (navy) */
  --primary-dark-light: #2d4a6c;    /* Lighter brand */
  
  /* Text Colors - Usually keep consistent */
  --text-dark: #1f2937;
  --text-light: #6b7280;
  --text-muted: #9ca3af;
  
  /* Background Colors */
  --bg-light: #f8fafc;
  --bg-white: #ffffff;
  --bg-dark: #111827;
  
  /* Utility */
  --success-green: #22c55e;
  --shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.05);
  --shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);
  --shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.1);
  --radius: 8px;
  --radius-lg: 12px;
}
```

### Color Scheme Examples

| Site Type | Primary | Accent | Notes |
|-----------|---------|--------|-------|
| Fayetteville | #1e3a5f (navy) | #f97316 (orange) | Professional, trustworthy |
| Alternative 1 | #064e3b (forest) | #fbbf24 (gold) | Earthy, premium |
| Alternative 2 | #1e40af (blue) | #dc2626 (red) | Bold, urgent |
| Alternative 3 | #44403c (stone) | #22c55e (green) | Natural, organic |

---

## 📜 Schema Implementation

### 1. Homepage (index.html)

**Required Schema:**
- LocalBusiness (primary)
- Organization
- WebSite (with SearchAction)
- FAQPage
- AggregateRating

```json
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "@id": "https://[DOMAIN]/#business",
  "name": "[BUSINESS NAME]",
  "image": "https://[DOMAIN]/images/logo.png",
  "telephone": "[PHONE]",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "[ADDRESS]",
    "addressLocality": "[CITY]",
    "addressRegion": "[STATE]",
    "postalCode": "[ZIP]",
    "addressCountry": "US"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": [LAT],
    "longitude": [LNG]
  },
  "url": "https://[DOMAIN]/",
  "priceRange": "$$",
  "openingHours": ["Mo-Fr 07:00-18:00", "Sa 08:00-16:00"],
  "areaServed": [...],
  "aggregateRating": {...},
  "hasOfferCatalog": {...}
}
```

### 2. Service Pages

**Required Schema:**
- LocalBusiness (reference homepage @id)
- FAQPage (service-specific questions)
- Service (via hasOfferCatalog)

### 3. Location Pages

**Required Schema:**
- LocalBusiness (with specific areaServed)
- FAQPage (location-specific questions)

---

## 📝 Page Templates

### Homepage Elements

1. **Header**
   - Logo (left)
   - Navigation (center/right)
   - Phone CTA button (right)
   - Mobile hamburger menu

2. **Hero Section**
   - Badge (e.g., "Serving [Area] Since [Year]")
   - H1 with keyword + location
   - Trust items (licensed, insured, experience)
   - Phone CTA button
   - Lead form card (above fold)

3. **Trust Bar**
   - Licensed badge
   - Insured badge
   - Years experience
   - Google rating

4. **Process Section**
   - 3 steps: Consultation → Quote → Work begins

5. **Services & Areas Grid**
   - Service list with links
   - Top service areas with links

6. **Gallery**
   - 8 project photos

7. **Reviews Section**
   - 5 Google reviews (3-column grid)
   - Star ratings, avatars, dates

8. **Features Bar**
   - Locally owned
   - No upfront payment
   - Licensed/insured
   - Years experience

9. **About Preview**
   - Brief company intro
   - Link to full about page

10. **FAQ Section**
    - 8-10 expandable questions
    - Schema markup

11. **CTA Section**
    - Phone button
    - Form button

12. **Footer**
    - Services links
    - Location links
    - Contact info
    - Legal links

### Service Page Elements

1. Hero with form
2. Service description content
3. Service images (3-column)
4. Why choose us list
5. Service-specific FAQ
6. CTA section
7. Related testimonials

### Location Page Elements

1. Hero with location name
2. Local content (neighborhoods, landmarks)
3. Service list for that area
4. Local FAQ
5. Form embed
6. CTA section

---

## ✅ Replication Checklist

### Phase 1: Setup
- [ ] Clone template structure
- [ ] Update domain in all files (find/replace)
- [ ] Update business name
- [ ] Update phone number (all pages + schema)
- [ ] Update address/NAP
- [ ] Update geo coordinates

### Phase 2: Content
- [ ] Update H1 tags with new city/business
- [ ] Update meta titles and descriptions
- [ ] Update FAQ questions for local relevance
- [ ] Update service areas in schema
- [ ] Generate location pages for target cities

### Phase 3: Design
- [ ] Update CSS color variables
- [ ] Create/replace logo
- [ ] Update hero background image
- [ ] Add local project photos

### Phase 4: Technical
- [ ] Update canonical URLs
- [ ] Regenerate sitemap.xml
- [ ] Update robots.txt sitemap URL
- [ ] Update GHL form embed ID
- [ ] Update Google Maps embed
- [ ] Update privacy/terms links

### Phase 5: Deploy
- [ ] Git init (if new)
- [ ] Git commit
- [ ] Connect to Cloudflare Pages
- [ ] Git push to deploy
- [ ] Add domain in Cloudflare
- [ ] Verify GSC access
- [ ] Submit sitemap to GSC

---

## 🔧 Key Files to Customize

| File | What to Change |
|------|----------------|
| css/styles.css | CSS variables (colors) |
| index.html | Business name, phone, schema, content |
| robots.txt | Domain in sitemap URL |
| sitemap.xml | All URLs with correct domain |
| All HTML | Canonical, OG URLs, phone, business name |

---

## 📊 SEO Best Practices

### Title Tags
- Format: `[Service] in [City], [State] | [Business Name]`
- Homepage: `[City] Concrete Contractors | Driveways & Patios`
- Service: `Concrete Driveway Contractors [City] NC`
- Location: `[Location] Concrete Contractors | [Business Name]`

### Meta Descriptions
- 150-160 characters
- Include phone number
- Include call-to-action
- Include primary keyword

### Schema Must-Haves
1. LocalBusiness with full NAP
2. FAQPage on every page
3. AggregateRating (if reviews exist)
4. Service (for each service page)
5. GeoCoordinates

### Internal Linking
- Service pages link to locations
- Location pages link to services
- All pages link to contact
- Footer has all key pages

---

## 🚀 Quick Deploy Commands

```bash
cd /home/ec2-user/clawd/sites/[site-name]

# After making changes
git add -A
git commit -m "SEO optimizations and fixes"
git push origin main

# Cloudflare auto-deploys from main branch
```

---

## 📞 NAP Format

**Phone:** (XXX) XXX-XXXX
- Use parentheses format in display
- Use tel:XXXXXXXXXX in href (no formatting)

**Address:**
```
[Street Address]
[City], [State] [ZIP]
```

---

## Notes

- All sites use Cloudflare Pages for hosting (auto-deploy from GitHub)
- GHL forms are embedded via iframe
- Exit intent popups are desktop-only
- Sticky mobile CTA is mobile-only
- Schema should be validated at schema.org/validator
