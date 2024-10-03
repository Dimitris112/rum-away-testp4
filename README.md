<h1 align="center">🥃 <a href="https://rum-away-testp4-d410f580ea18.herokuapp.com/">Rum Away Bar</a> 🥃</h1>

![Responsiveness](images_documentation/lighthouse_scores/responsive.png)

## The purpose of this project is a web based application designed to streamline the operations of a bar called **Rum Away Bar**, providing both customers and administrator with a platform to manage reservations, events and iteractions. It features a user friendly interface for users to browse events, make reservations and view testimonials while also offering an admin panel to control various aspects.

### Key features:

- Authentication & Authorization: Secure user authentication and authorization built using Django allauth, allowing users to register, login and manage their accounts.
- Reservation System: Users can create and manage their reservations while preventing them on multiple bookings for the same date.
- Event Management: Admin has full control over event creation and management via the admin panel, including the ability to create - edit - delete events.
- User Profiles & API Integration: API endpoints allow for dynamic content handling, such as profile management and profile images stored secured using Cloudinary.
- Media management: Integration with Cloudinary allows users and admin to upload, store, manage images efficiently.
- Testimonials Section: A dedicated area for users to view and interact with testimonials from other users.
- The platform is built using Django and PostgreSQL.

## [User Stories](https://github.com/users/Dimitris112/projects/5/views/1)

### 1. User Registration

- **As a** new user, **I want** an easy account setup **to** enjoy personalized features.
- **Acceptance**: Users enter email, username, and password. Errors show for taken usernames/emails.

### 2. User Profile Edit

- **As a** user, **I want** to update my profile **to** keep my details current.
- **Acceptance**: Users change name, email, or password. Changes save instantly.

### 3. Comment on Testimonials

- **As a** registered user, **I want** to comment on testimonials **to** share my thoughts.
- **Acceptance**: Users comment on testimonials, visible after submission. Errors appear for guideline violations.

### 4. Filter Testimonials

- **As a** user, **I want** to filter testimonials **to** find what interests me.
- **Acceptance**: Users filter testimonials by category, with options to reset filters.

### 5. Admin Dashboard Access

- **As an** admin, **I want** dashboard access **to** manage testimonials efficiently.
- **Acceptance**: Admins see user stats, testimonial counts, and can manage testimonials and accounts.

### 6. User Responsive Design

- **As a** user, **I want** a device-friendly website **for** a smooth experience on any device.
- **Acceptance**: The layout adjusts for mobile, keeping navigation user-friendly.

### 7. Admin Testimonial Analytics

- **As an** admin, **I want** to see testimonial analytics **to** gauge engagement and popularity.
- **Acceptance**: An analytics page shows total views and comments for each testimonial.

### 8. User Comment Character Limit

- **As a** user, **I want** a comment character limit **to** keep discussions concise.
- **Acceptance**: A 500-character limit is shown, with warnings as it approaches. A counter tracks remaining characters.

### 9. User Testimonial Details

- **As a** user, **I want** detailed testimonial info **to** better understand the context.
- **Acceptance**: Clicking a testimonial leads to a detail page with full text, user info, and comments.

### 10. User Account Deletion

- **As a** user, **I want** to delete my account **to** remove my data if I no longer want the service.
- **Acceptance**: A deletion option in settings, confirming without prompts for immediate removal.

### 11. User Edit Comment

- **As a** user, **I want** to edit my comments **to** correct mistakes.
- **Acceptance**: An "Edit" button allows modifications, with changes reflected instantly.

### 12. User Display Comments

- **As a** user, **I want** to see all comments on a testimonial detail page **to** view community feedback.
- **Acceptance**: The detail page shows all comments, sorted by most recent.

### 13. User Profile Customization

- **As a** user, **I want** to customize my profile **to** express my personality.
- **Acceptance**: Users upload a profile picture, change display name, and add a bio, with instant saving.

## User Experience

### Typography & Color scheme

The project uses Roboto and Lato fonts for a clean and modern design. The color scheme consists of:

    Primary Color: #c95a2a (warm orange) 🟠
    Secondary Color: #6d4c41 (rich brown) 🟤
    Background: #f8f2e6 (light beige) 🟡

This palette creates an inviting and cozy atmosphere, fitting for a bar setting, with subtle highlights and shadows adding depth to the design.

### Agile Planning

