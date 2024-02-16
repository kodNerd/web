// Event listener to the form submission
document.getElementById('student-form').addEventListener('submit', function(event) {
    // Get all form fields
    var fields = this.querySelectorAll('input, select, textarea');
    var valid = true;
    // Check if all fields are filled
    fields.forEach(function(field) {
        if (!field.value.trim()) {
            field.classList.add('is-invalid');
            valid = false;
        }
    });
    // If any field is empty, prevent form submission
    if (!valid) {
        event.preventDefault();
    }
});
