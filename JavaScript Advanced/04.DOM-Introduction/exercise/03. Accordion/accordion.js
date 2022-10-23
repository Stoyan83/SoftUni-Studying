function toggle() {
    let textElement = document.getElementById('extra');
    let buttonElement = document.getElementsByClassName('button')[0];    
    if (buttonElement.textContent === 'More') {
        textElement.style.display = 'block';
        buttonElement.textContent = 'Less'
    } else if (buttonElement.textContent === 'Less') {
        textElement.style.display = 'none';
        buttonElement.textContent = 'More'
    }
}