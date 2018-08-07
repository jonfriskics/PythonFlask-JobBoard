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

In order to verify that everything is setup correctly, run the following command, which should show you the failing tests. This is good! We'll be fixing this test once we jump into the build step.

```
pytest
```

Every time you want to check your work locally you can type that command, and it will report the status of every task in the project.

## Previewing Your Work

You can preview your work by running `flask run` in the root of your fork and then visit `http://localhost:5000` in your browser.

# Module 01 - Routing

## 1.1 - Import Flask

@pytest.mark.app-import-flask In order to create a flask application Import `Flask` and `render_template` from `flask`.

## 1.2 - Create a Flask Application

@pytest.mark.app-create-flask-app Create an instance of the Flask class called `app`. Pass in the special variable `__name__`.

## 1.3 - Templates Folder

@pytest.mark.templates-folder Create a folder called `templates` in the `jobs` directory.

## 1.4 - Create Index Template

@pytest.mark.index-template In the root of the `templates` folder, create a file called `index.html`. 

## 1.5 - Create the Index Route

@pytest.mark.app-create-index-route We will display all jobs on the index page. To start we will create a basic route that displays the contents of the index template. Create a function called `jobs` and attach a `route()` decorator with the URL of `/`. Add an additional path of `/jobs`. In the body of the function return a call to the `render_template()` passing the `index.html` template.

## 1.5 - Create Employer and Job Templates

@pytest.mark.detail-templates In the root of the `templates` folder, create two files one called `employer.html` and the other called `job.html`.

## 1.6 -Create Detail Routes

@pytest.mark.app-create-detail-routes We need routes for individual employers and jobs. Create two functions one called `employer` and the other called `job`.  Add route decorators to bind these functions with the appropriate URLs: 
- `/employer` to the `employer` function
- `/job` to the `job `function.

In the body of each function return a call to `render_template()` passing the appropriate template.

# Module 02 - Templates

## 2.1 - Create Layout Template

@pytest.mark.layout-template We want each template to have a  consistent look and feel. We can create a base layout that each template can extend. First create a new file called `layout.html` in the root of the `templates` folder. Copy the basic structure of the file from the file called `templates.html`.

## 2.2 - Add Styles

@pytest.mark.add-styles The app will be styled with bulma (bulma.io). Add three link tags to the head of `layout.html`. For the first `href` use mustache syntax `{{}}` and the `url_for()` function to link in the file `css/bulma.css` from the `static` folder. For the second add the file `css/app.css` using the same method. The last link tag should have an `href` value of `https://use.fontawesome.com/releases/v5.2.0/css/all.css`.

## 2.3 - Create Template Files

@pytest.mark.create-template-files We need to create some additional template files. In the `templates` folder create the following files:
- `_job.html`
- `job.html`
- `employer.html`
- `review.html`

Next create a new folder called `admin` in the `templates` folder, then create the following files:
- `index.html`
- `create.html`

## 2.4 - Template Files HTML
@pytest.mark.template-files-html Locate the `templates.html` file in the the root of the project. To prevent having to write all HTML from scratch the HTML structure of several of the template files is given here. Each block has a comment that describes what HTML file, the HTML block, needs to be copied too. Copy each block to the correct file.

## 2.5 - Extend Base Layout

@pytest.mark.extend-base-layout Each of the files list below needs to extend the base layout. This can be done by adding an `extends` directive with `{% %}` template syntax to the top of each file.

- `job.html`
- `employer.html`
- `review.html`
- `admin/index.html`
- `admin/create.html`

## 2.6 - Navigation

@pytest.mark.navigation We want to allow the user to navigate to the admin from the front page. In the `index.html` template file create a link to the main admin page by creating an `<a>` tag nested in the `<div>` with the two classes `columns` and `is-one-fifth`. The `<a>` tag should have an `href` with the value `/admin` and the classes `button`, `is-info`, and `is-pulled-right`. In the `admin/index.html` template file create a link to add a new job by creating an `<a>` tag nested in the `<div>` with the two classes `columns` and `is-one-fifth`. The `<a>` tag should have an `href` with the value `/admin` and the classes `button`, `is-info`, and `is-pulled-right`.

# Module 03 -

## 3.1 -

@pytest.mark.

## 3.2 -

@pytest.mark.

## 3.3 -

@pytest.mark.

## 3.4 -

@pytest.mark.

## 3.5 -

@pytest.mark.

## 3.6 -

@pytest.mark.

## 3.7 -

@pytest.mark.

## 3.8 -

@pytest.mark.

## 3.9 -

@pytest.mark.

## 3.10 -

@pytest.mark.

# Module 04 -

## 4.1 -

@pytest.mark.

## 4.2 -

@pytest.mark.

## 4.3 -

@pytest.mark.

## 4.4 -

@pytest.mark.

## 4.5 -

@pytest.mark.

## 4.6 -

@pytest.mark.

## 4.7 -

@pytest.mark.

## 4.8 -

@pytest.mark.

## 4.9 -

@pytest.mark.

## 4.10 -

@pytest.mark.

## 5.1 -

@pytest.mark.

## 5.2 -

@pytest.mark.

## 5.3 -

@pytest.mark.

## 5.4 -

@pytest.mark.

## 5.5 -

@pytest.mark.

## 5.6 -

@pytest.mark.

## 5.7 -

@pytest.mark.

## 5.8 -

@pytest.mark.

## 5.9 -

@pytest.mark.

## 5.10 -

@pytest.mark.

## 5.11 -

@pytest.mark.

## 5.12 -

@pytest.mark.

## 5.13 -

@pytest.mark.

## 5.14 -

@pytest.mark.

## 5.15 -

@pytest.mark.
