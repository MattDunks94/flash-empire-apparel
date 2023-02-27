# Flash Empire Apparel

<a href="">Flash Empire Apparel</a> is a fully working e-commerce site that demonstrates basic/advanced use of the web framework <a href="https://www.djangoproject.com/">django</a>. The site is targeted for people who are interested in streetwear fashion, tattoo designs and shopping. The site allows users to: 
<ul>
  <li>Sign up and register for an account.</li>
  <li>Browse the store as both a non user and registered user.</li>
  <li>Filter products via category and/or product colour.</li>
  <li>Sort products via price ascending/descending and product name ascending/descending.</li>
  <li>Securely Purchase products as both a non user and registered user.</li>
  <li>Leave product reviews as a registered user.</li>
  <li>Add, remove or edit products as a site administrator.</li>
</ul>

The site is fully responsive on most handheld and desktop devices.

index.html:
<img src="/README/images/homepage.png"> 

## Site Features

### Store Browsing:
<p>Users of the site are able to browse all products in the store. They have access to all products details.</p>

### Filter by Product Category and/or Product Colour:
<ul>
  <li>Category Filter Feature:</li>
  <p>This feature can sort products via category.<br>
      Users can find this category dropdown feature in the main nav.</p>
  <img src="/README/images/categories-dropdwn.png">
  <li>Colour Filter Feature:</li>
  <p>This feature can sort products via product colour.</p>
  <img src="/README/images/colour-filter.png">
</ul>

### Product Sorting:

<ul>
  <li>The users have the ability to sort/filter products and categories using the following features:
    <ul>
      <li>Sort By Feature:</li>
      <p>This feature can sort products via price ascending/descending and product name ascending/descending.<br>
      When a sort by option is selected, it is highlighted in red to notify the user has chosen that sort by method.</p>
      (Sort by 'Price High to Low' selected)
      <br>
      <img src="/README/images/sort-by.png">
      <br>
    </ul>
   </li>
</ul>

### Product Reviews (Site User):
<p>As a registered site user, you can write product reviews.</p>
(Review product form)
<img src="/README/images/product-review-form.png">
<br>
(Product Review whithin the products detail page.)
<img src="/README/images/product-review.png">

### Add, Remove or Modify Products (Site Admin):
<p>As site admin, you can add or modify existing products.</p>
(Add New Product form)
<img src="/README/images/add-product.png">
<br>
(Edit Existing Product Form)
<img src="/README/images/edit-product.png">
(Modify product buttons including the 'Remove Product' button)
<img src="/README/images/edit-product-btns.png">
(Edit Button on product detail page)
<img src="/main/README/images/edit-prod-btn.png">

### Secure Payment:
<p>The site uses a secure payment method. This ensures the user that their payment details and process are secure.</p>
<br>

### Creating Account / Signing In:
<p>Shoppers are able to sign up and register an account.</p>
<br>
<p>Sign Up page:</p>
<img src="/README/images/sign-up.png">
<br>
<p>Login page:</p>
<img src="/README/images/sign-in.png">

### Secure Payment:
<p>The site uses a secure payment method. This ensures the user that their payment details and process are secure.</p>
<br>
(Successfull Payment)
<img src="/README/images/payment-successfull.png">

### Profile Page:
<p>Once shoppers have registered an account, they can access their profile.<br>
Their profile contains delivery details and order history.</p>
<br>
<p>Profile page:</p>
<img src="/README/images/profile-page.png">

## Other Features

### Branding:
<ul>
<li>A logo and banner is provided to make the app look more efficient.</li>
<li>Homepage background image also contains a simplified brand logo, alongside it are products from the site.</li>
</ul>
<p>(Logo and Banner in top header.)</p>
<img src="/README/images/nav-header.png">

### Navbar Features:
<ul>
  <li>Responsive nav. When operating the site on a small device, the nav condenses down to a 'burger' menu.</li>
  <li>Contains all products link which directs the user to all of the stores products.</li>
  <li>A dropwdown menu for all product categories, with each link directing the user to the desired category page.</li>
  <li>Sale link. Takes the user to products that are on offer.</li>
  <li>Also, when logged in, username is displayed within the navbar.</li>
