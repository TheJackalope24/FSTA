const url = "http://127.0.0.1:5000/register";

function clearNotice(){
    customError.innerHTML = "";
}

function validate_password(pass, confirm){
    if(pass != confirm){
        customError.innerHTML = "passwords don't match";
        return false;
    }
    return true;
}

async function createAccount(data) {
    // Default options are marked with *
    const response = await fetch(url, {
      method: 'POST', // *GET, POST, PUT, DELETE, etc.
      mode: 'cors', // no-cors, *cors, same-origin
      cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
      credentials: 'same-origin', // include, *same-origin, omit
      headers: {
        'Content-Type': 'application/json'
        // 'Content-Type': 'application/x-www-form-urlencoded',
      },
      redirect: 'follow', // manual, *follow, error
      referrerPolicy: 'no-referrer', // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
      body: JSON.stringify(data) // body data type must match "Content-Type" header
    });
    return response.json(); // parses JSON response into native JavaScript objects
  }
  

function registerAccount(){

    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    var confirm_password = document.getElementById("confirm_password").value;
    var apikey = document.getElementById("apikey").value;
    var customError = document.getElementById("customError");
    
    
    clearNotice();
    if(validate_password(password, confirm_password)){
        createAccount({"username":username, "password": password, "apikey":apikey})
            .then(data => {
                if(data["success"] === "true"){
                    window.location.href = '/';
                }
            });
    }
}