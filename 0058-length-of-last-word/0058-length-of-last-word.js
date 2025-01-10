/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
    let count = 0;
    let foundLastWord = false;

    for (let i = s.length - 1; i >= 0; i--) {
        if (s[i] === " ") {
            if (foundLastWord) {
                break;
            }
        } else {
            foundLastWord = true;
            count++;
        }
    }

    return count;
};
