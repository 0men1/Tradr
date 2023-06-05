function myFunction() {
    document.getElementById("myDropdown").classList.toggle("hidden");
}

function filterFunction() {
    var input, filter, a;
    input = document.getElementById("myInput");
    filter = input.value.toUpperCase();
    div = document.getElementById("myDropdown");
    a = div.getElementsByTagName("a");

    for (var i = 0; i < a.length; i++) {
        txtValue = a[i].textContent || a[i].innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
            a[i].style.display = "";
        } else {
            a[i].style.display = "none";
        }
    }
}

function setSelectedOption(option) {
    var input = document.getElementById("myInput");
    input.value = option.textContent;
    document.getElementById("myDropdown").classList.add("hidden");
}
