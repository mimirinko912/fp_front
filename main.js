async function summation(){
    var data_1 = document.getElementById("int1").value
    var data_2 = document.getElementById("int2").value
    eel.add(data_1, data_2)(call_Back)
}

function call_Back(output){
    document.getElementById("res").textContent = output
}
