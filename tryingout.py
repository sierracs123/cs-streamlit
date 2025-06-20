import streamlit as st

st.set_page_config(page_title="Multipage Quiz App")

def quiz_harry_potter():
    st.header("Harry Potter Quiz")

    scores = {"Harry": 0, "Ron": 0, "Hermione": 0, "Draco": 0}

    q1 = st.radio("Favorite Hogwarts class?", 
                  ["Defense Against the Dark Arts", "Lunch", "Transfiguration", "Potions"], key="hp_q1")
    if q1 == "Defense Against the Dark Arts":
        scores["Harry"] += 1
    elif q1 == "Lunch":
        scores["Ron"] += 1
    elif q1 == "Transfiguration":
        scores["Hermione"] += 1
    elif q1 == "Potions":
        scores["Draco"] += 1

    q2 = st.radio("Biggest strength?", 
                  ["Bravery", "Loyalty", "Persistence", "Ambition"], key="hp_q2")
    if q2 == "Bravery":
        scores["Harry"] += 1
    elif q2 == "Loyalty":
        scores["Ron"] += 1
    elif q2 == "Persistence":
        scores["Hermione"] += 1
    elif q2 == "Ambition":
        scores["Draco"] += 1

    q3 = st.radio("Favorite activity at Hogwarts?", 
                  ["Playing Quidditch", "Playing Wizard Chess", "Going to the Library", "Pranking Other Students"], key="hp_q3")
    if q3 == "Playing Quidditch":
        scores["Harry"] += 1
    elif q3 == "Playing Wizard Chess":
        scores["Ron"] += 1
    elif q3 == "Going to the Library":
        scores["Hermione"] += 1
    elif q3 == "Pranking Other Students":
        scores["Draco"] += 1

    q4 = st.radio("Favorite wizard candy?", 
                  ["Chocolate Frogs", "Bertie Bott's Every Flavor Beans", "Sugar Quills", "Fizzing Whizzbees"], key="hp_q4")
    if q4 == "Chocolate Frogs":
        scores["Harry"] += 1
    elif q4 == "Bertie Bott's Every Flavor Beans":
        scores["Ron"] += 1
    elif q4 == "Sugar Quills":
        scores["Hermione"] += 1
    elif q4 == "Fizzing Whizzbees":
        scores["Draco"] += 1

    q5 = st.radio("How do you handle problems and stress?", 
                  ["Face it", "Vent to friends", "Make a detailed plan", "Pay someone to fix it"], key="hp_q5")
    if q5 == "Face it":
        scores["Harry"] += 1
    elif q5 == "Vent to friends":
        scores["Ron"] += 1
    elif q5 == "Make a detailed plan":
        scores["Hermione"] += 1
    elif q5 == "Pay someone to fix it":
        scores["Draco"] += 1

    if st.button("Submit Harry Potter Quiz"):
        st.session_state.hp_submitted = True

    if st.session_state.get("hp_submitted", False):
        max_score = max(scores.values())
        winners = [k for k, v in scores.items() if v == max_score]
        if len(winners) == 1:
            st.success(f"You are most like **{winners[0]}**!")
        else:
            st.info(f"It's a tie between: **{', '.join(winners)}**")

def quiz_cake():
    st.header("What Kind of Cake Are You?")

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

def quiz_what_pet():
    st.title("What Pet Should I Get? Quiz")

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

