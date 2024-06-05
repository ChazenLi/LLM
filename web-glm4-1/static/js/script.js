// static/js/script.js
document.addEventListener('DOMContentLoaded', function() {
    loadChatHistory(); // 加载聊天历史
    document.getElementById('ask-form').addEventListener('submit', function(event) {
        event.preventDefault();
        var questionInput = document.getElementById('question');
        var question = questionInput.value.trim(); // 去除输入的前后空格
        questionInput.value = ''; // 清空输入框

        if (question) { // 确保不发送空消息
            displayChatMessage(question, 'user-message'); // 显示用户的问题
            saveChatToLocalStorage(question, ''); // 只保存用户的问题，AI的回复稍后保存

            fetch('/ask', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({question: question}),
            })
            .then(response => response.json())
            .then(data => {
                displayChatMessage(data.answer, 'ai-message'); // 显示AI的回答
                saveChatToLocalStorage('', data.answer); // 保存AI的回复
            })
            .catch((error) => {
                console.error('Error:', error);
                displayChatMessage('无法获取答案', 'ai-message'); // 显示错误信息
            });
        }
    });
});

function displayChatMessage(message, className) {
    var historyDiv = document.getElementById('history');
    var messageDiv = document.createElement('div');
    messageDiv.className = className;
    messageDiv.textContent = message;
    historyDiv.appendChild(messageDiv);
    historyDiv.scrollTop = historyDiv.scrollHeight; // 滚动到最新消息
}

function saveChatToLocalStorage(userMessage, aiMessage) {
    var chatHistory = localStorage.getItem('chatHistory');
    chatHistory = chatHistory ? JSON.parse(chatHistory) : [];
    if (userMessage) {
        chatHistory.push({sender: 'user', message: userMessage});
    }
    if (aiMessage) {
        chatHistory.push({sender: 'ai', message: aiMessage});
    }
    localStorage.setItem('chatHistory', JSON.stringify(chatHistory));
}

function loadChatHistory() {
    var chatHistory = localStorage.getItem('chatHistory');
    chatHistory = chatHistory ? JSON.parse(chatHistory) : [];
    chatHistory.forEach(messageData => {
        displayChatMessage(messageData.message, messageData.sender === 'user' ? 'user-message' : 'ai-message');
    });
}