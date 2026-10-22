import itertools

counties = ["Thurston County", "Mason County", "Kitsap County"]
towns = ["Olympia", "Lacey", "Tumwater", "Shelton", "Hoodsport", "Bremerton", "Port Orchard", "Gig Harbor"]
services = [
    "Painting", "Drywall Repair", "Flooring Installation", 
    "Deck Staining", "Door Replacement", "Fencing", 
    "Sanding", "Property Maintenance"
]

def generate_local_targets():
    print("=== LOCAL SEARCH DOMINATION MATRIX ===")
    combos = list(itertools.product(services, towns))
    print(f"Total Local Search Keywords Generated: {len(combos)}")
    print("\nSample High-Intent Search Targets:")
    for service, town in combos[:10]:
        print(f" - '{service} in {town}'")
    print("\n[INFO] Use these keywords for your Google Business Profile posts and local citations.")

if __name__ == '__main__':
    generate_local_targets()
