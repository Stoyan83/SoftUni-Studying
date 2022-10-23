class Stringer {
  constructor(string, length) {
      this.innerString = string;
      this.innerLength = Number(length);
  }
  decrease(num){
     return this.innerLength = Math.max(0, this.innerLength - num);
  }
  increase(num){
      return this.innerLength += num;
  }
  toString(){
      if(this.innerLength >= this.innerString.length){
          return this.innerString;
      }
      else {
          return `${this.innerString.substr(0, this.innerLength)}...`;
      }
  }
}



let test = new Stringer("Test", 5);
console.log(test.toString()); // Test

test.decrease(3);
console.log(test.toString()); // Te...

test.decrease(5);
console.log(test.toString()); // ...

test.increase(4);
console.log(test.toString()); // Test