// nav Start
var mainListDiv = document.getElementById("mainListDiv"),
	mediaButton = document.getElementById("mediaButton");

mediaButton.onclick = function () {
	"use strict";

	mainListDiv.classList.toggle("show_list");
	mediaButton.classList.toggle("active");
};
// nav end
// api fun Start
function speak(sentence) {
	const text_speak = new SpeechSynthesisUtterance(sentence);

	text_speak.rate = 1;
	text_speak.pitch = 1;

	window.speechSynthesis.speak(text_speak);
}

window.addEventListener("load", () => {
	speak("Activating veer");

	speak("how can i help you?");
});

sendButton.addEventListener("click", () => {
	let recognization = new webkitSpeechRecognition();

	recognization.onresult = async (e) => {
		let beat = new Audio("/static/music/Scam.mp3");
		const utterance = new SpeechSynthesisUtterance();
		var transcript = e.results[0][0].transcript;
		var samllans = transcript.toLowerCase();
		userquestion.innerHTML = samllans;
		const noSpecialCharacters = samllans.replace(/[^a-zA-Z0-9 ]/g, "");
		console.log(noSpecialCharacters);

		if (transcript.includes("hello")) {
			const text = "Hello Boss.";
			utterance.text = text;
		} else if (noSpecialCharacters.includes("open youtube")) {
			window.open("https://YouTube.com", "_blank");
			const text = "Opening YouTube.";
			utterance.text = text;
		} else if (noSpecialCharacters.includes("open google")) {
			window.open("https://google.com", "_blank");
			const text = "Opening Google.";
			utterance.text = text;
		} else if (noSpecialCharacters.includes("play song")) {
			beat.play();
		} else if (noSpecialCharacters.includes("stop song")) {
			beat.pause();
		} else if (noSpecialCharacters.includes("search on google")) {
			let search = noSpecialCharacters.replace("search on google", " ");
			console.log(search);
			window.open(`https://www.google.com/search?q=${search}`, "_blank");
			const text =
				"This is what i found on internet regarding " + noSpecialCharacters;
			utterance.text = text;
		} else {
			async function postData(url = "", data = {}) {
				const response = await fetch(url, {
					method: "POST",
					headers: {
						"Content-Type": "application/json",
					},
					body: JSON.stringify(data),
				});
				return response.json();
			}

			//for api
			let result = await postData("/api", { question: noSpecialCharacters });
			// solution.innerHTML = result.answer;
			let text = result.answer;
			//for speech

			utterance.text = text;
			utterance.voice = window.speechSynthesis.getVoices()[0];
		}
		window.speechSynthesis.speak(utterance);
	};
	recognization.start();
});
// api fun End

//text start
var typed = new Typed(".auto-type", {
	strings: ["I'm Virtual Assistan", "My name is Veer"],
	typeSpeed: 150,
	backSpeed: 150,
	loop: true,
});
// text ENd
