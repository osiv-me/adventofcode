var countIncrease = (input) => {
    let values = require('fs').readFileSync(input, 'utf-8').split(/\r?\n/);
    let count = 0; 
    let inputLength = values.length
    let a, b, c;
     for (let i =0; i < inputLength; i++) {
         if (i % 3 == 0) {

            a = parseInt(values[i]) + parseInt(values[i+1]) + parseInt(values[i+2])

            if (c < a) {
                count ++;
            }

               b = parseInt(values[i+1]) + parseInt(values[i+2]) + parseInt(values[i+3])
               c = parseInt(values[i+2]) + parseInt(values[i+3]) + parseInt(values[i+4])

            if (a < b) {
                count ++;
            }
            if (b < c) {
                count ++;
            }
      }
    }
    return count;
}

console.log(countIncrease("input.txt"));