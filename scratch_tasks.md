## 1.5 - Create Employer and Job Templates

@pytest.mark.detail-templates In the root of the `templates` folder, create two files one called `employer.html` and the other called `job.html`.

## 1.6 - Create Detail Routes

@pytest.mark.app-create-detail-routes We need routes for individual employers and jobs. In `app.py` create two functions one called `employer` and the other called `job`.  Add route decorators to bind these functions with the appropriate URLs: 
- `/employer` to the `employer` function
- `/job` to the `job `function.

In the body of each function return a call to `render_template()` passing the appropriate template.


## 2.3 - Create Template Files

@pytest.mark.create-template-files We need to create some additional template files. In the `templates` folder create the following files:
- `_job.html`
- `job.html`
- `employer.html`
- `review.html`

Next, create a new folder called `admin` in the `templates` folder, then create the following files:
- `index.html`
- `create.html`

## 2.4 - Template Files HTML
@pytest.mark.template-files-html Locate the `templates.html` file in the root of the project. To prevent having to write all HTML from scratch the HTML structure of several of the template files is given here. Each block has a comment that describes what HTML file, the HTML block, needs to be copied too. Copy each block to the correct file.

## 2.5 - Extend Base Layout

@pytest.mark.extend-base-layout Each of the files listed below needs to extend the base layout. This can be done by adding an `extends` directive with `{% %}` template syntax to the top of each file.

- `job.html`
- `employer.html`
- `review.html`
- `admin/index.html`
- `admin/create.html`

## 2.6 - Navigation

@pytest.mark.navigation We want to allow the user to navigate to the admin from the front page. In the `index.html` template file create a link to the main admin page by creating an `<a>` tag nested in the `<div>` with the two classes `columns` and `is-one-fifth`. The `<a>` tag should have an `href` with the value `/admin` and the classes `button`, `is-info`, and `is-pulled-right`. In the admin we allow the user to create a new job. In the `admin/index.html` template file create a link to the new job form by creating an `<a>` tag nested in the `<div>` with the two classes `columns` and `is-one-fifth`. The `<a>` tag should have an `href` with the value `/admin/create` and the classes `button`, `is-info`, and `is-pulled-right`.


locate the `jobs` function. Above the `render_template` function call, call the `query_db`function. Pass in the SQL statement: `'SELECT job.id, job.title, job.description, job.salary, employer.id as employer_id, employer.name as employer_name FROM job JOIN employer ON employer.id = job.employer_id'`. Assign the results of the call to a variable called `jobs`. In the `render_template` function, pass a keyword argument of `jobs=jobs`.

## 4.2 - Individual Job Details

@pytest.mark.app-individual-job-details To bring back just one job from the database we are going to use a where clause. In the where clause we will need a `job_id`. We are going to get this from the URL. In `app.py` locate the `job` function. In the route decorator for the function after the URL path `/job` add `/<job_id>`.  To use this `job_id` we also need to pass it to the job function add `job_id` to the parameter list of the `job` function. Above the `render_template` function, call the `query_db` function and assign the results of the call to a `job` variable. Pass the function three arguments: 
- SQL Query: `'SELECT job.id, job.title, job.description, job.salary, employer.id as employer_id, employer.name as employer_name FROM job JOIN employer ON employer.id = job.employer_id WHERE job.id = ?'`
- List Literal: [job_id]
- True: This will bring back only one result.

In the `render_template` function, pass a keyword argument of `job=job`

## 4.3 - Individual Employer Details

@pytest.mark.app-individual-employer-details Similar to the `job` function the employer route will only need the details of one employer. Locate the `employer` function in `app.py`. Again we need the unique id of an employer and will receive this from the URL. Add `/<employer_id>` in the route decorator after `/employer`. So that the `employer` function has access to this value add `employer_id`to the parameter list. Make a call to `query_db` and assign the return value to `employer`. Pass in the arguments:
- SQL Query: 'SELECT * FROM employer WHERE id=?'
- List Literal: [employer_id]
- True: This will bring back only one result.

In the `render_template` function, pass a keyword argument of `employer=employer`

## 4.4 - All Employer Jobs

@pytest.mark.app-all-employer-jobs On the employer details page, we want to display all of the employers’ jobs. In the `employer` function in `app.py` below the `employer` variable, add a call to the `query_db` function and assign the results to a variable called `jobs`.  Pass the function two arguments: 
- SQL Query: `'SELECT job.id, job.title, job.description, job.salary FROM job JOIN employer ON employer.id = job.employer_id WHERE employer.id = ?'`
- List Literal: [employer_id]

