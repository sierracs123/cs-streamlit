import streamlit as st

st.set_page_config(page_title="Fun Personality Quizzes", page_icon="🧠")

st.sidebar.title("Choose a Quiz")
quiz = st.sidebar.radio("Select a quiz:", [
    "What Pet Should I Get?",
    "Cake Personality Quiz",
    "What Disney Princess Are You?"
    "What HP Character Are You?"
])



def quiz_what_pet_should_i_get():
    st.header("What Pet Should I Get? Quiz")

    activity = st.radio("Pick an ideal weekend activity:", 
                        options=["Going on a hike (a)", "Napping (b)", "Singing karaoke (c)", "Reading (d)"],
                        key="activity")
    trait = st.radio("Your best trait is:", 
                    options=["Loyalty (a)", "Independence (b)", "Cheerfulness (c)", "Calmness (d)"],
                    key="trait")
    time = st.radio("Your favorite time of day is:", 
                    options=["Morning (a)", "Evening (b)", "Noon (c)", "Night (d)"],
                    key="time")
    timespent = st.radio("How much time do you have to spend with your pet a day:",
                         options=["3+ hours (a)", "1 hour (b)", "30 mins (c)", "Not that much time (d)"],
                         key="timespent")
    place = st.radio("Pick a place to live:",
                     options=["Suburban house with a backyard (a)", "Condo near a bookstore and cafe (b)", 
                              "A cottage in the woods (c)", "An apartment in the city (d)"],
                     key="place")

    if st.button("Submit What Pet Quiz"):
        countdog = 0
        countcat = 0
        countbird = 0
        countfish = 0

        def get_choice_letter(option):
            return option[-2].lower()  # extracts letter before ')'

        for answer in [activity, trait, time, timespent, place]:
            choice = get_choice_letter(answer)
            if choice == 'a':
                countdog += 1
            elif choice == 'b':
                countcat += 1
            elif choice == 'c':
                countbird += 1
            elif choice == 'd':
                countfish += 1

        scores = {
            "Dog": countdog,
            "Cat": countcat,
            "Bird": countbird,
            "Fish": countfish,
        }
        max_score = max(scores.values())
        winners = [pet for pet, score in scores.items() if score == max_score]

        if len(winners) == 1:
            st.success(f"Your dream pet is a **{winners[0]}**!")
        else:
            tied_pets = ", ".join(winners)
            st.success(f"It's a tie between: **{tied_pets}**!")

def cake_quiz():
    st.header("Cake Personality Quiz")

    countcc = 0  # Chocolate Cake
    countvc = 0  # Vanilla Cake
    countcac = 0  # Carrot Cake
    countbc = 0  # Birthday Cake

    trait = st.radio("Best trait?", 
                     ['Sweetness', 'Sensibility', 'Elegance', 'Fun loving'], key="cake_trait")
    if trait == 'Sweetness':
        countcc += 1
    elif trait == 'Sensibility':
        countvc += 1
    elif trait == 'Elegance':
        countcac += 1
    elif trait == 'Fun loving':
        countbc += 1

    season = st.radio("Pick a season:", 
                      ['Fall', 'Winter', 'Spring', 'Summer'], key="cake_season")
    if season == 'Fall':
        countcc += 1
    elif season == 'Winter':
        countvc += 1
    elif season == 'Spring':
        countcac += 1
    elif season == 'Summer':
        countbc += 1

    texture = st.radio("Pick a texture of cake:", 
                       ['Moist', 'Smooth', 'Crunchy', 'Soft'], key="cake_texture")
    if texture == 'Moist':
        countcc += 1
    elif texture == 'Smooth':
        countvc += 1
    elif texture == 'Crunchy':
        countcac += 1
    elif texture == 'Soft':
        countbc += 1

    drink = st.radio("What is your favorite drink?", 
                     ['Soda', 'Smoothie', 'Coffee', 'Champagne'], key="cake_drink")
    if drink == 'Soda':
        countcc += 1
    elif drink == 'Smoothie':
        countvc += 1
    elif drink == 'Coffee':
        countcac += 1
    elif drink == 'Champagne':
        countbc += 1

    topping = st.radio("Which dessert topping do you prefer?", 
                       ['Chocolate Sauce', 'Whipped Cream', 'Chopped Nuts', 'Sprinkles'], key="cake_topping")
    if topping == 'Chocolate Sauce':
        countcc += 1
    elif topping == 'Whipped Cream':
        countvc += 1
    elif topping == 'Chopped Nuts':
        countcac += 1
    elif topping == 'Sprinkles':
        countbc += 1

    if st.button("Submit Cake Quiz"):
        st.session_state.cake_submitted = True

    if st.session_state.get("cake_submitted", False):
        max_score = max(countcc, countvc, countcac, countbc)
        cakes = []
        if countcc == max_score:
            cakes.append("Chocolate Cake")
        if countvc == max_score:
            cakes.append("Vanilla Cake")
        if countcac == max_score:
            cakes.append("Carrot Cake")
        if countbc == max_score:
            cakes.append("Birthday Cake")

        if len(cakes) == 1:
            st.success(f"You are most like a **{cakes[0]}**!")
        else:
            st.info(f"It's a tie between: **{', '.join(cakes)}**")

