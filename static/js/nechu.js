let x = new Date(); 
let y = x.getFullYear();
document.getElementById("year").innerHTML=y;


function showForm() {
    document.getElementById("mytokenform").style.display = "block";
}

function closeForm() {
    document.getElementById("mytokenform").style.display = "none";
}

function logout(){
    document.location = 'login.html'
}