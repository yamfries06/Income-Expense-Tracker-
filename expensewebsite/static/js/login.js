const usernameField = document.querySelector('#usernameField');
const usernameFeedBackArea = document.querySelector('.invalid_username');
const emailField = document.querySelector('#emailField');
const emailFeedBackArea = document.querySelector(".invalid_email");
const passwordField = document.querySelector("#passwordField");
const showPasswordToggle = document.querySelector(".showPasswordToggle");
const submitField = document.querySelector('input[type="submit"]');
const form = document.querySelector('#register-form');

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
                submitField.disabled = true;
                emailField.classList.add('is-invalid');
                emailFeedBackArea.style.display = 'block';
                emailFeedBackArea.innerHTML = data.email_error;
            }
            else { 
                submitField.disabled = false;
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
                submitField.disabled = true; 
                usernameField.classList.add('is-invalid');
                usernameFeedBackArea.style.display = 'block';
                usernameFeedBackArea.innerHTML = data.username_error;
            }
            else {
                submitField.disabled=false; 
            }
        });
    }
});

form.addEventListener('submit', (e) => {
    e.preventDefault(); // Prevent form from submitting by default

    // Perform any additional checks before allowing the form to submit
    const emailVal = emailField.value;
    const usernameVal = usernameField.value;
    const passwordVal = passwordField.value;

    if (emailVal.length === 0 || usernameVal.length === 0 || passwordVal.length === 0) {
        // Show error if fields are empty or validation fails
        console.log("Please fill in all fields.");
        return;
    }

    // If validation passes, manually submit the form
    form.submit(); // Use this to submit the form (loads the url of the action item of the form)
});
