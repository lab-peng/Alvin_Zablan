// memoization vs tabulation

const fib = (n) => {
    const table = Array(n + 1).fill(0)
    table[1] = 1
    for (let i = 2; i < n+1; i++) {
        table[i] = table[i-1] + table[i-2]
    }
    return table[n]
}

console.log(fib(6)) // 8
console.log(fib(7)) // 13
console.log(fib(8)) // 21
console.log(fib(50)) // 12_586_269_025

const gridTraveler = (m, n) => {
    const table = Array(m).fill(0).map(() => Array(n).fill(1));
    for (let i = 1; i < m; i++) {
        for (let j = 1; j < n; j++) {
            table[i][j] = table[i-1][j] + table[i][j-1];
            // console.log(table);
        }
    }
    return table[m-1][n-1]

}

console.log(gridTraveler(1, 1)) // 1
console.log(gridTraveler(2, 3)) // 3
console.log(gridTraveler(3, 2)) // 3
console.log(gridTraveler(3, 3)) // 6
console.log(gridTraveler(18, 18)) // 2_333_606_220