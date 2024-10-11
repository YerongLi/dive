import json

def solution(jsonData):
    # Parse the JSON string into a Python list of dictionaries
    listings = json.loads(jsonData)
    
    # Words to ignore if found right before "studio" or "1-bedroom"
    ignore_prefixes = ["yoga", "art", "dance"]

    def contains_valid_studio(description_words):
        """Check if the description contains a valid 'studio' (not preceded by ignore words)."""
        for i, word in enumerate(description_words):
            if word == "studio":
                # Ensure the word before 'studio' is not one of the ignore prefixes
                if i > 0 and description_words[i - 1] in ignore_prefixes:
                    continue
                return True
        return False

    def contains_valid_1_bedroom(description_words):
        """Check if the description contains '1-bedroom'."""
        for word in description_words:
            if word == "1-bedroom":
                return True
        return False

    corrected_bedrooms = []
    
    # Process each listing
    for listing in listings:
        description = listing["description"].lower()  # Convert to lowercase to handle casing issues
        description_words = description.replace(",", "").replace(".", "").split()  # Split into words
        
        # Check for valid "1-bedroom" and "studio" and correct the num_bedrooms field
        if contains_valid_1_bedroom(description_words):
            corrected_bedrooms.append(1)
        elif contains_valid_studio(description_words):
            corrected_bedrooms.append(0)
        else:
            # If no relevant info found, keep the original value
            corrected_bedrooms.append(listing["num_bedrooms"])
    
    return corrected_bedrooms

# Test case
jsonData = """
[
    {"id": "1", "agent": "Radulf Katlego", "unit": "#3", "description" : "This luxurious studio apartment is in the heart of downtown.", "num_bedrooms": 1},
    {"id": "2", "agent": "Kelemen Konrad", "unit": "#36", "description": "We have a 1-bedroom available on the third floor.", "num_bedrooms": 1},
    {"id": "3", "agent": "Ton Jett", "unit": "#12", "description": "Beautiful 1-bedroom apartment with nearby yoga studio.", "num_bedrooms": 1},
    {"id": "4", "agent": "Fishel Salman", "unit": "#13", "description": "Beautiful studio with a nearby art studio.", "num_bedrooms": 1}
]
"""
print(solution(jsonData))  # Output should be [0, 1, 1, 0]
