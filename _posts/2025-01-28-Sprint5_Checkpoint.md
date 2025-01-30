---
toc: True
comments: true
layout: post
title: Sprint 5 Dynamic Checkpoint Blog
description: Individual blog for Sprint 5 Dynamic Checkpoint Blog
permalink: /Blog_5
---

# Purpose of Program
The purpose of our program is to create a functioning, user-friendly,  studying social media website for students. Users can interact with flashcards, quizzes, chatbots, studylogs, gradelogs, and more, and the changes are reflected in the backend database.

# Purpose of Individual Feature
- Flashcards allow students to Create, Update, and Delete flashcards in specefic Decks


CPT REQUIREMENT 1: Input from a User, a Device, an Online Data Stream, or a File
-The user enters a deck title as input.
-The frontend sends this user input to the backend via a POST request to store the deck in the database.


# Input/Output Requests
async function fetchDecks() {
    try {
        const response = await fetch('http://127.0.0.1:8887/api/deck', {
            method: 'GET',
            headers: { 'Content-Type': 'application/json' },
            credentials: 'include',
        });

        if (response.ok) {
            const fetchedDecks = await response.json();
            console.log('Fetched decks:', fetchedDecks);

            deckContainer.innerHTML = ''; // Clear container

            fetchedDecks.forEach(deck => {  // ✅ FOR LOOP EQUIVALENT
                displayDeck(deck);
            });
        }
    } catch (error) {
        console.error('Error fetching decks:', error);
    }
}
```      

- For loop to iterate over fetchedDecks

in order to Create the Flashcards/Decks. 



As you can see in this photo, 

  <div id="123456">
    <img src="{{site.baseurl}}/images/123456.png" style="width: 190000px;">
  </div>
<br><br>

Users can add their own data that get's stored in the Backend Database. 

  <div id="123456">
    <img src="{{site.baseurl}}/images/image.png" style="width: 190000px;">
  </div>
<br><br>

The frontend also uses DELETE in order to Remove unwanted Decks/Flashcards.

```
 try {
                const response = await fetch(`http://127.0.0.1:8887/api/deck/${deck.id}`, {
                    method: 'DELETE',
                    headers: { 'Content-Type': 'application/json' },
                    credentials: 'include',
                });

                if (response.ok) {
                    alert('Deck deleted successfully!');
```


# Using postman to show raw API request and RESTful response 
POST Request to Add Flashcard:

URL: http://127.0.0.1:8887/api/flashcard
Method: POST
Body:
{
  "title": "What is 10 x 2",
  "content": "20",
  "user_id": 1,
  "deck_id": 1
}

Response:

Status: 200 OK
Body:
{
    "content": "20",
    "deck_id": 1,
    "id": 8,
    "title": "What is 10 x 2",
    "user_id": 1
}

  <div id="t3">
    <img src="{{site.baseurl}}/images/t3.png" style="width: 190000px;">
  </div>
<br><br>

DELETE Request to delete a Deck:
URL: http://127.0.0.1:8887/api/deck
Method: DELETE

Response:
{
    "message": "Deck with ID 2 deleted successfully"
}

  <div id="t6">
    <img src="{{site.baseurl}}/images/t6.png" style="width: 190000px;">
  </div>
<br><br>

# Using db_init, db_restore, db_backup to show tester data creation and data recovery

Tester Data: 
```
# Add some flashcards with test data
            flashcards_data = [
                {"title": "What is 2+2?", "content": "4", "user_id": user.id, "deck_id": deck.id},
                {"title": "What is 5+3?", "content": "8", "user_id": user.id, "deck_id": deck.id},
                {"title": "What is 10-6?", "content": "4", "user_id": user.id, "deck_id": deck.id}
            ]
```
  <div id="t69">
    <img src="{{site.baseurl}}/images/t69.png" style="width: 190000px;">
  </div>
<br><br>

# Use of List, Dictionaries, and Database

CPT Requirement #2: Use of at Least One List (or Other Collection Type)

Lists: Used to manage user interests.
Dictionaries: Used to handle JSON data in API requests and responses.
Database: Used to store user data, including interests.

CPT requirement #5: Query

1) Extracting Data (Python List from SQLAlchemy Query)
```
flashcards = Flashcard.query.filter_by(_deck_id=deck.id).all()
```
Explanation: This retrieves all flashcards linked to a specific deck and returns a list.


2) Formatting Data for API Response (Dictionaries)
```
def read(self):
    return {
        "id": self.id,
        "title": self._title,
        "content": self._content,
        "user_id": self._user_id,
        "deck_id": self._deck_id
    }
```
Explanation: This function converts a database record into a dictionary, allowing JSON responses in the API.

3) Working With Database records (CRUD Operations)
```
class Flashcard(db.Model):
    def create(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
```



# API Methods & Algorithmic Code

CPT Requirement #3: At Least One Procedure That Contributes to the Program’s Purpose

1)  API Endpoints for CRUD Operations
```
@app.route('/api/flashcard', methods=['POST'])
def create_flashcard():
    data = request.get_json()
    flashcard = Flashcard(data['title'], data['content'], data['user_id'], data['deck_id'])
    flashcard.create()
    return jsonify(flashcard.read()), 201
```

Explanation: This method creates a new flashcard and stores it in the database.


CPT Requirement #4: An Algorithm That Includes Sequencing, Selection, and Iteration

2) Algorithm with Sequencing, Selection, and Iteration
```
document.getElementById('add-card-btn').addEventListener('click', async () => {
    const question = document.getElementById('question').value.trim();
    const answer = document.getElementById('answer').value.trim();
    
    if (!question || !answer) {  // Selection (if condition)
        alert('Please provide both a question and an answer.');
        return;
    }
    
    try {
        const response = await fetch('http://127.0.0.1:8887/api/flashcard', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ title: question, content: answer, deck_id: currentDeck.id })
        });
        
        if (response.ok) {
            alert('Flashcard added!');
        }
    } catch (error) {
        console.error('Error:', error);
    }
});
```
Explanation: This function:

Checks for missing input (if (!question || !answer)) → Selection

Fetches data from API → Sequencing

Handles response data using loops → Iteration

# Call to Algorithim Request

1) Parameters (Body of Request) and Return Type (jsonify) of the Function

```
@token_required()
def post(self):
    """Create a new flashcard."""
    current_user = g.current_user
    data = request.get_json()

    if not data or 'title' not in data or 'content' not in data or 'deck_id' not in data:
        return jsonify({'message': 'Title, content, and deck_id are required'}), 400

    flashcard = Flashcard(data['title'], data['content'], current_user.id, data['deck_id'])
    flashcard = flashcard.create()

    if not flashcard:
        return jsonify({'message': 'Failed to create flashcard'}), 400

    return jsonify(flashcard.read()), 201  # Return created flashcard as JSON
