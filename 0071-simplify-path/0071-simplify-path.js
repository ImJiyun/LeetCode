/**
 * @param {string} path
 * @return {string}
 */
const simplifyPath = function(path) {
    const stack = [];

    const dir = path.split("/");

    for (let item of dir) {
        if (item === "" || item === ".") continue;
        else if (item === "..") stack.pop();
        else stack.push(item);
    }

    return "/" + stack.join("/");
    
};