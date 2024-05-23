function score(input) {
    var var0;
    if (input[8] <= 3.5) {        
        if (input[20] <= 3.5) {            
            if (input[19] <= 1.5) {                
                var0 = [0.0, 1.0];
            } else {
                if (input[21] <= 0.5) {
                    var0 = [0.0, 1.0];
                } else {
                    var0 = [1.0, 0.0];
                }
            }
        } else {
            if (input[10] <= 2.0) {
                if (input[12] <= 0.5) {
                    if (input[1] <= 2.5) {
                        var0 = [0.0, 1.0];
                    } else {
                        var0 = [1.0, 0.0];
                    }
                } else {
                    var0 = [0.0, 1.0];
                }
            } else {
                var0 = [1.0, 0.0];
            }
        }
    } else {
        if (input[19] <= 1.5) {
            if (input[10] <= 0.5) {
                var0 = [1.0, 0.0];
            } else {
                var0 = [0.0, 1.0];
            }
        } else {
            if (input[7] <= 0.5) {
                if (input[14] <= 1.5) {
                    var0 = [0.0, 1.0];
                } else {
                    if (input[17] <= 1.5) {
                        var0 = [1.0, 0.0];
                    } else {
                        if (input[19] <= 6.0) {
                            var0 = [0.0, 1.0];
                        } else {
                            var0 = [1.0, 0.0];
                        }
                    }
                }
            } else {
                if (input[9] <= 0.5) {
                    if (input[1] <= 0.5) {
                        if (input[21] <= 1.0) {
                            var0 = [0.0, 1.0];
                        } else {
                            var0 = [1.0, 0.0];
                        }
                    } else {
                        if (input[14] <= 5.5) {
                            if (input[10] <= 0.5) {
                                var0 = [0.0, 1.0];
                            } else {
                                var0 = [1.0, 0.0];
                            }
                        } else {
                            var0 = [0.0, 1.0];
                        }
                    }
                } else {
                    var0 = [1.0, 0.0];
                }
            }
        }
    }
    console.log(var0)
    return var0;
}

function submitForm() {
    var userData = {};

    for (var i = 0; i <= 21; i++) {
        var attributeName = 'attribute' + i ;
        var attributeValue = document.getElementById(attributeName).value;
        userData[i] = attributeValue;
    }    
    return userData;
}

function btnSubmit_Click() {
    const input = submitForm();
    console.log(input);
    const result = score(input);
    console.log(result);
    if(result[1] == 1)
        document.getElementById('txtMushroom').value = "Poisonous";
    else
        document.getElementById('txtMushroom').value = "Edible";
}