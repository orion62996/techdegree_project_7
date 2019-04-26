// Create meter element on password field
var passwordField = document.querySelector('#div_id_password1 div');
var passwordHelpText = document.querySelector('#div_id_password1 small');
var passwordInput = document.querySelector('[name=password1]');
var passwordMeter = document.createElement('meter');
var passwordFieldBreak = document.createElement('br');
passwordMeter.setAttribute('max', '5');
passwordField.insertBefore(passwordMeter, passwordHelpText);
passwordField.insertBefore(passwordFieldBreak, passwordMeter);

function passwordProgress(input){
  let counter = 0;
  let inputLength = input.length;

  if (inputLength >= 14) {
    counter += 1;
  }

  return counter.toString()

}

// Listen for password input on keypress
passwordInput.addEventListener('keypress', function() {
  passwordMeter.setAttribute('value', passwordProgress(passwordInput));
})
