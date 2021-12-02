const { dir } = require("console");
const fs = require("fs");
const { prependListener } = require("process");
function imABoat () {
    const data = fs.readFileSync("./input.txt", "utf8").split("\n");
    const boat = { horizontal: 0, depth: 0 }
    for (let i = 0; i < data.length; i++) {
        direction = data[i].split(" ")[0];
        amount = parseInt(data[i].split(" ")[1]);
        if (direction === "forward") { boat.horizontal += amount; }
        else if (direction === "down") { boat.depth += amount; }
        else if (direction === "up") { boat.depth -= amount; }
    }
    return boat.horizontal * boat.depth;
}
console.log(imABoat());
