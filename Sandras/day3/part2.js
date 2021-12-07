const values = require('fs').readFileSync("input.txt", 'utf-8').split(/\r?\n/);
const positionMultiplier = (input, type) => {
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
        if(ones >= zeroes) {
            gamma.push(1);
            epsilon.push(0);
        }
        else {
            gamma.push(0);
            epsilon.push(1);
        }
     }
     if (type === "gamma") {
         return gamma.join("");
     } else {
         return epsilon.join("");
     }
}

const gamma = positionMultiplier("input.txt", "gamma")
const epsilon = positionMultiplier("input.txt", "epsilon")

const length = values[0].length;

function getCount(values) {
    const zeros = Array(length).fill(0);
    const ones = Array(length).fill(0);
  
    for (const line of values) {
      const bits = [...line];
      bits.forEach((bit, index) => {
        if (bit === "0") {
          zeros[index]++;
        } else {
          ones[index]++;
        }
      });
    }
  
    return { zeros, ones };
}


function getOxygenRating(lines, index = 0) {
    const { zeros, ones } = getCount(lines);
    let mostCommonBit = "1";
    if (zeros[index] > ones[index]) {
      mostCommonBit = "0";
    }
    const filtered = lines.filter((line) => line[index] === mostCommonBit)
    if(filtered.length === 1) {
        return filtered[0]; 
    }
    return getOxygenRating(filtered, index+1);
}

function getCO2Rating(lines, index = 0) {
    const { zeros, ones } = getCount(lines);
    let leastCommonBit = "0";
    if (zeros[index] > ones[index]) {
        leastCommonBit = "1";
    }
    const filtered = lines.filter((line) => line[index] === leastCommonBit)
    if(filtered.length === 1) {
        return filtered[0]; 
    }
    return getCO2Rating(filtered, index+1);
}

function main () {
    const oxy = getOxygenRating(values);
    const co2 = getCO2Rating(values);

    console.log(parseInt(oxy, 2) * parseInt(co2, 2));
}

main();


