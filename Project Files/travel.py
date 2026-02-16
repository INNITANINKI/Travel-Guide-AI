import streamlit as st
import google.generativeai as genai

# Configure Gemini API Key
genai.configure(api_key="AIzaSyCADqpnvJyfPflO4EKythO5QhP34YG9eRg")

# Initialize the model
model = genai.GenerativeModel(model_name="gemini-2.5-flash")

def generate_itinerary(destination, days, nights, interests):
    prompt = f"""
    Create a personalized travel itinerary for {destination}.
    Trip duration: {days} days and {nights} nights.
    Interests: {interests}

    Include:
    - Day-wise plan
    - Tourist attractions
    - Local food recommendations
    - Travel tips
    """

    chat = model.start_chat(history=[])
    response = chat.send_message(prompt)
    return response.text


# Streamlit UI
st.title("🌍 Travel Itinerary Generator")
st.subheader("Explore with AI: Custom Itineraries for Your Next Journey")

destination = st.text_input("Enter Destination")
days = st.number_input("Number of Days", min_value=1, step=1)
nights = st.number_input("Number of Nights", min_value=1, step=1)
interests = st.text_area("Your Interests (e.g., beaches, food, adventure)")

if st.button("Generate Itinerary ✨"):
    if destination and interests:
        with st.spinner("Generating your personalized itinerary..."):
            itinerary = generate_itinerary(destination, days, nights, interests)
            st.success("Itinerary Generated Successfully!")
            st.write(itinerary)
    else:
        st.warning("Please enter all required details.")
