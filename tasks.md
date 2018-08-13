# Setup

## Create Virtual Environment

In a terminal run the following commands from the root folder of the forked project. 

Windows
```
python -m venv .\venv
```

macOS & Linux
```
python -m venv ./venv
```

Once that completes, also run this command from the same folder.

Windows
```
\venv\Scripts\activate.bat
```

macOS & Linux
```
source venv/bin/activate
```

Now that you are working in the virtualenv, install the project dependencies with the following command.

```
pip install -r requirements.txt
```

## Verify Setup

In order to verify that everything is setup correctly, run the following command, which should show you the failing tests. This is good! We’ll be fixing this test once we jump into the build step.

```
pytest
```

Every time you want to check your work locally you can type that command, and it will report the status of every task in the project.

## Previewing Your Work

You can preview your work by running `flask run` in the root of your fork. Then visit `http://localhost:5000` in your browser.

# Module 01 - Flask Setup

## 1.1 - Import Flask

@pytest.mark.app-import-flask In order to create a flask application, Import the `Flask` class and the `render_template` function from `flask` at the top of the `jobs/app.py` file.

## 1.2 - Create a Flask Application

@pytest.mark.app-create-flask-app Still in `app.py` create an instance of the `Flask` class called `app`. Pass the special variable `__name__` to the `Flask` class constructor.

## 1.3 - Templates Folder

@pytest.mark.templates-folder Create a folder called `templates` in the `jobs` directory.

## 1.4 - Create Index Template

@pytest.mark.index-template In the root of the `templates` folder, create a file called `index.html`. Add a single line to the file: 
- `<h1>Jobs</h1>`

## 1.5 - Index Route Function

@pytest.mark.app-index-route-function The homepage of our job board will display all of the jobs in our database. 

For now let’s setup a basic route that displays our simplified `index.html` template. 

Create a basic route in `app.py` by creating a function called `jobs`. 

In the body of the function return a call to the `render_template()` function, pass a parameter of `index.html`.

## 1.6 - Route Decorators

@pytest.mark.app-route-decoractors Still in `app.py` attach a `route()` decorator with the URL of `/` to the `jobs` function. Attach an additional route decorator so that this function can also be reach at the URL `/jobs`.

At this point you have a working application with a single route. Try it out by opening a terminal at the root of the project and running the command `flask run`. Open a browser and navigate to the URL: `http://localhost:5000`. Appending `/jobs` should display the same page.

# Module 02 - Styling

## 2.1 - Create a Layout Template

@pytest.mark.layout-template We want each template to have a  consistent look and feel. We can create a base layout that all templates can extend. 

Create a new file called `layout.html` in the root of the `templates` folder. Next, copy the basic structure of this file from the file called `templates.html`.

## 2.2 - Add the Bulma CSS Framework

@pytest.mark.add-bulma-css-framework The app will be styled with the [Bulma CSS Framework](bulma.io) and icons will be provided by [FontAwesome](fontawesome.com). 

Add a `<link>` tag to the head of `layout.html`. Give it an attribute of `rel="stylesheet"`.

For the `href` use the mustache template markup `{{}}` and the flask `url_for()` function to construct a link for the file `css/bulma.min.css` in `static` folder. **Hint: use the keyword argument `filename`**.

## 2.3 - Add Custom CSS

@pytest.mark.add-custom-css For the second `<link>` tag in `layout.html` construct an `href` for the file `css/app.css`, also in the `static` folder, using the same method. Don't forget   `rel` attribute. 

## 2.4 - Add FontAwesome

@pytest.mark.add-fontawesome The last `<link>` tag in `layout.html` should have an `href` value of `https://use.fontawesome.com/releases/v5.2.0/css/all.css`. Make sure to preview the application and check out the _awesome_ styling. 

# Module 03 - Preparing for Dynamic Content

## 3.1 - Import SQLite

@pytest.mark.app-import-sqlite At the top of `app.py` import the built-in `sqlite3` library.

## 3.2 - Import Global Namespace

@pytest.mark.app-import-global-namespace To provide access to the database throughout the application import the global helper `g` from `flask`. **Hint: the `from` statement already exists add `g` to the `import` comma separated list. 

## 3.3 - Database Path

@pytest.mark.app-database-path below all of the import statements, create a constant called `DATABASE`, that contains the path to the already created database stored in `db/jobs.sqlite`.

