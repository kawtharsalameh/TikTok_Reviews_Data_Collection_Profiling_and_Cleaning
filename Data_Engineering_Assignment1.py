#!/usr/bin/env python
# coding: utf-8

# # Data Collection and Storage in MongoDB
# 
# This notebook demonstrates how to collect user reviews from the TikTok app on Google Play, save them to a CSV file, and insert them into a MongoDB database.
# 

# ## 1. Import Libraries
# 
# Import all the required libraries for data scraping, data manipulation, and database operations.
# 

# In[1]:


# Install necessary packages (if not already installed)
get_ipython().system('pip install pymongo google_play_scraper')

# Import libraries
from pymongo import MongoClient
from google_play_scraper import reviews, Sort
import csv
import pandas as pd
import pprint


# ## 2. Connect to MongoDB
# 
# Establish a connection to the MongoDB Atlas cluster using the provided connection URI.
# 

# In[4]:


from pymongo.mongo_client import MongoClient

uri = "mongodb://kawthar_salameh:7ala2007@cluster0-shard-00-00.fo12f.mongodb.net:27017,cluster0-shard-00-01.fo12f.mongodb.net:27017,cluster0-shard-00-02.fo12f.mongodb.net:27017/?ssl=true&replicaSet=atlas-3cbt0r-shard-0&authSource=admin&retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


# ## 3. Define Functions
# 
# Create a function to fetch reviews from Google Play Store for a specified app.
# 

# In[5]:


def get_reviews(app_id, total_reviews):
    """
    Fetches reviews for the specified app from Google Play Store.

    Parameters:
    - app_id (str): The app's unique identifier on Google Play.
    - total_reviews (int): Total number of reviews to fetch.

    Returns:
    - list: A list of review dictionaries.
    """
    all_reviews = []
    next_token = None

    while len(all_reviews) < total_reviews:
        review_batch, next_token = reviews(
            app_id,
            lang='en',          # Language of the reviews
            country='us',       # Country of the reviews
            sort=Sort.NEWEST,   # Sort reviews by newest
            count=200,          # Number of reviews to fetch in this batch
            continuation_token=next_token  # For pagination
        )

        all_reviews.extend(review_batch)

        # Break if there are no more reviews
        if not next_token:
            break

    return all_reviews[:total_reviews]


# ## 4. collect Reviews from Google Play
# 
# Use the defined function to fetch the desired number of reviews for the TikTok app.
# 

# In[6]:


# Specify the app ID and total number of reviews to fetch
app_id = 'com.zhiliaoapp.musically'  # TikTok app ID
total_reviews = 5000

# Fetch the reviews
reviews_data = get_reviews(app_id, total_reviews)

print(f"Fetched {len(reviews_data)} reviews.")


# ## 5. Save Reviews to CSV
# 
# Save the fetched reviews to a CSV file for backup and further analysis.
# 

# In[7]:


# Define the CSV file path
csv_file_path = "tiktok_reviews.csv"

# Write reviews to CSV
with open(csv_file_path, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Rating", "Review", "Timestamp"])  # Write header
    for review in reviews_data:
        writer.writerow([review['score'], review['content'], review['at']])

print(f"Reviews saved to {csv_file_path}.")


# ## 6. Insert Reviews into MongoDB
# 
# Load the reviews from the CSV file and insert them into the MongoDB collection.
# 

# In[8]:


# Load CSV data into a pandas DataFrame
df = pd.read_csv(csv_file_path)

# Convert DataFrame to list of dictionaries
data = df.to_dict(orient="records")

# Specify the database and collection names
db = client["Data_Engineering"]
collection = db["reviews"]

# Insert data into MongoDB
collection.insert_many(data)

print("Data inserted into MongoDB successfully!")


# ## 7. Query and Display Data from MongoDB
# 
# Retrieve and display some of the inserted reviews to verify the insertion.
# 

# In[9]:


# Retrieve documents from the collection
print("Sample documents from MongoDB:")
for doc in collection.find().limit(5):
    pprint.pprint(doc)


# ## 8. Conclusion
# 
# Successfully collected 5,000 reviews from the Google Play Store for the TikTok app, saved them to a CSV file, and inserted them into a MongoDB database for further analysis.
# 

# In[ ]:




