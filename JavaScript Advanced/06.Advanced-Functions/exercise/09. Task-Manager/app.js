function solve() {
  // collect field values
  const input = {
    name: document.getElementById("task"),
    description: document.getElementById("description"),
    date: document.getElementById("date"),
  };

  const [_, openSection, progressSection, finishedSection] = Array.from(document.querySelectorAll("section"))
  .map((e) => e.children[1]);

  document.getElementById("add").addEventListener("click", addTask);

  function addTask(event) {
    event.preventDefault();

    // create elements
    const article = document.createElement("article");
    article.appendChild(createElement("h3", input.name.value));
    article.appendChild(createElement("p", `Description: ${input.description.value}`));
    article.appendChild(createElement("p", `Due Date: ${input.date.value}`));

    const div = document.createElement("div", "", "flex");

    const startButton = createElement("button", "Start", "green");   
    const deleteButton = createElement("button", "Delete", "red");    
    const finishButton = createElement("button", `Finish`, "orange");

    div.appendChild(startButton);
    div.appendChild(deleteButton);

    article.appendChild(div);

    // append to open section
    openSection.appendChild(article);

    // Object.values(input).forEach(i => i.value = '')
    document.getElementsByTagName("form")[0].reset();

    // add functionality for start, finish, delete
    startButton.addEventListener("click", onStart);
    finishButton.addEventListener("click", onFinish);
    deleteButton.addEventListener("click", onDelete);
    

    function onDelete() {
      article.remove();
    }

    function onStart() {
      startButton.remove();
      div.appendChild(finishButton);
      progressSection.appendChild(article);
    }

    function onFinish() {
      div.remove();
      finishedSection.appendChild(article);   
      
    }
  }

  function createElement(type, content, className) {
    const element = document.createElement(type);
    element.textContent = content;
    if (className) {
      element.className = className;
    }
    return element;
  }
}
