var countIncrease = (input) => {
    let values = require('fs').readFileSync(input, 'utf-8').split(/\r?\n/);
    let count = 0; 
    let inputLength = values.length
     for(let i =0; i < inputLength; i++) {
         if(parseInt(values[i]) < parseInt(values[i+1]))
         {  
            count ++;
         }
     }
     return count;
}

console.log(countIncrease("input.txt"));