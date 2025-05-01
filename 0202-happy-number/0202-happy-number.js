/**
 * @param {number} n
 * @return {boolean}
 */
const isHappy = function(n) {

    function square(num) {
        const digits = String(num).split('');
        let sum = 0;
        for (let digit of digits) {
            sum += digit * digit;
        }
        return sum;
    }

    const seen = new Set();

    while (n !== 1) {
        if (seen.has(n)) return false;
        seen.add(n);
        n = square(n);
    }
    return true;
};