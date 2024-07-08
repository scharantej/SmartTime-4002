## Flask Application Design for Smart Time

### HTML Files

- `index.html`:
   - The main interface for user interaction, allowing input of tasks, time slots, and customization options.
   - Contains the form for submitting the data to generate the schedule.

- `schedule.html`:
   - Displays the generated schedule visually, showcasing the tasks and their allocated time slots.
   - Provides navigation options to edit or modify the schedule.

### Routes

- `/`:
   - The home route, renders the `index.html` template.

- `/generate`:
   - Receives the user's input from the `index.html` form.
   - Processes the tasks and time slots to generate the personalized schedule.
   - Renders the `schedule.html` template with the generated schedule.

- `/edit`:
   - Receives the request to edit the schedule.
   - Renders a form prefilled with the existing schedule, allowing users to make changes.

- `/update`:
   - Receives the updated schedule from the `edit` form.
   - Processes the changes and updates the schedule.
   - Renders the `schedule.html` template with the updated schedule.