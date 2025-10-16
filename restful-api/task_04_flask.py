from flask import Flask, jsonify, request

# Create Flask application instance
app = Flask(__name__)

# In-memory storage for users
# NOTE: Start with empty dictionary - do not include test data when pushing code
users = {}


@app.route('/')
def home():
    """
    Root endpoint - returns welcome message.
    """
    return "Welcome to the Flask API!"


@app.route('/status')
def status():
    """
    Status endpoint - returns OK.
    """
    return "OK"


@app.route('/data')
def data():
    """
    Data endpoint - returns list of all usernames.
    
    Returns:
        JSON list of usernames
    """
    # Extract all usernames (keys) from the users dictionary
    usernames = list(users.keys())
    return jsonify(usernames)


@app.route('/users/<username>')
def get_user(username):
    """
    Get user endpoint - returns full user object for the given username.
    
    Args:
        username (str): The username to look up
        
    Returns:
        JSON object with user data or 404 error if not found
    """
    # Check if user exists
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """
    Add user endpoint - accepts POST requests to add new users.
    
    Expected JSON format:
    {
        "username": "john",
        "name": "John",
        "age": 30,
        "city": "New York"
    }
    
    Returns:
        201: Success with user data
        400: Invalid JSON or missing username
        409: Username already exists
    """
    
    # Try to parse JSON from request body
    try:
        user_data = request.get_json()
        
        # Check if get_json() returned None (invalid JSON)
        if user_data is None:
            return jsonify({"error": "Invalid JSON"}), 400
            
    except Exception:
        return jsonify({"error": "Invalid JSON"}), 400
    
    # Check if username is provided
    if 'username' not in user_data:
        return jsonify({"error": "Username is required"}), 400
    
    username = user_data['username']
    
    # Check if username already exists
    if username in users:
        return jsonify({"error": "Username already exists"}), 409
    
    # Add user to the dictionary
    users[username] = user_data
    
    # Return success response with 201 status code
    return jsonify({
        "message": "User added",
        "user": user_data
    }), 201


# Run the Flask development server
if __name__ == "__main__":
    app.run()
