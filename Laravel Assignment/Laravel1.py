from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

# Create the PDF file
pdf_path = "/mnt/data/CCS4360_Laravel_Social_Auth_Assignment_Report.pdf"
doc = SimpleDocTemplate(pdf_path, pagesize=A4)
styles = getSampleStyleSheet()
story = []

# Title and student details
story.append(Paragraph("<b>CCS4360 - Laravel Social Authentication Assignment Report</b>", styles['Title']))
story.append(Spacer(1, 12))
story.append(Paragraph("Full Name: <b>IGBP Samaranatha</b>", styles['Normal']))
story.append(Paragraph("Student Index: <b>22UG1-0028</b>", styles['Normal']))
story.append(Paragraph("Date of Submission: <b>2025-08-08</b>", styles['Normal']))
story.append(Spacer(1, 12))

# GitHub URL
story.append(Paragraph("URL to Public Code Repository:", styles['Heading2']))
story.append(Paragraph("https://github.com/yourusername/laravel-social-auth-assignment", styles['Normal']))
story.append(Spacer(1, 12))

# Screenshot checklist
story.append(Paragraph("Screenshots Required:", styles['Heading2']))
screenshot_list = [
    "1. Laragon’s Laravel folder structure",
    "2. Login screen",
    "3. Google App Configuration Screen",
    "4. Route file (`web.php`)",
    "5. Controller file code (LoginController, PagesController)",
    "6. Screen after login"
]
for item in screenshot_list:
    story.append(Paragraph(item, styles['Normal']))
story.append(Spacer(1, 12))

# Sample code snippets section
story.append(Paragraph("Sample Code Snippets:", styles['Heading2']))
story.append(Paragraph("<b>web.php</b>", styles['Normal']))
webphp_code = """
Route::get('/', function () {
    return view('welcome');
});
Route::get('/auth/redirect', [LoginController::class, 'redirectToGoogle']);
Route::get('/auth/callback', [LoginController::class, 'handleGoogleCallback']);
Route::middleware('auth')->group(function () {
    Route::get('/calendar', [PagesController::class, 'showCalendar']);
    Route::get('/email', [PagesController::class, 'showEmail']);
    Route::get('/todos', [PagesController::class, 'showTodos']);
});
"""
story.append(Paragraph(f"<pre>{webphp_code}</pre>", styles['Code']))
story.append(Spacer(1, 12))

# Reflection section
story.append(Paragraph("Note on Lessons Learnt (400+ words):", styles['Heading2']))
reflection = """
During this assignment, I learned how to set up Laravel for social authentication using Google's OAuth 2.0 services. Initially, I set up Laragon as the local development environment. This was a smooth process since Laragon bundles Apache, PHP, MySQL, and other tools required for Laravel development.

Next, I installed Laravel and created a new project. After installation, I configured Laravel Socialite, a Laravel package that simplifies social login integration. It required adding the `laravel/socialite` package via Composer and registering it in the `config/services.php` file with credentials obtained from Google Cloud Console.

Setting up the Google OAuth application was a key learning point. I had to register the app, set the correct redirect URI, and enable the appropriate APIs (like Gmail, Calendar, etc.). Once connected, I implemented the login functionality using Socialite’s `redirect` and `user` methods to authenticate users.

After login, I displayed user data and built three functional pages: Calendar, Email, and ToDos. I learned how to fetch basic data from the authenticated Google account, such as emails and calendar events, using Google APIs. This involved using HTTP requests with the authenticated token and parsing JSON responses.

In the ToDos page, I created a simple task manager that allows users to view static or demo tasks in a table. All three pages were styled using basic HTML and Blade templates. I used Laravel’s route protection to ensure only logged-in users could access these pages.

Throughout this project, I also gained experience with version control using Git. I created a public GitHub repository, committed my changes, and pushed the final code online. This taught me the importance of code organization and clean commit history.

In conclusion, this assignment helped me understand how Laravel integrates with external APIs and services. Social authentication is a critical part of modern web apps, and using Socialite made it easier to implement. This knowledge is highly applicable in real-world applications where user convenience and security are priorities.
"""
story.append(Paragraph(reflection, styles['Normal']))

# Build PDF
doc.build(story)
pdf_path
