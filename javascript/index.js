console.log("Meu código está rodando!");

let firstName = "Bruno";        
let lastName = "Silva";
let fullName = firstName + " " + lastName;
console.log(fullName);

let age = 29;
age = 29;
console.log(age);



// Tipos de dados Primitivos

let itemName = "Pen"; //    String
let itemPrice = 2 //    Number 
let itemAvailable = true //    Boolean
let itemColor = undefined //    Undefined
//itemName = null //    Null

console.log(typeof itemColor); // typeof é uma função que retorna o tipo de dado de uma variável

// tipos de dados de referência
//objects - propriedades

let pen = {
itemName: "Pen",
itemPrice: 3,
itemAvailable: true,
itemColor: "blue",   
}

pen.itemColor = "red";
console.log(pen);

// arrays
let colors = ["red", "blue", "green"];
colors[2] = "magenta"; // exemplo de como alterar um valor de um array
console.log(colors);
