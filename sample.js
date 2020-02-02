/*
 * Copyright
 *
 * This software
 * Capital One
 * any form
 * any manner
 *
 *
 */

//Class-based object
class Student {
    fullName: string; //Full Name
    // Supports constructor
    contructor(public firstName: string) {
        //TODO: Refactor this to
        this.fullName = firstName + " ";
    }
}

/*
 * In TypeScript,
 * This allows us to implement an interface just by having  the shape the interface requires, without an explicit implements clause.
 */
interface Person { /**/
    firstName: string;
    lastName: string;
}

/*
 * Type annotations  in  TypeScript are light
 * */
function  greeter(person : Person) { //Add a : string ' peroson'
    return "hello, " + person.firstName;
}

let user = new Student("Jane", "M.", "User");

document.body.innerHTML = greeter(user);