def quiz_disney_princess():
    st.header("Which Disney Princess Are You?")

    # Initialize counts
    countr = 0  # Rapunzel
    countb = 0  # Belle
    countc = 0  # Cinderella
    countm = 0  # Moana

    color = st.radio("Pick a color:", ["green ", "brown ", "red ", "blue "], key="dp_color")
    if color.startswith("green"):
        countr += 1
    elif color.startswith("brown"):
        countb += 1
    elif color.startswith("red"):
        countc += 1
    elif color.startswith("blue"):
        countm += 1

    place = st.radio("Pick a place to live:", ["village ", "library", "cozy home ", "house boat "], key="dp_place")
    if place.startswith("village"):
        countr += 1
    elif place.startswith("library"):
        countb += 1
    elif place.startswith("cozy"):
        countc += 1
    elif place.startswith("house boat"):
        countm += 1

    pet = st.radio("Pick a pet:", ["bird ", "cat ", "puppy ", "hamster "], key="dp_pet")
    if pet.startswith("bird"):
        countr += 1
    elif pet.startswith("cat"):
        countb += 1
    elif pet.startswith("puppy"):
        countc += 1
    elif pet.startswith("hamster"):
        countm += 1

    jewelry = st.radio("Pick a kind of jewelry:", ["tiara ", "pearl necklace ", "diamond earrings ", "beaded bracelet "], key="dp_jewelry")
    if jewelry.startswith("tiara"):
        countr += 1
    elif jewelry.startswith("pearl"):
        countb += 1
    elif jewelry.startswith("diamond"):
        countc += 1
    elif jewelry.startswith("beaded"):
        countm += 1

    flower = st.radio("Pick a flower:", ["tulip (a)", "pink rose ", "daisies ", "hibiscus "], key="dp_flower")
    if flower.startswith("tulip"):
        countr += 1
    elif flower.startswith("pink rose"):
        countb += 1
    elif flower.startswith("daisies"):
        countc += 1
    elif flower.startswith("hibiscus"):
        countm += 1

    season = st.radio("Pick a season:", ["spring ", "fall ", "winter ", "summer "], key="dp_season")
    if season.startswith("spring"):
        countr += 1
    elif season.startswith("fall"):
        countb += 1
    elif season.startswith("winter"):
        countc += 1
    elif season.startswith("summer"):
        countm += 1

    song = st.radio("Pick a song:", ["baby ", "wildflower ", "denial is a river ", "blinding lights "], key="dp_song")
    if song.startswith("baby"):
        countr += 1
    elif song.startswith("wildflower"):
        countb += 1
    elif song.startswith("denial"):
        countc += 1
    elif song.startswith("blinding"):
        countm += 1

    companion = st.radio("Pick a Disney princess companion:", ["Anna ", "Aurora ", "Tiana ", "Ariel "], key="dp_companion")
    if companion.startswith("anna"):
        countr += 1
    elif companion.startswith("aurora"):
        countb += 1
    elif companion.startswith("tiana"):
        countc += 1
    elif companion.startswith("ariel"):
        countm += 1

    if st.button("Submit Disney Princess Quiz"):
        st.session_state.dp_submitted = True

    if st.session_state.get("dp_submitted", False):
        # Determine winner with your tie logic
        max_count = max(countr, countb, countc, countm)

        # Collect princesses with max score
        winners = []
        if countr == max_count:
            winners.append("Rapunzel")
        if countb == max_count:
            winners.append("Belle")
        if countc == max_count:
            winners.append("Cinderella")
        if countm == max_count:
            winners.append("Moana")

        # Tie message logic (same as your original)
        if len(winners) == 1:
            st.success(f"Your Disney princess is **{winners[0]}**!")
        elif len(winners) == 2:
            st.info(f"It's a tie between **{winners[0]}** and **{winners[1]}**!")
        elif len(winners) == 3:
            st.info(f"It's a tie between **{', '.join(winners)}**!")
        else:
            st.info("It's a tie between all princesses!")

def main():
    st.sidebar.title("Quiz Navigation")
    quiz_choice = st.sidebar.radio("Choose a quiz to take:", 
                                   ("Harry Potter Quiz", "Cake Quiz", "What Pet Should I Get?", "Disney Princess Quiz"))

    if quiz_choice == "Harry Potter Quiz":
        quiz_harry_potter()
    elif quiz_choice == "Cake Quiz":
        quiz_cake()
    elif quiz_choice == "What Pet Should I Get?":
        quiz_what_pet()
    elif quiz_choice == "Disney Princess Quiz":
        quiz_disney_princess()

if __name__ == "__main__":
    main()
