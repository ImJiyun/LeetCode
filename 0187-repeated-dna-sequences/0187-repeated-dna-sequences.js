/**
 * @param {string} s
 * @return {string[]}
 */
const findRepeatedDnaSequences = function(s) {
    const seen = new Set();
    const repeated = new Set();

    for (let left = 0; left <= s.length - 10; left++) {
        const substring = s.slice(left, left+10);
        if (seen.has(substring)) repeated.add(substring);
        else seen.add(substring);
    }
    return [...repeated];
};