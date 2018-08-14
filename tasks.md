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

@pytest.mark.app-import-flask In order to create a flask application, import the `Flask` class and the `render_template` function from `flask` at the top of the `jobs/app.py` file.

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

- Create a basic route in `app.py` by creating a function called `jobs`. 
- In the body of the function return a call to the `render_template()` function, pass a parameter of `index.html`.

## 1.6 - Route Decorators

@pytest.mark.app-route-decoractors Still in `app.py`:
- Attach a `route()` decorator with the URL of `/` to the `jobs` function. 
- Attach an additional route decorator of `/jobs`. **Note: The `jobs` function can now be reached at `/` and `/jobs`**

**Preview**
    
At this point you have a working application with a single route. Try it out:

- Open a terminal at the root of the project
- Run the command `flask run`. 
- Open a browser and navigate to the URL: `http://localhost:5000`. 

**Note: Appending `/jobs` should display the same page.**

# Module 02 - Base Template and Styling

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

## 2.5 - Extend Base Template

@pytest.mark.extend-base-template To use `layout.html` as the base template:
- Open `index.html`, above the `<h1>` use the template markup `{% %}` and the extends tag to inherit `layout.html`. 
- Wrap the `<h1>` element in a `block` called `content`.

**Preview** 

At this point you have a styled application. Check out the styles: 
    
- Open a terminal at the root of the project
- Run the command `flask run`. 
- Open a browser and navigate to the URL: `http://localhost:5000`.

# Module 03 - Preparing for Dynamic Content

## 3.1 - Import SQLite

@pytest.mark.app-import-sqlite At the top of `app.py` import the built-in `sqlite3` library.

## 3.2 - Import Global Namespace

@pytest.mark.app-import-global-namespace To provide access to the database throughout the application import the global helper `g` from `flask`. **Hint: the `from` statement already exists add `g` to the `import` comma separated list.** 

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

## 3.10 - Query Database Function Fetchall
@pytest.mark.app-query-database-function-fetchall In the body of `query_db`:
- `fetchall` data from the `cursor` and assign it to a variable called `results`.
- Close the `cursor` with the `close` function. 

## 3.11 - Query Database Function Single
@pytest.mark.app-query-database-function-single Next, in the function body of `query_db` add a test if `one` is `True`:
- if true return a ternary if, `results[0] if results else None`.
- else return all `results`.

## 3.12 - Close the Connection

@pytest.mark.app-close-the-connection In order to make sure the database connection is closed when the `app_context` is torn down:
- Create a function in `app.py` called `close_connection`.
- Add a parameter called `exception` to the parameter list.

In the function body:
- Call `getattr` with three arguments `g`, `'_database'`, and `None` 
- Assign the return value to a `db` variable. 
- If `db` is not `None` `close` the `db`. 

## 3.13 - Close the Connection Decorator

@pytest.mark.app-close-the-connection-decorator To ensure the `close_connection` function is called when the `app_context` is destroyed give decorate it with `@app.teardown_appcontext`.

# Module 04 - Display All Jobs

## 4.1 - Template Macros

@pytest.mark.template-macros In the template folder create a new file called `_macros.html`. 

## 4.2 - Show Job Macro Definition

@pytest.mark.show-job-macro-definition In `_macros.html` create a template macro, using the `macro` tag, called `show_job`. `show_job` should take one parameter called `job`. Don't forgot to end the macro.

## 4.3 - Show Job Macro HTML

@pytest.mark.show-job-macro-html Locate the `template.html` file in the root of the project. Open it and find the code labeled 
`<!-- show_job -->`. Copy the code to the body of the `show_job` macro in `_macros.html`.

## 4.4 - Show Job Macro Header

@pytest.mark.show-job-macro-header Still in the body of  the `show_job` macro in `_macros.html` find the `<p>` tag with a class of `card-header-title`. 
- Add an `<a>` tag with an `href` of `{{ url_for('job', job_id=job['id']) }}`. 
- The content should be `{{ job['title'] }}`. 

## 4.5 - Show Job Macro Body

@pytest.mark.show-job-macro-body Next find the `<div>` with a class of `content` in the `show_job` macro and add a `<p>` tag. 
In `<p>` tag add the following: 
- `<a>` tag with an `href` of `{{ url_for('employer', employer_id=job['employer_id']) }}`.The content should be `{{ job['employer_name'] }}`. 
- Line break
- ${{ job['salary'] }} 
- Line break
- {{ job['description'] }}

## 4.6 - Show Jobs Macro Definition

@pytest.mark.show-jobs-macro-definition In `_macros.html` create a template macro using the `macro` tag call it `show_jobs`. `show_jobs` should take one parameter called `jobs`. Don't forgot to end the macro.

## 4.7 - Show Jobs Macro For Loop

