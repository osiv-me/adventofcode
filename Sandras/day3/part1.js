
const positionMultiplier = (input) => {
    let values = require('fs').readFileSync(input, 'utf-8').split(/\r?\n/);

    const gamma = [];
    const epsilon = [];
     for(let i =0; i < values[0].length; i++) {
        let ones = 0;
        let zeroes = 0; 
        for (let j = 0; j < values.length; j++) {
            if(values[j][i] === "1") {
                ones++;
            } else {
                zeroes++;
            }
        }
        if(ones > zeroes) {
            gamma.push(1);
            epsilon.push(0);
        }
        else {
            gamma.push(0);
            epsilon.push(1);
        }
     }
     
     const gammaInt = gamma.join("")
     const epsilonInt = epsilon.join("")
     console.log(gammaInt)
     console.log(parseInt(gammaInt, 2))
     return parseInt(epsilonInt, 2) * parseInt(gammaInt, 2);
}

console.log(positionMultiplier("input.txt"));