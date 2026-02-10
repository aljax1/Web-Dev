//Interaction: alert, prompt, confirm

// The mini-window with the message is called a modal window. The word “modal” means that the visitor can’t interact with the rest of the page, press other buttons, etc, until they have dealt with the window. In this case – until they press “OK”.
alert("Hello");

// result = prompt(title, [default]);
let age = prompt('How old are you?', 100);

alert(`You are ${age} years old!`); // You are 100 years old!

result = confirm(question);
let isBoss = confirm("Are you the boss?");

alert( isBoss ); // true if OK is pressed