@pytest.mark.show-jobs-macro-for-loop Still in `_macros.html` and in the body of the `show_jobs` macro add the following HTML:
- Add a `<div>` with two classes `columns` and `is-multiline`.
- In this `<div>` add a `for in` loop that loops through all jobs. **Note: Use the `{% %}` template syntax, don’t forget about ending the `for` loop.**

## 4.8 - Show Jobs Macro For Loop Body

@pytest.mark.show-jobs-macro-for-loop-body In the body of the `for` loop add a `<div>` with two classes `column` and `is-half`.  
- In this `column` `<div>` add a call to the `show_job` macro passing in a individual `job` from the `for` loop.

## 4.9 - Import Macros

@pytest.mark.import-macros In `templates/layouts.html` import the `show_job`, and `show_jobs` macros using the following code:
```
{% from '_macros.html' import show_job, show_jobs with context %}
``` 
**Notes: Because each template extends `layouts.html` all of them will have access to these two new macros.**

## 4.10 - Import Macros

@pytest.mark.import-macros Copy the HTML structure of the `index.html` from `templates.html`. Paste in the new block replacing the existing `content` block.

## 4.11 - Display All Jobs

@pytest.mark.display-all-jobs In the `index.html` template above the `{% endblock %}` add a call to the `show_jobs` macro passing in the argument `jobs`.

## 4.12 - Gather All Jobs

@pytest.mark.gather-all-jobs In `app.py` locate the `jobs` function. 

Above the `render_template` function, call the `query_db` function:
- Pass in the SQL statement: `'SELECT job.id, job.title, job.description, job.salary, employer.id as employer_id, employer.name as employer_name FROM job JOIN employer ON employer.id = job.employer_id'`. 
- Assign the results of the call to a variable called `jobs`. 
- In the `render_template` function, pass a keyword argument of `jobs=jobs`.

**Preview**
    
At this point you can see all jobs on the homepage:

- Open a terminal at the root of the project
- Run the command `flask run`. 
- Open a browser and navigate to the URL: `http://localhost:5000`. 

**Note: Appending `/jobs` should display the same page.**

# Module 05 - Display Individual Jobs

## 5.1 - Job Template

@pytest.mark.app-job-route We need a template to display an individual job. Create a new file called `job.html` in the `template` folder. 

In the file use an `extends` template tag to inherit `layout.html`. 

After the `extends` tag add a call to the `show_job` macro passing in `job`. **Note: Use the `{{}}` for the macro call.**
 
## 5.2 - Job Route Function

@pytest.mark.app-job-route-function In `app.py` create a function called `job`. In the body return a call to the `render_template` function passing in the newly created `job.html` template.

## 5.3 - Job Route Decorator

@pytest.mark.app-job-route-decorator We only need one job from the database, we will use the `query_db` function passing in a query with a where clause. In the where clause we will need a `job_id`. We are going to get this from the URL. 

Still in `app.py`, add a route decorator with the URL path `/job/<job_id>` to the `job` function. 

## 5.4 - Job Route Parameter

@pytest.mark.app-job-route-parameter. To use the `job_id`, received from the URL, we need to pass it to the `job` function. Add `job_id` to the parameter list of the `job` function. 

## 5.5 - Job Route Data

@pytest.mark.app-job-route-data In the `job` function, above the `render_template` function, call the `query_db` function and assign the results of the call to a `job` variable. 
Pass these three arguments to `query_db`: 
- SQL Query: `'SELECT job.id, job.title, job.description, job.salary, employer.id as employer_id, employer.name as employer_name FROM job JOIN employer ON employer.id = job.employer_id WHERE job.id = ?'`
- List Literal: [job_id]
- True: This will bring back only one result.

## 5.6 - Job Route Pass Data

@pytest.mark.app-job-route-pass-data The template needs access to the job data. Let's pass the newly created variable `job` to the `render_template` function. This is done using the keyword argument syntax `job=job`.

**Preview**
    
At this point you can see an individual job:

- Open a terminal at the root of the project
- Run the command `flask run`. 
- Open a browser and navigate to the URL: `http://localhost:5000/job/1`. 

# Module 06 - Display Individual Employers

## 6.1 - Employer Template

@pytest.mark.employer-template To display an employer create a new file called `employer.html` in the `templates` folder. Open `templates.html`, find the appropriate block of HTML and copy and paste it to `employer.html`. 

To the top of the file inherit from the `layout.html` template by using an `extends` template tag.

## 6.2 - Employer Template Details

@pytest.mark.employer-template-details Still in `employer.html` as the first thing in the template block add the following HTML:

- `<div>`
- Nested in the `<div>` add an `<h1>` with the content {{ employer['name'] }}
- Nested in the `<div>` add a `<div>` with a class of `description`
- Nested in the description `<div>` add a`<p>` with the content {{ employer['description'] }}

## 6.3 - Employer Template All Jobs

@pytest.mark.employer-template-all-jobs Below the `<h2>` Jobs header in `employer.html` add a call to the `show_jobs` macro passing in `jobs`.

## 6.4 - Employer Template Reviews

