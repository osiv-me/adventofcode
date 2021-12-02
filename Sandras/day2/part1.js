
const positionMultiplier = (input) => {
    let values = require('fs').readFileSync(input, 'utf-8').split(/\r?\n/);
    let forward = 0; 
    let depth = 0;
    let inputLength = values.length
     for(let i =0; i < inputLength; i++) {

         if(values[i].split(' ')[0] === "forward")
         {  
            forward += parseInt(values[i].split(' ')[1])
         }
         else if(values[i].split(' ')[0] === "down")
         {  
            depth += parseInt(values[i].split(' ')[1])
         }
         else
         {  
            depth -= parseInt(values[i].split(' ')[1])
         }
     }
     return forward * depth;
}

console.log(positionMultiplier("input.txt"));