</ul>
<img src="/README/images/nav-header.png">

### Footer:
<ul>
  <li>The footer contains homepage link, social links, shop category links and a subscribe input field</li>
</ul>
<img src="/README/images/footer.png">

### Social Media Pages:
<ul>
  <li>I created two social media pages for my site.<br>
  Both these links can be found in the footer.</li>
  (Facebook Page)
  <img src="/README/images/facebook.png">
  (Instagram Account)
  <img src="/README/images/instagram.png">
</ul>
<img src="/README/images/footer.png">

### Messages / Toasts:
<ul>
  <li>Added meassages/toasts to indicate a successful operation. For example, when a shopper adds an item to their bag, or edits their shopping bag a pop-up message appears indicating the users operation and their details.</li>
  <li>Other messages/toasts include errors, info and warnings. These occur when the user/shopper searches for a product that isn't recognised or when their payment is unsuccessfull.</li>
</ul>
(Successfull message.)
<img src="/README/images/successfull-alert.png">
(Info Alert)
<img src="/README/images/info-alert.png">

### Back To Top Button:
<p>Added back to top button for when users/shoppers are scrolling through the stores products, saves them having to scroll back to the top.</p>
<img src="/README/images/btt-btn.png">

## Features For The Future
<ul>
  <li>Add a remove review feature when signed in as admin</li>
  <ul>
    <li>This allows the admin control over all customer reviews and can remove them if any explicit content is used.</li>
    <li>Creates a more safe environment for the user.</li>
  </ul>
  <li>Image Carousel</li>
  <ul>
    <li>Add a bootstrap carousel to product detail images. This allows the opportunity to really show off the products and their details.</li>
  </ul>
</ul>


## Testing

### Device Testing:
<ul>
  <li>Tested the application on several different devices, such as iPhone (11, SE), iPad air and Google nest hub (2nd gen).</li>
  <li>No bugs or errors returned when testing on these devices.</li>
</ul>

### Browser Testing:
<ul>
  <li>No bugs or errors occurred when testing on the following browsers:</li>
  <ul>
    <li>Google Chrome</li>
    <li>Firefox</li>
    <li>Safari</li>
  </ul>
</ul>

### Lighthouse Validator Results:
<ul>
  <li>Homepage Results:
  <img src="/README/images/homepage-lighthouse.png"></li>
  <br>
  <li>All Product Page Results:
  <img src="/README/images/all-products-lighthouse.png"></li>
  <br>
  <li>Product Detail Page Results:
  <img src="/README/images/product-detail-lighthouse.png"></li>
</ul>

### Bugs & Errors:
<ul>
  <li>Adjust Product Quantity:</li>
  <ul>
    <li>When editing shopping bag I noticed, when adjusting product quantity, you could only adjust the latest product added quantity.<br>
    Think this maybe a Javascript glitch?</li>
    <img src="/README/images/qty-bug.png">
  </ul>
  <li>Value too long error:
    <ul>
      <li>One error I came up against was this 'value too long' error (as seen below).<br>
      I overcame this error by removing my database and creating new one.</li>
      <img src="/README/images/value-too-long-error.png">
      <br>
    </ul>
  </li>
  <li>No Media Files:</li>
  <ul>
  <li>Unfortunately, my final deployed site, on <a href="https://www.heroku.com/">Heroku</a>, does not have any media files. This includes all product           files.<br> Tried to overcome this by altering the AWS media path but unfortunately no luck.</li>
  </ul>
</ul>


## User Experience (UX)

### Design:
<ul>
  <li>Colour Scheme:</li>
  <ul>
    <li>The colour scheme is quite powerful and attractive to the user. The palette consists of black, earth yellow, white and dark red. All four colours create a strong yet vulnerable combination. I wanted colours that represented the name of the brand, Flash Empire, as much as possible. The black and dark red are seen as strong and powerful (Empire), the earth yellow is almost like a gold that represents royalty, wealth (Empire) and the white is used to create a sense of light (Flash) and vulnerability.</li>
  </ul>
    <li>Navigation:</li>
  <ul>
    <li>The navigation is very modern and efficient. There's very little content within the nav, this makes it easy for the user to navigate round the site.</li>
  </ul>
    <li>Icons:</li>
  <ul>
    <li>There are many icons on the app. Icons indicate what the content consists of and/or what it carries out (ex.trash bin indicates remove).</li>
  </ul>
