/**
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function(digits) {
    let str = "";
    for (let digit of digits) str += digit;
    let number = BigInt(str) + BigInt(1);
    number = number.toString();
    const answer = [];
    for (let num of number) answer.push(Number(num));
    return answer;
};