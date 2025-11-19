from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def read_json_file():
    """Read and return data from products.json file"""
    try:
        with open('products.json', 'r') as file:
            products = json.load(file)
        return products
    except FileNotFoundError:
        return None
    except json.JSONDecodeError:
        return None

def read_csv_file():
    """Read and return data from products.csv file"""
    try:
        products = []
        with open('products.csv', 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                # Convert id to int and price to float for consistency
                product = {
                    'id': int(row['id']),
                    'name': row['name'],
                    'category': row['category'],
                    'price': float(row['price'])
                }
                products.append(product)
        return products
    except FileNotFoundError:
        return None
    except (ValueError, KeyError):
        return None

def read_sql_database():
    """Read and return data from SQLite database"""
    try:
        # Connect to the database
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        
        # Execute query to get all products
        cursor.execute('SELECT id, name, category, price FROM Products')
        
        # Fetch all rows
        rows = cursor.fetchall()
        
        # Convert rows to list of dictionaries for consistency with JSON/CSV
        products = []
        for row in rows:
            product = {
                'id': row[0],
                'name': row[1],
                'category': row[2],
                'price': row[3]
            }
            products.append(product)
        
        conn.close()
        return products
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

@app.route('/products')
def products():
    """Route to display products from JSON, CSV, or SQL based on query parameters"""
    # Get query parameters
    source = request.args.get('source')
    product_id = request.args.get('id')
    
    # Validate source parameter
    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', 
                             error="Wrong source")
    
    # Read data based on source
    if source == 'json':
        products_list = read_json_file()
    elif source == 'csv':
        products_list = read_csv_file()
    else:  # source == 'sql'
        products_list = read_sql_database()
    
    # Check if data was read successfully
    if products_list is None:
        return render_template('product_display.html', 
                             error="Error reading data source")
    
    # Filter by id if provided
    if product_id:
        try:
            product_id = int(product_id)
            # Filter products by id
            filtered_products = [p for p in products_list if p['id'] == product_id]
            
            if not filtered_products:
                return render_template('product_display.html', 
                                     error="Product not found")
            
            products_list = filtered_products
        except ValueError:
            return render_template('product_display.html', 
                                 error="Invalid product ID")
    
    # Render template with products data
    return render_template('product_display.html', 
                         products=products_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)