/**
 * @param {string} s
 * @return {string[]}
 */
const findRepeatedDnaSequences = function(s) {
    let window = s.slice(0, 10);
    let leftWindowIdx = 0;
    const answer = new Set();

    while (leftWindowIdx <= s.length - 10) {
        for (let leftIdx = leftWindowIdx + 1; leftIdx <= s.length - 10; leftIdx++) {
            const str = s.slice(leftIdx, leftIdx + 10);
            if (window === str) {
                answer.add(window);
                break;
            }
        }
        leftWindowIdx++;
        window = s.slice(leftWindowIdx, leftWindowIdx + 10);
    }
    return [...answer];
};