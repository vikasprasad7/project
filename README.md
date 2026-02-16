A simple web-based chat application for healthcare consultations, built and maintained by **Vikas Prasad**.

## Overview

This project provides a user-friendly chat interface for patients to register their communication with 
healthcare professionals. The system leverages a Large Language Model (LLM) to process user conversations, 
extract relevant details, display them in a structured form, and persist the information in a database 
for future reference.

## Features

- **Chat Interface**: Save communication between users and healthcare professionals via a chatbox.
- **LLM Integration**: Automatically processes chat messages to extract key details.
- **Structured Forms**: Extracted information is displayed in dedicated columns/fields for review.
- **Data Persistence**: All chat data and extracted details are securely stored in the database.
- **Separation of Concerns**: 
  - `app.py` - Backend logic and API endpoints  
  - `chatbox.js` - Frontend user chat interface

## Technology Stack

- **Backend**: Python (`app.py`)  
- **Frontend**: JavaScript (`chatbox.js`), HTML, CSS  
- **AI/ML**: Integration with a Large Language Model (LLM)  
- **Database**: MySQL