In the `render_template` function, add another keyword argument of `jobs=jobs`

## 4.5 - Job Card

@pytest.mark.job-card Open the file `templates/_jobs.html` find the `<p>` tag with a class of `card-header-title`. Add an `<a>` tag with an `href` of `{{ url_for('job', job_id=job['id']) }}`. The content should be `{{ job['title'] }}`. Next find the `<div>` with a class of `content`. To this tag add a `<p>` tag and in this tag add the following: 
- `<a>` tag with an `href` of `{{ url_for('employer', employer_id=job['employer_id']) }}`. The content should be `{{ job['employer_name'] }}`. Add line break.
- ${{ job['salary'] }}. Add line break.
- {{ job['description'] }}

## 4.6 -Display All Jobs

@pytest.mark.display-all-jobs Open the file `templates/index.html` above the `{% endblock %}` add a `<div>` with two classes `columns` and `is-multiline`. In the div add a `for in` loop that loops through all jobs. Use the `{% %}` template syntax, don’t forget about ending the `for` loop. In the `for` loop add a `<div>` with two classes `column` and `is-half`.  Too this `<div>` add the following template code: 

```
{% with job=job %}
  {% include "_job.html" %}
{% endwith %}
```

## 4.7 - Display Individual Job Details

@pytest.mark.display-individual-job-details In `templates/job.html` add a template block called `content` using the `{% %}` template markup. In the template block add the following template code: 

```
{% with job=job %}
  {% include "_job.html" %}
{% endwith %}
```

## 4.8 - Display Individual Employer Details

@pytest.mark.display-individual-employer-details Open `templates/employer.html` as the first thing in the template block add the following HTML:

- `<div>`
- Nested in the `<div>` add an `<h1>` with the content {{ employer['name'] }}
- Nested in the `<div>` add a`<div>` with a class of `description`
- Nested in the description `<div>`add a`<p>` with the content {{ employer['description'] }}
  
## 4.9 -Display All Employer Jobs

@pytest.mark.display-all-employer-jobs Open the file `templates/employer.html` below the jobs `<h2>` add a `<div>` with two classes `columns` and `is-multiline`. In the div add a `for in` loop that loops through all jobs. Use the `{% %}` template syntax, don’t forget about ending the `for` loop. In the `for` loop add a `<div>` with two classes `column` and `is-half`.  To the `<div>` add the following template code: 

```
{% with job=job %}
  {% include "_job.html" %}
{% endwith %}
```

# Module 08 - Add Jobs

## 8.1 - Admin Route

@pytest.mark.app-admin-route We will display all jobs on the admin page. To start, in `app.py` create a basic route that displays the contents of the admin index template. Create a function called `admin` and attach a `route()` decorator with the URL of `/admin`. In the body of the function use the `query_db` function to get all jobs from the database. The SQL can be found in other routes. Next, return a call to the `render_template()` passing in the `admin/index.html` template and the correct keyword arguments. 

## 8.2 - Admin Create Job Route

@pytest.mark.app-admin-create-job-route In `app.py` create a route at the path `/admin/create` that accepts the methods 'GET' and 'POST'. 

## 8.3 - Check for POST method

@pytest.mark.app-admin-check-for-post-method In the body of your route check if data has been posted then create four variables `title`, `description`, `salary`, and `employer_id`. Set them equal to their respective `request.form` values. Create an `error` variable set to `None`.

## 8.3 - Check for Values

@pytest.mark.app-admin-check-for-values In the body of the post `if` statement in your route function in `app.py`, below the variables, check if there is a value for `title`, and `employer_id`. If either is empty set `error` to  an appropriate error message i.e. 'Title field is required.'

## 8.4 - Check for Error

@pytest.mark.app-admin-check-for-error Still in your route function below the value checks add an `if` statement that checks if `error` is `None`. If there are no errors we are going to add the form values to the database. Connect to the database and commit the changes.
**Hint: The SQL is `'INSERT INTO job (title, description, salary, employer_id) VALUES (?, ?, ?, ?)'`**

If there are errors `flash` the error. **Hint: `else` statement**

## 8.5 - Admin Navigation

@pytest.mark.admin-navigation Find the admin index template and add an href attribute to the `New Job` link. Send the user to the URL ``/admin/create`. Open create job template and find the cancel anchor tag. Point the link back to the admin page using `url_for()`.

