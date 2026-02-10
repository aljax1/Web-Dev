// The command “debugger”
function hello(name) {
  let phrase = `Hello, ${name}!`;

  debugger;  // <-- the debugger stops here

  say(phrase);
}
// Logging
// open console to see
for (let i = 0; i < 5; i++) {
  console.log("value,", i);
}