"""
COMP 163 - Project 3: Quest Chronicles
Game Data Module - Starter Code

Name: Aaron Williams

AI Usage: [Document any AI assistance used]

This module handles loading and validating game data from text files.
"""

import os
from custom_exceptions import (
    InvalidDataFormatError,
    MissingDataFileError,
    CorruptedDataError
)

# ============================================================================
# DATA LOADING FUNCTIONS
# ============================================================================
#AI helped me with writing out the exception statements for this part of the program
def load_quests(filename="data/quests.txt"):
    """
    Load quest data from file
    
    Expected format per quest (separated by blank lines):
    QUEST_ID: unique_quest_name
    TITLE: Quest Display Title
    DESCRIPTION: Quest description text
    REWARD_XP: 100
    REWARD_GOLD: 50
    REQUIRED_LEVEL: 1
    PREREQUISITE: previous_quest_id (or NONE)
    
    Returns: Dictionary of quests {quest_id: quest_data_dict}
    Raises: MissingDataFileError, InvalidDataFormatError, CorruptedDataError
    """
    try:
        with open(filename, "r") as file:
            specs = file.readlines()
            print(f"{specs}\n")
    except FileNotFoundError: 
        raise MissingDataFileError ("Data is missing")
    except InvalidDataFormatError:
        raise InvalidDataFormatError ("Invalid data format")
    except Exception:
        raise CorruptedDataError ("Corrupted Data")
    # TODO: Implement this function
    # Must handle:
    # - FileNotFoundError → raise MissingDataFileError
    # - Invalid format → raise InvalidDataFormatError
    # - Corrupted/unreadable data → raise CorruptedDataError
    pass

def load_items(filename="data/items.txt"):
    """
    Load item data from file
    
    Expected format per item (separated by blank lines):
    ITEM_ID: unique_item_name
    NAME: Item Display Name
    TYPE: weapon|armor|consumable
    EFFECT: stat_name:value (e.g., strength:5 or health:20)
    COST: 100
    DESCRIPTION: Item description
    
    Returns: Dictionary of items {item_id: item_data_dict}
    Raises: MissingDataFileError, InvalidDataFormatError, CorruptedDataError
    """
    try:
        with open(filename, "r") as file:
            specs = file.readlines()
            print(f"{specs}\n")
    except FileNotFoundError: 
        raise MissingDataFileError ("Data is missing")
    except InvalidDataFormatError:
        raise InvalidDataFormatError ("Invalid data format")
    except Exception:
        raise CorruptedDataError ("Corrupted Data")
    # TODO: Implement this function
    # Must handle same exceptions as load_quests
    # Ai helped me with the for loop for the keys list
def validate_quest_data(quest_dict):
    """
    Validate that quest dictionary has all required fields
    
    Required fields: quest_id, title, description, reward_xp, 
                    reward_gold, required_level, prerequisite
    
    Returns: True if valid
    Raises: InvalidDataFormatError if missing required fields
    """
    keys = ["quest_id", "title", "description", "reward_xp", "reward_gold", "required_level", "prerequisite"]
    for key in keys:
        if key not in quest_dict:
            raise InvalidDataFormatError ("Missing required fields")
    return True
    # TODO: Implement validation
    # Check that all required keys exist
    # Check that numeric values are actually numbers
    pass

def validate_item_data(item_dict):
    """
    Validate that item dictionary has all required fields
    
    Required fields: item_id, name, type, effect, cost, description
    Valid types: weapon, armor, consumable
    
    Returns: True if valid
    Raises: InvalidDataFormatError if missing required fields or invalid type
    """
    keys: ["item_id", "name", "type", "effect", "cost", "description"]
    types: ["weapon", "armor", "consumable"]
    for key in keys:
         if key not in item_dict:
            raise InvalidDataFormatError ("Missing required fields")
    for type in types:
         if type not in item_dict:
            raise InvalidDataFormatError ("Missing required fields")
    return True
    # TODO: Implement validation

def create_default_data_files():
    """
    Create default data files if they don't exist
    This helps with initial setup and testing
    """
    # TODO: Implement this function
    # Create data/ directory if it doesn't exist
    # Create default quests.txt and items.txt files
    # Handle any file permission errors appropriately
    pass

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================
# AI helped me understand what parse meant here. AI helped me with the logic here
def parse_quest_block(lines):
    """
    Parse a block of lines into a quest dictionary
    
    Args:
        lines: List of strings representing one quest
    
    Returns: Dictionary with quest data
    Raises: InvalidDataFormatError if parsing fails
    """
    if len(lines) < 7:
        raise InvalidDataFormatError ("Parsing failed")
    try:
        if lines[1].strip().isdigit() == False:
            raise InvalidDataFormatError ("Level must be a number")
        if lines[5].strip().isdigit() == False:
            raise InvalidDataFormatError ("Parsing failed")
        if lines[6].strip().isdigit() == False:
            raise InvalidDataFormatError ("Parsing failed")
        return {"QUEST_ID": lines[0].strip(), 
            "REQUIRED_LEVEL": int(lines[1].strip()), 
            "PREREQUISITE": lines[2].strip(), 
            "DESCRIPTION": lines[3].strip(),
            "TITLE": lines[4].strip(), 
            "REWARD_GOLD": int(lines[5].strip()), 
            "REWARD_XP": int(lines[6].strip())}
    except (IndexError, AttributeError, ValueError):
        raise InvalidDataFormatError ("Parsing failed")
    
    # TODO: Implement parsing logic
    # Split each line on ": " to get key-value pairs
    # Convert numeric strings to integers
    # Handle parsing errors gracefully

def parse_item_block(lines):
    """
    Parse a block of lines into an item dictionary
    
    Args:
        lines: List of strings representing one item
    
    Returns: Dictionary with item data
    Raises: InvalidDataFormatError if parsing fails
    """
    if len(lines) < 5:
        raise InvalidDataFormatError ("Parsing failed")
    try:
        if lines[4].strip().isdigit() == False:
            raise InvalidDataFormatError ("Parsing failed")
        return {"ITEM_ID": lines[0].strip(), 
            "NAME": int(lines[1].strip()), 
            "TYPE": lines[2].strip(), 
            "EFFECT": lines[3].strip(),
            "COST": lines[4].strip(),
            "DESCRIPTION": lines[5].strip()}
    except (IndexError, AttributeError, ValueError):
        raise InvalidDataFormatError ("Parsing failed")
    # TODO: Implement parsing logic

# ============================================================================
# TESTING
# ============================================================================

if __name__ == "__main__":
    print("=== GAME DATA MODULE TEST ===")
    
    # Test creating default files
    # create_default_data_files()
    
    # Test loading quests
    # try:
    #     quests = load_quests()
    #     print(f"Loaded {len(quests)} quests")
    # except MissingDataFileError:
    #     print("Quest file not found")
    # except InvalidDataFormatError as e:
    #     print(f"Invalid quest format: {e}")
    
    # Test loading items
    # try:
    #     items = load_items()
    #     print(f"Loaded {len(items)} items")
    # except MissingDataFileError:
    #     print("Item file not found")
    # except InvalidDataFormatError as e:
    #     print(f"Invalid item format: {e}")

