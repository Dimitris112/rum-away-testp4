document.addEventListener('DOMContentLoaded', function() {
    var phoneInput = document.getElementById('telephone');
    if (phoneInput) {
        Inputmask("(999) 999-9999").mask(phoneInput);
    }
});
