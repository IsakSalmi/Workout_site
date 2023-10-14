const loginForm = document.getElementById("login-form");
const loginButton = document.getElementById("login-form-submit");
const loginErrorMsg = document.getElementById("login-error-msg");
const createAccount = document.getElementById("createaccount");

createAccount.onclick = function () {
    let baseUrl = window.location.origin;
    location.href = baseUrl + '/create_account'
}
loginButton.addEventListener("click", (e) => {
    e.preventDefault();
    const username = loginForm.username.value;
    const password = loginForm.password.value;

    var xhr = new XMLHttpRequest();
    xhr.open("POST","/",true);
    xhr.setRequestHeader("Content-Type","application/json");

    xhr.onreadystatechange = function() {
        if(xhr.readyState == XMLHttpRequest.DONE && xhr.status == 200) {
            let baseUrl = window.location.origin
            window.location.replace(baseUrl + '/Log_in');
        }
        else if(xhr.readyState == XMLHttpRequest.DONE && xhr.status == 400){
            loginErrorMsg.style.opacity = 1;
        }
    };
    xhr.send(JSON.stringify(username+"/"+password));
    console.log(xhr);
})
