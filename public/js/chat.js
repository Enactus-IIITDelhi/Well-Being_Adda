const chatForm = document.querySelector("#chat-form");
const chatMessages = document.querySelector(".chat-messages");
const roomName = document.querySelector("#room-name");
const userList = document.querySelector("#users");

const queryString = window.location.search;
console.log(queryString);
const urlParams = new URLSearchParams(queryString);
const nickname = urlParams.get("nickname");
const room = urlParams.get("room");

console.log(nickname, room);

const socket = io();

//Join Chat Room
socket.emit("joinRoom", { nickname, room });

// Get room and users
socket.on("roomUsers", ({ room, users }) => {
	outputRoomName(room);
	outputUsers(users);
});

//Message from server
socket.on("message", message => {
	console.log(message);
	outputMessage(message);

	//Scroll down
	chatMessages.scrollTop = chatMessages.scrollHeight;
});

chatForm.addEventListener("submit", e => {
	e.preventDefault();

	//get message text
	const msg = e.target.elements.msg.value;

	//emit message to server
	socket.emit("chatMessage", msg);

	//clear input
	e.target.elements.msg.value = "";
	e.target.elements.msg.focus();
});

//Output message to DOM
function outputMessage(message) {
	const div = document.createElement("div");
	div.classList.add("message");
	div.innerHTML = `<p class="meta">${message.username}
	<span>${message.time}</span>
	</p>
	<p class="text">
	${message.text}
	</p>`;
	document.querySelector(".chat-messages").appendChild(div);
}

//Add room name to DOM
function outputRoomName(room) {
	roomName.innerText = room;
}

//Add users to DOM
function outputUsers(users) {
	userList.innerHTML = `
	${users.map(user => `<li>${user.nickname}</li>`).join("")}
	`;
}
