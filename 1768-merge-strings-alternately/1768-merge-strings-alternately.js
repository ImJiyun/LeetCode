/**
 * @param {string} word1
 * @param {string} word2
 * @return {string}
 */
var mergeAlternately = function(word1, word2) {
    const arr = [];

    let idx = 0;
    for (let word of word1) {
        arr[idx] = word;
        idx+=2;
    }

    idx = 1;
    for (let word of word2) {
        arr[idx] = word;
        idx+=2;
    }
    return arr.join("");
};