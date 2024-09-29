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
