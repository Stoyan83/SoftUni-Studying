// function solve() {
//   let [generateBtn, buyBtn] = document.querySelectorAll('button');
//   let tableBody = document.querySelector('tbody');
//   let outputFieldElement = document.querySelectorAll('textarea')[1];

//   generateBtn.addEventListener('click', generate);
//   buyBtn.addEventListener('click', buy);

//   function generate() {
//     const list = JSON.parse(document.querySelectorAll('textarea')[0].value);

//     for (const furniture of list) {
//       const row = document.createElement('tr');

//       let imageData = document.createElement('td');
//       let img = document.createElement('img');
//       img.src = furniture.img;
//       imageData.appendChild(img);
//       row.appendChild(imageData);

//       let nameData = document.createElement('td');
//       let furnitureName = document.createElement('p');
//       furnitureName.textContent = furniture.name;
//       nameData.appendChild(furnitureName);
//       row.appendChild(nameData);

//       let priceData = document.createElement('td');
//       let furniturePrice = document.createElement('p');
//       furniturePrice.textContent = furniture.price;
//       priceData.appendChild(furniturePrice);
//       row.appendChild(priceData);

//       let decData = document.createElement('td');
//       let furnitureDec = document.createElement('p');
//       furnitureDec.textContent = furniture.decFactor;
//       decData.appendChild(furnitureDec);
//       row.appendChild(decData);

//       const inputData = document.createElement('td');
//       const input = document.createElement('input');
//       input.type = 'checkbox';
//       inputData.appendChild(input);
//       row.appendChild(inputData);

//       tableBody.appendChild(row);

//     }
//   }
//   function buy() {
//     let checkBoxes = Array.from(document.querySelectorAll('input[type="checkbox"]')).filter(cb => cb.checked);

//     let bought = [];
//     let totalPrice = 0;
//     let averageDecFactor = 0;

//     for (let checkbox of checkBoxes) {
//       let [name, price, decFactor] =
//         checkbox.parentElement.parentElement.querySelectorAll('td p');

//       bought.push(name.textContent);
//       totalPrice += Number(price.textContent);
//       averageDecFactor += Number(decFactor.textContent);
//     }
//     averageDecFactor /= bought.length;

//     outputFieldElement.value =
//       `Bought furniture: ${bought.join(', ')}\n` +
//       `Total price: ${totalPrice.toFixed(2)}\n` +
//       `Average decoration factor: ${averageDecFactor}`;

//   }
// }

function solve() {
  const [generateBtn, buyBtn] = Array.from(document.querySelectorAll('button'));
  const [input, output] = Array.from(document.querySelectorAll('textarea'));
  const tbody = document.querySelector('tbody');

  generateBtn.addEventListener('click', generate);
  buyBtn.addEventListener('click', buy);

  const items = [];

  // parse input JSON and create table
  // -- find input textarea
  // -- parse JSON
  // -- for every item
  // ---- create row
  // ---- append row to table body
  function generate() {
      const data = JSON.parse(input.value);

      for (let item of data) {
          const row = document.createElement('tr');

          row.appendChild(createColumn('img', item.img));         // Image column
          row.appendChild(createColumn('p', item.name));          // Name column
          row.appendChild(createColumn('p', item.price));         // Price column
          row.appendChild(createColumn('p', item.decFactor));     // Decoration column

          // Input column
          const c5 = document.createElement('td');
          const checkbox = document.createElement('input');
          checkbox.type = 'checkbox';
          c5.appendChild(checkbox);
          row.appendChild(c5);

          tbody.appendChild(row);

          items.push({
              ...item,
              isChecked
          });

          function isChecked() {
              return checkbox.checked;
          }
      }
  }

  // find user choices and summarize purchase
  // -- find all checked boxes
  // -- for every box
  // ---- read data from parent row
  // ---- append to result
  // -- output result to textarea
  function buy() {
      let list = [];
      let total = 0;
      let decoration = 0;

      const bought = items.filter(i => i.isChecked());

      for (let item of bought) {
          list.push(item.name);
          total += Number(item.price);
          decoration += Number(item.decFactor);
      }
      decoration /= bought.length;

      output.value = [
          `Bought furniture: ${list.join(', ')}`,
          `Total price: ${total.toFixed(2)}`,
          `Average decoration factor: ${decoration}`
      ].join('\n');
  }

  function createColumn(type, content) {
      const result = document.createElement('td');
      let inner;
      if (type == 'img') {
          inner = document.createElement('img');
          inner.src = content;
      } else {
          inner = document.createElement('p');
          inner.textContent = content;
      }
      result.appendChild(inner);

      return result;
  }
}