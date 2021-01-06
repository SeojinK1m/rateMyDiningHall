
document.addEventListener("DOMContentLoaded", () => {
    let form = document.querySelector('#form1')
    form.querySelector('input[name="schoolName"]').onkeyup = () => {
        if(form.querySelector('input[name="schoolName"]').value.includes("\'")){
            alert('alphanumeric and spaces only')
        }
        if(form.querySelector('input[name="schoolName"]').value.includes("\"")){
            alert('alphanumeric and spaces only')
        }
    }
    form.querySelector('input[name="eateryName"]').onkeyup = () => {
        if(form.querySelector('input[name="eateryName"]').value.includes("\'")){
            alert('alphanumeric and spaces only')
        }
        if(form.querySelector('input[name="eateryName"]').value.includes("\"")){
            alert('alphanumeric and spaces only')
        }
    }
});