@pytest.mark.employer-template-reviews Open `employer.html` and find the review `<h2>`, remove the comment surrounding the empty `{% %}` template tag. To this tag add a `for in` loop to loop through all `reviews`. Add the `endfor` directive to the second empty `{% %}` template tag, don't forget to the remove the comment. 

## 6.5 - Employer Template Review Stars

@pytest.mark.employer-template-reviews Still `employer.html` in the `<div>` with a class of `media-left` add this for loop:

```
{% for _ in range(1, review['rating']): %}
  <span class="fa fa-star checked"></span>
{% endfor %}
```

## 6.6 - Employer Template Review Details

@pytest.mark.employer-template-review-details Still in `employer.html` in the `content <div>` add a paragraph tag. In the paragraph display the details of a review:

- `title` (Recommend Style: `<strong>`)
- `status`(Recommend Style: `<small>`)
- `date` (Recommend Style: `<small>`)
- `review`

## 6.7 - Employer Route

@pytest.mark.app-employer-route The template we have just built needs access to employer, job, and review data. Let's create a new function in `app.py` called `employer`. 

Add a route decorator with a URL pattern of `/employer/<employer_id>`.

In the body return a call to the `render_template` function passing in the `employer.html` template.

## 6.8 - Employer Route Employer Details

@pytest.mark.app-employer-route-employer-details Still working with the `employer` function add `employer_id` to the parameter list so that we have access to this value. Above the `render_template` function make a call to `query_db` and assign the return value to `employer`. 

Pass the following arguments to `query_db`:

- SQL Query: 'SELECT * FROM employer WHERE id=?'
- List Literal: [employer_id]
- True: This will bring back only one result.

In the `render_template` function, pass a keyword argument of `employer=employer`.

## 6.9 - Employer Route Employer Jobs

@pytest.mark.app-employer-route-employer-jobs On the employer details page, we want to display all of the employers' jobs. In the `employer` function in `app.py` below the `employer` variable, add a call to the `query_db` function and assign the results to a variable called `jobs`.  Pass the function two arguments: 

- SQL Query: `'SELECT job.id, job.title, job.description, job.salary FROM job JOIN employer ON employer.id = job.employer_id WHERE employer.id = ?'`
- List Literal: [employer_id]

In the `render_template` function, add another keyword argument of `jobs=jobs`

## 6.10 - Employer Route Employer Review

@pytest.mark.app-employer-route-employer-reviews Still in the `employer` function in `app.py` below the jobs query add a new query to get all review for the employer. Make a call to `query_db` and assign the return value to `reviews`. Pass in the arguments:

- SQL Query: 'SELECT review, rating, title, date, status FROM review JOIN employer ON employer.id = review.employer_id WHERE employer.id = ?'
- List Literal: [employer_id]

In the `render_template` function, add another keyword argument of `reviews=reviews`

**Preview**
    
At this point you can see an individual employer:

- Open a terminal at the root of the project
- Run the command `flask run`. 
- Open a browser and navigate to the URL: `http://localhost:5000/employer/1`. 

# Module 07 - Employer Reviews

## 7.1 - Review Route

@pytest.mark.app-review-route In `app.py` below the `employer` function create a new function called `review`. Add `employer_id` to the parameter list. 

Add a route decorator with a URL pattern of `/employer/<employer_id>/review`. Also add a keyword argument `methods` set to a tuple with two values: `'GET'` and `'POST'`.

In the body of the function return the `render_template` function passing in the `review.html` template and a keyword argument of `employer_id=employer_id`.

## 7.2 - POST Request Check

@pytest.mark.app-review-post-request-check In the body of the `review` above the render_template function call, create an `if` statement that checks if `request.method` is `'POST'`. 

- In the `if` statement create four variables `review`, `rating`, `title`, and `status`. Set them equal to their respective `request.form` values i.e. `request.form['review']`. 
- Create a `date` variable assign it todays date formatted like '08/10/2018`. **Hint: Use `now()` and `strftime("%m/%d/%Y")`. If you use `now()` add an `import datetime` statement to the top of `app.py`.**

## 7.3 - Insert Review

@pytest.mark.app-review-insert-review Still in the `review` function below the variables in the `if` statement connect to the database, insert the form values, and commit the changes. Follow these steps:

- Assign a `db` variable to a call to `get_db()`
- `execute` the following SQL statement: `'INSERT INTO review (review, rating, title, date, status, employer_id) VALUES (?, ?, ?, ?, ?, ?)'` passing the values: `(review, rating, title, date, status, employer_id)`
- `commit` the changes to the database.
- return a redirect taking the user back to the employer page. **Hint: use `redirect()` and `url_for()` (pass a keyword argument of `employer_id=employer_id`) both of which need to be imported from flask.**

## 7.4 - Review Form Cancel

@pytest.mark.review-form-cancel Open `review.html` and find the cancel anchor tag. Add an `href` attribute with a value of `{{ url_for('employer', employer_id=employer_id) }}`.

