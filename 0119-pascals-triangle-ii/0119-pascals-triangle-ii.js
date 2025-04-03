/**
 * @param {number} rowIndex
 * @return {number[]}
 */
const getRow = function(rowIndex) {
    const number = [[1], [1, 1]];
    if (rowIndex < 2) return number[rowIndex];
    
    let curIdx = 1;

    while (curIdx !== rowIndex) {
        const newArr = [1];
        for (let i = 0; i < number[curIdx].length - 1; i++) {
            newArr.push(number[curIdx][i] + number[curIdx][i+1]);
        }
        newArr.push(1);
        number.push(newArr);
        curIdx++;
    }
    return number.pop();
};