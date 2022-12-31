// const fib = n => {
//     if (n <= 2) return 1;
//     return fib(n - 1) + fib(n - 2)
// }

const fib = (n, memo={}) => {
    if (n in memo) return memo[n];
    if (n <= 2) return 1;
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo);
    return memo[n];
}

console.log(fib(6)) // 8
console.log(fib(7)) // 13
console.log(fib(8)) // 21
console.log(fib(50)) // 12_586_269_025


// const gridTraveler = (m, n) => {
//     if (m == 1 && n == 1) return 1;
//     if (m == 0 || n == 0) return 0;
//     return gridTraveler(m - 1, n) + gridTraveler(m, n - 1);
// }

const gridTraveler = (m, n, memo={}) => {
    const key = m + ', ' + n;
    if (key in memo) return memo[key];
    if (m == 1 && n == 1) return 1;
    if (m == 0 || n == 0) return 0;
    memo[key] =  gridTraveler(m - 1, n, memo) + gridTraveler(m, n - 1, memo);
    return memo[key];
}

console.log(gridTraveler(1, 1)) // 1
console.log(gridTraveler(2, 3)) // 3
console.log(gridTraveler(3, 2)) // 3
console.log(gridTraveler(3, 3)) // 6
console.log(gridTraveler(18, 18)) // 2_333_606_220