This project was developed using agile methodologies over a span of approximately four weeks. The development process included the use of various labels such as "documentation" - "good first issue" - "enhancement" to organize tasks and streamline progress. An MVP (Minimum Viable Product) milestone was established to focus on delivering essential features. Each user story is accompanied by a comprehensive set of acceptance criteria, ensuring that all functionalities, including those for the 404 and 505 error pages, are well defined and meet completion standards. For more details, you can view the kanban board [here](https://github.com/users/Dimitris112/projects/5).

<div style="text-align: center;">
    <img src="images_documentation/gifs/kanban.png" alt="Kanban board" style="max-width: 55%; height: auto;">
</div>

### Features

<details>
    <summary><strong>Navigation & Footer</strong></summary>
    <p>
        The navigation bar displays the <strong>Rum Away Bar</strong> text, which serves as an index anchor. The <strong>Home</strong> - <strong>Profile</strong> links, for non-logged-in users, also include the <strong>Register</strong> - <strong>Login</strong> links. For logged-in users, the Register and Login links are replaced with the <strong>Logout</strong> option.
    </p>
    <p>
        The footer displays <em>© 2024 Rum Away Bar. Educational project by Dimitris</em> followed by <a href="https://www.linkedin.com/in/dimitrios-thlivitis/" target="_blank">My LinkedIn</a> and <a href="https://github.com/Dimitris112" target="_blank">My GitHub</a>.
    </p>
    <p>
        The <code>base.html</code> is extended throughout the platform; therefore, both elements can be seen on all pages because this is where they are “formed.”
    </p>
    <ul>
        <li>Clicking the <em>Rum Away Bar</em> and <em>Home</em> takes the users back to the homepage (index.html).</li>
        <li>Clicking the <em>Profile</em> takes the users to the profile page (profile.html).</li>
        <li>Clicking the <em>Register</em> takes the users to the register page (signup.html).</li>
        <li>Clicking the <em>Login</em> takes the users to the login page (login.html).</li>
        <li>Clicking the <em>Logout</em> takes the users to the logout page (logout.html).</li>
    </ul>
    <div style="text-align: center;">
        <div style="display: inline-block; margin: 10px;">
            <img src="images_documentation/gifs/navbar_loggedin.png" alt="Navbar while logged in" style="max-width: 55%; height: 65px;">
            <img src="images_documentation/gifs/navbar_loggedout.png" alt="Navbar while logged out" style="max-width: 55%; height: 65px;">
        </div>
    </div>
    <div style="text-align: center;">
        <img src="images_documentation/gifs/footer.png" alt="Footer with a text and two icons" style="max-width: 55%; height: auto; margin: 10px;">
    </div>
</details>

<br>

<details>
  <summary><strong>Home Page</strong></summary>
  <p>
    When the users land on the platform, they see the <strong>Home</strong> page. It starts with a carousel of three images, each containing explanatory text and an anchor button leading to the correct page.
  </p>
  <h4>Images</h4>
  <ol>
    <li>
      <strong>"Featured Cocktail"</strong> - Try our special cocktail of the month - 
      <em>Discover more</em> (button) which leads to the <strong><a href="https://rum-away-testp4-d410f580ea18.herokuapp.com/menu/">menu</a></strong> page.
    </li>
    <li>
      <strong>"Weekend Special"</strong> - Enjoy our weekend special with friends - 
      <em>See specials</em> (button) which leads to the <strong><a href="https://rum-away-testp4-d410f580ea18.herokuapp.com/events/">events</a></strong> page.
    </li>
    <li>
      <strong>"Happy Hour"</strong> - Join us for happy hour every evening - 
      <em>Join us</em> (button) which leads to the <strong><a href="https://rum-away-testp4-d410f580ea18.herokuapp.com/events/4/">happy hour details</a></strong> page.
    </li>
  </ol>
  <p>
    Scrolling a bit further down, users see the welcoming title <strong><em>Welcome to the Rum Away Bar</em></strong> and an image of the hall along with two buttons:
  </p>
  <ul>
    <li><strong><a href="https://rum-away-testp4-d410f580ea18.herokuapp.com/menu/">view our menu</a></strong> leads the users to the menu page.</li>
    <li><strong><a href="https://rum-away-testp4-d410f580ea18.herokuapp.com/contact/">contact us</a></strong> leads the users to the contact page.</li>
  </ul>
  <p>
    Next, they see <strong><em>Share your Experience!</em></strong> along with a catchy phrase and a <strong><a href="https://rum-away-testp4-d410f580ea18.herokuapp.com/testimonials/">Read testimonials</a></strong> button, which directs users to the testimonial page.
  </p>
  <p>
    Following that comes the <strong><em>Upcoming Events</em></strong>. Two events are active at the moment: one weekly (every Friday at 8 PM) and one daily (5-7 PM). Each event card contains a description and a "Learn more" button:
  </p>
  <ul>
    <li>The first is the <strong><em>Live music night</em></strong>.</li>
    <li>The second is the <strong><em>Happy Hour</em></strong>.</li>
  </ul>
  <p>
    Beneath them is another button, <strong><a href="https://rum-away-testp4-d410f580ea18.herokuapp.com/events/">View All Events</a></strong>, which takes users to the events list.
  </p>
  <p>
    Then there's a small paragraph of <strong><em>Our menu</em></strong> with a catchy phrase and a <strong><a href="https://rum-away-testp4-d410f580ea18.herokuapp.com/menu/">View full menu</a></strong> button.
  </p>
  <p>
    Below that is the <strong><em>Contact Us</em></strong>, following the same format as the rest, with a catchy phrase and a <strong><a href="https://rum-away-testp4-d410f580ea18.herokuapp.com/contact/">Contact</a></strong> button.
  </p>
  <p>
    Finally, users see the footer, which has a dark grey background with white text and two social icons.
  </p>
  <div style="text-align: center;">
      <img src="images_documentation/gifs/home.gif" alt="Home gif" style="max-width: 85%; height: auto;">
  </div>
</details>

<br>

<details>
  <summary><strong>Sign Up Page</strong></summary>
  <p>
    On the <strong>Sign Up</strong> page, users who already have an account can click the <em>Sign in</em> link to be redirected to the <strong>Login</strong> page.
  </p>
  <p>
    To make reservations or add testimonials, users must first create a profile, which is done through the <strong><em>Sign Up</em></strong> page.
  </p>
  <h4>The form includes the following inputs:</h4>
  <ul>
    <li><strong>Username</strong> (required)</li>
    <li><strong>Email</strong> (optional)</li>
    <li><strong>Password</strong> (required)</li>
    <li><strong>Confirm Password</strong> (required)</li>
  </ul>
  <p>
    By default, password fields are masked with <code>*</code> symbols and a 🙈 icon to indicate privacy. Users can toggle the visibility of their password by clicking the <code>👁️</code> icon.
  </p>
  <h4>Password requirements:</h4>
  <ul>
    <li>Must not be too similar to other personal information.</li>
    <li>Must contain at least 8 characters.</li>
    <li>Must not be a commonly used password.</li>
    <li>Must not be entirely numeric.</li>
  </ul>
  <p>
    If any of these conditions are not met, specific error messages will be displayed under the respective input field.
  </p>
  <p>
    After completing the form, users can click the <strong>Sign Up</strong> button and will be redirected to the <strong>Home</strong> page with a message displayed:  
    <strong>"Successfully signed up as (username)."</strong>
  </p>
  <div style="text-align: center;">
      <img src="images_documentation/gifs/sign_up.gif" alt="Sign up gif" style="max-width: 85%; height: auto;">
  </div>
</details>

<br>

<details>
  <summary><strong>Sign In Page</strong></summary>
  <p>
    On the <strong>Sign In</strong> page, users can enter their credentials to access their account.
  </p>
  <h4>The form includes the following inputs:</h4>
  <ul>
    <li><strong>Username</strong> (required)</li>
    <li><strong>Password</strong> (required)</li>
  </ul>
  <p>
    Additionally, there is a <em>Forgot your password?</em> link to help users reset their password if needed, and a <strong>Remember Me</strong> checkbox to keep users signed in across sessions.
  </p>
  <p>
    Once users complete the form and click the <strong>Sign In</strong> button, they will be redirected to the <strong>Home</strong> page with a message displayed:  
    <strong>"Successfully signed in as (username)."</strong>
  </p>
  <div style="text-align: center;">
      <img src="images_documentation/gifs/login.png" alt="Sign in png" style="max-width: 85%; height: auto;">
  </div>
</details>

<br>

<details>
  <summary><strong>Profile Page</strong></summary>
  
  <p>
    At the top of the <strong>Profile</strong> page, users will see their profile card, which includes the following details:
  </p>
  <ul>
    <li><strong>Profile Image</strong>: Displays a default "nobody image" if no image is uploaded.</li>
    <li><strong>Username</strong></li>
    <li><strong>First Name</strong></li>
    <li><strong>Last Name</strong></li>
    <li><strong>Email</strong></li>
    <li><strong>Bio</strong></li>
    <li><strong>Member Since</strong>: The date the user joined.</li>
  </ul>

  <hr>

  <p>
    Below the profile card is the <strong>My Information</strong> section, where users can update their details. This section includes a form with the following inputs:
  </p>
  <ul>
    <li><strong>First Name</strong> (required)</li>
    <li><strong>Last Name</strong> (required)</li>
    <li><strong>Email</strong>: Must be valid, otherwise, an error message will be displayed.</li>
    <li>
      <strong>Profile Image</strong>: Upload options allow formats in <code>.png</code>, <code>.jpg</code>, <code>.jpeg</code>, <code>.gif</code>, and <code>.webp</code>, with a file size limit of 8MB. If the size or format is invalid, an error message will appear.
    </li>
    <li><strong>Bio</strong>: A text area where users can enter up to <strong>50 characters</strong>.</li>
  </ul>
  
  <p>
    At the bottom of the form are the following buttons:
  </p>
  <ul>
    <li><strong>Save Changes</strong></li>
    <li><strong>Delete Account</strong></li>
    <li><strong>Reset Profile Picture</strong></li>
  </ul>
  
  <p>
    Additionally, there is a text below the buttons:  
    <strong>Need help? <a href="https://rum-away-testp4-d410f580ea18.herokuapp.com/contact/#contact-form">Contact support</a></strong> — Clicking the link takes users to the Contact page.
  </p>

  <hr>

  <h4>My Testimonials</h4>
  
  <p>
    If the user has not added any testimonials, the following message is displayed:  
    <strong>"No testimonials yet. Share your experiences to inspire others!"</strong>
  </p>
  
  <p>
    If the user has submitted testimonials, they will be displayed in individual cards, showing:
  </p>
  <ul>
    <li><strong>Testimonial Content</strong></li>
    <li><strong>Submitted On</strong> date</li>
    <li><strong>Edited On</strong> date (if applicable)</li>
    <li><strong>Rating</strong></li>
    <li>
      <strong>View Testimonial Details</strong>, <strong>Edit</strong>, and <strong>Delete</strong> buttons
    </li>
  </ul>
  
  <p>
    Below the testimonials, users will find the <strong>Share Your Experience</strong> section:
    <strong>"Your voice matters! Each testimonial helps create a welcoming atmosphere for new guests."</strong>
  </p>
  
  <p>
    A button labeled <strong>"Add Your Testimonial"</strong> leads users to the testimonials page to submit a new testimonial.
  </p>

  <hr>

  <h4>Upcoming Reservations</h4>
  
  <p>
    If no reservations have been made, the page will display:  
    <strong>No upcoming reservations.</strong>
  </p>
  
  <p>
    If the user has made reservations, each reservation will be shown in a card format with:
  </p>
  <ul>
    <li><strong>Date</strong></li>
    <li><strong>Time</strong></li>
    <li><strong>Number of Guests</strong></li>
    <li><strong>Hall</strong></li>
  </ul>
  
  <p>
    The card also includes <strong>Edit</strong> and <strong>Delete</strong> buttons for managing reservations.
  </p>
  
  <p>
    Below this section is a prompt for making new reservations:  
    <strong>Ready to Reserve? Make your reservation today to ensure you get the best experience!</strong>
  </p>
  
  <p>
    The <strong>Make a Reservation</strong> button takes users to the Contact page, specifically targeting the reservation section.
  </p>

  <div style="text-align: center;">
      <img src="images_documentation/gifs/profile_testimonial_reservation.gif" alt="Profile, testimonial, and reservation gif" style="max-width: 85%; height: auto;">
  </div>
</details>

<br>

<details>
  <summary><strong>Menu Page</strong></summary>
  
  <p>
    The <strong>Menu</strong> page invites users to explore a wide selection of drinks with the heading:  
    <strong>Explore our menu</strong>
  </p>
  
  <p>
    Below the heading, users can select a drink category from the dropdown labeled:  
    <strong>Select a category</strong>
  </p>
  <p>
    The available categories are:
  </p>
  <ul>
    <li><strong>Wines</strong></li>
    <li><strong>Beer</strong></li>
    <li><strong>Whiskey</strong></li>
    <li><strong>Vodka</strong></li>
    <li><strong>Rum</strong></li>
    <li><strong>Cocktails</strong></li>
  </ul>

  <p>
    When users click on a category, a modal opens, displaying a catalogue of drinks for that category. Up to <strong>4 drinks</strong> are shown per page, each represented by its own card, which includes:
  </p>
  <ul>
    <li><strong>A Photo</strong> of the drink</li>
    <li><strong>A brief Description</strong></li>
    <li><strong>The Price</strong></li>
    <li><strong>A View Details</strong> button, which opens another modal with more information.</li>
  </ul>

  <p>
    In the <strong>Cocktails</strong> category, the <strong>View Details</strong> modal provides an extra section describing the <strong>Ingredients</strong> of each cocktail, offering users additional insight into the drink.
  </p>

  <div style="text-align: center;">
      <img src="images_documentation/gifs/menu.gif" alt="Menu gif" style="max-width: 85%; height: auto;">
  </div>
</details>

<br>

<details>
  <summary><strong>Contact Page</strong></summary>

  <p>
    The <strong>Contact</strong> page begins with a warm welcome:  
    <strong>We'd love to hear from you!</strong>
  </p>

  <h3>Contact Form</h3>
  <p>
    Users can reach out to the admin by filling in the following fields:
  </p>
  <ul>
    <li><strong>Your Name</strong> (required)</li>
    <li><strong>Your Email Address</strong> (required)</li>
    <li><strong>Phone Number</strong> (optional, masked format)</li>
    <li><strong>Your Message</strong> (required)</li>
  </ul>
  <p>
    A button labeled <strong>"Send Your Message"</strong> is available for submitting the form.
  </p>

  <h3>Reservation Form</h3>
  <p>
    Below the contact form, users can make a reservation by filling out the reservation form. The form includes:
  </p>
  <ul>
    <li><strong>Date of Reservation</strong>: Users cannot select past dates or dates more than <strong>6 months</strong> in advance. Error messages will appear if these conditions aren't met.</li>
    <li><strong>Time of Reservation</strong>: The time slots start from <strong>16:00</strong> and end at <strong>02:00</strong>, with intervals of <strong>5 minutes</strong>.</li>
    <li><strong>Number of Guests</strong>: This field allows users to specify the size of their party.</li>
    <li><strong>Select Location</strong>: Users can choose the preferred location for the reservation.</li>
    <li><strong>Indoor or Outdoor</strong>:
      <ul>
        <li>Indoor reservations allow up to <strong>70 guests</strong>.</li>
        <li>Outdoor reservations allow up to <strong>120 guests</strong>.</li>
      </ul>
      The form dynamically calculates the <strong>available spots</strong> based on the number of guests the user selects. If the user exceeds the available spots, an error message will be shown.
    </li>
    <li><strong>Special Requests</strong>: A text area for any additional requests.</li>
  </ul>
  <p>
    A <strong>Submit Reservation</strong> button is provided for completing the reservation.
  </p>

  <h3>Bar Showcase</h3>
  <p>
    Next, the page features some catchy paragraphs about the bar, followed by a <strong>carousel</strong> showcasing images:
  </p>
  <ul>
    <li><strong>Indoor Hall</strong>: A carousel with 3 images of the indoor area.</li>
    <li><strong>Outdoor Hall</strong>: A carousel with 3 images of the outdoor area.</li>
  </ul>

  <h3>Find Us Here</h3>
  <p>
    At the bottom of the page, users can find contact details and location information:
  </p>
  <ul>
    <li><strong>Phone</strong>: +123 456 7890</li>
    <li><strong>Email</strong>: contact@rumaway.com</li>
    <li><strong>Location</strong>: Area 51, Nevada</li>
  </ul>
  <p>
    The <strong>Google Maps</strong> integration shows the precise location of the bar.
  </p>
  
  <blockquote>
    <p><strong>Note:</strong> To review the reservation procedure, refer to the <a href="#profile-page">profile page reservation section</a>.</p>
  </blockquote>

  <div style="text-align: center;">
      <img src="images_documentation/gifs/contact_send_message.gif" alt="Contact page gif" style="max-width: 85%; height: auto;">
  </div>
</details>

<br>

<details>
  <summary><strong>Testimonials Page</strong></summary>

  <p>
    On the <strong>Testimonials</strong> page, users can:
  </p>

  <h3>Rate Your Experience:</h3>
  <p>
    Curious about our ratings? 🍺  
    <strong>Red</strong> means 'Room for Improvement', <strong>Yellow</strong> signifies 'Good, but Could Be Better,' and <strong>Green</strong> represents 'Top-Notch Experience!' 🍺
  </p>

  <div style="display: flex; justify-content: center; align-items: center; flex-direction: column;">
      <table style="border-collapse: collapse; width: auto; text-align: left;">
          <tr>
              <th style="text-align: left;">Rating Scale</th>
              <th style="text-align: left;">CSS Code</th>
          </tr>
          <tr>
              <td>1 - 🔴 Red</td>
              <td>.bar-rating[data-rating="1"] { width: 20%; background: red; }</td>
          </tr>
          <tr>
              <td>2 - 🟡 Yellow</td>
              <td>.bar-rating[data-rating="2"] { width: 40%; background: orange; }</td>
          </tr>
          <tr>
              <td>3 - 🟠 Bright Yellow</td>
              <td>.bar-rating[data-rating="3"] { width: 60%; background: yellow; }</td>
          </tr>
          <tr>
              <td>4 - 🟢 Light Green</td>
              <td>.bar-rating[data-rating="4"] { width: 80%; background: lightgreen; }</td>
          </tr>
          <tr>
              <td>5 - 🟩 Dark Green</td>
              <td>.bar-rating[data-rating="5"] { width: 100%; background: green; }</td>
          </tr>
          <tr>
              <td colspan="2" style="text-align: left; padding-top: 20px;">
                  <strong>Background Gradient CSS:</strong><br>
                  .bar-rating {<br>
                  &nbsp;&nbsp;background: linear-gradient(to right, red 0%, yellow 20%, orange 40%, lightgreen 60%, green 100%);<br>
                  }
              </td>
          </tr>
      </table>
  </div>

  <h3>Sort By:</h3>
  <p>
    The testimonials can be sorted by the following criteria, with the default set to <strong>Date Added</strong>:
  </p>
  <ul>
    <li><strong>Date</strong></li>
    <li><strong>Views</strong></li>
    <li><strong>Comments</strong></li>
    <li><strong>Ratings</strong></li>
  </ul>
  <p><strong>Sort Order:</strong> Ascending or Descending</p>

  <h3>Testimonials Display:</h3>
  <p>
    - Two testimonial cards are displayed per row.
  </p>
  <p>
    Each testimonial card includes:
  </p>
  <ul>
    <li><strong>Profile Picture</strong> of the user. Other users can click on the picture to open a modal titled <strong>[Username] Info</strong>, displaying:
      <ul>
        <li>Profile picture</li>
        <li>Username</li>
        <li>Member since</li>
        <li>Bio</li>
      </ul>
    </li>
    <li><strong>Testimonial Content</strong>: The message provided by the user.</li>
    <li><strong>Submitted On</strong>: The date the testimonial was submitted.</li>
    <li><strong>Edited On</strong>: The date if the testimonial was edited.</li>
    <li><strong>Views Counter</strong></li>
    <li><strong>Comments Counter</strong>  
      If no comments have been added, it displays: <strong>No comments yet!</strong>
    </li>
  </ul>

  <h4>Action Buttons:</h4>
  <p>
    For the testimonial's author:
  </p>
  <ul>
    <li><strong>Edit</strong></li>
    <li><strong>Delete</strong></li>
    <li><strong>Comment</strong></li>
    <li><strong>View Details</strong></li>
  </ul>
  <p>
    For other users:
  </p>
  <ul>
    <li><strong>Comment</strong></li>
    <li><strong>View Details</strong></li>
  </ul>
  <p>
    Clicking <strong>View Details</strong> takes users to a new page, <strong>Testimonial Detail</strong>, with the following information:
  </p>
  <ul>
    <li><strong>Testimonial Content</strong></li>
    <li><strong>Submitted On</strong></li>
    <li><strong>Edited On</strong> (if applicable)</li>
    <li><strong>Comments Section</strong>: Users can add their own comments directly from this page, with the same action buttons available as on the main testimonials page.</li>
  </ul>

  <h3>Add Your Testimonial</h3>
  <p>
    Below the last testimonial displayed, there is an <strong>"Add Your Testimonial"</strong> button, inviting users to share their experiences.
  </p>

  <div style="text-align: center;">
      <img src="images_documentation/gifs/testimonial_with_details.gif" alt="Testimonials page gif" style="max-width: 85%; height: auto;">
  </div>
</details>

### Wireframes

The wireframes have been designed for both PC and mobile screens to provide a visual representation of each page's layout and functionality.

<table style="width: 100%; border-collapse: collapse;">
    <tr>
        <th style="text-align: center;">Home</th>
        <th style="text-align: center;">Sign Up</th>
        <th style="text-align: center;">Sign In</th>
        <th style="text-align: center;">Profile</th>
        <th style="text-align: center;">Testimonials</th>
    </tr>
    <tr>
        <td style="text-align: center; vertical-align: top;">
            <div style="display: flex; flex-direction: column; align-items: center; flex-wrap: wrap;">
                <img src="images_documentation/wireframes/home_mobile_wirreframe.png" alt="Home Mobile Wireframe" style="max-width: 60%; height: auto; margin-bottom: 20px;">
                <img src="images_documentation/wireframes/home_pc_wireframe.png" alt="Home PC Wireframe" style="max-width: 100%; height: auto;">
            </div>
        </td>
        <td style="text-align: center; vertical-align: top;">
            <div style="display: flex; flex-direction: column; align-items: center; flex-wrap: wrap;">
                <img src="images_documentation/wireframes/signup_mobile_wireframe.png" alt="Sign Up Mobile Wireframe" style="max-width: 60%; height: auto; margin-bottom: 20px;">
                <img src="images_documentation/wireframes/signup_pc_wireframe.png" alt="Sign Up PC Wireframe" style="max-width: 100%; height: auto;">
            </div>
        </td>
        <td style="text-align: center; vertical-align: top;">
            <div style="display: flex; flex-direction: column; align-items: center; flex-wrap: wrap;">
                <img src="images_documentation/wireframes/signin_mobile_wireframe.png" alt="Sign In Mobile Wireframe" style="max-width: 60%; height: auto; margin-bottom: 20px;">
                <img src="images_documentation/wireframes/signin_pc_wireframe.png" alt="Sign In PC Wireframe" style="max-width: 100%; height: auto;">
            </div>
        </td>
        <td style="text-align: center; vertical-align: top;">
            <div style="display: flex; flex-direction: column; align-items: center; flex-wrap: wrap;">
                <img src="images_documentation/wireframes/profile_mobile_wireframe.png" alt="Profile Mobile Wireframe" style="max-width: 60%; height: auto; margin-bottom: 20px;">
                <img src="images_documentation/wireframes/profile_pc_wireframe.png" alt="Profile PC Wireframe" style="max-width: 100%; height: auto;">
            </div>
        </td>
        <td style="text-align: center; vertical-align: top;">
            <div style="display: flex; flex-direction: column; align-items: center; flex-wrap: wrap;">
                <img src="images_documentation/wireframes/testimonial_mobile_wireframe.png" alt="Testimonials Mobile Wireframe" style="max-width: 60%; height: auto; margin-bottom: 20px;">
                <img src="images_documentation/wireframes/testimonials_pc_wireframe.png" alt="Testimonials PC Wireframe" style="max-width: 100%; height: auto;">
            </div>
        </td>
    </tr>
</table>

### Database design

The database was designed to allow CRUD functionality to registered users.

- Users can register, log in, and manage their profiles, allowing for the creation and updating of personal information and images in the `user_profiles` table.
- Reservations enable users to create, view, and modify their bookings, with relevant details like name, reservation time, special requests, and guest count stored in the `reservations` table.
- The Testimonials table allows users to submit their experiences, read others' testimonials, and update or delete their submissions as needed. It includes ratings and counters for views and comments to enhance community interaction.
- Comments associated with testimonials allow users to provide feedback, with the ability to add, edit, or delete their comments.

The ERD (Entity Relationship Diagram) was designed on [dbdiagram.io](https://dbdiagram.io/d)

  <div style="text-align: center;">
      <img src="images_documentation/flowcharts/ERD.png" alt="ERD" style="max-width: 85%; height: auto;">
  </div>

## Technology Stack

<table>
  <tr>
    <td valign="top">
      <h3>Technology Used</h3>
      <table>
        <tr>
          <td><strong>Backend</strong></td>
          <td style="text-align:right;">Django 5.1.1 <code>Django==5.1.1</code></td>
        </tr>
        <tr>
          <td><strong>API</strong></td>
          <td style="text-align:right;">Django REST Framework <code>djangorestframework==3.15.2</code></td>
        </tr>
        <tr>
          <td><strong>Database</strong></td>
          <td style="text-align:right;">PostgreSQL <code>psycopg2==2.9.9</code></td>
        </tr>
        <tr>
          <td><strong>Authentication</strong></td>
          <td style="text-align:right;">Django Allauth <code>django-allauth==64.2.1</code></td>
        </tr>
        <tr>
          <td><strong>Frontend</strong></td>
          <td style="text-align:right;">JavaScript, JSON, HTML5, CSS3</td>
        </tr>
        <tr>
          <td><strong>Styling</strong></td>
          <td style="text-align:right;">Crispy Forms + Bootstrap 5 <code>crispy-bootstrap5==2024.2</code></td>
        </tr>
        <tr>
          <td><strong>Media Storage</strong></td>
          <td style="text-align:right;">Cloudinary <code>cloudinary==1.41.0</code></td>
        </tr>
        <tr>
          <td><strong>Static Files</strong></td>
          <td style="text-align:right;">Whitenoise <code>whitenoise==6.7.0</code></td>
        </tr>
        <tr>
          <td><strong>Server</strong></td>
          <td style="text-align:right;">Gunicorn <code>gunicorn==23.0.0</code></td>
        </tr>
        <tr>
          <td><strong>Image Handling</strong></td>
          <td style="text-align:right;">Pillow <code>pillow==10.4.0</code></td>
        </tr>
      </table>
    </td>
    <td valign="top" style="padding-left: 20px;">
      <h3>Other Dependencies</h3>
      <ul style="list-style-type: none; padding-left: 0;">
        <li><code>asgiref==3.8.1</code></li>
        <li><code>dj-database-url==2.2.0</code></li>
        <li><code>dj3-cloudinary-storage==0.0.6</code></li>
        <li><code>django-crispy-forms==2.3</code></li>
        <li><code>django-summernote==0.8.20.0</code></li>
        <li><code>oauthlib==3.2.2</code></li>
        <li><code>PyJWT==2.9.0</code></li>
        <li><code>python3-openid==3.2.0</code></li>
        <li><code>requests-oauthlib==2.0.0</code></li>
        <li><code>sqlparse==0.5.1</code></li>
        <li><code>urllib3==1.26.20</code></li>
      </ul>
    </td>
  </tr>
</table>

### Tools used

- Git: Used commands such as `git` `add` - `commit -m "message'` - `push`.
- Gitpod: Used as my IDE.
- Github: Used as the code hosting.
- [Font awesome](https://fontawesome.com/): Used for a variety of icons through the pages.
- [Favicon io](https://favicon.io/favicon-converter/): Used to generate the faveicon.
- [Balsamiq](https://balsamiq.com/wireframes/desktop/): Used to create the wireframes - desktop version.
- [TinyPNG](https://tinypng.com/): Used to compress each image used in the project for optimal load times.
- [dbdiagraim.io](https://dbdiagram.io/home): Used to create the ERD.

## Fixed bugs

<details>
    <summary>Patch 1.0.0</summary>
    <div style="display: flex; justify-content: center;">
        <div style="overflow-x: auto; width: 80%;">
            <table style="margin: 0 auto; border-collapse: collapse; width: 100%;">
                <tr>
                    <th>Issue</th>
                    <th>Description of Fix</th>
                    <th>Pass/Fail</th>
                </tr>
                <tr>
                    <td>Drinks and Drink Detail Modals Collision</td>
                    <td>Resolved the collision issue between drinks and drink detail modals.</td>
                    <td>Pass</td>
                </tr>
                <tr>
                    <td>UserProfile Image Upload Error</td>
                    <td>Fixed the issue where image uploads to UserProfile were failing due to file size restrictions.</td>
                    <td>Pass</td>
                </tr>
                <tr>
                    <td>Reservation Date Duplication</td>
                    <td>Corrected the logic to prevent users from making multiple reservations on the same date.</td>
                    <td>Pass</td>
                </tr>
                <tr>
                    <td>Testimonial Character Count Validation</td>
                    <td>Enhanced validation to ensure comments do not exceed 50 characters.</td>
                    <td>Pass</td>
                </tr>
                <tr>
                    <td>Navbar Active Link Highlighting</td>
                    <td>Improved the active link highlighting on the navbar for better navigation.</td>
                    <td>Pass</td>
                </tr>
            </table>
        </div>
    </div>
</details>

<details>
    <summary>Patch 1.0.1</summary>
    <div style="display: flex; justify-content: center;">
        <div style="overflow-x: auto; width: 80%;">
            <table style="margin: 0 auto; border-collapse: collapse; width: 100%;">
                <tr>
                    <th>Issue</th>
                    <th>Description of Fix</th>
                    <th>Pass/Fail</th>
                </tr>
                <tr>
                    <td>UserProfile Form Validation</td>
                    <td>Improved validation for image formats in the UserProfile form.</td>
                    <td>Pass</td>
                </tr>
                <tr>
                    <td>User Data Update</td>
                    <td>Fixed issues in the UserForm to ensure proper data updates.</td>
                    <td>Pass</td>
                </tr>
                <tr>
                    <td>Profile Template Changes</td>
                    <td>Updated profile template to enhance user experience during profile updates.</td>
                    <td>Pass</td>
                </tr>
                <tr>
                    <td>Reset Profile Picture Functionality</td>
                    <td>Ensured reset functionality correctly sets the profile image to None.</td>
                    <td>Pass</td>
                </tr>
                <tr>
                    <td>Improved Form Handling</td>
                    <td>Refined form handling in the views to enhance performance.</td>
                    <td>Pass</td>
                </tr>
                <tr>
                    <td>Cloudinary URL Error</td>
                    <td>Fixed error from Cloudinary URL when changing profile info.</td>
                    <td>Pass</td>
                </tr>
                <tr>
                    <td>Editing Testimonials</td>
                    <td>Fixed issues in the testimonials editing process and display updated timestamps correctly.</td>
                    <td>Pass</td>
                </tr>
            </table>
        </div>
    </div>
</details>

<details>
    <summary>Patch 1.0.2</summary>
    <div style="display: flex; justify-content: center;">
        <div style="overflow-x: auto; width: 80%;">
            <table style="margin: 0 auto; border-collapse: collapse; width: 100%;">
                <tr>
                    <th>Issue</th>
                    <th>Description of Fix</th>
                    <th>Pass/Fail</th>
                </tr>
                <tr>
                    <td>User Authentication</td>
                    <td>Implemented a login requirement for making reservations, ensuring only authenticated users can access this feature.</td>
                    <td>Pass</td>
                </tr>
                <tr>
                    <td>Reservation Restrictions</td>
                    <td>Added logic to prevent users from making multiple reservations on the same date.</td>
                    <td>Pass</td>
                </tr>
                <tr>
                    <td>Admin Panel Enhancements</td>
                    <td>Strengthened admin-only access for creating events to enhance security.</td>
                    <td>Pass</td>
                </tr>
                <tr>
                    <td>Content Management</td>
                    <td>Adjusted testimonial and comment models to validate content length, improving the quality of user-generated content.</td>
                    <td>Pass</td>
                </tr>
                <tr>
                    <td>UI/UX Improvements</td>
                    <td>Enhanced CSS for better contrast and accessibility.</td>
                    <td>Pass</td>
                </tr>
                <tr>
                    <td>Testing and Quality Assurance</td>
                    <td>Improved testing for user profile APIs and reservation functionality to ensure stability.</td>
                    <td>Pass</td>
                </tr>
                <tr>
                    <td>Documentation Updates</td>
                    <td>Updated README.md to include the new ERD section and relevant videos, with clearer issue descriptions.</td>
                    <td>Pass</td>
                </tr>
            </table>
        </div>
    </div>
</details>

<details>
    <summary>Patch 1.0.3</summary>
    <div style="display: flex; justify-content: center;">
        <div style="overflow-x: auto; width: 80%;">
            <table style="margin: 0 auto; border-collapse: collapse; width: 100%;">
                <tr>
                    <th>Issue</th>
                    <th>Description of Fix</th>
                    <th>Pass/Fail</th>
                </tr>
                <tr>
                    <td>Username Case Insensitivity</td>
                    <td>Implemented CaseInsensitiveUsernameBackend to allow login with lowercase or uppercase usernames.</td>
                    <td>Pass</td>
                </tr>
                <tr>
                    <td>Custom Login View Update</td>
                    <td>Updated CustomLoginView to authenticate users with case-insensitive usernames.</td>
                    <td>Pass</td>
                </tr>
                <tr>
                    <td>Added backends.py</td>
                    <td>Created backends.py in the bar app to handle custom authentication logic.</td>
                    <td>Pass</td>
                </tr>
                <tr>
                    <td>Settings Update</td>
                    <td>Updated settings.py to include the custom authentication backend.</td>
                    <td>Pass</td>
                </tr>
                <tr>
                    <td>Comment Character Limit</td>
                    <td>Updated comment editing functionality to restrict character count to a maximum of 50 characters and changed color indication for exceeding limit.</td>
                    <td>Pass</td>
                </tr>
                <tr>
                    <td>Was Edited Field</td>
                    <td>Added <code>was_edited</code> field to Comment model and updated relevant migration files.</td>
                    <td>Pass</td>
                </tr>
            </table>
        </div>
    </div>
</details>

<details>
    <summary>Patch 1.0.4</summary>
    <div style="display: flex; justify-content: center;">
        <div style="overflow-x: auto; width: 80%;">
            <table style="margin: 0 auto; border-collapse: collapse; width: 100%;">
                <tr>
                    <th>Issue</th>
                    <th>Description of Fix</th>
                    <th>Pass/Fail</th>
                </tr>
                <tr>
                    <td>Fixed Testimonial Deletions</td>
                    <td>Updated the delete functionality for testimonials to ensure proper handling and messaging in the admin panel.</td>
                    <td>Pass</td>
                </tr>
                <tr>
                    <td>Comment Functionality Update</td>
                    <td>Improved comment section UI and backend handling for better user experience.</td>
                    <td>Pass</td>
                </tr>
                <tr>
                    <td>Admin Panel Enhancements</td>
                    <td>Updated TestimonialAdmin to display comment counts and included additional fields in the admin view for better management.</td>
                    <td>Pass</td>
                </tr>
                <tr>
                    <td>Textarea Update in Add Testimonial</td>
                    <td>Updated textarea for testimonial content to enforce character limits.</td>
                    <td>Pass</td>
                </tr>
                <tr>
                    <td>Improved Delete Testimonial Template</td>
                    <td>Enhanced the delete testimonial template for clearer user messaging and action confirmation.</td>
                    <td>Pass</td>
                </tr>
                <tr>
                    <td>Testimonial List Enhancements</td>
                    <td>Improved the layout and functionality of the testimonial list page, including comment display and delete buttons.</td>
                    <td>Pass</td>
                </tr>
                <tr>
                    <td>Security on Edit and Delete</td>
                    <td>Added permission checks to ensure only authorized users can edit or delete testimonials and comments.</td>
                    <td>Pass</td>
                </tr>
            </table>
        </div>
    </div>
</details>

<details>
    <summary>Patch 1.0.5</summary>
    <div style="display: flex; justify-content: center;">
        <div style="overflow-x: auto; width: 80%;">
            <table style="margin: 0 auto; border-collapse: collapse; width: 100%;">
                <tr>
                    <th>Issue</th>
                    <th>Description of Fix</th>
                    <th>Pass/Fail</th>
                </tr>
                <tr>
                    <td>JavaScript Code Duplication</td>
                    <td>Removed duplicate lines of code for variable declarations and event listeners to improve readability and maintainability.</td>
                    <td>Pass</td>
                </tr>
                <tr>
                    <td>Update Available Spots Logic</td>
                    <td>Refactored the logic for updating available spots based on reservation input to ensure accurate calculations.</td>
                    <td>Pass</td>
                </tr>
                <tr>
                    <td>Validation for Future Reservations</td>
                    <td>Implemented validation to ensure that reservations can only be made for future dates and times, enhancing user experience.</td>
                    <td>Pass</td>
                </tr>
                <tr>
                    <td>Error Handling in Fetch Requests</td>
                    <td>Added error handling to the fetch request for availability to provide clear feedback in case of network issues.</td>
                    <td>Pass</td>
                </tr>
                <tr>
                    <td>Improve Alert Messaging</td>
                    <td>Enhanced alert messaging to provide users with clearer instructions regarding reservation limits and issues.</td>
                    <td>Pass</td>
                </tr>
                <tr>
                    <td>UI Improvements for Time Selection</td>
                    <td>Updated the time selection UI to ensure users can only select valid time options for their reservations.</td>
                    <td>Pass</td>
                </tr>
                <tr>
                    <td>Clearer Comments for Future Dates</td>
                    <td>Provided clearer comments in the code for future dates validation to aid developers in understanding the logic.</td>
                    <td>Pass</td>
                </tr>
            </table>
        </div>
    </div>
</details>

<details>
    <summary>Patch 1.0.6</summary>
    <div style="display: flex; justify-content: center;">
        <div style="overflow-x: auto; width: 80%;">
            <table style="margin: 0 auto; border-collapse: collapse; width: 100%;">
                <tr>
                    <th>Issue</th>
                    <th>Description of Fix</th>
                    <th>Pass/Fail</th>
                </tr>
                <tr>
                    <td>Fix Hour Option Population</td>
                    <td>Refactored the hour options population logic to ensure proper formatting and prevent duplicates in the hour selection dropdown.</td>
                    <td>Pass</td>
                </tr>
                <tr>
                    <td>Fix Minute Option Population</td>
                    <td>Corrected the population of minute options to avoid duplication and ensure that only valid minute intervals are displayed.</td>
                    <td>Pass</td>
                </tr>
                <tr>
                    <td>Update Available Spots Logic</td>
                    <td>Revised the available spots calculation to accommodate new logic and ensure it reflects the correct number of spots based on input.</td>
                    <td>Pass</td>
                </tr>
                <tr>
                    <td>Validation for Reservation Date and Time</td>
                    <td>Improved validation checks to ensure the selected reservation time and date are in the future, enhancing usability.</td>
                    <td>Pass</td>
                </tr>
                <tr>
                    <td>Consistent API Response Handling</td>
                    <td>Ensured consistency in how API responses are handled, with error checking for network responses to improve reliability.</td>
                    <td>Pass</td>
                </tr>
                <tr>
                    <td>Alert Function Enhancements</td>
                    <td>Enhanced the alert function to provide clearer feedback messages to users when input is invalid or unavailable.</td>
                    <td>Pass</td>
                </tr>
                <tr>
                    <td>Comment Documentation Improvement</td>
                    <td>Improved inline comments within the code to clarify the purpose of functions and logic for better maintainability.</td>
                    <td>Pass</td>
                </tr>
            </table>
        </div>
    </div>
</details>

<details>
    <summary>Patch 1.0.7</summary>
    <div style="display: flex; justify-content: center;">
        <div style="overflow-x: auto; width: 80%;">
            <table style="margin: 0 auto; border-collapse: collapse; width: 100%;">
                <tr>
                    <th>Issue</th>
                    <th>Description of Fix</th>
                    <th>Pass/Fail</th>
                </tr>
                <tr>
                    <td>Validation Logic for Reservation Time</td>
                    <td>Improved the clean method in ReservationForm to ensure hour and minute selection is validated before creating the reservation time.</td>
                    <td>Pass</td>
                </tr>
                <tr>
                    <td>Error Handling for Past Reservations</td>
                    <td>Added checks to ensure users cannot create reservations in the past, with appropriate validation messages.</td>
                    <td>Pass</td>
                </tr>
                <tr>
                    <td>Existing Reservations Check</td>
                    <td>Implemented checks in both the form and view logic to prevent users from making multiple reservations on the same date.</td>
                    <td>Pass</td>
                </tr>
                <tr>
                    <td>Refactored Code for Readability</td>
                    <td>Refactored the form and view code to enhance readability and maintainability, reducing duplication of logic.</td>
                    <td>Pass</td>
                </tr>
                <tr>
                    <td>Consistent User Messaging</td>
                    <td>Standardized error messages across different views for consistency in user experience when handling reservations.</td>
                    <td>Pass</td>
                </tr>
                <tr>
                    <td>Enhanced Reservation Logic</td>
                    <td>Updated the reservation creation and editing logic to better handle user input and reservation time management.</td>
                    <td>Pass</td>
                </tr>
                <tr>
                    <td>Documentation Updates</td>
                    <td>Enhanced comments and docstrings in the code to provide clearer explanations of the logic and validation rules implemented.</td>
                    <td>Pass</td>
                </tr>
            </table>
        </div>
    </div>
</details>

## Deployment

### via Heroku

1. Navigate to [heroku](https://www.heroku.com/home) and create an account.
2. Click `Create new app`, enter the app name and choose your region, hit `create app`.
3. Click **Deploy** and in the _Deployment method_ option choose **Github**. Enter the repository's name and click connect, you can leave the branch deployment to `main`.
   > You need to have created your github repository.
4. Head to **Settings** and click `Reveal config vars`
5. On the KEY inputs add: DATABASE_URL - SECRET_KEY - CLOUDINARY_URL. On the VALUE inputs add your own, for each one.
6. Click **Add buildpack** and choose `python`.
7. Now you're set. Go back to `Deploy` and click **Deploy branch**.

### Via Forking

Forking a repository is commonly done to contribute to another developer's project or to use it as the foundation for your own. To fork a repository:

1. Click the **Fork** button at the top right of the repository page.
2. This will create a copy of the repository in your own GitHub account, which you can modify independently.

## Credits

🎓 **𝕽𝖔𝖍𝖎𝖙** - **Code Institute Mentor** [<img src="https://img.icons8.com/color/24/ffffff/github.png"/>](https://github.com/rohit0286)

💡 **[Gareth's readme](https://github.com/Gareth-McGirr/Portfolio-Project-4-SizzleAndSteak)** as inspiration to mine.

[ChatGPT 4o](https://openai.com/chatgpt/) / [Codeium](https://codeium.com/) / [Stack Overflow](https://stackoverflow.com/) for adjustments and bug fixing aid.

The main idea for this project was obtained by the [Django Blog](https://www.youtube.com/watch?v=YH--VobIA8c) walkthrough project of the [Code Institute course](https://codeinstitute.net/global/).

### Media

All photos used in the project - including favicon - were taken from [Pexels](https://www.pexels.com/) / [Unsplash](https://unsplash.com/) / [Freepik](https://www.freepik.com/).