```

Here, the jsonify(flashcard.read()) method ensures that the response is formatted in JSON.

2) Call to Algorithm Request: Show the Definition of Code Block to Make a Request

```
async function addFlashcard(question, answer, deckId) {
    try {
        const response = await fetch('http://127.0.0.1:8887/api/flashcard', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            credentials: 'include',
            body: JSON.stringify({
                title: question,
                content: answer,
                deck_id: deckId,
                user_id: 1  // Replace with actual user ID
            }),
        });

        if (response.ok) {
            const newCard = await response.json();
            console.log('Flashcard added:', newCard);
            return newCard;
        } else {
            console.error('Failed to add flashcard');
        }
    } catch (error) {
        console.error('Error:', error);
    }
}
```
CPT Requirement #6: Instructions for Output

The fetch API sends a request to the /api/flashcard endpoint. It provides the flashcard details in the request body.

function sends a POST request to the backend API. This is a call to the backend algorithm that processes the data.

-The frontend sends a POST with the flashcard details.
-The backend validates the request and processes it.
-The flashcard is saved to the database via SQLAlchemy.
-The API returns the created flashcard in JSON format.
-The frontend receives the response and updates frontend. 

3) Show How Changing Data or Method Triggers a Different Response

Normal:
```
{
    "title": "What is the capital of France?",
    "content": "Paris",
    "deck_id": 2,
    "user_id": 1
}
```

If you get rid of some data, error codes come back as

{
    "message": "Title, content, and deck_id are required"
}

