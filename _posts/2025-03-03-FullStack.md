---
toc: True
comments: true
layout: post
title: Full Stack Blog
description: Individual blog for Sprint 5 Dynamic Checkpoint Blog
permalink: /FullStack
---
## 🚀 Flashcards Feature - Full Stack Development Breakdown

# Site and Individual Feature 
The purpose of our program is to create a functioning, user-friendly, studying social media website for students. Users can interact with flashcards, quizzes, chatbots, studylogs, gradelogs, and more, and the changes are reflected in the backend database.

Flashcards allow students to Create, Update, and Delete flashcards in specefic Decks

  <div id="123456">
    <img src="{{site.baseurl}}/images/flashcard1.png" style="width: 190000px;">
  </div>
<br><br>

  <div id="123456">
    <img src="{{site.baseurl}}/images/deck.png" style="width: 190000px;">
  </div>
<br><br>


## 🏆 Meeting CPT & FRQ Requirements

This project fully satisfies the **[College Board CPT requirements](https://apcentral.collegeboard.org/media/pdf/ap-csp-student-task-directions.pdf)**
and the **FRQ specifications** by implementing structured programming concepts, data storage, and algorithmic logic. Below is a **detailed breakdown** of how the requirements are met with supporting code examples.

  <div id="123456">
    <img src="{{site.baseurl}}/images/frq.png" style="width: 190000px;">
  </div>
<br><br>





### 🔍 CPT & FRQ Requirement Breakdown

| **Requirement** | **How It Appears in Code** |
|----------------|--------------------------|
| **Input Handling** | Users input flashcard data via HTML forms, triggering JavaScript functions that send `fetch` requests to the backend API. |
| **Data Collection** | Uses **lists** (`decks`, `flashcards`) to manage and store data, and a **SQL database** (`Flashcard` model) for persistent storage. |
| **Student-Developed Procedures** | Functions like `updateFlashcard()`, `deleteFlashcard()`, `fetchDecks()`, and `openDeck()` ensure modularity and reusability. |
| **Algorithm Design** | Implements **Sequencing (step-by-step execution), Selection (conditionals for validation), and Iteration (loops for fetching/displaying data)** in UI and backend logic. |
| **Procedures with Parameters** | Functions such as `createFlashcard(title, content, deck_id)`, `updateFlashcard(flashcard_id, newTitle, newContent)`, and `deleteFlashcard(flashcard_id)` take parameters to process flashcard data dynamically. |
| **Instructions for Output** | The frontend updates dynamically with visual elements that reflect user actions (flashcard flipping, adding/removing decks, and modifying flashcards). |
| **Database Usage** | The backend **SQLAlchemy model** (`Flashcard`) stores and retrieves flashcards with relationships to users (`user_id`) and decks (`deck_id`). |
| **Use of Lists and Dictionaries** | Lists (`decks = []`, `flashcards = []`) store collections of data in the frontend, while dictionaries (`read()` function) format data for API responses. |
| **Querying a Database** | SQLAlchemy queries like `Flashcard.query.filter_by(_deck_id=deck.id).all()` extract relevant data for users and decks. |
| **Tester Data and Recovery** | Uses functions like `db_init()`, `db_restore()`, and `db_backup()` to manage test data and recover previous states. |
| **RESTful API Endpoints** | Implements RESTful principles with `POST`, `GET`, `PUT`, and `DELETE` routes for managing flashcards and decks. |

---

### ✅ CPT Code Implementation

#### **1️⃣ Input Handling (User Input)**
```python
@flashcard_api.route('/flashcard', methods=['POST'])
@token_required()
def create_flashcard():
    data = request.json
    flashcard = Flashcard(
        title=data['title'],
        content=data['content'],
        user_id=g.current_user.id,
        deck_id=data['deck_id']
    )
    flashcard.create()
    return jsonify(flashcard.read()), 201
```
- **Accepts user input** from the frontend (`title`, `content`, `deck_id`).
- **Stores flashcard data** in the database.
- **Returns a response** confirming the creation.

#### **2️⃣ Data Collection (Lists & Databases)**

Frontend:

```python
let decks = []; // Array to store all decks
let currentDeck = null; // Currently active deck
let currentCardIndex = 0; // Tracks the current flashcard
```
- Uses a list (decks) to store all decks and an index (currentCardIndex) to navigate through flashcards.

Backend:

```python
class Flashcard(db.Model):
    __tablename__ = 'flashcards'
    id = db.Column(db.Integer, primary_key=True)
    _title = db.Column(db.String(255), nullable=False)
    _content = db.Column(db.String(255), nullable=False)
    _user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    _deck_id = db.Column(db.Integer, db.ForeignKey('decks.id'), nullable=True)
```
- Uses a **database model** to store **flashcards persistently**.
- **Maintains relationships** using `ForeignKey` to link users and decks.

#### **3️⃣ Student-Developed Procedure**
```python
def update_flashcard(flashcard_id, new_title, new_content):
    flashcard = Flashcard.query.get(flashcard_id)
    flashcard._title = new_title
    flashcard._content = new_content
    db.session.commit()
    return flashcard.read()
```
- **Defined procedure** (`update_flashcard`) with **parameters** (`flashcard_id`, `new_title`, `new_content`).
- **Modifies existing flashcard records** in the database.


#### **4️⃣ Algorithm Design (Sequencing, Selection, Iteration)**
```python
document.getElementById('add-card-btn').addEventListener('click', async () => {
    const question = document.getElementById('question').value.trim();
    const answer = document.getElementById('answer').value.trim();

    if (!question || !answer) {  // ❗️ Selection (IF statement)
        alert('Please provide both a question and an answer.');
        return;
    }

    try {
        const response = await fetch(`${pythonURI}/api/flashcard`, {  // 🔄 Sequencing
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            credentials: 'include',
            body: JSON.stringify({
                title: question,
                content: answer,
                deck_id: currentDeck.id,
                user_id: 1
            }),
        });

        if (response.ok) {  // ❗️ Selection
            const newCard = await response.json();
            currentDeck.cards.push(newCard); // 🔄 Iteration (managing multiple flashcards)
            displayFlashcards(currentDeck.cards);
        }
    } catch (error) {
        console.error('Error adding flashcard:', error);
    }
});
```
- **Selection**: The code uses if statements to check if the question or answer is missing (if (!question || !answer) {}) or if the response is successful (if (response.ok) {}).
- **Sequencing**: The code follows a logical sequence where it first checks for input, then makes a network request, and finally updates the deck with the new card if the request is successful.
- **Iteration**: The currentDeck.cards.push(newCard) adds the newly created card to an array, and displayFlashcards(currentDeck.cards) iterates through the updated cards to display them.

#### **5️⃣ Output Handling (Visual Updates)**
```js
function displayFlashcards(cards) {
    cards.forEach(card => {
        const cardElement = document.createElement('div');
        cardElement.textContent = card.title;
        cardElement.onclick = () => {
            cardElement.textContent = cardElement.textContent === card.title ? card.content : card.title;
        };
        container.appendChild(cardElement);
    });
}
```
- Updates the **frontend dynamically** based on user interaction.

---



## 🗄️ Databasing & Backend (Flask API)

The **backend** is a Flask-based REST API that provides **CRUD functionality**, data persistence, and secure authentication.

### 📌 Database Model (SQLAlchemy)
Each **flashcard** is stored in the database using a structured model:
```python
class Flashcard(db.Model):
    __tablename__ = 'flashcards'
    id = db.Column(db.Integer, primary_key=True)
    _title = db.Column(db.String(255), nullable=False)
    _content = db.Column(db.String(255), nullable=False)
    _user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    _deck_id = db.Column(db.Integer, db.ForeignKey('decks.id'), nullable=True)
```
- The **primary key (`id`)** ensures uniqueness.
- **Foreign keys (`_user_id`, `_deck_id`)** associate flashcards with users and decks.
- **String fields (`_title`, `_content`)** store the flashcard data.

### 📌 API Endpoints and CRUD operations
The backend handles **creating, reading, updating, and deleting** flashcards through these routes:
As you can see in this photo, 

  <div id="123456">
    <img src="{{site.baseurl}}/images/flashcard.png" style="width: 190000px;">
  </div>
<br><br>

Users can add and edit own data that get's stored in the Backend Database. 

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

#### 1️⃣ Creating a Flashcard (`POST /api/flashcard`)
```python
@flashcard_api.route('/flashcard', methods=['POST'])
@token_required()
def create_flashcard():
    data = request.json
    flashcard = Flashcard(
        title=data['title'],
        content=data['content'],
        user_id=g.current_user.id,
        deck_id=data['deck_id']
    )
    flashcard.create()
    return jsonify(flashcard.read()), 201
```
- **Takes user input** (title, content, deck association).
- **Saves it in the database** using `SQLAlchemy`.
- **Ensures authentication** using JWT tokens.

#### 2️⃣ Fetching Flashcards (`GET /api/flashcard`)
```python
@flashcard_api.route('/flashcard', methods=['GET'])
@token_required()
def get_flashcards():
    current_user = g.current_user
    flashcards = Flashcard.query.filter_by(_user_id=current_user.id).all()
    return jsonify([flashcard.read() for flashcard in flashcards])
```
- Retrieves **all flashcards** for the logged-in user.
- Uses **SQLAlchemy query filtering** to ensure user privacy.

#### 3️⃣ Updating a Flashcard (`PUT /api/flashcard/<id>`)
```python
@flashcard_api.route('/flashcard/<int:flashcard_id>', methods=['PUT'])
@token_required()
def update_flashcard(flashcard_id):
    data = request.get_json()
    flashcard = Flashcard.query.get(flashcard_id)
    if not flashcard or flashcard._user_id != g.current_user.id:
        return jsonify({'message': 'Flashcard not found or unauthorized'}), 404
    flashcard._title = data.get('title', flashcard._title)
    flashcard._content = data.get('content', flashcard._content)
    db.session.commit()
    return jsonify(flashcard.read())
```
- **Updates** the title and content dynamically.
- **Verifies user authorization** before modifying data.

#### 4️⃣ Deleting a Flashcard (`DELETE /api/flashcard/<id>`)
```python
@flashcard_api.route('/flashcard/<int:flashcard_id>', methods=['DELETE'])
@token_required()
def delete_flashcard(flashcard_id):
    flashcard = Flashcard.query.get(flashcard_id)
    if not flashcard or flashcard._user_id != g.current_user.id:
        return jsonify({'message': 'Flashcard not found or unauthorized'}), 404
    db.session.delete(flashcard)
    db.session.commit()
    return jsonify({'message': 'Flashcard deleted successfully'})
```
- **Removes flashcards permanently** from the database.
- **Ensures users can only delete their own flashcards**.

---

## 🔄 CRUD Operations Summary

| **Operation** | **Backend Endpoint** | **Example Code** |
|--------------|---------------------|-----------------|
| **Create** | `POST /api/flashcard` | `create_flashcard()` |
| **Read** | `GET /api/flashcard` | `get_flashcards()` |
| **Update** | `PUT /api/flashcard/<id>` | `update_flashcard()` |
| **Delete** | `DELETE /api/flashcard/<id>` | `delete_flashcard()` |

> This project **effectively manages flashcard data** with an optimized database model, secure API access, and efficient CRUD operations.

## Using postman to show raw API request and RESTful response 
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

## Using db_init, db_restore, db_backup to show tester data creation and data recovery

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

## Use of List, Dictionaries, and Database

CPT Requirement: Use of at Least One List (or Other Collection Type)

Lists: Used to manage user interests.
Dictionaries: Used to handle JSON data in API requests and responses.
Database: Used to store user data, including interests.

CPT requirement: Query

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

---

## 🚀 Next Steps

🔹 **Improve Database Performance**: Implement indexing and caching for faster queries.  
🔹 **Enhance API Security**: Strengthen authentication mechanisms to prevent unauthorized access.  
🔹 **Introduce Flashcard Sharing**: Allow users to share decks with friends.  

---

## 🎯 Conclusion

This project **demonstrates Full Stack Development** by integrating **a structured backend with a secure, database-driven API**. The **use of CRUD operations, authentication, and data persistence** ensures reliability and scalability. 🎉

By implementing **structured programming principles**, **database best practices**, and **user-focused features**, this project **successfully meets the CPT and FRQ requirements**, making it a **strong candidate for real-world applications**. 🚀
