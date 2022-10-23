function validate() {
  document.querySelector("#submit").type = "button";

  document.querySelector("#company").addEventListener("change", (e) => {
    if (document.querySelector("#company").checked) {
      document.querySelector("#companyInfo").style.display = "block";
    } else {
      document.querySelector("#companyInfo").style.display = "none";
    }
  });

  document.querySelector("#submit").addEventListener("click", (e) => {
    // e.preventDefault()
    let invalidFields = [];
    let username = document.querySelector("#username");
    let email = document.querySelector("#email");
    let password = document.querySelector("#password");
    let confirmPass = document.querySelector("#confirm-password");
    let checkBox = document.querySelector("#company");

    let usernamePattern = /^[A-Za-z0-9]{3,20}$/;
    let emailPattern = /^[^@.]+@[^@]*\.[^@]*$/;
    let passwordPattern = /^[\w]{5,15}$/;

    if (!usernamePattern.test(username.value)) {
      username.style.borderColor = "red";
      invalidFields.push(false);
    } else {
      username.style.borderColor = "";
      invalidFields.push(true);
    }

    if (emailPattern.exec(email.value) === null) {
      email.style.borderColor = "red";
      invalidFields.push(false);
    } else {
      email.style.borderColor = "";
      invalidFields.push(true);
    }

    if (
      password.value === confirmPass.value &&
      passwordPattern.exec(confirmPass.value) != null &&
      passwordPattern.exec(password.value) != null
    ) {
      confirmPass.style.borderColor = "";
      password.style.borderColor = "";
      invalidFields.push(true);
    } else {
      confirmPass.style.borderColor = "red";
      password.style.borderColor = "red";
      invalidFields.push(false);
    }

    if (checkBox.checked) {
      let company = document.querySelector("#companyNumber");

      if (company.value < 1000 || company.value > 9999) {
        company.style.borderColor = "red";
        invalidFields.push(false);
      } else {
        company.style.borderColor = "";
        invalidFields.push(true);
      }
    }

    if (!invalidFields.includes(false)) {
      document.querySelector("#valid").style.display = "block";
    } else {
      document.querySelector("#valid").style.display = "none";
    }
  });
}
