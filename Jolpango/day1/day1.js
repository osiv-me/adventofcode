const fs = require("fs");
const { prependListener } = require("process");

(function() {
    const data = fs.readFileSync("./day1input.txt", "utf8").split("\n");
    let nrOfIncreases = 0;
    for (let i = 1; i < data.length; i++) {
        if (parseInt(data[i - 1]) < parseInt(data[i])) {
            nrOfIncreases++;
        }
    }
    console.log(nrOfIncreases);
}());


(function() {
    const data = fs.readFileSync("./day1input.txt", "utf8").split("\n");
    let nrOfIncreases = 0;
    let previousSum = Infinity;
    for (let i = 0; i < data.length - 3; i++) {
        let currentSum = 0;
        for (let j = i; j < i + 3; j++) {
            currentSum += parseInt(data[j]);
        }
        if(currentSum > previousSum) {
            nrOfIncreases++;
        }
        previousSum = currentSum;
    }
    console.log(nrOfIncreases);
}());
