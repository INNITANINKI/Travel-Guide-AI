# Travel-Guide-AI
# 🌍 AI Travel Itinerary Generator

An AI-powered Travel Guide Web Application built using **Streamlit** and **Google Gemini API**.  
This application generates personalized travel itineraries based on destination, trip duration, and user interests.

---

## 📌 Project Overview

Planning trips can be time-consuming and overwhelming. This AI-based Travel Itinerary Generator simplifies travel planning by automatically creating a customized day-wise itinerary including tourist attractions, food recommendations, and useful travel tips.

The application leverages Google’s Gemini AI model to generate intelligent and structured travel plans instantly.

---

## 🚀 Features

- ✨ AI-generated personalized travel itineraries
- 📅 Day-wise detailed planning
- 🗺️ Tourist attractions suggestions
- 🍽️ Local food recommendations
- 💡 Travel tips and guidance
- ⚡ Fast and interactive Streamlit interface
- ✅ Input validation for better user experience

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit**
- **Google Generative AI (Gemini API)**
- **VS Code**

---

## 📂 Project Structure

travel-itinerary-generator/
│
├── app.py
├── requirements.txt
└── README.md

## 🔑 Gemini API Configuration

1. Go to **Google AI Studio**
2. Generate your API Key
3. Replace this line in `app.py`:
genai.configure(api_key="YOUR GOOGLE API KEY HERE")

With:

genai.configure(api_key="your_actual_api_key")

http://localhost:8501


---

## 🧠 How It Works

1. User enters:
   - Destination
   - Number of days
   - Number of nights
   - Travel interests

2. The application creates a structured AI prompt.

3. The prompt is sent to the Gemini AI model.

4. The AI generates:
   - Day-wise itinerary
   - Tourist attractions
   - Food recommendations
   - Travel tips

5. The response is displayed on the Streamlit interface.

---

## 📌 Example Input

- Destination: Bali  
- Days: 4  
- Nights: 3  
- Interests: Beaches, Adventure, Local Food  

---

## 📷 Application Screens

### 1️⃣ Application Interface
- Destination input field
- Days and nights input
- Interests text area
- Generate button

### 2️⃣ Generated Itinerary Output
- Structured day-wise plan
- Attractions list
- Food suggestions
- Travel guidance

### 3️⃣ Error Validation
- Warning message if required fields are missing

---

## 📈 Future Enhancements

- 🗺️ Google Maps Integration
- 💰 Budget estimation feature
- 🏨 Hotel and transport recommendations
- 📄 Download itinerary as PDF
- 🌐 Multi-language support
- 📱 Mobile-responsive UI improvements

---

## 🎯 Use Cases

- Personal trip planning
- Travel blog inspiration
- Tourism-based startup prototype
- Academic mini/major project
- AI-based web application demonstration





