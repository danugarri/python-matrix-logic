// 1. Bi-dimensional Matrix
const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout,
  });
  
  readline.question(`Type the number of rows and columns: `, input => {
  
    const size= parseInt(input)
    // Handling Type exceptions
    if (isNaN(size) || size <= 0) {
        console.log('Invalid input. Please enter a positive number.');
        readline.close();
        return;
    }
      // Matrix generation
      let matrix = new Array(size);
      
      // Initialize each element as an array
      for (let i = 0; i < matrix.length; i++) {
          matrix[i] = new Array(size);
      }
      
      // Matrix population
      for (let row of matrix) {
          for (let column = 0; column < matrix.length; column++) {
            // Random population with numbers between 0 and 9
              row[column] = Math.floor(Math.random()*10) ;
          }
      }
      
      // Printing Matrix
      for (let row of matrix) {
          console.log(`|\t${row.join('\t')}\t|`);
      
      }
    readline.close();
  });
