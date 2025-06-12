import streamlit as st

def what_harry_potter_character_are_you():
    st.title("What Harry Potter Character Are You?")

    count = {"Harry Potter": 0, "Ron Weasley": 0, "Hermione Granger": 0, "Draco Malfoy": 0}

    q1 = st.radio("Pick your favorite class at Hogwarts:", 
                  ["Defense Against the Dark Arts", "Lunch", "Transfiguration", "Potions"])
    if q1 == "Defense Against the Dark Arts":
        count["Harry Potter"] += 1
    elif q1 == "Lunch":
        count["Ron Weasley"] += 1
    elif q1 == "Transfiguration":
        count["Hermione Granger"] += 1
    elif q1 == "Potions":
        count["Draco Malfoy"] += 1

    q2 = st.radio("What is your biggest strength:", 
                  ["Bravery", "Loyalty", "Persistence", "Ambition"])
    if q2 == "Bravery":
        count["Harry Potter"] += 1
    elif q2 == "Loyalty":
        count["Ron Weasley"] += 1
    elif q2 == "Persistence":
        count["Hermione Granger"] += 1
    elif q2 == "Ambition":
        count["Draco Malfoy"] += 1

    q3 = st.radio("Your favorite activity at Hogwarts:", 
                  ["Playing Quidditch", "Playing Wizard Chess", "Going to the Library", "Pranking Other Students"])
    if q3 == "Playing Quidditch":
        count["Harry Potter"] += 1
    elif q3 == "Playing Wizard Chess":
        count["Ron Weasley"] += 1
    elif q3 == "Going to the Library":
        count["Hermione Granger"] += 1
    elif q3 == "Pranking Other Students":
        count["Draco Malfoy"] += 1

    q4 = st.radio("Favorite wizard candy:", 
                  ["Chocolate Frogs", "Every Flavor Beans", "Sugar Quills", "Fizzing Whizzbees"])
    if q4 == "Chocolate Frogs":
        count["Harry Potter"] += 1
    elif q4 == "Every Flavor Beans":
        count["Ron Weasley"] += 1
    elif q4 == "Sugar Quills":
        count["Hermione Granger"] += 1
    elif q4 == "Fizzing Whizzbees":
        count["Draco Malfoy"] += 1

    q5 = st.radio("How do you handle stress:", 
                  ["Face it", "Vent to friends", "Make a plan", "Pay someone to fix it"])
    if q5 == "Face it":
        count["Harry Potter"] += 1
    elif q5 == "Vent to friends":
        count["Ron Weasley"] += 1
    elif q5 == "Make a plan":
        count["Hermione Granger"] += 1
    elif q5 == "Pay someone to fix it":
        count["Draco Malfoy"] += 1

    if st.button("Submit"):
        max_score = max(count.values())
        top_characters = [name for name, score in count.items() if score == max_score]

        if len(top_characters) == 1:
            st.success(f"You are most like **{top_characters[0]}**!")
        else:
            st.info(f"It's a tie between: {', '.join(top_characters)}")

