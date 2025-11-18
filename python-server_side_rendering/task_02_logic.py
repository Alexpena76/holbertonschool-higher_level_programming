from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def home():
    """Route for the home page"""
    return render_template('index.html')

@app.route('/about')
def about():
    """Route for the about page"""
    return render_template('about.html')

@app.route('/contact')
def contact():
    """Route for the contact page"""
    return render_template('contact.html')

@app.route('/items')
def items():
    """Route for the items page - displays items from JSON file"""
    # Read the JSON file
    try:
        with open('items.json', 'r') as file:
            data = json.load(file)
            items_list = data.get('items', [])
    except FileNotFoundError:
        # If file doesn't exist, use an empty list
        items_list = []
    except json.JSONDecodeError:
        # If JSON is invalid, use an empty list
        items_list = []
    
    # Pass the items list to the template
    return render_template('items.html', items=items_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)