function sendMessage() {
    let input = document.getElementById("user-input").value;
    if (input.trim() === "") return;

    let chatBox = document.getElementById("chat-box");
    chatBox.innerHTML += "<p><b>You:</b> " + input + "</p>";

    fetch("/get_response", {
        method: "POST",
        headers: {"Content-Type": "application/x-www-form-urlencoded"},
        body: "message=" + input
    })
    .then(res => res.json())
    .then(data => {
        chatBox.innerHTML += "<p><b>Bot:</b> " + data.reply + "</p>";
        speak(data.reply);
    });

    document.getElementById("user-input").value = "";
}

// Text-to-Speech
function speak(text) {
    let speech = new SpeechSynthesisUtterance(text);
    speech.lang = "en-US";
    window.speechSynthesis.speak(speech);
}

// Speech-to-Text
function startVoice() {
    let recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
    recognition.lang = "en-US";
    recognition.onresult = function(event) {
        document.getElementById("user-input").value = event.results[0][0].transcript;
        sendMessage();
    };
    recognition.start();
}
