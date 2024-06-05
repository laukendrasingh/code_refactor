// Function to add two numbers
function addTwoNumbers() {
    // Get the first number from the input
    const num1 = parseFloat(document.getElementById("num1").value);
    
    // Get the second number from the input
    const num2 = parseFloat(document.getElementById("num2").value);
    
    // Calculate the sum of the two numbers
    const sum = num1 + num2;
    
    // Display the result
    document.getElementById("result").innerText = "The sum is " + sum;
}
