console.log("Lynn Chanan")

function myFunction() {
    const inpCheck = document.getElementById("Email");
    if (!inpCheck.checkValidity()) {
    document.getElementById("Email").innerHTML = inpCheck.setCustomValidity("your Email has to have at least 12 characters");
    } else {
    document.getElementById("Email").innerHTML = "Input OK";
    }
}