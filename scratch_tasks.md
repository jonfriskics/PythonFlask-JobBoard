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
