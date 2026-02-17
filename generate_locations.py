#!/usr/bin/env python3
"""Generate location pages for Naples Pool Construction"""

import os
import re

# Location data: (city, county, slug)
LOCATIONS = [
    # Collier County
    ("Marco Island", "Collier", "marco-island"),
    ("Golden Gate", "Collier", "golden-gate"),
    ("Immokalee", "Collier", "immokalee"),
    ("Naples Park", "Collier", "naples-park"),
    ("North Naples", "Collier", "north-naples"),
    ("Pelican Bay", "Collier", "pelican-bay"),
    ("Lely", "Collier", "lely"),
    ("Lely Resort", "Collier", "lely-resort"),
    ("Naples Manor", "Collier", "naples-manor"),
    ("Orangetree", "Collier", "orangetree"),
    ("Vineyards", "Collier", "vineyards"),
    ("Ave Maria", "Collier", "ave-maria"),
    ("Everglades City", "Collier", "everglades-city"),
    ("Goodland", "Collier", "goodland"),
    ("East Naples", "Collier", "east-naples"),
    ("Island Walk", "Collier", "island-walk"),
    ("Pine Ridge", "Collier", "pine-ridge"),
    ("Vanderbilt Beach", "Collier", "vanderbilt-beach"),
    
    # Lee County
    ("Fort Myers", "Lee", "fort-myers"),
    ("Cape Coral", "Lee", "cape-coral"),
    ("Bonita Springs", "Lee", "bonita-springs"),
    ("Estero", "Lee", "estero"),
    ("Lehigh Acres", "Lee", "lehigh-acres"),
    ("Fort Myers Beach", "Lee", "fort-myers-beach"),
    ("North Fort Myers", "Lee", "north-fort-myers"),
    ("Sanibel", "Lee", "sanibel"),
    ("Captiva", "Lee", "captiva"),
    ("San Carlos Park", "Lee", "san-carlos-park"),
    ("Gateway", "Lee", "gateway"),
    ("Pine Island", "Lee", "pine-island"),
    ("Matlacha", "Lee", "matlacha"),
    ("Tice", "Lee", "tice"),
    ("Buckingham", "Lee", "buckingham"),
    ("Alva", "Lee", "alva"),
    ("Three Oaks", "Lee", "three-oaks"),
    ("Whiskey Creek", "Lee", "whiskey-creek"),
    ("Cypress Lake", "Lee", "cypress-lake"),
    ("Villas", "Lee", "villas"),
    ("McGregor", "Lee", "mcgregor"),
    ("Iona", "Lee", "iona"),
    ("Miromar Lakes", "Lee", "miromar-lakes"),
    ("Boca Grande", "Lee", "boca-grande"),
    
    # Charlotte County
    ("Punta Gorda", "Charlotte", "punta-gorda"),
    ("Port Charlotte", "Charlotte", "port-charlotte"),
    ("Englewood", "Charlotte", "englewood"),
    ("Rotonda West", "Charlotte", "rotonda-west"),
]

def get_nearby_links(current_slug, current_county):
    """Generate links to nearby locations"""
    links = []
    
    # First add same county locations
    same_county = [(city, county, slug) for city, county, slug in LOCATIONS 
                   if county == current_county and slug != current_slug]
    # Then add other counties
    other_counties = [(city, county, slug) for city, county, slug in LOCATIONS 
                      if county != current_county]
    
    all_nearby = same_county[:6] + other_counties[:8]  # Limit to 14 links
    
    for city, county, slug in all_nearby:
        links.append(f'<a href="/locations/{slug}/">{city}</a>')
    
    # Always add link to Naples home
    links.append('<a href="/">Naples</a>')
    
    return '\n                '.join(links)

def main():
    # Read template
    with open('locations/_template.html', 'r') as f:
        template = f.read()
    
    # Generate each location page
    for city, county, slug in LOCATIONS:
        # Create directory
        os.makedirs(f'locations/{slug}', exist_ok=True)
        
        # Replace placeholders
        content = template.replace('{{CITY}}', city)
        content = content.replace('{{COUNTY}}', county)
        content = content.replace('{{SLUG}}', slug)
        content = content.replace('{{NEARBY_LINKS}}', get_nearby_links(slug, county))
        
        # Write file
        with open(f'locations/{slug}/index.html', 'w') as f:
            f.write(content)
        
        print(f"Created: locations/{slug}/index.html")
    
    print(f"\nTotal location pages created: {len(LOCATIONS)}")

if __name__ == '__main__':
    main()
