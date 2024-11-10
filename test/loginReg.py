# {% extends "base.html" %}
# {% load static %}

# {% block pageTitle %}
# Login Page
# {% endblock pageTitle %}

# {% block cssLinks %}
# <link rel="stylesheet" href="{% static "blog/navigations/slideBar.css" %}">
# {% endblock cssLinks %}

# {% block slidePanel %}
# {% include "blog/navigations/slideBar.html" %}
# {% endblock slidePanel %}

# {% block header %}
# {% include "blog/navigations/header.html" %}
# {% endblock header %}

# {% block content %}
#     <div class="w3-row">
#         <div class="w3-card-4 w3-margin w3-white">
#             <div class="w3-container w3-padding">
#                 <h2>Login</h2>
#             </div>
#             <div class="w3-container">
#                 <form method="POST" action="{% url 'loginUrl' %}">
#                     {% csrf_token %}
#                     <div class="w3-margin-bottom">
#                         <label for="username">Username:</label>
#                         <input class="w3-input" type="text" id="username" name="username" required>
#                     </div>
#                     <div class="w3-margin-bottom">
#                         <label for="password">Password:</label>
#                         <input class="w3-input" type="password" id="password" name="password" required>
#                     </div>
#                     <button class="w3-button w3-blue" type="submit">Login</button>
#                 </form>
#                 # <p>Don't have an account? <a href="{% url '' %}">Register here</a></p>
#             </div>
#         </div>
#     </div>
# {% endblock content %}

# {% block footer %}
# {% include "blog/navigations/footer.html" %}
# {% endblock footer %}
# # ====================================================================================


# {% extends "base.html" %}
# {% load static %}

# {% block pageTitle %}
# Register Page
# {% endblock pageTitle %}

# {% block cssLinks %}
# <link rel="stylesheet" href="{% static "blog/navigations/slideBar.css" %}">
# {% endblock cssLinks %}

# {% block slidePanel %}
# {% include "blog/navigations/slideBar.html" %}
# {% endblock slidePanel %}

# {% block header %}
# {% include "blog/navigations/header.html" %}
# {% endblock header %}

# {% block content %}
#     <div class="w3-row">
#         <div class="w3-card-4 w3-margin w3-white">
#             <div class="w3-container w3-padding">
#                 <h2>Register</h2>
#             </div>
#             <div class="w3-container">
#                 <form method="POST" action="{% url 'registerUrl' %}">
#                     {% csrf_token %}
#                     <div class="w3-margin-bottom">
#                         <label for="username">Username:</label>
#                         <input class="w3-input" type="text" id="username" name="username" required>
#                     </div>
#                     <div class="w3-margin-bottom">
#                         <label for="email">Email:</label>
#                         <input class="w3-input" type="email" id="email" name="email" required>
#                     </div>
#                     <div class="w3-margin-bottom">
#                         <label for="password">Password:</label>
#                         <input class="w3-input" type="password" id="password" name="password" required>
#                     </div>
#                     <div class="w3-margin-bottom">
#                         <label for="confirm_password">Confirm Password:</label>
#                         <input class="w3-input" type="password" id="confirm_password" name="confirm_password" required>
#                     </div>
#                     <button class="w3-button w3-blue" type="submit">Register</button>
#                 </form>
#                 <p>Already have an account? <a href="{% url 'loginUrl' %}">Login here</a></p>
#             </div>
#         </div>
#     </div>
# {% endblock content %}

# {% block footer %}
# {% include "blog/navigations/footer.html" %}
# {% endblock footer %}
