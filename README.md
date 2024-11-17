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


