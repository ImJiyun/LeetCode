/**
 * @param {number[][]} grid
 * @return {number}
 */
const islandPerimeter = function(grid) {
    const dir = [[-1, 0], [1, 0], [0, -1], [0, 1]];
    let perimeter = 0;

    for (let rowIdx = 0; rowIdx < grid.length; rowIdx++) {
        for (let colIdx = 0; colIdx < grid[rowIdx].length; colIdx++) {
            if (grid[rowIdx][colIdx] === 1) {
                for (let [dr, dy] of dir) {
                    let nr = rowIdx + dr;
                    let ny = colIdx + dy;
                    if (nr < 0 || ny < 0 || nr >= grid.length || ny >= grid[rowIdx].length || grid[nr][ny] === 0) perimeter++;
                }
            }
        }
    }

    return perimeter;

};