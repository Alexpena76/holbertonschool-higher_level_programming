from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity, get_jwt
)
from werkzeug.security import generate_password_hash, check_password_hash

# Create Flask application
app = Flask(__name__)

# Configure JWT
app.config['JWT_SECRET_KEY'] = 'your-secret-key-change-this-in-production'
jwt = JWTManager(app)

# Initialize HTTP Basic Auth
auth = HTTPBasicAuth()

# In-memory user storage
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


# ============================================
# Basic Authentication
# ============================================

@auth.verify_password
def verify_password(username, password):
    """
    Verify username and password for Basic Authentication.
    
    Args:
        username (str): The username
        password (str): The password
        
    Returns:
        str or None: Username if valid, None otherwise
    """
    if username in users:
        if check_password_hash(users[username]['password'], password):
            return username
    return None


@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    """
    Protected route using Basic Authentication.
    
    Returns:
        str: Success message if authenticated
    """
    return "Basic Auth: Access Granted"


# ============================================
# JWT Authentication
# ============================================

@app.route('/login', methods=['POST'])
def login():
    """
    Login endpoint that returns a JWT token.
    
    Expected JSON:
    {
        "username": "user1",
        "password": "password"
    }
    
    Returns:
        JSON with access_token or error message
    """
    # Get JSON data
    data = request.get_json()
    
    if not data:
        return jsonify({"error": "Missing JSON in request"}), 400
    
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 400
    
    # Check if user exists
    if username not in users:
        return jsonify({"error": "Invalid credentials"}), 401
    
    # Verify password
    if not check_password_hash(users[username]['password'], password):
        return jsonify({"error": "Invalid credentials"}), 401
    
    # Create JWT token with user info
    additional_claims = {"role": users[username]['role']}
    access_token = create_access_token(
        identity=username,
        additional_claims=additional_claims
    )
    
    return jsonify({"access_token": access_token}), 200


@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    """
    Protected route using JWT Authentication.
    
    Requires:
        Authorization: Bearer <JWT_TOKEN>
        
    Returns:
        str: Success message if authenticated
    """
    current_user = get_jwt_identity()
    return "JWT Auth: Access Granted"


@app.route('/admin-only')
@jwt_required()
def admin_only():
    """
    Protected route that requires admin role.
    
    Requires:
        Authorization: Bearer <JWT_TOKEN>
        User must have admin role
        
    Returns:
        str: Success message if user is admin
        403: If user is not admin
    """
    # Get current user identity
    current_user = get_jwt_identity()
    
    # Get additional claims (role)
    claims = get_jwt()
    user_role = claims.get('role')
    
    # Check if user is admin
    if user_role != 'admin':
        return jsonify({"error": "Admin access required"}), 403
    
    return "Admin Access: Granted"


# ============================================
# JWT Error Handlers
# ============================================

@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """Handle missing or invalid authorization header"""
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """Handle invalid token format"""
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_payload):
    """Handle expired token"""
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(jwt_header, jwt_payload):
    """Handle revoked token"""
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(jwt_header, jwt_payload):
    """Handle when fresh token is required"""
    return jsonify({"error": "Fresh token required"}), 401


# ============================================
# Run Application
# ============================================

if __name__ == '__main__':
    app.run(debug=True)
