/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    const opening = ["(", "{", "["];
    const closing = [")", "}", "]"];

    const stack = [];
    for (let char of s) {
        if (opening.includes(char)) {
            stack.push(char);
        } else if (closing.includes(char)) {
            if (opening.indexOf(stack[stack.length - 1]) === closing.indexOf(char)) {
                stack.pop();    
            } else {
                return false;
            }
        }
    }
    return stack.length === 0;
};