// Create meter element on password field

// Select all password fields
const passwordFields = document.querySelectorAll('div input[type="password"]')
// Select the second from last password field to attach the meter element
const passwordField = passwordFields[passwordFields.length - 2];
// Select the next element to place the meter
const passwordHelpText = passwordField.nextSibling;
// Create the meter element
const passwordMeter = document.createElement('meter');
// Create break for layout purposes
const passwordFieldBreak = document.createElement('br');
// Select password requirement list to allow styling
const lis = document.querySelector('small ul').children;
// Set meter attributes
passwordMeter.setAttribute('max', '5');
passwordMeter.setAttribute('value', '0');
// Insert meter and line break
passwordField.parentNode.insertBefore(passwordMeter, passwordHelpText);
passwordField.parentNode.insertBefore(passwordFieldBreak, passwordMeter);

// Functions to evaluate password input
function hasUpperCase(str) {
  return (/[A-Z]/.test(str));
}

function hasLowerCase(str) {
  return (/[a-z]/.test(str));
}

function hasNumericDigit(str) {
  return (/[0-9]/.test(str));
}

function hasSpecialCharacter(str) {
  return (/[!@#$%^&*(),.-]/.test(str))
}

// Generate password requirment score for the meter
function passwordProgress(input){
  let counter = 0;
  // Greyout password requirments that haven't been met
  for (let i = lis.length - 5; i < lis.length; i += 1) {
    lis[i].style.color = 'firebrick';
  }
  // Check that the password isn't entirely numeric
  if (hasLowerCase(input) || hasUpperCase(input) || hasSpecialCharacter(input)) {
    counter += 1;
    lis[lis.length - 5].removeAttribute('style');
  }
  // Check the length of the password
  let inputLength = input.length;
  if (inputLength >= 14) {
    counter += 1;
    lis[lis.length - 4].removeAttribute('style');
  }
  // Check that the password has uppercase and lowercase characters
  if (hasLowerCase(input) && hasUpperCase(input)) {
    counter += 1;
    lis[lis.length - 3].removeAttribute('style');
  }
  // Check that the password has a numeric digit
  if (hasNumericDigit(input)) {
    counter += 1;
    lis[lis.length - 2].removeAttribute('style');
  }
  // Check that the password has a special character
  if (hasSpecialCharacter(input)) {
    counter += 1;
    lis[lis.length - 1].removeAttribute('style');
  }
  return counter.toString()
}
// Run an initial evaluation to set requirement styling
passwordProgress(passwordField.value);


// Listen for password input on keypress
passwordField.addEventListener('keyup', function() {
  passwordMeter.value = passwordProgress(passwordField.value);
})
