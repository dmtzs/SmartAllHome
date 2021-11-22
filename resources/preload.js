window.addEventListener("DOMContentLoaded", () => {
	var { ipcRenderer } = require("electron");
	document.getElementById("close-btn").addEventListener("click", () => {
		// alert("WWWWWW");//PAra testear de ser el caso.
		ipcRenderer.send("window-close");
	});
});