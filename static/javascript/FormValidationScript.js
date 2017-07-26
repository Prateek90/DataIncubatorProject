function inputFocus(i){
    if(i.value==i.defaultValue){ i.value=""; i.style.color="#000"; }
}

function inputBlur(i){
    if(i.value==""){ i.value=i.defaultValue; i.style.color="#888"; }
}

function validateForm() {
    var x = document.getElementById("users") ;
    var y = document.getElementById("reviewCount");

    if (x.value == "") {
        alert("Users cannot be empty");
        return false;
    }else if(y.value == ""){
        alert("Reviews per video cannot be empty")
        return false;
    }else if (x.value <= 0) {
        alert("Users should be greater than zero");
        return false;
    }else if(y.value < 0){
        alert("Reviews cannot be negative")
        return false;
    }else if(x.value <= y.value){
        alert("Users should be greater than reviews per video")
        return false;
    }
    else
        return true;
}