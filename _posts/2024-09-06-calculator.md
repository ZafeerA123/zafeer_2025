---
comments: true
layout: post
title: Calculator IPYNB 
description: Grab Calculator Code and place in IPYNB
type: hacks
permalink: calculator
---

## Make a GitHub Pages Repository
Understanding Calculator code is a great way to learn JavaScript.
- Calculator was obtained from Teacher in _post directory
- Calculator also requires assets directory also obtained from Teacher
    - assets/css contains customized style for buttons
    - assets/js contains vanta animations 
- Code cell requires `%%html` at the top of cell to support css, html, script.



%%html
<style>
  .calculator-container {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    grid-gap: 10px;
    width: 200px;
  }

  .calculator-number, .calculator-operation, .calculator-clear, .calculator-equals {
    padding: 20px;
    font-size: 20px;
    background-color: #f0f0f0;
    border: 1px solid #000;
    text-align: center;
    cursor: pointer;
  }

  .calculator-output {
    grid-column: span 4; /* Make the output span across 4 columns */
    padding: 20px;
    font-size: 25px;
    background-color: #ffffff;
    color: #000000; /* Answer text color set to black */
    border: 2px solid #000000; /* Black border */
    text-align: right; /* Right-align the output */
  }

  .calculator-number {
    color: #2b2d42; /* Blueish black color */
  }

  .calculator-clear {
    background-color: #ff9999;
  }

  .calculator-operation {
    background-color: #99ccff;
  }

  .calculator-equals {
    background-color: #99ff99;
  }
</style>

<!-- Add a container for the animation -->
<div id="animation">
  <div class="calculator-container">
      <!--result-->
      <div class="calculator-output" id="output">0</div>
      <!--row 1-->
      <div class="calculator-number">1</div>
      <div class="calculator-number">2</div>
      <div class="calculator-number">3</div>
      <div class="calculator-operation">+</div>
      <!--row 2-->
      <div class="calculator-number">4</div>
      <div class="calculator-number">5</div>
      <div class="calculator-number">6</div>
      <div class="calculator-operation">-</div>
      <!--row 3-->
      <div class="calculator-number">7</div>
      <div class="calculator-number">8</div>
      <div class="calculator-number">9</div>
      <div class="calculator-operation">*</div>
      <!--row 4-->
      <div class="calculator-clear">A/C</div>
      <div class="calculator-number">0</div>
      <div class="calculator-number">.</div>
      <div class="calculator-operation">/</div> <!-- Division symbol -->
      <div class="calculator-equals">=</div>
  </div>
</div>

<!-- JavaScript (JS) implementation of the calculator. -->
<script>
  // initialize important variables to manage calculations
  var firstNumber = null;
  var operator = null;
  var nextReady = true;
  // build objects containing key elements
  const output = document.getElementById("output");
  const numbers = document.querySelectorAll(".calculator-number");
  const operations = document.querySelectorAll(".calculator-operation");
  const clear = document.querySelectorAll(".calculator-clear");
  const equals = document.querySelectorAll(".calculator-equals");

  // Number buttons listener
  numbers.forEach(button => {
    button.addEventListener("click", function() {
      number(button.textContent);
    });
  });

  // Number action
  function number (value) { // function to input numbers into the calculator
      if (value != ".") {
          if (nextReady == true) { // nextReady is used to tell the computer when the user is going to input a completely new number
              output.innerHTML = value;
              if (value != "0") { // if statement to ensure that there are no multiple leading zeroes
                  nextReady = false;
              }
          } else {
              output.innerHTML = output.innerHTML + value; // concatenation is used to add the numbers to the end of the input
          }
      } else { // special case for adding a decimal; can not have two decimals
          if (output.innerHTML.indexOf(".") == -1) {
              output.innerHTML = output.innerHTML + value;
              nextReady = false;
          }
      }
  }

  // Operation buttons listener
  operations.forEach(button => {
  button.addEventListener("click", function() {
    operation(button.textContent);
  });
});

  // Operator action
  function operation(choice) {
  if (firstNumber == null) {
    firstNumber = parseFloat(output.innerHTML); // Use parseFloat for floating-point division
    nextReady = true;
    operator = choice;
    return;
  }
  firstNumber = calculate(firstNumber, parseFloat(output.innerHTML));
  operator = choice;
  output.innerHTML = firstNumber.toString();
  nextReady = true;
}
 // Calculator
function calculate(first, second) {
  let result = 0;
  switch (operator) {
    case "+":
      result = first + second;
      break;
    case "-":
      result = first - second;
      break;
    case "*":
      result = first * second;
      break;
    case "/":
      if (second === 0) {
        result = "Error"; // Handle division by zero
      } else {
        result = first / second;
      }
      break;
    default:
      break;
  }
  return result;
}

  // Equals button listener
  equals.forEach(button => {
    button.addEventListener("click", function() {
      equal();
    });
  });

  // Equal action
  function equal () { // function used when the equals button is clicked; calculates equation and displays it
      firstNumber = calculate(firstNumber, parseFloat(output.innerHTML));
      output.innerHTML = firstNumber.toString();
      nextReady = true;
  }

  // Clear button listener
  clear.forEach(button => {
    button.addEventListener("click", function() {
      clearCalc();
    });
  });

  // A/C action
  function clearCalc () { // clears calculator
      firstNumber = null;
      output.innerHTML = "0";
      nextReady = true;
  }
  // Listen for keyboard events
  document.addEventListener("keydown", function(event) {
  // Check which key was pressed
  const key = event.key;

  // Handle numbers (0-9) and decimal point
  if (/^[0-9]$/.test(key) || key === ".") {
    number(key);
  }

  // Handle Backspace key for delete
  if (key === "Backspace") {
    deleteLastCharacter();
  }
  });

  // Function to delete the last character
  function deleteLastCharacter() {
  const currentOutput = output.innerHTML;
  if (currentOutput.length > 1) {
    output.innerHTML = currentOutput.slice(0, -1);
  } else {
    output.innerHTML = "0";
    nextReady = true;
  }
}

</script>

<!-- 
Vanta animations just for fun, load JS onto the page
-->
<script src="assets/js2/three.r119.min.js"></script>
<script src="assets/js2/vanta.halo.min.js"></script>
<script src="assets/js2/vanta.birds.min.js"></script>
<script src="assets/js2/vanta.net.min.js"></script>
<script src="assets/js2/vanta.rings.min.js"></script>

<script>
// setup vanta scripts as functions
var vantaInstances = {
  halo: VANTA.HALO,
  birds: VANTA.BIRDS,
  net: VANTA.NET,
  rings: VANTA.RINGS
};

// obtain a random vanta function
var vantaInstance = vantaInstances[Object.keys(vantaInstances)[Math.floor(Math.random() * Object.keys(vantaInstances).length)]];

// run the animation
vantaInstance({
  el: "#animation",
  mouseControls: true,
  touchControls: true,
  gyroControls: false
});
</script>