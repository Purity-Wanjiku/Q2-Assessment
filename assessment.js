// Qstn. 5
// Create a class called Product with attributes for name, price, and quantity.
// Implement a method to calculate the total value of the product (price * quantity).
// Create multiple objects of the Product class and calculate their total values.

class Product {
    constructor(name, price, quantity) {
        this.name = name;
        this.price = price;
        this.quantity = quantity;

    totalValue = () => {
            let calculateValue = this.price * this.quantity
            return calculateValue
        }
    // }
// }
   

let product1 = new Product("Banana", 50, 4);
console.log(product1.price);
let x = product1.totalValue()
console.log(x);
        
const product2 = new Product("Orange", 30, 10);
        console.log(product2.price);
        
        const product3 = new Product("Watermelon", 70, 30)
        product3.totalValue

}
}