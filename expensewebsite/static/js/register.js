const usernameField = document.querySelector('#usernameField');

usernameField.addEventListener('keyup', (e) => {
    console.log('777777', 777777);
    const usernameVal = e.target.value; // The username the user enters

    if (usernameVal.length > 0) {
        fetch('/authentication/validate-username', {
            method: 'POST',
            body: JSON.stringify({ username: usernameVal }) // Serialize the data to JSON
        })
        .then((res) => res.json())
        .then((data) => {
            console.log("data", data);
            if(data.username_error){
                usernameField.classList.add('is-invalid'); 
            }
        }); 
    } 
});
