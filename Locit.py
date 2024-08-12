

# Simulate user data and authentication
users = {
    "user1": {"name": "User 1", "location": None},
    "user2": {"name": "User 2", "location": None}
}

user_sessions = {}  # Simulate active user sessions

def get_location(address):
    """Gets coordinates from an address."""
    geolocator = Nominatim(user_agent="my_app")
    try:
        location = geolocator.geocode(address)
        if location:
            return location.latitude, location.longitude
        else:
            st.error("Location not found.")
    except Exception as e:
        st.error(f"Error getting location: {e}")
        return None

def set_location(user_id, latitude, longitude):
    """Sets a user's location."""
    users[user_id]["location"] = (latitude, longitude)
    st.success("Location set.")

def share_location(sender_id, receiver_id):
    """Shares location with another user."""
    sender_location = users[sender_id]["location"]
    if sender_location:
        users[receiver_id]["shared_location"] = sender_location
        st.success(f"Location shared with {users[receiver_id]['name']}")
    else:
        st.error("Sender's location is not available.")

def login(username, password):
    """Simulate login"""
    if username in users and password == "password":  # Replace with actual password verification
        user_sessions[username] = True
        st.success("Logged in successfully")
        return True
    else:
        st.error("Invalid username or password")
        return False

def logout(username):
    """Simulate logout"""
    if username in user_sessions:
        del user_sessions[username]
        st.success("Logged out")
    else:
        st.error("You are not logged in")

def main():
    st.title("Location Sharing App")

    if "username" not in st.session_state:
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            if login(username, password):
                st.session_state.username = username

    else:
        st.write(f"Welcome, {st.session_state.username}!")
        action = st.selectbox("Select action", ["Get Location", "Set Location", "Share Location", "Logout"])

        if action == "Get Location":
            address = st.text_input("Enter address:")
            if st.button("Get"):
                location = get_location(address)

        elif action == "Set Location":
            latitude = st.number_input("Enter latitude:")
            longitude = st.number_input("Enter longitude:")
            if st.button("Set"):
                set_location(st.session_state.username, latitude, longitude)

        elif action == "Share Location":
            receiver_id = st.text_input("Enter receiver's user ID:")
            if st.button("Share"):
                share_location(st.session_state.username, receiver_id)

        elif action == "Logout":
            logout(st.session_state.username)
            del st.session_state.username

if __name__ == "__main__":
    main()

