import streamlit as st

def what_pet_should_i_get():
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

    if st.button("Submit"):
        countdog = 0
        countcat = 0
        countbird = 0
        countfish = 0

        def get_choice_letter(option):
            return option[-2].lower()

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

what_pet_should_i_get()
