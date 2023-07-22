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
    console.log(`|\t${row.join("\t")}\t|`);
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
  console.log("Rows Array:", rowsSumationArray);
};

module.exports = { generateMatrix, populateMatrix, printMatrix, printRowsSumation };
