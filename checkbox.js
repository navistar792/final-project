var checkbox = document.createElement("input");
checkbox.type = 'checkbox';
checkbox.name = 'checkbox';

var label = document.createElement('label')
label.id = 'label'
label.text = {language}

document.getElementById('checkdiv').appendChild(checkbox)
document.getElementsByName('checkbox').appendChild(label)