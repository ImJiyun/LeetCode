/**
 * @param {string} s
 * @return {string}
 */
var removeStars = function(s) {
    const arr = [];

    for (let idx = 0; idx < s.length; idx++) {
        if (s[idx] === "*") {
            arr.pop();
        } else {
            arr.push(s[idx]);
        }
    }
    return arr.join("");
};