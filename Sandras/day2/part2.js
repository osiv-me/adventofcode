
const positionMultiplier = (input) => {
    let values = require('fs').readFileSync(input, 'utf-8').split(/\r?\n/);
    let depth = 0;
    let horizontal = 0;
    let aim = 0;
    let inputLength = values.length
     for(let i =0; i < inputLength; i++) {

         if(values[i].split(' ')[0] === "forward")
         {  
            horizontal += parseInt(values[i].split(' ')[1])
            if (aim != 0) {
                depth += values[i].split(' ')[1] * aim;
            }
         }
         else if(values[i].split(' ')[0] === "down")
         {  
            aim += parseInt(values[i].split(' ')[1])
         }
         else
         {  
            aim -= parseInt(values[i].split(' ')[1])
         }
     }
     return horizontal * depth;
}

console.log(positionMultiplier("input.txt"));