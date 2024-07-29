# Function to get user inputs for the Mad Libs variables
def get_inputs():
    inputs = {}
    inputs['object'] = input("An object that would make a terrible wand: ")
    
    inputs['emotion'] = input("Enter an emotion: ")
    inputs['verbed'] = input("Enter a past tense verb: ")
    inputs['adverb1'] = input("Enter an adverb: ")
    inputs['adjective2'] = input("Enter another adjective: ")
    inputs['place'] = input("Enter a confusing place: ")
    inputs['verb1'] = input("Enter a verb ending in -ing: ")
    inputs['verb2'] = input("Enter another verb ending in -ing: ")
    inputs['item'] = input("Enter a household item: ")
    inputs['food'] = input("Enter a type of food: ")
    inputs['adjective3'] = input("Enter another adjective: ")
    inputs['noun'] = input("Enter a noun: ")
    inputs['laugh'] = input ("Sound a computer makes when it laughs: ")
    inputs['captcha'] = input("Worst Captcha challenge of all time: ")
    inputs['sad_verb'] = input("past tense verb instead of 'said': ")
    return inputs

# Function to print the Mad Libs story with the user's inputs
def print_story(inputs):
    story = f"""
    When we last left our hero, Little Sammy, or Little Rock, Arksamsas for short, who was trying to get their job back. Bob had just shown up and granted Little Sammy's wish, but what was their wish???

    Bob once again waved their {inputs['object']}, and suddenly, they were both transported to {inputs['place']}. There, the AI was waiting, looking very {inputs['adjective3']}. Little Sammy was feeling {inputs['emotion']}. 
    
    Bob handed Little Sammy a {inputs['item']} and said, "To defeat the AI and get your job back, you must solve this {inputs['adjective2']} CAPTCHA!"
     
    Little Sammy took a deep breath, ate a {inputs['food']} for good luck, and faced the AI. With a swift move, Little Sammy clicked "I am not a robot". However, the AI had clicked it just as fast! 'IMPOSSIBLE,' Little Sammy said. 'They can't do that.' The AI laughed, '{inputs['laugh']}' and stared at Little Sammy.

    'How can I defeat AI that knows how to solve a captcha!?' Little Sammy {inputs['verbed']}.
    'Also, what was that laugh?' Little Sammy asked no one in particular. 'Let's see them do this,' Little Sammy said {inputs['adverb1']}. 
    Sammy began to quickly move his hands around in the air, tracing arcane symbols in the air with their fingers, each gesture precise and purposeful. Their hands weaved through complex patterns, creating shimmering trails of light. Simultaneously, they muttered incantations in an ancient, forgotten language, their voice rising and falling in a hypnotic rhythm. Little Sammy's, or Jim's for short, eyes glow with a mystical energy as they channel the raw forces of ancient and powerful magic. With a final, sweeping motion, they draw the energy into a focal point, and suddenly in it's place appeared the instructions: {inputs['captcha']}. 

    'OH HOLY MOLY. I AM DEFEATED.' shouted the AI suddenly {inputs['verb2']}. Little Sammy was {inputs['verb1']} for joy at their sudden win.

    'Wow' said Bob, still there for some reason. 'Pretty cool.'

    Little Sammy, or Big Pat for short, chuckled to himself and picked up his {inputs['noun']}. 'Just a normal day at work.' they {inputs['sad_verb']}. 

    The End! 
    """

    print(story)

# Main function to run the Mad Libs game
def main():
    print("Welcome to the Mad Libs game!")
    inputs = get_inputs()
    print_story(inputs)

if __name__ == "__main__":
    main()
