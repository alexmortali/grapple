Code Institute - Full Stack Frameworks with Django Milestone Project 
Grapple
by Alex Mortali  

[![Build Status](https://travis-ci.org/alexmortali/project-four-grapple.svg?branch=master)](https://travis-ci.org/alexmortali/project-four-grapple)

This is an online ecommerce store where users come to view/purchase BJJ Equipment and training gear.
Users can sign up, search and filter products, add products to their cart and purchase products. 
There is also a news and events section to keep users up to date.

![Grapple screen examples](https://alex-grapple.s3.eu-west-2.amazonaws.com/static/jumbo-images/readme-image.png)

# Demo  

A live version of the site can be found [here](https://final-project-grapple.herokuapp.com/)

A superuser has been created with the credentials:
> username: admin  
> password: adminpassword

# UX  

#### Wireframes  
All Wireframes can be found [here.](https://github.com/alexmortali/project-four-grapple/tree/master/documentation/wireframes) 

The website is mobile first with a simple layout. For a lot of features on the home page and products a card layout is used, this looks good on both mobile and desktop.
There are many features that make the site user friendly such as being able to search for products within the navbar, filter products by category and then filter those by 
price, name, ascending and descending. The navbar is accessible from all pages at the top of the page meaning if a user has an idea they perhaps can't find, they can search the product within 2 clicks from any given page.

#### Focus
The focus of the layout of the dashboard is to keep it simple so users can easily interact with the data. This is done by using a neutral colour scheme, a simple layout where each area is clearly distinguished from the next. 
It is also important for users to navigate the site easily. This is why I have included back links so users can return to the previous page in one click.
To make the site more engaging I have added feauters such as the news app for users to read articles and the reviews app so users can see what previous customers think 
about the products, for an ecommerce site this could lead to more sales.

#### Users 
The users of the website will be Jiu Jitsu practitioner looking for clothing / equipment or looking to stay upto date on Jiu Jitsu news.  

#### What Can They Do
Users can interact with the site in many ways.. They can:
  - Create an account  
  - Login / Logout  
  - Reset their Password  
  - View Products  
  - Search Products  
  - Order Product listings  
  - Add Products to their Cart  
  - Pay for products @ Checkout  
  - Read New Articles  
  - Add their own reviews  

#### User Stories  
  - I would like to purchase mulitple items at once.  
  - I would like to be able to leave reviews on products.  
  - I would like to view similar products of the same category in a list.  
  - I would like to create my own account.  
  - I would like to read other users reviews on products.  
  - I would like access to blog articles about Jiu Jitsu without creating an account.
  - I would like to see the contact information of the company should I need to contact them.  

#### Colour Pallet  
The main consideration for the colour pallet was to keep it neutral to not distract users from what there looking for unless I needed to. For example to navbar is a very light shade of grey compared the white color of the body, this shows a clear separation but is also very easy on the eye. However when I needed to grab the users attention brighter colors are used such as red/green and blue to grab the users attention. 
For example blue is used for links as most users will be acclimatized to this as it is the standard color used across the web.  

Red is used to be more eye catching and stand out. It used in the reviews section of the product detail page to highlight the average review rating and each reviews rating. I have highlighted these numbers as they are the key point of information for a review, therefore a user can come to this section and gather information very quickly rather than all the information blending into one.  

Green is used for any buttons that can be considered progressive or that this button will submit something and take action. For example when searching products, when submitting forms, when adding something to your cart. They are all progressive actions and by keeping the same color for all of these actions aids the user when using the site.  

#### Typography
For the font 'Roboto' is imported from [google fonts](https://fonts.google.com/) and used throughout the site. It is a clear and simple font that is easy to read and does not interupt the users interaction with the site. A soft black is also used for the font accross the site, keeping it consistent and easy to read.

#### Design Changes
When coming to the end of development I felt like some pages lacked style and iterest. This is why I chose to the shadow class to cards and buttons, it allows each element to stand out on the page. This is particularly good when viewing the news home page or all products page as it stops all the elements blending in together and allows each item to be differentiated from the next. 

Along with adding shadows I made some unplanned changes to the about page. This page was particularly boring so I added a counter section which the user will see when they load the page. The interaction with the user by seeing the numbers go up may make them more interested in the page and go on to read the about content.

# Set Backs
- There was only one real set back during the development process. This was towards the beginning of development when I originally chose to use class based views. Having no experience in class based views it proved very tricky for my and was taking far to long to develop along with myself not having a deep understanding of what I was creating. This lead to me switching back to function based views and development was back on track.

# Features  
### Current Features  
  #### Sign Up:
   - This allows users to fill in a form and create an account. If a username already exists the user will be told to try another username. If the passwords don't match the user will also be told.  

  #### Login:
   - This allows users to login to their account. It checks to see if the username exists, if it doesn't it tells them. If it does it checks the password they have entered vs the password stored in the database. If they match the user is logged in and returned to the home page, if they don't the user is notified that the passwords don't match. Once logged in a user will now have access to their cart and from here they can go on to purchase products.  

  #### Reset Passowrd:
  - If a user has forgotten their password then they can reset it. They will receive and email which will contain a link allowing them to reset their password.  

  #### View Products:
   - Users can view products of their liking. From the navbar they can select 'All Products' to view all of the products. They can also view products by their category by selecting that option from the dropdown choices.

  #### Search Products:
   - Users can search products from the navbar. If what they have typed is in any of the product names then these products will be shown to them.

  #### Order Product Listings:
   - Once a user is on a products listings page they can order the products. They can choose from Price: Low to High / High to Low or Name: A to Z / Z to A.

  #### Add Products to their Cart:
   - From the products listings page a user can select the size and quantity of the item they want to purchase and add it to their cart. This is accessible from the navbar and on this will show a an overview of the items they have added including the cost of each item and a total of all their items. They can continue shopping or proceed to checkout from this page.

  #### Pay for products @ Checkout:
   - When a user has finished shopping and has items in their Cart they may pay for them. At the checkout page user will fill out 2 forms. One for their address and one for payment information. If both forms are valid the user clicks 'Pay Now' to submit the forms and they are return to the home page with a message saying their order is confirmed.

  #### Read News Articles:
   - From the Navbar users can access the news app. Here users can select different articles to read about different subjects. On each article page they can go straight to the 5 newest article pages.

  #### Add Reviews:
   - Users can leave reviews for products they wish too. Users simply fill out a form choosing the product, giving the review a title and a rating the submit the form to leave the review.
  
  #### Read Reviews:
   - Users can read other users reviews at the bottom of the products page. A good example of multiple reviews being added to one product is [here](https://final-project-grapple.herokuapp.com/products/ibjjf-2020-short-sleeve/). This should help to illustrate the design thinking of using red to highlight the rating, as menntioned above. 

  #### Logout:
   - This allows users to Logout out of their profile. This link is in the nav and is accessible from all pages. It logs the user out and send them to home page telling them they have been logged out.

### Features Left To Implement  
 - Add a my profile page. Here users could see their previous orders, save an address for easier checkout and save products to a list that could be viewed from here.
 - Add a carousel to product detail page so products and contain more than one image.

# Technologies Used   

- [Visual Studio Code](https://code.visualstudio.com/): Was used to code the project.
- [GitHub](https://github.com/): Used as a remote repository for all project code with git version control.

#### Front End Technologies  
 - [HTML](https://html.com/): HTML is used as the skeleton of the website.  
 - [CSS](https://devdocs.io/css/): CSS is used to control the presentation of the website.    
 - [jQuery(3.3.1)](https://jquery.com/): Javascript framework used to for Bootstrap functions.
 - [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript): Javascript is used for vaiours functions such as processing stripe payments.
 - [Google Fonts](https://fonts.google.com/): Google font Roboto is used across the site. 
 - [Google Maps Api](https://cloud.google.com/maps-platform/): Used on the contact page to display location.
 - [Font Awesome](https://fontawesome.bootstrapcheatsheets.com/): Font awesome icons help style the site.  
 - [Vanilla Top](https://www.npmjs.com/package/vanillatop) Allows users to return to the top of the page.

#### Frameworks  
- [Django](https://www.djangoproject.com/): This project uses Django as it's framework to connect the back end to the front end.  
- [Bootstrap(4.3.1)](https://getbootstrap.com/): Bootstrap has been used as a framework to make the site responsive.  

#### Back End Technologies  
 - [Python(3.7.6)](https://www.python.org/doc/): The language used for all backend functions on this project.  
 - [Heorku](https://www.heroku.com/): Hosts the deployed version of this project.  
 - [Heroku Postgres - PostgreSQL](https://devcenter.heroku.com/categories/heroku-postgres): Relational database management system.
 - [Amazon S3](https://aws.amazon.com/free/storage/): Used to store staticfiles and media folders and files.
 - [Stripe](https://stripe.com/gb): Stripe is used to handle payments securely.

# Testing  

### Validator Tests Conducted 
 - HTML Code was put through [W3 HTML Validator](https://validator.w3.org/) which reported minor issues such as "The element button must not appear as a descendant of the a element." This has not been changed as it is done for design reasons and the funcitonality still works perfect.
 - CSS Code was put through [W3 CSS Validator](https://jigsaw.w3.org/css-validator/) which reported no problems.
 - Java Script Code was put through [Esprima Syntax Validator](https://esprima.org/demo/validate.html) and was found to be syntactically valid.
 - All python code was put through [PEP8 Validator](http://pep8online.com/) with no problems, other than some white space at the end of lines and blank lines between functions.
 - The site was tested on Chrome / Safari and Micosoft Edge on multiple devices including iPhone 7, iPad, laptop and desktop. To ensure the site is responsive and responds correctly the site was contanstly tested on chrome developer tools throughout development.

#### Automated testing
Each app has their own tests created using Django TestCase class. Views, forms and Models were tested as much as possible using unit tests. In all, 32 tests were written. All tests pass successfully.

Travis-CI integration has been completed and also shows all tests completing successfully, with the project showing as "build: passing".

#### Manual testing 
Along with the automated testing the website was constantly tested during the development process. Browser developer tools such as chrome developer tools were used to test the responsivity of the sire along with responses from the server. Extensive manual testing has been completed to check that the site performs as it should in different environments and in different browsers. During and after each piece of the site was developed it was manually tested to ensure it works properly.

#### Example of manual tests below:
##### Home Page
 - Click on navigation links and confirm they are going to the correct pages
 - If user is not logged in, "Login/Register" is displayed in the navbar and clicking the links will bring you to the relevant page.
 - If user is logged in, "Cart/Logout" is displayed in the navbar and clicking the links will bring you to the relevant page..
 - Click on links to featured categories and ensure they are going to the correct pages.
 - Click on footer links and confirm they are going to the correct pages
 - Click on news articles 'read more' links and ensure they go to correct article.
 - Ensure arrow displays when scrolling down the page and when clicked return you to the top of the page.
 - Ensure featured categories links transform when hovered over.

##### Login Page
 - Enter correct information into the form and ensure user is signed in and redirected to home page with correct message.
 - Enter an inccorect username/password combination and ensure correct error message is displayed.
 - Enter no information and submit the form and ensure the required fields message comes up.

##### Registration Page
 - Enter information into the form and create an account and ensure user is signed in and redirected to home page with correct message.
 - Enter an inccorect password combination and ensure correct error message is displayed.
 - Enter no information and submit the form and ensure the required fields message comes up.
 - Enter an existing users username to the form with other correct information and ensure the correct error message displays.

##### About Page
 - Ensure correct image is shown.
 - Load the page and observe the count javascript working correctly. Some adjustments to the timing here were made.

##### Contact Page
 - Ensure Google Map is showing correct location.
 - Click on 'view larger map' and ensure page opens in different browser and correct location is shown.

##### News Home Page
 - Confirm that only featured posts are shown in the featured posts section.
 - Click on Home back link and confirm it goes to Home page.
 - Click on News posts 'read more' link and confirm it goes to the correct article page.

##### News Post Page
 - Confirm that correct information is displaying for the article.
 - Click on Home/News back links and confirm it goes to relevant page.
 - Click on latest article links and confirm they go to the correct article page.

##### All Products Page
 - Confirm that All products are displaying.
 - Check that pagination is working. This was done by lowering the number of items per page to 1.
 - Click on Home back link and confirm it goes to relevant page.
 - Click on each product and confirm they go to the correct product page.
 - Ensure when hovering over each product the correct transitions are occuring.
 - Check that all the sort options are loading from the selection box.
 - Check that products reorder themselves once a sort option has been submitted.

##### Products by Category Page
 - Confirm that only products withing the category are displaying.
 - Confirm that the page title is the category tite.
 - Check that pagination is working. This was done by lowering the number of items per page to 1.
 - Click on Home/All Products back links and confirm it goes to relevant page.
 - Click on each product and confirm they go to the correct product page.
 - Ensure when hovering over each product the correct transitions are occuring.
 - Check that all the sort options are loading from the selection box.
 - Check that products reorder themselves once a sort option has been submitted.

##### Product Detail Page
 - Confirm that correct information is displaying for the product.
 - Click on Home/category back links and confirm it goes to relevant page.
 - Check to Size / Quantity forms are displaying correctly
 - Click on 'Add to Cart' button and check the product has been added with the correct size / quantity.
 - Check that the reviews section is displaying or that it says 0 reviews.
 - Click on 'leave a review' link and ensure it take you to the 'add review' form.

##### Add Review Page
 - Confirm that the add review form is loading correctly.
 - Click on Home/All Products back links and confirm it goes to relevant page.
 - Submit the form with no information to ensure the form shows fields that are needed.
 - Test max characters out on form fields.
 - Fill in form correctly and submit it to ensure review is added and user is returned to product page.

##### Cart Page
 - Confirm that the cart loading correctly with the correct product / total.
 - Click on coninue shopping/proceed links and confirm it goes to relevant page.
 - Adjust the quantity of an item and ensure the new quantity is updated correctly.
 - Delete an item from the cart and ensure it has gone.
 - Visit the cart page with no items in cart to ensure proceed button isn't displaying.

##### Checkout Review Page
 - Confirm that the review table is loading correctly with the correct products / total.
 - Click on coninue proceed link and confirm it goes to relevant page.
 - Click on the 'back to cart' link and ensure it goes to the cart page.

##### Checkout Payment Page
 - Confirm that the review table is loading correctly with the correct products / total.
 - Click on the 'back to review' link and ensure it goes to the review page.
 - Ensure both the address form and card details form are loading correctly.
 - Submit the forms with no information the check form shows required fields.
 - Submit the forms with the correct information to ensure the forms are saved and user is returned to home page with correct message.
 - Submit the forms with incorrect information to ensure the forms respond with correct error message.

##### Issues when testing
 - For the majority of the development process there was very little set backs that could be considered an issue. However there was one. In the orignal wireframes the forms for address and payment were supposed to be split and load on different pages address being first then onto payment. However I could not get the data to save correctly so quickly decided to create the checkout/review page and then have both forms on one page, the checkout/payment page. With this the plan was to have the order review at the top of the page and then have both forms side by side below it with the submit button below them. However when both forms were side by side, only on the Chrome browser which ever form was on the left hand side would render but not be editable, you could not select any field to enter data to. Using Chrome Dev tools I managed to narrow this down to the float-left class being used. Once removing this class it made sense to just leave the forms on top of eachother going down the page to avoid further problems. Now forms work properly and users can purchase products.

##### Testing to ensure user stories are met
- Making sure the user stories were met was a key consideration when testing. All of the stories have been met as the above tests cover all of those scenarios.

##### Other Tests
Other tests were conducted to check the security of the site. For example trying to manipulate the url, when I was logged out I entered all the urls of the site which require a user be logged. All of these redirected me to the login page. I also tried when logged in going the a page that requires login such as checkout/payment, loggin out, then clicking back page on the browser and this also sent me to the login page.

# Deployement
This project was developed using [Visual Studio Code](https://code.visualstudio.com/). [Git](https://git-scm.com/) was used for version control and backup. From Github the site is deployed to [Heorku](https://www.heroku.com/).

The results of this can be seen here.

These steps were carried out:
- Install Python3 and Django to run the application.
- Create the project - grapple
- Create git respository, add files not required to gitignore. Git add the rest and commit with 'Initial Commit'
- Set up file structure including templates and static files.
- Create env.py file and add to gitignore.
- Generate a requirements.txt file so Heroku can install the required dependencies to run the app.
- Create a Procfile to tell Heroku what type of application is being deployed, and how to run it.
- Create a new app on Heroku to host and run the site.
- In Heroku add a Postgres Database
- Retrieve the Postgres DB url and add to env.py
- Go to the settings.py file and update the DB details to look at the DB hosted on Heroku
- This is followed by migrations to create tables on heroku database.
- Create a super user on the new DB.
- In Heroku, connect newly created app to the correct github repository.
- Set up config vars.
- Create a bucket on Amazon S3.
- Create a custom_storages.py file and add static file settings and media storage information to the setting.py file.
- Add DISABLE_COLLECTSTATIC with the value of 1 to the Config Variables on Heroku.
- On completion of the project set debug mode to False in the settings.py file.
- On Heroku find the "Manual Deploy" section, select the master branch of your repo, and "Deploy Branch"

#### Cloning
You must have the following tools installed to deploy this project locally:
 - Python
 - Git
You must also have an account set up for the following services:
 - Amazon AWS + S3 Bucket
 - Stripe
 1. Clone this repository
 2. Open a terminal or command prompt
 3. Install requirements
 4. Set up environment variables
 5. Add this file to your .gitignore
 6. Migrate the models to create the database tables
 7. Create a superuser account so you can access the Django Admin Panel
 8. Run the server locally
 9. You should now be able to navigate to the local link in the terminal. Append '/admin' to the end to access the admin panel, and log in using the user you just created

# Credits   
#### CONTENT
- All content besides what is mentioned below was written by my self.  
- Some content such as products were taken from various sites such as [Tatami](https://www.tatamifightwear.com/) and [Made 4 Fighters](https://made4fighters.com/).  
- Other content such as news articles were taken from various blogs such as [Renzo Gracie](http://www.renzogracie.com/jiu-jitsu).  
- Background images were all licensed from [Adobe Stock](https://stock.adobe.com/uk/)

#### ACKNOWLEDGEMENTS
- Various tutorial were used to aid the development of this project - [Solving NoReverseMatch](https://www.youtube.com/watch?v=SFgnKRHWHIg), [Categories](https://www.youtube.com/watch?v=o6yYygu-vvk&t=747s), [Pagination](https://www.youtube.com/watch?v=acOktTcTVEQ), [Reviews](https://www.youtube.com/watch?v=IVyc06bASSg&list=PLeyK9Dw9ShReHUdt5Nh2qlgF6keN6DI7z&index=31).
- Big thanks to tutors and my mentor at Code Institue for their help and support throughout this project.