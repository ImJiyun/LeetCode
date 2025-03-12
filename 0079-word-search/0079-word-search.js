/**
 * @param {character[][]} board
 * @param {string} word
 * @return {boolean}
 */
const exist = function(board, word) {
    const rows = board.length;
    const cols = board[0].length;
    const dir = [[-1, 0], [1, 0], [0, -1], [0, 1]];
    const visited = Array.from({ length: rows }, () => Array(cols).fill(false));

    function dfs(idx, r, c) {
        if (idx === word.length) return true; 
        if (r < 0 || c < 0 || r >= rows || c >= cols || visited[r][c] || board[r][c] !== word[idx]) return false;

        visited[r][c] = true;
        for (let [dr, dc] of dir) {
            if (dfs(idx + 1, r + dr, c + dc)) return true;
        }
        visited[r][c] = false; 

        return false;
    }

    for (let r = 0; r < rows; r++) {
        for (let c = 0; c < cols; c++) {
            if (board[r][c] === word[0] && dfs(0, r, c)) {
                return true;
            }
        }
    }
    return false;
};
