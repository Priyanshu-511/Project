document.addEventListener('DOMContentLoaded', () => {
    const chatMessages = document.getElementById('chat-messages');
    const userInput = document.getElementById('user-input');
    const sendBtn = document.getElementById('send-btn');

    function createMessageElement(content, isUser) {
        const element = document.createElement('div');
        element.className = `p-3 rounded-lg message-enter ${
            isUser ? 'bg-blue-100 ml-6' : 'bg-gray-100 mr-6'
        }`;
        element.textContent = content;
        return element;
    }

    async function handleSend() {
        const message = userInput.value.trim();
        if (!message) return;

        // Add user message
        chatMessages.appendChild(createMessageElement(message, true));
        userInput.value = '';
        sendBtn.disabled = true;

        try {
            const response = await fetch('/chat', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ message })
            });

            const data = await response.json();

            if (!response.ok) {
                throw new Error(data.error || 'Failed to get response');
            }

            // Add AI response
            chatMessages.appendChild(createMessageElement(data.response, false));

        } catch (error) {
            const errorMessage = error.message.startsWith('Invalid API') 
                ? 'Configuration error - check server settings' 
                : error.message;
            chatMessages.appendChild(createMessageElement(`Error: ${errorMessage}`, false));
        } finally {
            sendBtn.disabled = false;
            userInput.focus();
            chatMessages.scrollTop = chatMessages.scrollHeight;
        }
    }

    // Event Listeners
    sendBtn.addEventListener('click', handleSend);
    userInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            handleSend();
        }
    });
});