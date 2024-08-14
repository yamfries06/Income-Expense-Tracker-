const usernameField = document.querySelector('#usernameField');
const usernameFeedBackArea = document.querySelector('.invalid_username');
const emailField = document.querySelector('#emailField');
const emailFeedBackArea = document.querySelector(".invalid_email");
const passwordField = document.querySelector("#passwordField");
const showPasswordToggle = document.querySelector(".showPasswordToggle");

const handleToggleInput = (e) => {
    if (showPasswordToggle.textContent === 'SHOW') {
        showPasswordToggle.textContent = 'HIDE';
        passwordField.type = 'text'; //Makes password visible as 'text'
    } else {
        showPasswordToggle.textContent = 'SHOW'; 
        passwordField.type = 'password'; //Makes password hidden as 'password'
    }
}
showPasswordToggle.addEventListener('click', handleToggleInput);

emailField.addEventListener('keyup', (e) => {
    console.log('111', 111);
    const emailVal = e.target.value;

    emailField.classList.remove('is-invalid');
    emailFeedBackArea.style.display = 'none';

    if (emailVal.length > 0) {
        fetch('/authentication/validate-email', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ email: emailVal })
        })
        .then((res) => res.json())
        .then((data) => {
            console.log("data", data);
            if (data.email_error) {
                emailField.classList.add('is-invalid');
                emailFeedBackArea.style.display = 'block';
                emailFeedBackArea.innerHTML = data.email_error;
            }
        });
    }
});

usernameField.addEventListener('keyup', (e) => {
    console.log('777777', 777777);
    const usernameVal = e.target.value;

    usernameField.classList.remove('is-invalid');
    usernameFeedBackArea.style.display = 'none';

    if (usernameVal.length > 0) {
        fetch('/authentication/validate-username', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ username: usernameVal })
        })
        .then((res) => res.json())
        .then((data) => {
            console.log("data", data);
            if (data.username_error) {
                usernameField.classList.add('is-invalid');
                usernameFeedBackArea.style.display = 'block';
                usernameFeedBackArea.innerHTML = data.username_error;
            }
        });
    }
});


//piece of code runs whenever a key is released, hence, "key-up"