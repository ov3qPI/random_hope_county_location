import random
import argparse

# List of Far Cry 5 Locations
regions = {
    'Henbane': [
        "8-Bit Pizza Bar", "Abercrombie Residence", "Administrator's Cabin", "Ancient Bison Tunnel", "Angel's Peak",
        "Aubrey's Diner", "Barlow Residence", "Boshaw Manor", "Bright Warden Radon Spa", "Camp Cougars",
        "Can of Worms Fishing Store", "Chan Residence", "Counselor's Cabin", "Dead Man's Mill",
        "Deep North Water Treatment Plant", "Deer Tiger Mine", "Dire Wolf Basin", "Drubman Marina", "Eden's Altar",
        "Eden's Convent", "Eden's Gate Outreach Center", "Faith's Gate", "Feeney Residence", "Gethsemane Greenhouse",
        "Ghost Cat Mine", "Grimalkin Radon Mine", "Harrison Lookout Tower", "Henbane River Chalets", "Henbane River Station",
        "Hollyhock Saloon", "Hope County Jail", "Horned Serpent Cave", "Howling Cave", "Jessop Conservatory",
        "Johnson Residence", "Jones Residence", "Joseph's Word", "King's Hot Springs Hotel", "Lorna's Truck Stop",
        "Lydia's Cave", "Mastodon Geothermal Park", "McCallough's Garage", "McCoy Cabin", "Misty River Gas",
        "Moonflower Trailer Park", "Nature Cabin", "Nelson Residence", "Nolan's Fly Shop", "O'Hara's Haunted House",
        "Peaches' Taxidermy", "Pepper Residence", "Prosperity", "Puma Mine", "Purpletop Antenna", "Raptor Peak",
        "Sabre-Tooth Springs", "Sacred Skies Youth Camp", "Seeley's Cabin", "Silver Lake Campgrounds", "Silver Lake Summer Camp",
        "Sinclair Residence", "Taft Lookout Tower", "Tanami Residence", "The Last Best Resting Place", "The Misery",
        "The Pillars of Eden", "Throne of Mercy Church", "Vasquez Residence", "Whistling Beaver Brewery"
    ],
    'Holland': [
        "Adams Ranch", "Armstrong Residence", "Boyd Residence", "Bradbury Farm", "Bradbury Hay Field", "Bradbury Tractor Shed",
        "Bridge of Tears", "Catamount Mines", "Copperhead Rail Yard", "Davenport Farm", "Deep North Irrigation Reservoir",
        "Dodd Residence", "Dodd's Dumps", "Doverspike Compound", "Dupree Residence", "Eden's Gate Greenhouse", "Fall's End",
        "Fillmore Residence", "Flatiron Stockyards", "Frobisher's Cave", "Gardenview Ciderworks", "Gardenview Orchards",
        "Gardenview Packing Facility", "Golden Valley Gas", "Grain Elevator", "Green-Busch Fertilizer Co.", "Harris Residence",
        "Henbane River Rail Bridge", "Hilgard Electric Power Station", "Holland Valley Station", "Hope County Clinic",
        "Hope County Jail Bus", "Howard Cabin", "Hyde Barn", "John's Gate", "Kay-Nine Kennels", "Kellett Cattle Co.",
        "Kupka Ranch", "Lamb of God Church", "Lamb of God Sacristy", "Laurel Residence", "Lincoln Lookout Tower",
        "Miller Residence", "Old Silo", "Parker Laboratories", "Purpletop Telecom Tower", "Rae-Rae's Pumpkin Farm",
        "Red's Farm Supply", "Redler Residence", "Reservoir Construction Yard", "Roberts Cabin", "Rye & Sons Aviation",
        "Sawyer Residence", "Security Gate", "Seed Boat Launch", "Seed Ranch", "Sergey's Place", "Silver Lake Trailer Park",
        "Spread Eagle Bar", "St. Isidore School", "Steele Farm", "Strickland Farm", "Sunrise Farm", "Sunrise Threshing",
        "Wellington Residence", "Woodson Pig Farm"
    ],
    'Whitetail': [
        "Baron Lumber Mill", "Bo's Cave", "Breakthrough Camp", "Clagett Boathouse", "Cooper Cabin", "Dansky Cabin",
        "Dylan's Master Bait Shop", "Elk Jaw Lodge", "Elliot Residence", "F.A.N.G. Center", "Fort Drubman", "Fowler's Retreat",
        "Frank's Cabin", "Grand View Hotel", "Haskell Lookout Tower", "Hawkeye Tunnel", "Helipad 3", "Hunter's Pass Shelter",
        "Jacob's Armory", "Jefferson Lookout Tower", "Kestrel Cabin", "Langford Falls Parking Lot", "Lansdowne Airstrip",
        "Linero Building Supplies", "Loresca Residence", "MCA Mobile Lab", "Mansfield Lookout Tower", "McClean Residence",
        "McKinley Dam", "McNeill Residence", "North Park Entrance", "Oberlin Picnic Area", "Old Sun Outfitters",
        "Osprey Cabin", "Ozhigwan Falls", "PIN-K0 Radar Station", "Plane crash site (Unmarked)", "Rattlesnake Trail Bridge",
        "Red Tail Cabin", "Salvage Camp", "Silver Lake", "Silver Lake Parking Lot", "Snowshoe Lake", "South Park Entrance",
        "Stone Ridge Chalet", "Stone Ridge Training Post", "The Grill Streak", "Valley View Overlook",
        "Whitetail Mountains Rail Bridge", "Whitetail Park Ranger Station", "Whitetail Park Visitor Center",
        "Whitetail Ranger Station (Unmarked)", "Widow's Creek", "Wishbone Lake", "Wolf's Den"
    ]
}

def generate_location(region=None):
    if region:
        region = region.capitalize()
        if region in regions:
            return random.choice(regions[region])
        else:
            return f"Invalid region specified: {region}. Choose from Henbane, Holland, Whitetail."
    else:
        all_locations = [loc for locs in regions.values() for loc in locs]
        return random.choice(all_locations) if all_locations else "No locations available."

def main():
    parser = argparse.ArgumentParser(description='Generate a Far Cry 5 location.')
    parser.add_argument('-r', '--region', type=str, help='Specify region: Henbane, Holland, Whitetail')
    args = parser.parse_args()

    location = generate_location(args.region)
    print(location)

if __name__ == "__main__":
    main()
