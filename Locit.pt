
import streamlit as st
import time
from geopy.geocoders import Nominatim

# Simulating user data (replace with actual user authentication)
users = {
    "user1": {"name": "User 1", "location": None},
    "user2": {"name": "User 2", "location": None}
}

def get_location(address):
    """Gets coordinates from an address."""
    geolocator = Nominatim(user_agent="my_app")
    location = geolocator.geocode(address)
    if location:
        return location.latitude, location.longitude
    else:
        return None

def set_location(user_id, latitude, longitude):
    """Sets a user's location."""
    users[user_id]["location"] = (latitude, longitude)

def share_location(sender_id, receiver_id):
    """Shares location with another user."""
    sender_location = users[sender_id]["location"]
    if sender_location:
        users[receiver_id]["shared_location"] = sender_location
        st.success(f"Location shared with {users[receiver_id]['name']}")
    else:
        st.error("Sender's location is not available.")

def main():
    st.title("Location Sharing App")

    user_id = st.text_input("Enter your user ID:")
    action = st.selectbox("Select action", ["Get Location", "Set Location", "Share Location"])

    if action == "Get Location":
        address = st.text_input("Enter address:")
        if st.button("Get"):
            location = get_location(address)
            if location:
                st.success(f"Latitude: {location[0]}, Longitude: {location[1]}")
            else:
                st.error("Location not found.")

    elif action == "Set Location":
        latitude = st.number_input("Enter latitude:")
        longitude = st.number_input("Enter longitude:")
        if st.button("Set"):
            set_location(user_id, latitude, longitude)
            st.success("Location set.")

    elif action == "Share Location":
        receiver_id = st.text_input("Enter receiver's user ID:")
        if st.button("Share"):
            share_location(user_id, receiver_id)

if __name__ == "__main__":
    main()

