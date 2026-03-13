function square(n) {
  return n * n;
}

const defaultMessage = "you didnt add something to the printSomething function...";

function printSomething(theSomething = defaultMessage) {
  if(theSomething != defaultMessage ) {
    return console.log(theSomething);
  }

  return console.error(theSomething);

}

printSomething("wow");
printSomething();