</ul>

## Technologies Used:

### Languages Used:
<ul>
  <li><a href="https://en.wikipedia.org/wiki/HTML5">HTML5</a></li>
  <li><a href="https://en.wikipedia.org/wiki/CSS">CSS3</a></li>
  <li><a href="https://en.wikipedia.org/wiki/JavaScript">Javascript</a></li>
  <li><a href="https://en.wikipedia.org/wiki/Python_(programming_language)">Python</a></li>
</ul>

### Frameworks, Libraries and Programs Used:
<ul>
  <li><a href="https://fonts.google.com/">Google Fonts</a></li>
  <ul>
    <li>Google fonts was used to import the '' font.</li>
  </ul>
    <li><a href="https://fontawesome.com/">FontAwesome</a></li>
  <ul>
    <li>Fontawesome was used to add icons to several elements.</li>
  </ul>
    <li><a href="https://git-scm.com/">Git</a></li>
  <ul>
    <li>Git was used for version control and using the Gitpod terminal to commit and push to GitHub.</li>
  </ul>
  <li><a href="https://github.com/">GitHub</a></li>
    <ul>
    <li>GitHub is used to store the projects code after being pushed from Git.</li>
  </ul>
  <li><a href="https://www.pixelmator.com/pro/">Pixelmator</a></li>
  <ul>
    <li>I used Pixelmator to edit logo, homepage image and product images.</li>
  </ul>
  <li><a href="https://getbootstrap.com/docs/4.3/getting-started/introduction/">Bootstrap4</a></li>
  <ul>
    <li>Bootstrap framework is used for styling, structuring and reponsive development.</li>
  </ul>
  <li><a href="https://en.wikipedia.org/wiki/JQuery">jQuery</a></li>
  <ul>
    <li>jQuery is a fast, small, and feature-rich JavaScript library. It makes things like HTML document traversal and manipulation, event handling and       animation much simpler with an easy-to-use API that works across a multitude of browsers.</li>
  </ul>
    <li><a href="https://www.djangoproject.com/">Django</a></li>
  <ul>
    <li>Django framework was used to create the app/project.</li>
  </ul>
    <li><a href="https://en.wikipedia.org/wiki/Stripe,_Inc.">Stripe</a></li>
  <ul>
    <li>Stripe was used for the payment process integration.</li>
  </ul>
    <li><a href="https://www.heroku.com/">Heroku</a></li>
  <ul>
    <li>Heroku is used for creating my app.</li>
  </ul>
    <li><a href="https://aws.amazon.com/">AWS</a></li>
  <ul>
    <li>AWS is used for storing my static and media files.</li>
  </ul>
</ul>

## Credits:

### Code:
<ul>
  <li>The hover underline effect is from <a href="30secondsofcode.org/css/s/hover-underline-animation/">30secondsofcode.org</a>.</li>
  <li>The slanted div effect is from <a href="html-css-js.com/css/generator/transform/">html-css-js.com</a>.</li>
  <li>I gathered my colour palette from <a href="https://coolors.co">html-css-js.com</a>.</li>
  <li>I followed the <a href="https://codeinstitute.net/">Code Institutes</a> walkthrough project 'Boutique Ado'. This project was a big help, especially,    with the stripe payment backend code.</li>
  <li>The colour filter code was from <a href="https://www.youtube.com/watch?v=exN6RdC_xbE">Youtube</a>.</li>
  <li>I occasionally referenced to <a href="https://stackoverflow.com/">StackOverFlow</a> to overcome any issues.</li>
  
</ul>

### Media:
<ul>
  <li>The logo and branding are from <a href="https://smashinglogo.com/en/">smashinglogo</a>.</li>
  <li>The product graphic print designs are from <a href="https://www.vecteezy.com/">Vecteezy.com</a></li>
  <li>The clothing product images are from <a href="https://www.vistaprint.co.uk/">VistaPrint</a>.<br>
  I used their upload design feature to add the my graphic print designs onto their apparel products, and print screened the resulting images.</li>
</ul>
