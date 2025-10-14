import requests
import csv


def fetch_and_print_posts():
    """
    Fetches all posts from JSONPlaceholder and prints their titles.
    Also prints the status code of the response.
    """
    # Define the API endpoint
    url = "https://jsonplaceholder.typicode.com/posts"
    
    try:
        # Send GET request to the API
        response = requests.get(url)
        
        # Print the status code
        print(f"Status Code: {response.status_code}")
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the response as JSON
            posts = response.json()
            
            # Iterate through all posts and print their titles
            for post in posts:
                print(post['title'])
        else:
            print(f"Failed to fetch posts. Status code: {response.status_code}")
            
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


def fetch_and_save_posts():
    """
    Fetches all posts from JSONPlaceholder and saves them to a CSV file.
    The CSV file contains columns: id, title, and body.
    """
    # Define the API endpoint
    url = "https://jsonplaceholder.typicode.com/posts"
    
    try:
        # Send GET request to the API
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the response as JSON
            posts = response.json()
            
            # Structure the data into a list of dictionaries
            # Extract only id, title, and body from each post
            structured_posts = [
                {
                    'id': post['id'],
                    'title': post['title'],
                    'body': post['body']
                }
                for post in posts
            ]
            
            # Write data to CSV file
            with open('posts.csv', 'w', newline='', encoding='utf-8') as csvfile:
                # Define the column headers
                fieldnames = ['id', 'title', 'body']
                
                # Create a DictWriter object
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                
                # Write the header row
                writer.writeheader()
                
                # Write all posts to the CSV file
                writer.writerows(structured_posts)
            
            print(f"Successfully saved {len(structured_posts)} posts to posts.csv")
        else:
            print(f"Failed to fetch posts. Status code: {response.status_code}")
            
    except requests.exceptions.RequestException as e:
        print(f"An error occurred during the request: {e}")
    except IOError as e:
        print(f"An error occurred while writing to the file: {e}")