## 3.4 - Global Database Attribute

@pytest.mark.app-global-database-attribute At the top of `app.py` create a function called `get_db`. 

In the body of the `get_db` function use the built-in `getattr()` function to get the `'_database'` attribute from the `g` object, and set the default to `None`. Assign the return value of the `getattr` function to `db`. 

## 3.5 - Global Database Connection

@pytest.mark.app-global-database-connection Still in the `get_db` function, test if `db` is `None` if it is, set `db` and `g._database` to `sqlite3.connect(DATABASE)` using multiple assignment. 

## 3.6 - sqlite3 Row Factory

@pytest.mark.app-sqlite3-row-factory To make accessing data easier, after the if statement in `get_db`:
- Set the row_factory of `db` to `sqlite3.Row`. **Note: All rows returned from the database will be named tuples.**
- Return the `db` variable.

## 3.7 - Query Database Function

@pytest.mark.app-query-database-function Let’s create a function  to make it easier to query the database. 

Below the `get_db` function in `app.py` create a function called `query_db`. 

In the body of `query_db` create a variable called `db`. Assign this variable the return value of a call to the newly created `get_db` function.

## 3.8 - Query Database Function Parameters

@pytest.mark.app-query-database-function-parameters Still working with the `query_db` function:
- Add three parameters: `query`, `args`, and `one`.  
- Set the default of `args` to an empty tuple `()`. 
- Set the default of `one` to `False`.   

## 3.9 - Query Database Function Execute
@pytest.mark.app-query-database-function-execute In the body of `query_db` call the `execute` function on `db`, pass in the `query` and `args` variables. Assign the return value to a variable called `cursor`.

## 3.10 - Query Database Function Execute
@pytest.mark.app-query-database-function-fetchall In the body of `query_db`:
- `fetchall` data from the `cursor` and assign it to a variable called `results`.
- Close the `cursor` with the `close` function. 

## 3.11 - Query Database Function Execute
@pytest.mark.app-query-database-function-single Next, in the function body add a test if `one` is `True`:
- if true return a ternary if, `results[0] if results else None`.
- else return all `results`.

## 3.12 - Close the Connection

@pytest.mark.app-close-the-connection In order to make sure the database connection is closed when the `app_context` is torn down create a function in `app.py` called `close_connection`.
Add a parameter called `exception` to the parameter list.

In the function body:
- Call `getattr` with three arguments `g`, `'_database'`, and `None` and assign the return value to a `db` variable. 
- If `db` is not `None` `close` the `db`. 

To ensure this function is called when the `app_context` is destroyed use the `@app.teardown_appcontext` decorator.

# Module 04 - Display Jobs and Employers

## 4.1 - All Jobs

@pytest.mark.app-jobs In `app.py` locate the `jobs` function. Above the `render_template` function call, call the `query_db`function. Pass in the SQL statement: `'SELECT job.id, job.title, job.description, job.salary, employer.id as employer_id, employer.name as employer_name FROM job JOIN employer ON employer.id = job.employer_id'`. Assign the results of the call to a variable called `jobs`. In the `render_template` function, pass a keyword argument of `jobs=jobs`.

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

# Module 05 - Employer Reviews

## 5.1 - Review Route

@pytest.mark.app-review-route In `app.py` below the `employer` function create a new function called review. Add `employer_id` to the parameter list. Add a route decorator will a URL pattern of `/employer/<employer_id>/review` as well as a keyword argument `methods` set to a tuple with two values: 'GET' and 'POST'.
In the body of the function return the render_template function passing in `review.html`  template and a keyword argument of `employer_id=employer_id`.

## 5.2 - Check for POST method

@pytest.mark.app-review-check-for-post-method In the body of the `review` above the render_template function call, create an `if` statement that checks if the request method is 'POST'. In the `if` statement create four variables `review`, `rating`, `title`, and `status`. Set them equal to their respective `request.form` values i.e. `request.form['review']`. Create two more variables  `error` (set to `None`) and `date` (set to `datetime.datetime.now().strftime("%m/%d/%Y")`) . For `datetime` add an `import datetime` statement to the top of `app.py`. 

## 5.3 - Check for Values

@pytest.mark.app-review-check-for-values In the body of the post `if` statement in the review function in `app.py`, below the variables check if there is a value for `review`, `rating`,  and `title`. If any of these are empty set `error` to  an appropriate error message i.e. 'Review field is required.'

