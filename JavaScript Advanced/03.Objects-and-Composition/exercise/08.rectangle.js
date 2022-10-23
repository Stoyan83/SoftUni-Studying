function rectangle(width, height, color){
  const object = {width, height, color};
  object.calcArea = function(){
      return this.width * this.height;
  }
  object.color = object.color[0].toUpperCase() + object.color.slice(1);
  return object;
}


let rect = rectangle(4, 5, 'red');
console.log(rect.width);
console.log(rect.height);
console.log(rect.color);
console.log(rect.calcArea());
console.log(rectangle(4, 5, 'red'));