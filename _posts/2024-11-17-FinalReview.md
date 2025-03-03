---
toc: True
comments: True
layout: post
title: Final Review
description: College Board Practie MCQ 
permalink: /FinalReview
---
# Flashcard Feature - Retrospective Blog

## Overview
Over the past 12 weeks, I worked on implementing a **Flashcard Feature** for my full-stack application. This feature allows users to **create, update, delete, and review flashcards** within decks. The backend is built with **Flask (Python)**, and the frontend is implemented using **HTML, CSS, and JavaScript**.

## 1️⃣ How the Flashcard Feature Works
The Flashcard system consists of:
- **Decks**: Groups of flashcards.
- **Flashcards**: Individual cards containing a question and an answer.
- **User Interactions**: Users can create, update, delete, and flip flashcards.

### Frontend Implementation
The UI consists of a **deck container** and a **flashcard display area**. Below is the JavaScript code that dynamically loads flashcards:

```javascript
function displayFlashcards(cards) {
    const container = document.getElementById('flashcard-container');
    container.innerHTML = ''; // Clear previous flashcards

    cards.forEach(card => {
        const cardElement = document.createElement('div');
        cardElement.classList.add('flashcard');
        cardElement.innerHTML = `
            <div class="flashcard-content">
                <span class="question-text">${card.title}</span>
                <span class="edit-icon">✏️</span>
                <span class="delete-icon">❌</span>
            </div>
        `;

        // Flip between question and answer
        cardElement.onclick = (event) => {
            if (!event.target.classList.contains("edit-icon") && !event.target.classList.contains("delete-icon")) {
                const isQuestion = cardElement.textContent === card.title;
                cardElement.textContent = isQuestion ? card.content : card.title;
                cardElement.classList.toggle('answer', isQuestion);
            }
        };

        container.appendChild(cardElement);
    });
}
```

### Backend Implementation (Flask API)
The backend provides **CRUD operations** for flashcards:

```python
from flask import Blueprint, request, jsonify, g
from flask_restful import Api, Resource
from model.flashcard import Flashcard

flashcard_api = Blueprint('flashcard_api', __name__, url_prefix='/api')
api = Api(flashcard_api)

class FlashcardAPI(Resource):
    def post(self):
        data = request.get_json()
        flashcard = Flashcard(data['title'], data['content'], data['user_id'], data['deck_id'])
        flashcard.create()
        return jsonify(flashcard.read())

    def get(self, flashcard_id):
        flashcard = Flashcard.query.get(flashcard_id)
        return jsonify(flashcard.read()) if flashcard else (jsonify({'message': 'Not found'}), 404)

    def put(self, flashcard_id):
        data = request.get_json()
        flashcard = Flashcard.query.get(flashcard_id)
        flashcard.update(data)
        return jsonify(flashcard.read())

    def delete(self, flashcard_id):
        flashcard = Flashcard.query.get(flashcard_id)
        flashcard.delete()
        return jsonify({'message': 'Flashcard deleted'})

api.add_resource(FlashcardAPI, '/flashcard', '/flashcard/<int:flashcard_id>')
```

## 2️⃣ Challenges & Issues Faced
1. **404 Error for Deployed API** - The backend routes for `/api/flashcard/{id}` did not work in deployment but worked locally.
    - **Fix**: Ensured `flashcard_id` was passed correctly in API routes and restarted Gunicorn.
2. **Update Bug** - After updating a flashcard, only the question was showing on both sides.
    - **Fix**: Used `dataset.answer` to store the updated answer and properly reassign values.
3. **Delete Function Not Working** - The API call returned a `500 Internal Server Error`.
    - **Fix**: Corrected the API to retrieve `flashcard_id` from the URL instead of the request body.
4. **Live Updates Issue** - Flashcards would not update without refreshing the page.
    - **Fix**: Used JavaScript to dynamically update the UI after an API call instead of reloading the page.

## 3️⃣ Burndown Progress
| Week  | Task | Status |
|--------|----------------------------------------|---------|
| Week 1-2 | Set up Flask API & Database | ✅ Done |
| Week 3-4 | Implement Create & Read Flashcards | ✅ Done |
| Week 5-6 | Add Flashcard Flipping | ✅ Done |
| Week 7-8 | Implement Update Flashcards | ✅ Done (Fixed UI issue) |
| Week 9-10 | Implement Delete Flashcards | ✅ Done (Fixed API issue) |
| Week 11-12 | Test & Fix Deployment Issues | ✅ Done |

## 4️⃣ Final Presentation Details
For my **final presentation**, I will:
1. **Demo the Flashcard Feature** – Show creating, updating, deleting, and flipping flashcards.
2. **Explain API Requests** – Show how requests are handled in Flask.
3. **Show Fixes to Bugs** – Highlight the debugging process.
4. **Discuss Next Steps** – Plans to improve the feature, such as adding categories, user progress tracking, and AI-generated flashcards.

## 5️⃣ Future Improvements
- **User Progress Tracking**: Store how many flashcards a user got right.
- **AI-Generated Flashcards**: Auto-generate flashcards based on text input.
- **Categorization & Search**: Allow users to categorize and filter flashcards.

## **Conclusion**
Building the **Flashcard Feature** was a challenging but rewarding experience. I faced **deployment issues, UI bugs, and API errors**, but by debugging and iterating on my code, I was able to **successfully deploy** a fully functional flashcard system. 🚀
