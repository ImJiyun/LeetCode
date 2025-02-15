/**
 * @param {string[]} operations
 * @return {number}
 */
var calPoints = function(operations) {
    const points = [];

    for (let op of operations) {
        if (op === "C") {
            if (points.length !== 0) points.pop();
        } else if (op === "D" && points.length !== 0) {
            points.push(points[points.length - 1] * 2);
        } else if (op === "+" && points.length >=2) {
            points.push(points[points.length - 1] + points[points.length - 2]);
        } else {
            points.push(Number(op));
        }
    }
    let sum = 0;
    for (let point of points) {
        sum += point;
    }
    return sum;
};