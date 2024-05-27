import '../css/style.css';

console.log('Hello from hello.js');

export const sayHello = () => {
    console.log('Hello from sayHello function');
}

window.sayHello = sayHello;