## 5.4 - Check for Error

@pytest.mark.app-review-check-for-error Still in the review function below the value checks add an `if` statement that checks if `error` is `None`. If there are no errors we are going to add the form values to the database. To do this we need to connect to the database and commit some changes. Follow these steps: 
- Set a `db` variable to a call to `get_db()`
- `execute` the following SQL statement: `'INSERT INTO review (review, rating, title, date, status, employer_id) VALUES (?, ?, ?, ?, ?, ?)'` passing the values: `(review, rating, title, date, status, employer_id)`
- `commit` the changes to the database.
- return a redirect taking the user back to the employer page. **Hint: use `redirect()` and `url_for()` (pass keyword argument of `employer_id=employer_id`) both of which need to be imported from flask.**

If there are errors (`else` statement) `flash` the error. **Hint: `else` statement; use `flash()` (imported from flask)**

## 5.5 - Review Form Cancel

@pytest.mark.review-form-cancel Open `templates/review.html` and find the cancel anchor tag. Add an `href` attribute with a value of `{{ url_for('employer', employer_id=employer_id) }}`.

## 5.6 - Individual Employer Reviews

@pytest.mark.app-individual-employer-reviews Now that employer reviews can be created, let’s display them on the individual employer pages. Switch back to `app.py` and find the `employer` function below the jobs query add a new query to get all review for the employer. Make a call to `query_db` and assign the return value to `reviews`. Pass in the arguments:
- SQL Query: 'SELECT review, rating, title, date, status FROM review JOIN employer ON employer.id = review.employer_id WHERE employer.id = ?'
- List Literal: [employer_id]

In the `render_template` function, add another keyword argument of `reviews=reviews`

## 5.7 - Display Individual Employer Reviews

@pytest.mark.display-individual-employer-reviews Open `templates/employer.html` find the review `<h2>` in the empty `{% %}` template tag add a `for in` loop to loop through all `reviews`. Add the `endfor` directive to the second empty `{% %}` template tag. In the `<div>` with a class of `media-left` add this for loop:
```
{% for _ in range(1, review['rating']): %}
  <span class="fa fa-star checked"></span>
{% endfor %}
```
In the `content <div>` add a paragraph tag. In the paragraph display the details of a review:
- `title`
- `status`
- `date`
- `review`

For the `Create Review` button to work, add an `href` that points to the individual employer page. 

# Module 06 - Add Jobs

## 6.1 - Admin Route

@pytest.mark.app-admin-route We will display all jobs on the admin page. To start, in `app.py` create a basic route that displays the contents of the admin index template. Create a function called `admin` and attach a `route()` decorator with the URL of `/admin`. In the body of the function use the `query_db` function to get all jobs from the database. The SQL can be found in other routes. Next, return a call to the `render_template()` passing in the `admin/index.html` template and the correct keyword arguments. 

## 6.2 - Admin Create Job Route

@pytest.mark.app-admin-create-job-route In `app.py` create a route at the path `/admin/create` that accepts the methods 'GET' and 'POST'. 

## 6.3 - Check for POST method

@pytest.mark.app-admin-check-for-post-method In the body of your route check if data has been posted then create four variables `title`, `description`, `salary`, and `employer_id`. Set them equal to their respective `request.form` values. Create an `error` variable set to `None`.

## 6.3 - Check for Values

@pytest.mark.app-admin-check-for-values In the body of the post `if` statement in your route function in `app.py`, below the variables, check if there is a value for `title`, and `employer_id`. If either is empty set `error` to  an appropriate error message i.e. 'Title field is required.'

## 6.4 - Check for Error

@pytest.mark.app-admin-check-for-error Still in your route function below the value checks add an `if` statement that checks if `error` is `None`. If there are no errors we are going to add the form values to the database. Connect to the database and commit the changes.
**Hint: The SQL is `'INSERT INTO job (title, description, salary, employer_id) VALUES (?, ?, ?, ?)'`**

If there are errors `flash` the error. **Hint: `else` statement**

## 6.5 - Admin Navigation

@pytest.mark.admin-navigation Find the admin index template and add an href attribute to the `New Job` link. Send the user to the URL ``/admin/create`. Open create job template and find the cancel anchor tag. Point the link back to the admin page using `url_for()`.