// 1. Bi-dimensional Matrix

// Matrix generation
let matrix = new Array(input);

// Initialize each element as an array
for (let i = 0; i < matrix.length; i++) {
    matrix[i] = new Array(2);
}

// Matrix population
for (let row = 0; row < matrix.length; row++) {
    for (let column = 0; column < matrix.length; column++) {
        matrix[row][column] = 0;
    }
}

// Printing Matrix
for (let row = 0; row < matrix.length; row++) {
    console.log(`|\t${matrix[row].join('\t')}\t|`);

}
