from fastapi import FastAPI
import random

app = FastAPI()

quotes_db = [
    {"text": "The only way to do great work is to love what you do.", "author": "Steve Jobs"},
    {"text": "Success is not final, failure is not fatal: It is the courage to continue that counts.", "author": "Winston Churchill"},
    {"text": "Believe you can and you're halfway there.", "author": "Theodore Roosevelt"},
    {"text": "Your time is limited, don't waste it living someone else's life.", "author": "Steve Jobs"},
    {"text": "It does not matter how slowly you go as long as you do not stop.", "author": "Confucius"},
    {"text": "Hardships often prepare ordinary people for an extraordinary destiny.", "author": "C.S. Lewis"},
    {"text": "The future belongs to those who believe in the beauty of their dreams.", "author": "Eleanor Roosevelt"},
    {"text": "Don't watch the clock; do what it does. Keep going.", "author": "Sam Levenson"},
    {"text": "The secret of getting ahead is getting started.", "author": "Mark Twain"},
    {"text": "Whatever you are, be a good one.", "author": "Abraham Lincoln"},
    {"text": "You miss 100% of the shots you don't take.", "author": "Wayne Gretzky"},
    {"text": "I have not failed. I've just found 10,000 ways that won't work.", "author": "Thomas Edison"},
    {"text": "Do not wait for leaders; do it alone, person to person.", "author": "Mother Teresa"},
    {"text": "If you are going through hell, keep going.", "author": "Winston Churchill"},
    {"text": "Start where you are. Use what you have. Do what you can.", "author": "Arthur Ashe"},
    {"text": "Everything you’ve ever wanted is on the other side of fear.", "author": "George Addair"},
    {"text": "Opportunities don't happen. You create them.", "author": "Chris Grosser"},
    {"text": "Success usually comes to those who are too busy to be looking for it.", "author": "Henry David Thoreau"},
    {"text": "Don't be afraid to give up the good to go for the great.", "author": "John D. Rockefeller"},
    {"text": "I find that the harder I work, the more luck I seem to have.", "author": "Thomas Jefferson"},
    {"text": "There are no secrets to success. It is the result of preparation, hard work, and learning from failure.", "author": "Colin Powell"},
    {"text": "The only limit to our realization of tomorrow will be our doubts of today.", "author": "Franklin D. Roosevelt"},
    {"text": "It always seems impossible until it is done.", "author": "Nelson Mandela"},
    {"text": "If you can dream it, you can do it.", "author": "Walt Disney"},
    {"text": "A river cuts through rock, not because of its power, but because of its persistence.", "author": "Jim Watkins"},
    {"text": "Action is the foundational key to all success.", "author": "Pablo Picasso"},
    {"text": "What we think, we become.", "author": "Buddha"},
    {"text": "The best time to plant a tree was 20 years ago. The second best time is now.", "author": "Chinese Proverb"},
    {"text": "Go the extra mile. It's never crowded there.", "author": "Dr. Wayne D. Dyer"},
    {"text": "Keep your face always toward the sunshine—and shadows will fall behind you.", "author": "Walt Whitman"},
    {"text": "Dream big and dare to fail.", "author": "Norman Vaughan"},
    {"text": "Act as if what you do makes a difference. It does.", "author": "William James"}
]

@app.get("/")
async def get_motivational_quote():
    quote = random.choice(quotes_db)
    return quote