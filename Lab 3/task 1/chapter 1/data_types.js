// no error
let message = "hello";
message = 123456;


alert( 1 / 0 ); // Infinity

alert( "not a number" / 2 ); // NaN, such division is erroneous

// the "n" at the end means it's a BigInt
const bigInt = 1234567890123456789012345678901234567890n;

let name = "John";
// embed a variable
alert( `Hello, ${name}!` ); // Hello, John!

// embed an expression
alert( `the result is ${1 + 2}` ); // the result is 3


typeof undefined // "undefined"

typeof 0 // "number"

typeof 10n // "bigint"

typeof true // "boolean"

typeof "foo" // "string"

typeof Symbol("id") // "symbol"

typeof Math // "object"  (1)

typeof null // "object"  (2)

typeof alert // "function"  (3)