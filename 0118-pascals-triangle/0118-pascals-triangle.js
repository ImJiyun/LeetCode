/**
 * @param {number} numRows
 * @return {number[][]}
 */
const generate = function(numRows) {
    const number = [[1]];
    if (numRows === 1) return number;
    number.push([1, 1]);
    if (numRows === 2) return number;

    while (number.length !== numRows) {
        const nested = [1];
        const newArr = [...number[number.length-1]];
        
        for (let i = 0; i < newArr.length -1; i++) {
            nested.push(newArr[i] + newArr[i+1]);
        }
        nested.push(1);
        number.push(nested);
    }
    return number;
};