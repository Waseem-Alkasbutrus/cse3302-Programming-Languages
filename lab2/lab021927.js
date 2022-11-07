// 1
const inputtable = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
console.log('Question 1:')
console.log(inputtable)

// 2
const fiveTable = inputtable.map(x => x * 5)
const thirteenTable = inputtable.map(x => x * 13)
const squaresTable = inputtable.map(x => x * x)
console.log('Question 2:')
console.log(fiveTable)
console.log(thirteenTable)
console.log(squaresTable)

// 3
const startingNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
const multiplesOfFive = startingNumbers.map(x => x * 5)
const oddMultiplesOfFive = multiplesOfFive.filter(x => (x % 2 == 1))
console.log('Question 3:')
console.log(oddMultiplesOfFive)

// 4
const multiplesOfSeven = startingNumbers.map(x => x * 7)
const evenMultiplesOfSeven = multiplesOfSeven.filter(x => (x % 2 == 0) && (x <= 100))
console.log('Question 4:')
console.log(evenMultiplesOfSeven)

// 5
function cylinder_volume(r) {
    return function (h) {
        return r * r * h * 3.14
    }
}

const curriedFunction = cylinder_volume(5)
let a = curriedFunction(10)
let b = curriedFunction(17)
let c = curriedFunction(11)
console.log('Question 5:')
console.log(a)
console.log(b)
console.log(c)

// 6
makeTag = function (beginTag, endTag) {
    return function (textcontent) {
        return beginTag + textcontent + endTag;
    }
}

const tableBody = makeTag("<td>", "</td>")
const tableRow = makeTag("<tr>", "</tr>")
const table = makeTag("<table>", "</table>")

const tableHeaderList = [
    ["Waseem", "Alkasbutrus", "20"],
    ["John", "Doe", "40"],
    ["Jane", "Doe", "34"],
    ["Peter", "Parker", "18"]
]

const tableHTML = table(
    tableHeaderList.map(
        row => tableRow(
            row.map(cell => tableBody(cell)).join('')
        )
    ).join('')
)

console.log('Question 6:')
console.log(tableHTML)

// 7 (extra credit)
function multiplesOf(multiple) {
    const startingNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]    
    const multiples = startingNumbers.map(x => x * multiple)
    return function filterCondition(a) {
        return multiples.filter(a)
    }
}

const five = multiplesOf(5)
console.log("Question 7 (extra credit)")
console.log(five(x => (x%2 == 1)))