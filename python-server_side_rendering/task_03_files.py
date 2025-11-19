from flask import Flask, render_template, request
import json
import csv

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

@app.route('/products')
def products():
    """Route to display products from JSON or CSV based on query parameters"""
    # Get query parameters
    source = request.args.get('source')
    product_id = request.args.get('id')
    
    # Validate source parameter
    if source not in ['json', 'csv']:
        return render_template('product_display.html', 
                             error="Wrong source")
    
    # Read data based on source
    if source == 'json':
        products_list = read_json_file()
    else:  # source == 'csv'
        products_list = read_csv_file()
    
    # Check if file was read successfully
    if products_list is None:
        return render_template('product_display.html', 
                             error="Error reading file")
    
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