def what_disney_princess_are_you():
    st.header("What Disney Princess Are You?")

    countr = 0
    countb = 0
    countc = 0
    countm = 0

    color = st.radio("Pick a color:", ['Green', 'Brown', 'Red', 'Blue'], key="princess_color")
    if color == 'Green':
        countr += 1
    elif color == 'Brown':
        countb += 1
    elif color == 'Red':
        countc += 1
    elif color == 'Blue':
        countm += 1

    place = st.radio("Pick a place to live:", ['Village', 'Library', 'Cozy Home', 'House Boat'], key="princess_place")
    if place == 'Village':
        countr += 1
    elif place == 'Library':
        countb += 1
    elif place == 'Cozy Home':
        countc += 1
    elif place == 'House Boat':
        countm += 1

    pet = st.radio("Pick a pet:", ['Bird', 'Cat', 'Puppy', 'Hamster'], key="princess_pet")
    if pet == 'Bird':
        countr += 1
    elif pet == 'Cat':
        countb += 1
    elif pet == 'Puppy':
        countc += 1
    elif pet == 'Hamster':
        countm += 1

    jewelry = st.radio("Pick a kind of jewelry:", ['Tiara', 'Pearl Necklace', 'Diamond Earrings', 'Beaded Bracelet'], key="princess_jewelry")
    if jewelry == 'Tiara':
        countr += 1
    elif jewelry == 'Pearl Necklace':
        countb += 1
    elif jewelry == 'Diamond Earrings':
        countc += 1
    elif jewelry == 'Beaded Bracelet':
        countm += 1

    flower = st.radio("Pick a flower:", ['Tulip', 'Pink Rose', 'Daisies', 'Hibiscus'], key="princess_flower")
    if flower == 'Tulip':
        countr += 1
    elif flower == 'Pink Rose':
        countb += 1
    elif flower == 'Daisies':
        countc += 1
    elif flower == 'Hibiscus':
        countm += 1

    season = st.radio("Pick a season:", ['Spring', 'Fall', 'Winter', 'Summer'], key="princess_season")
    if season == 'Spring':
        countr += 1
    elif season == 'Fall':
        countb += 1
    elif season == 'Winter':
        countc += 1
    elif season == 'Summer':
        countm += 1

    song = st.radio("Pick a song:", ['Baby', 'Wildflower', 'Denial is a River', 'Blinding Lights'], key="princess_song")
    if song == 'Baby':
        countr += 1
    elif song == 'Wildflower':
        countb += 1
    elif song == 'Denial is a River':
        countc += 1
    elif song == 'Blinding Lights':
        countm += 1

    companion = st.radio("Pick a Disney princess companion:", ['Anna', 'Aurora', 'Tiana', 'Ariel'], key="princess_companion")
    if companion == 'Anna':
        countr += 1
    elif companion == 'Aurora':
        countb += 1
    elif companion == 'Tiana':
        countc += 1
    elif companion == 'Ariel':
        countm += 1

    if st.button("Submit Princess Quiz"):
        scores = {
            "Rapunzel": countr,
            "Belle": countb,
            "Cinderella": countc,
            "Moana": countm
        }
        max_score = max(scores.values())
        top_princesses = [name for name, score in scores.items() if score == max_score]
        if len(top_princesses) == 1:
            st.success(f"You are most like **{top_princesses[0]}**!")
        else:
            st.info(f"It's a tie between: **{', '.join(top_princesses)}**")

if quiz == "What Pet Are You?":
    what_pet_are_you()
elif quiz == "Cake Personality Quiz":
    cake_quiz()
elif quiz == "What Disney Princess Are You?":
    what_disney_princess_are_you()
