"""In this thank_you.html template, the variables name and feedback are dynamically inserted using Jinja2 syntax ({{ name }} and {{ feedback }}).
Mini-Project: Feedback Form App

For the mini-project, you will create a Feedback Form App using Flask.
Requirements:

    HTML Form:
        Create a form with fields for the user's name and feedback.
        The form should send a POST request to a route that handles the form submission.

    Flask Routes:
        Create two routes:
            The / route displays the form to the user.
            The /submit-feedback route handles the form submission and displays a thank-you message with the user's name and feedback.

    Response:
        After the form is submitted, show a confirmation page that thanks the user for their feedback and displays what they submitted.

    Styling:
        Use basic HTML and CSS to make the form user-friendly and visually appealing. (Optional but encouraged.)

Project Steps:

    Set up a basic Flask project with the necessary structure:
        app.py for Flask routes and app logic.
        templates/ directory for HTML templates (e.g., index.html, thank_you.html).
        Optionally, a static/ directory for CSS or JavaScript files.

    Implement the form in index.html to collect user name and feedback.

    Set up Flask routes to handle displaying the form and processing the submitted data.

    Display the submitted feedback dynamically on a thank-you page (thank_you.html).

    Test the form submission to ensure everything works as expected."""