const createAccount = document.getElementById("createacc-form-submit");
const createAccForm = document.getElementById("createacc-form")
createAccount.addEventListener("click", (e) => {
    e.preventDefault();
    const username = createAccForm.username.value;
    const password = createAccForm.password.value;
    const repassword = createAccForm.checkpassword.value;

    if (password !== repassword) {
        console.log("Passwords do not match!");
        return;
    }

    var xhr = new XMLHttpRequest();
    xhr.open("POST","/create_account",true);
    xhr.setRequestHeader("Content-Type","application/json");

    xhr.onreadystatechange = function() {
        if(xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
            let baseUrl = window.location.origin
            window.location.replace(baseUrl + '/');
        }
        else if(xhr.readyState === XMLHttpRequest.DONE && xhr.status === 400){ }
    };

    xhr.send(JSON.stringify(username+" "+password+" "+repassword));
    console.log(xhr);

})