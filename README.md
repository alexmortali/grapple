Code Institute - Full Stack Frameworks with Django Milestone Project 
Grapple
by Alex Mortali  

This is an online ecommerce store where users come to view/purchase BJJ Equipment and training gear.
Users can sign up, search and filter products, add products to their cart and purchase products. 
There is also a news and events section to keep users up to date.

# Demo  

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
  - I would like to view similar product of the same category in a list.  
  - I would like to create my own account.  
  - I would like to read other users reviews on products.  
  - I would like to see the contact information of the company should I need to contact them.  

#### Colour Pallet  
The main consideration for the colour pallet was to keep it neutral to not distract users from what there looking for unless I needed to. For example to navbar is a very light shade of grey compared the white color of the body, this shows a clear separation but is also very easy on the eye. However when I needed to grab the users attention brighter colors are used such as red/green and blue to grab the users attention. 
For example blue is used for links as most users will be acclimatized to this as it is the standard color used across the web.  

Red is used to be more eye catching and stand out. It used in the reviews section of the product detail page to highlight the average review rating and each reviews rating. I have highlighted these numbers as they are the key point of information for a review, therefore a user can come to this section and gather information very quickly rather than all the information blending into one.  

Green is used for any buttons that can be considered progressive or that this button will submit something and take action. For example when searching products, when submitting forms, when adding something to your cart. They are all progressive actions and by keeping the same color for all of these actions aids the user when using the site.  

#### Typography
For the font 'Roboto' is imported from [google fonts](https://fonts.google.com/) and used throughout the site. It is a clear and simple font that is easy to read and does not interupt the users 
interaction with the site. A soft black is also used for the font accross the site, keeping it consistent and easy to read.

# Features  
### Current Features  
  #### Sign Up:
   - This allows users to fill in a form and create an account. If a username already exists the user will be told to try another username. If the passwords don't match the user will also be told.  

  #### Login:
   - This allows users to login to their account. It checks to see if the username exists, if it doesn't it tells them. If it does it checks the password they have entered vs the password stored in the database. If they match the user is logged in and returned to the home page, if they don't the user is notified that the passwords don't match.  

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

  #### Logout:
   - This allows users to Logout out of their profile. This link is in the nav and is accessible from all pages. It logs the user out and send them to home page telling them they have been logged out.

### Features Left To Implement  
In the future I would like to add a my profile page. Here users could see their previous orders, save an address for easier checkout and save products to a list that could be viewed from here.

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
 - [Stripe](https://stripe.com/gb): Stripe is used to handle payments securely.
 - [Vanilla Top](https://www.npmjs.com/package/vanillatop) Allows users to return to the top of the page.

#### Frameworks  
- [Django](https://www.djangoproject.com/): This project uses Django as it's framework to connect the back end to the front end.  
- [Bootstrap(4.3.1)](https://getbootstrap.com/): Bootstrap has been used as a framework to make the site responsive.  

#### Back End Technologies  
 - [Python(3.7.6)](https://www.python.org/doc/): The language used for all backend functions on this project.  
 - [Heorku](https://www.heroku.com/): Hosts the deployed version of this project.  
 - [Heroku Postgres - PostgreSQL](https://devcenter.heroku.com/categories/heroku-postgres): Relational database management system.
 - [Amazon S3](https://aws.amazon.com/free/storage/): Used to store staticfiles and media folders and files.

# Testing  

### Tests Conducted 


#### Manual testing


# Deployement


# Credits   
#### CONTENT
- All content besides what is mentioned below was written by my self.  
- Some content such as products were taken from various sites such as [Tatami](https://www.tatamifightwear.com/) and [Made 4 Fighters](https://made4fighters.com/).  
- Other content such as news articles were taken from various blogs such as [Renzo Gracie](http://www.renzogracie.com/jiu-jitsu).  
- Background images were all licensed from [Adobe Stock](https://stock.adobe.com/uk/)

#### ACKNOWLEDGEMENTS
- Various tutorial were used to aid the development of this project - [Solving NoReverseMatch](https://www.youtube.com/watch?v=SFgnKRHWHIg), [Categories](https://www.youtube.com/watch?v=o6yYygu-vvk&t=747s), [Pagination](https://www.youtube.com/watch?v=acOktTcTVEQ), [Reviews](https://www.youtube.com/watch?v=IVyc06bASSg&list=PLeyK9Dw9ShReHUdt5Nh2qlgF6keN6DI7z&index=31).
- Big thanks to tutors and my mentor at Code Institue for their help and support throughout this project.