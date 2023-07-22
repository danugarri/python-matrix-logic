const generateMatrix = (size) => {
  // Matrix generation
  let matrix = new Array(size);

  // Initialize each element as an array
  for (let i = 0; i < matrix.length; i++) {
    matrix[i] = new Array(size);
  }
  return matrix;
};
const populateMatrix = (matrix) => {
  for (let row of matrix) {
    for (let column = 0; column < matrix.length; column++) {
      // Random population with numbers between 0 and 9
      row[column] = Math.floor(Math.random() * 10);
    }
  }
};
const printMatrix = (matrix) => {
  for (let row of matrix) {
    console.log(`\n|\t${row.join("\t")}\t|`);
  }
};

const printRowsSumation = (matrix) => {
  console.log("\n\nRows Array: \n");
  // Printing Rows sumation
  let rowsSumation = 0;
  const rowsSumationArray = [];
  for (let row of matrix) {
    row.forEach((element) => {
      rowsSumation += element;
    });

    console.log(`This is the sumation for row ${matrix.indexOf(row)}: `, rowsSumation);
    rowsSumationArray.push(rowsSumation);
  }
  console.log("\nRows Array sumation:", rowsSumationArray);
};
const printColumnsSumation = (matrix) => {
  console.log("\n\nColumns Array: \n");
  // Printing Columns sumation
  const columnsSumationArray = [];
  const columnsArray = [];

  // Calculate the sum for each column
  for (let col = 0; col < matrix[0].length; col++) {
    let columnSum = 0;
    let column = [];
    for (let row = 0; row < matrix.length; row++) {
      columnSum += matrix[row][col];
      column.push(matrix[row][col]);
    }

    console.log(`This is the sumation for column ${col}: `, columnSum);
    columnsSumationArray.push(columnSum);
    columnsArray.push(column);
  }
  console.log("Array of array with each column: ", columnsArray);

  console.log("\nColumns Array Sumation:", columnsSumationArray);
};

module.exports = {
  generateMatrix,
  populateMatrix,
  printMatrix,
  printRowsSumation,
  printColumnsSumation,
};
