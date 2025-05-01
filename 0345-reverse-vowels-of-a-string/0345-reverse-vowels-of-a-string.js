/**
 * @param {string} s
 * @return {string}
 */
const reverseVowels = function(s) {
    const strs = s.split('');
    let leftIdx = 0;
    let rightIdx = strs.length - 1;
    const vowels = new Set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']);

    while (leftIdx < rightIdx) {
        if (!vowels.has(strs[leftIdx])) {
            leftIdx++;
            continue;
        }

        if (!vowels.has(strs[rightIdx])) {
            rightIdx--;
            continue;
        }

        let temp = strs[leftIdx];
        strs[leftIdx] = strs[rightIdx];
        strs[rightIdx] = temp;

        leftIdx++;
        rightIdx--;
    }
    return strs.join('');
};