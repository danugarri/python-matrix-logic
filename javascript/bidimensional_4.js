const { printMatrix, generateMatrix, printRowsSumation, populateMatrix } = require("./utils");

// 1. Bi-dimensional Matrix
const readline = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});

readline.question(`Type the number of rows and columns: `, (input) => {
  const size = parseInt(input);
  // Handling Type exceptions
  if (isNaN(size) || size <= 0) {
    console.log("Invalid input. Please enter a positive number.");
    readline.close();
    return;
  }

  const matrix = generateMatrix(size);
  // Matrix population
  populateMatrix(matrix);
  // Printing Matrix
  printMatrix(matrix);
  // Printing rows sumation
  printRowsSumation(matrix);

  readline.close();
});
