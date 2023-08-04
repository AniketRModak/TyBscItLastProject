var mainListDiv = document.getElementById("mainListDiv"),
	mediaButton = document.getElementById("mediaButton");

mediaButton.onclick = function () {
	"use strict";

	mainListDiv.classList.toggle("show_list");
	mediaButton.classList.toggle("active");
};

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

submitbtn.addEventListener("click", async (e) => {
	const loadingGif = document.getElementById("loadingGif");
	const tempbg = document.getElementById("tempbg");
	loadingGif.style.display = "block";
	tempbg.style.display = "none";
	e.preventDefault();

	const promptTxt = imgprompt.value;

	let result = await postData("/api", { question: promptTxt });

	loadingGif.style.display = "none";

	const images = result.answer;
	console.log(result.answer);
	const container = document.querySelector(".imageCont");
	let totalHtml = "";

	images.forEach((image) => {
		let html = `<div class="colum">
            <img width="340" src="${image.url}" class="img-responsive">
        </div>`;
		totalHtml += html;
	});
	container.innerHTML = totalHtml;
});
