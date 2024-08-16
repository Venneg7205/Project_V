// Регистрация пользователя
document.getElementById('register-form').addEventListener('submit', async (e) => {
    e.preventDefault();

    const username = document.getElementById('reg-username').value;
    const email = document.getElementById('reg-email').value;
    const password = document.getElementById('reg-password').value;

    const response = await fetch('http://localhost:5000/api/register', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, email, password })
    });

    const data = await response.json();

    if (response.ok) {
        window.location.href = 'chat.html';
    } else {
        document.getElementById('message').textContent = `Registration failed: ${data.message}`;
    }
});

// Логин пользователя
document.getElementById('login-form').addEventListener('submit', async (e) => {
    e.preventDefault();

    const email = document.getElementById('login-email').value;
    const password = document.getElementById('login-password').value;

    const response = await fetch('http://localhost:5000/api/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email, password })
    });

    const data = await response.json();

    if (response.ok) {
        window.location.href = 'chat.html';
    } else {
        document.getElementById('message').textContent = `Login failed: ${data.message}`;
    }
});

// Отправка вопроса в чат
if (document.getElementById('chat-form')) {
    document.getElementById('chat-form').addEventListener('submit', async (e) => {
        e.preventDefault();

        const question = document.getElementById('chat-input').value;
        const response = await fetch('http://localhost:5000/api/ask', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ question })
        });

        const data = await response.json();

        const chatOutput = document.getElementById('chat-output');
        chatOutput.innerHTML += `<p><strong>You:</strong> ${question}</p>`;
        chatOutput.innerHTML += `<p><strong>AI:</strong> ${data.answer}</p>`;

        document.getElementById('chat-input').value = '';
        chatOutput.scrollTop = chatOutput.scrollHeight;
    });
}
