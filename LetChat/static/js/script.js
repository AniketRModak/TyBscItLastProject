// nav start
var mainListDiv = document.getElementById("mainListDiv"),
	mediaButton = document.getElementById("mediaButton");

mediaButton.onclick = function () {
	"use strict";

	mainListDiv.classList.toggle("show_list");
	mediaButton.classList.toggle("active");
};
// nav end
// Example POST method implementation:
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

sendButton.addEventListener("click", async () => {
	let userQes = document.getElementById("userQes");

	let questionInput = document.getElementById("questionInput").value;
	let questionIn = questionInput.toLowerCase();
	userQes.innerHTML = questionInput;
	document.getElementById("questionInput").value = "";
	document.querySelector(".right2").style.display = "block";
	document.querySelector(".right1").style.display = "none";

	question1.innerHTML = questionIn;
	question2.innerHTML = questionIn;

	// Get the answer and populate it!
	let result = await postData("/api", { question: questionIn });
	solution.innerText = result.answer;
});

let btnchat = document.getElementById("btnchat");
btnchat.addEventListener("click", () => {
	let chat2 = document.getElementById("chat2");
	if (chat2.style.display === "none") {
		chat2.style.display = "block";
	} else {
		chat2.style.display = "none";
	}
});
