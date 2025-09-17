#import the random module
import random

#create subject
subjects = ["Shahruk khan","Virat Kohli","Nirmala Sitharaman","A mumbai cat","A Group of Monkeys","Prime Minister Modi","Auto Rickshaw Driver from Delhi"]
actions=["launches","cancels","dance with","eats","declare war on","orders","celebrates" ]
places_or_things=["at Red Fort","in Mumbai Local Train","a plate of samosa","inside parliament","at Ganga Ghat","during IPL Match","at India Gate"]

#start the headline generation loop
while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)

    headline = f"BREAKING NEWS: {subject} {action} {place_or_thing}"
    print("\n" + headline)

    user_input = input("\nDo you want another headline? (yes/no): ").strip().lower()
    if user_input == "no":
        break

#print goodbye message
print("\nThanks for using the Fake News Headline Generator.Have a fun day")

