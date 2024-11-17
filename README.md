# Data Collection and Storage in MongoDB

## **Project Overview**
This project demonstrates how to automate the process of collecting user reviews for the TikTok app from the Google Play Store, saving the reviews into a CSV file, and storing them in a MongoDB database for further analysis. 

The project uses Python and several libraries to implement a workflow that enables efficient data collection and storage.

---

## **Features**
- Fetches up to 5,000 reviews from the Google Play Store for the TikTok app.
- Saves the collected data in a CSV file (`tiktok_reviews.csv`) for analysis and backup.
- Inserts the reviews into a MongoDB database for querying and visualization.
- Verifies the stored data by querying MongoDB.

---

## **Project Files**
1. `Data_engineering_Assignment1.ipynb`: 
   - A Jupyter Notebook containing all the code for the project.
   - Includes the following steps:
     - Installing required libraries.
     - Fetching app reviews using the `google-play-scraper` library.
     - Saving reviews to a CSV file.
     - Connecting to MongoDB and inserting the data.
     - Querying and verifying the stored data.

2. `tiktok_reviews.csv`: 
   - A CSV file containing the collected reviews, including:
     - `Rating`: The numerical rating given by users.
     - `Review`: The text content of the review.
     - `Timestamp`: The date and time of the review.

3. `README.md`: 
   - This documentation file.

---

## **How to Run the Project**

### **1. Prerequisites**
- Install Python 3.x.
- Install the required libraries:
  ```python
  !pip install pymongo google-play-scraper pandas


---
## **Project Workflow**

1. **Data Collection:**
   - Fetches reviews for the TikTok app using the `google-play-scraper` library.
   - Captures data fields like:
     - `Rating`
     - `Review text`
     - `Timestamp`

2. **Saving Data:**
   - Saves the collected reviews to a CSV file (`tiktok_reviews.csv`).

3. **Storing in MongoDB:**
   - Inserts the reviews into the `Data_Engineering` database under the `reviews` collection.

4. **Querying Data:**
   - Verifies the inserted data by querying MongoDB and displaying a sample.

---

## **Example Document from MongoDB**

Here’s an example of a document stored in MongoDB:
```json
{
    "_id": "64f77bd2efb7da85a14cdbb2",
    "rating": 5,
    "review": "Great app! Easy to use and lots of fun.",
    "timestamp": "2023-11-17T08:34:21"
}

Added Project Workflow section to README.md"

