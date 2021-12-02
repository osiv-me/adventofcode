const { dir } = require("console");
const fs = require("fs");
const { prependListener } = require("process");
function imAlsoABoat () {
    const data = fs.readFileSync("./input.txt", "utf8").split("\n");
    const boat = { forward: 0, aim: 0, depth: 0 }
    for (let i = 0; i < data.length; i++) {
        direction = data[i].split(" ")[0];
        amount = parseInt(data[i].split(" ")[1]);
        if (direction === "forward") {
            boat.forward += amount;
            boat.depth += boat.aim * amount;
        }
        else if (direction === "down") { boat.aim += amount; }
        else if (direction === "up") { boat.aim -= amount; }
    }
    return boat.forward * boat.depth;
}
console.log(imAlsoABoat());
