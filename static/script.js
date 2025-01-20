// static/script.js
let sessionId = Math.random().toString(36).substring(7);

async function sendMessage() {
    const input = document.getElementById('message-input');
    const message = input.value;
    input.value = '';
    
    // Add user message to chat
    addMessageToChat('user', message);
    
    try {
        const response = await fetch(`/chat/${sessionId}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message }),
        });
        
        const data = await response.json();
        addMessageToChat('bot', data.message);
    } catch (error) {
        console.error('Error:', error);
        addMessageToChat('bot', 'Sorry, there was an error processing your message.');
    }
}

function addMessageToChat(sender, message) {
    const chatMessages = document.getElementById('chat-messages');
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${sender}-message`;
    messageDiv.textContent = message;
    chatMessages.appendChild(messageDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

// Pomodoro Timer
let timerInterval;
let timeLeft = 25 * 60; // 25 minutes in seconds

function startPomodoro() {
    if (!timerInterval) {
        timerInterval = setInterval(updateTimer, 1000);
    }
}

function pausePomodoro() {
    clearInterval(timerInterval);
    timerInterval = null;
}

function updateTimer() {
    const minutes = Math.floor(timeLeft / 60);
    const seconds = timeLeft % 60;
    document.getElementById('timer').textContent = 
        `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
    
    if (timeLeft === 0) {
        pausePomodoro();
        alert('Pomodoro session completed!');
        timeLeft = 25 * 60;
    } else {
        timeLeft--;
    }
}