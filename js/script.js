const loginBtn = document.getElementById('loginBtn');
const signupBtn = document.getElementById('signupBtn');
const authForm = document.getElementById('authForm');

loginBtn.addEventListener('click', () => {
    authForm.querySelector('button[type="submit"]').innerText = 'Log In';
});

signupBtn.addEventListener('click', () => {
    authForm.querySelector('button[type="submit"]').innerText = 'Sign Up';
});

// Reset function to clear the form
function resetForm() {
    authForm.reset();
}
