# utils/quotes.py
import random

# A simple collection of motivational quotes for students
QUOTES = [
    {
        "text": "The expert in anything was once a beginner.",
        "author": "Helen Hayes"
    },
    {
        "text": "Success is not final, failure is not fatal: it is the courage to continue that counts.",
        "author": "Winston Churchill"
    },
    {
        "text": "The beautiful thing about learning is that no one can take it away from you.",
        "author": "B.B. King"
    },
    {
        "text": "Education is not preparation for life; education is life itself.",
        "author": "John Dewey"
    },
    {
        "text": "The more that you read, the more things you will know. The more that you learn, the more places you'll go.",
        "author": "Dr. Seuss"
    },
    {
        "text": "Don't let what you cannot do interfere with what you can do.",
        "author": "John Wooden"
    }
]

def get_random_quote():
    """Return a random motivational quote"""
    quote = random.choice(QUOTES)
    return f'"{quote["text"]}" - {quote["author"]}'

def get_context_quote(context: str = None):
    """
    Get a quote based on context (e.g., 'stress', 'motivation', 'success')
    For now, returns a random quote, but you could extend this to match quotes to contexts
    """
    return get_random_quote()