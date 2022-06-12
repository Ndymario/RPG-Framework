# Documentation on Stories
(Stories are still being thought out. Until this notice goes away, be warned anything and everything could change at any time!)

## Story Basics

Stories are JSON files that serve as a way to use the framework without coding each line manually in python.

More than one story can be contained in a single JSON file, allowing for the creation of connected stories or simply not requiring a large quantity of files.

### File Structure

Story files are comprised of the following structure:

- Story Container: This should be the same as the story_id; houses the contents of the Story
  - Battles Container: Houses the battles this chapter has
    - Enemy JSON Path: Path to a folder that contains enemy JSON files to be used in this battle
    - Battle Container: This should be the same as battle_id; houses the contents of the battle
      - Battle ID: A unique identifier for the framework to reference your battle
      - Enemies: A list of enemies that the user will be fighting in this battle. Enemies don't have id's, so the file name is used instead
      - Fixed EXP Flag: A boolean that, when set true, will make the framework ignore the EXP each enemy gives and allows you to set the awarded EXP manually
      - Fixed EXP: The amount of EXP to award if the fixed exp fight flag is set to true
  - Chapters Container: Houses the chapters this story has
    - Chapter Container: This should be the same as the chapter_id; houses the contents of the Chapter
      - Chapter ID: A unique identifier for the framework to reference your chapter
      - Chapter Title: The title of the chapter shown to the user. If this fails to load, the Chapter ID will be shown instead
      - Chapter Description: The description of the chapter shown to the user. If this fails to load, nothing will be shown
      - Battle Order: A list of battles that this chapter has. The battles will occur in the order of this list
  - Story ID: A unique identifier for the framework to reference your story
  - Story Title: The title of the story shown to the user. If this fails to load, the Story ID will be used instead
  - Story Description: A description of the story shown to the user. If this fails to load, nothing will be shown
