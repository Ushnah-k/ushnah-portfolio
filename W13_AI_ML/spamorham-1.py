# -*- coding: utf-8 -*-
# Naive Bayes Email Classifier using scikit-learn

import os
import io
import numpy
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# ------------------------------------------------------------------------------
# SECTION 1: Function to Read Emails from File System
# ------------------------------------------------------------------------------

def readFiles(path):
    """
    Reads email files from the specified directory.
    Extracts the body of each email (ignoring headers) and yields its content.
    
    Args:
        path (str): Path to the directory containing email files.

    Yields:
        tuple: (filename, email body as string)
    """
    for root, dirnames, filenames in os.walk(path):
        for filename in filenames:
            filepath = os.path.join(root, filename)
            inBody = False
            lines = []

            with io.open(filepath, 'r', encoding='latin1') as f:
                for line in f:
                    if inBody:
                        lines.append(line)
                    elif line == '\n':  # Empty line indicates end of header
                        inBody = True

            message = '\n'.join(lines)
            yield filepath, message

# ------------------------------------------------------------------------------
# SECTION 2: Convert Email Files into a DataFrame
# ------------------------------------------------------------------------------

def dataFrameFromDirectory(path, classification):
    """
    Builds a DataFrame from email files with a given classification (e.g., 'spam' or 'ham').

    Args:
        path (str): Path to email directory.
        classification (str): Label for classification ('spam' or 'ham').

    Returns:
        pandas.DataFrame: DataFrame containing messages and their class labels.
    """
    rows = []
    index = []
    
    for filename, message in readFiles(path):
        rows.append({'message': message, 'class': classification})
        index.append(filename)

    return pd.DataFrame(rows, index=index)

# ------------------------------------------------------------------------------
# SECTION 3: Create DataFrame for Spam and Ham Emails
# ------------------------------------------------------------------------------

# Initialize an empty DataFrame
data = pd.DataFrame({'message': [], 'class': []})

# Use absolute paths to the spam and ham folders
data = pd.concat([
    dataFrameFromDirectory(
        '/home/ugrads/majors/ushnahk/CS2104/W13_AI_ML/full/spam', 'spam'),
    dataFrameFromDirectory(
        '/home/ugrads/majors/ushnahk/CS2104/W13_AI_ML/full/ham', 'ham')
])

# Print dataset summary
print(data.head())
print(data.tail())
print(data.info())

# ------------------------------------------------------------------------------
# SECTION 4: Train a Naive Bayes Classifier
# ------------------------------------------------------------------------------

# CountVectorizer tokenizes text and converts it to a frequency matrix
vectorizer = CountVectorizer()
counts = vectorizer.fit_transform(data['message'].values)

# Extract the target labels (spam or ham)
targets = data['class'].values

# Create and train the Multinomial Naive Bayes classifier
classifier = MultinomialNB()
classifier.fit(counts, targets)

# ------------------------------------------------------------------------------
# SECTION 5: Test the Model with Sample Emails (Fun Part!)
# ------------------------------------------------------------------------------

sample = ['Free iPhone!', "We regret to inform that your paper has been rejected."]
sample_counts = vectorizer.transform(sample)
predictions = classifier.predict(sample_counts)
probabilities = classifier.predict_proba(sample_counts)

print(sample, predictions)
print(sample, probabilities)

#Students own examples
sample = [
    "Your UPS package has been delayed.",
    "Congrats! You have been accepted to win this raffle!",
    "You can click on this button to receive your $50 benefit.",
    "Enroll today in bestTutor.com!",
    "Subscribe now to see weekly letters about your community!"
]
sample_counts = vectorizer.transform(sample)
predictions = classifier.predict(sample_counts)
probabilities = classifier.predict_proba(sample_counts)
print(sample, predictions, probabilities)  

# ------------------------------------------------------------------------------