# Testing Documentation

## Automated Testing

- **HTML Validation**: Used the [W3C HTML Validator](https://validator.w3.org/) which returned the following results:
  <div style="text-align: center; margin: 10px 0;">
      <img src="images_documentation/lighthouse_scores/html_validator.png" alt="HTML Validator Results" style="max-width: 50%; height: auto;">
  </div>

- **CSS Validation**: Used the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) which returned the following results:
  <div style="text-align: center; margin: 10px 0;">
      <img src="images_documentation/lighthouse_scores/css_validator.png" alt="CSS Validator Results" style="max-width: 50%; height: auto;">
  </div>

- **JavaScript Validation**: Used [JSHint](https://jshint.com/) to validate JavaScript code. The validation process returned a clean report compliant with ES6+ standards.

### Lighthouse scores

Lighthouse metrics were scored on Incognito Chrome

<div style="text-align: center;">
    <img src="images_documentation/lighthouse_scores/add_testimonial_lighthouse.png" alt="Add Testimonial Lighthouse Score" style="max-width: 85%; height: auto; margin: 0 10px;">
    <img src="images_documentation/lighthouse_scores/contact_lighthouse.png" alt="Contact Page Lighthouse Score" style="max-width: 85%; height: auto; margin: 0 10px;">
    <img src="images_documentation/lighthouse_scores/event_details_lighthouse.png" alt="Event Details Lighthouse Score" style="max-width: 85%; height: auto; margin: 0 10px;">
    <img src="images_documentation/lighthouse_scores/events_lighthouse.png" alt="Events Lighthouse Score" style="max-width: 85%; height: auto; margin: 0 10px;">
    <img src="images_documentation/lighthouse_scores/index_lighthouse.png" alt="Homepage Lighthouse Score" style="max-width: 85%; height: auto; margin: 0 10px;">
    <img src="images_documentation/lighthouse_scores/login_lighthouse.png" alt="Login Page Lighthouse Score" style="max-width: 85%; height: auto; margin: 0 10px;">
    <img src="images_documentation/lighthouse_scores/menu_lighthouse.png" alt="Menu Lighthouse Score" style="max-width: 85%; height: auto; margin: 0 10px;">
    <img src="images_documentation/lighthouse_scores/profile_lighthouse.png" alt="Profile Page Lighthouse Score" style="max-width: 85%; height: auto; margin: 0 10px;">
    <img src="images_documentation/lighthouse_scores/register_lighthouse.png" alt="Register Page Lighthouse Score" style="max-width: 85%; height: auto; margin: 0 10px;">
    <img src="images_documentation/lighthouse_scores/reservations_lighthouse.png" alt="Reservations Lighthouse Score" style="max-width: 85%; height: auto; margin: 0 10px;">
    <img src="images_documentation/lighthouse_scores/testimonial_details_lighthouse.png" alt="Testimonial Details Lighthouse Score" style="max-width: 85%; height: auto; margin: 0 10px;">
    <img src="images_documentation/lighthouse_scores/testimonials_lighthouse.png" alt="Testimonials Lighthouse Score" style="max-width: 85%; height: auto; margin: 0 10px;">
</div>

## Manual Testing

- **Jest**: A JavaScript testing framework used for unit and integration tests.
- **Django Test Framework**: The built-in testing framework for Django applications.

## Running Tests

Make sure to include the correct versions for both JavaScript & Django testing.

JavaScript -> `package.json`

Django -> `requirements.txt`

On the terminal write the commands below:

```bash
# For javascript
npm test

# For Django
python3 manage.py test
```

- **JavaScript Testing**: The JavaScript tests returned the following results:
  <div style="text-align: center; margin: 10px 0;">
      <img src="images_documentation/lighthouse_scores/js_tests.png" alt="JavaScript Tests Results" style="max-width: 50%; height: auto; margin: 0 10px;">
  </div>

  - **Django Testing**: The Django tests for the application returned the following results:

  - **Bar App Tests**:
    <div style="text-align: center; margin: 10px 0;">
        <img src="images_documentation/lighthouse_scores/bar_app_tests.png" alt="Bar App Test Results" style="max-width: 50%; height: auto; margin: 0 10px;">
    </div>

  - **Testimonial App Tests**:
    <div style="text-align: center; margin: 10px 0;">
        <img src="images_documentation/lighthouse_scores/testimonial_app_tests.png" alt="Testimonial App Test Results" style="max-width: 50%; height: auto; margin: 0 10px;">
    </div>
