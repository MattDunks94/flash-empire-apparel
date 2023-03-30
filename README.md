# Flash Empire Apparel

<a href="https://flash-empire-apparel.herokuapp.com/">Flash Empire Apparel</a> is a fictional B2C e-commerce store that is designed and created using the <a href="https://www.djangoproject.com/">Django</a> web framework. The site's main purpose is selling tattoo inspired streetwear to online customers. 

<img src="/documentation/README/images/amiresponsive.png">

## Table of Contents:
- [Business Model](#business-model)
- [User Experience (UX)](#user-experience-ux)
  - [User Stories](#user-stories)
    - [As Admin](#--as-admin)
    - [As Site User / Shopper](#--as-site-user--shopper)
  - [Database Design](#database-design)
  - [Interaction Design](#interaction-design)
  - [Design](#design)
    - [Mockup Diagrams](#--mockup-diagrams)
    - [Colour Palette](#--colour-palette)
    - [Typography](#--typography)
    - [Imagery](#--imagery)
  - [Features](#features)
    - [Header & Navigation](#header--navigation)
    - [The Homepage](#the-homepage)
    - [Register Account](#register-account)
    - [Signing In](#signing-in)
    - [Signing Out](#signing-out)
    - [All Products](#all-products)
    - [Product Detail](#product-detail)
    - [Add Product Review (For registered users)](#add-product-review-for-registered-users)
    - [Wishlist (For registered users)](#wishlist-for-registered-users)
    - [Blog](#blog)
    - [Blog Post Detail](#blog-post-detail)
    - [Add Blog Post (For super users only)](#add-blog-post-for-super-users-only)
    - [Edit Blog Post(For super users only)](#edit-blog-post-for-super-users-only)
    - [Users / Shoppers Shopping Bag](#users--shoppers-shopping-bag)
    - [Checkout](#checkout)
    - [Successful Checkout](#successful-checkout)
    - [Add Product (For super users only)](#add-product-for-super-users-only)
    - [Edit Product (For super users only)](#edit-product-for-super-users-only)
    - [Footer](#footer)
    - [Facebook Page](#facebook-page)
    - [Instagram Page](#instagram-page)
    - [My Profile Page (For registered users)](#my-profile-page-for-registered-users)
- [Testing](#testing)
  - [HTML Validation](#html-validation)
  - [CSS Validation](#css-validation)
  - [Python Validation](#python-validation)
  - [Lighthouse Reports](#lighthouse-reports)
    - [Homepage Lighthouse Report](#homepage-lighthouse-report)
    - [All Products Page Lighthouse Report](#all-products-lighthouse-report)
    - [Product Detail Page Lighthouse Report](#product-detail-lighthouse-report)
    - [Add Product Page Lighthouse Report](#add-product-lighthouse-report)
    - [Edit Product Page Lighthouse Report](#edit-product-lighthouse-report)
    - [Blog Page Lighthouse Report](#blog-lighthouse-report)
    - [Blog Post Detail Page Lighthouse Report](#blog-post-detail-lighthouse-report)
    - [Bag Page Lighthouse Report](#bag-lighthouse-report)
    - [My Profile Page Lighthouse Report](#profile-page-lighthouse-report)
    - [Wishlist Page Lighthouse Report](#wishlist-page-lighthouse-report)
   - [Manual Testing](#manual-testing)
   - [Device Testing](#device-testing)
   - [Browser Testing](#browser-testing)
- [Deployment](#deployment)
- [Features for the Future](#features-for-the-future)
- [Bugs & Errors](#bugs--errors)
- [Technologies Used](#technologies-used)
  - [Languages Used](#languages-used) 
  - [Frameworks, Libraries & Programs Used](#frameworks-libraries-and-programs-used)
- [Credits](#credits)
  - [Code](#code)
  - [Media](#media)
- [Acknowledgement & Support](#acknowledgement--support)

### Business Model

Flash Empire Apparel is a business to consumer (B2C) fashion retailer that sells tattoo inspired streetwear. We sell a range of products including:
- T-shirts
- Sweatshirts
- Joggers
- Headwear
- Bags


## User Experience (UX)

### User stories
#### - As Admin:
<ul>
  <li>As a Site Admin I can add new products to the site so that I can keep customers interested.</li>
  <li>As a Site Admin I can edit products so that I can update products price, name and image.</li>
  <li>As a Site Admin I can remove products from the store so that when stock runs out and/or product isn't selling well I can remove product from the site.</li>
  <li>As a Site Admin I can create a blog post so that I can show site users what our brand/business has been up to.</li>
  <li>As a Site Admin I can edit a posted blog post so that I can alter any spelling mistakes and/or add content, images etc.</li>
  <li>As a Site Admin I can remove a posted blog post so that I can remove any out of date posts.</li>
</ul>

#### - As Site User / Shopper:
<ul>
  <li>As a Site User I can register for an account so that I have a personal account and can view my profile.</li>
  <li>As a Site User I can receive an account registration confirmation Email so that I can verify my account was successfully created.</li>
  <li>As a Site User I can login and logout with ease so that I can access my personal information.</li>
  <li>As a Site User / Shopper I can view a list of all products so that I can select some to purchase.</li>
  <li>As a Site User / Shopper I can sort all products so that I can identify the desired products through category type and price.</li>
  <li>As a Site User / Shopper I can sort products of a certain category type so that I can view products by name and by price.</li>
  <li>As a Site User / Shopper I can search for products so that I can identify exactly what product I'd like to purchase.</li>
  <li>As a Site User I can save delivery information so that going through checkout will be quicker.</li>
  <li>As a Site User / Shopper I can edit items in my basket so that I can change size, quantity and/or remove item(s).</li>
  <li>As a Site User / Shopper I can securely pay for products so that my order is processed.</li>
  <li>As a Site User I can leave a product review so that I can share my opinion on the product and add a rating.</li>
</ul>

### Database Design
I used [LucidChart](https://www.lucidchart.com/pages/) to create the ERD.

<details>
<summary>Database ERD</summary>

![](/documentation/README/images/erd.jpg)
</details>

### Interaction Design
I used [LucidChart](https://www.lucidchart.com/pages/) to create the following user accessibility / functionality flowchart.

<details>
<summary>Super Users & Site Users Accessibility & Functionality Flowchart</summary>

![](documentation/README/images/accessibility_functionality_flowchart.jpeg)
</details>

### Design
#### - Mockup Diagrams:
Prior to writing any sort of code, I made a few mockup diagrams based on the sites layout.<br>
Diagrams were created using [Wireframe.cc](https://wireframe.cc/)
<details>
<summary>Homepage Mockup Diagram</summary>

![](/documentation/diagrams/homepage.png)
</details>

<details>
<summary>All Products Page Mockup Diagram</summary>

![](/documentation/diagrams/all-products-page.png)
</details>

<details>
<summary>Product Detail Page Mockup Diagram</summary>

![](/documentation/diagrams/product-detail.png)
</details>

<details>
<summary>Blog Page Mockup Diagram</summary>

![](/documentation/diagrams/blog-page.png)
</details>

<details>
<summary>Blog Post Detail Page Mockup Diagram</summary>

![](/documentation/diagrams/blog-post-detail.png)
</details>

#### - Colour Palette:
I used [Coolors](https://coolors.co/) to generate my colour palette.
![](/documentation/README/images/colour-palette.png) <br>
The colour scheme is quite powerful and attractive to the user. The palette consists of black, dark red, earth yellow and white. <br>All four colours create a strong yet vulnerable combination. I wanted colours that represented the name of the brand, Flash Empire, as much as possible. The black and dark red are seen as strong and powerful (Empire), the earth yellow is almost like a gold that represents royalty, wealth (Empire) and the white is used to create a sense of light (Flash) and vulnerability.

#### - Typography:
![](/documentation/README/images/google-font.png)
The font used throughout the site is 'Big Shoulder Display' from [Google Fonts](https://fonts.google.com/) with 'cursive' as the fallback font if the google font fails to load correctly.<br>
I wanted a font that represented the brands name and 'Big Shoulders Display' does exactly that. It is bold and strong, especially using the 600 weight, these attributes makes it an appealling font for the user.

#### - Imagery:
In e-commerce, imagery is very important. Not just product images, but background images, brand banners and brand logos. And the quality of these images is equally as important.<br>
I used [Vistaprint](https://www.vistaprint.co.uk/) product design to upload, royalty free, vector images from [Vecteezy](https://www.vecteezy.com/) onto clothing templates to create my product images. I got the brand logo design from [Smashing Logo](https://smashinglogo.com/en/). I edited, modified all images using [Pixelmator](https://www.pixelmator.com/pro/).
<details>
  <summary>Background Hero Image</summary>
  
  ![](media/FLASH-BANNER.png)
</details>
<details>
  <summary>Mobile Background Hero Image</summary>
  
  ![](media/FLASH-SM-BANNER.png)
</details>
<details>
  <summary>Brand Logo</summary>
  
  ![](documentation/README/images/FLASH-BADGE-LOGO.jpg)
</details>
<details>
  <summary>Brand Banner</summary>
  
  ![](documentation/README/images/banner.png)
</details>
<details>
  <summary>Blog Post Placeholder Image</summary>
  
  ![](media/FLASH-BLOG-BANNER.png)
</details>

### Features 
#### Header & Navigation:
![](/documentation/README/images/nav-header.png)
The header contains:
- Brand logo and name
- Product search input so the shoppers can search for a specific product
- Account dropdown menu so Site Users can view profile, order history and wishlist. If user is superuser a product management option is available, where admin can add, edit or delete products. Also displays user's username.<br>
  - <details>
      <summary>Site User Account Dropdown</summary>
  
    ![](/documentation/README/images/account-drpdwn-user.png)
    </details>
   - <details>
      <summary>Super User Account Dropdown</summary>
  
     ![](/documentation/README/images/account-drpdwn-admin.png)
    </details>
 - User's shopping bag, where users/shoppers can view what they've added to their bag.
 
The navigation contains:
- All products link, takes the user to all products page.
- Categories dropwdown menu, gives the user the ability to filter products via their category.
  - <details>
      <summary>Categories Dropdown</summary>
  
     ![](/documentation/README/images/categories-drpdwn.png)
      </details>
- Sale link, takes users/shoppers to the stores discounted product.

#### The Homepage:
![](documentation/README/images/homepage.png)
The homepage contains:
- Background hero image.
- A short tagline summary of what the site offers.
- A shop now link, takes users/shoppers to all products page.

#### Register Account:
![](documentation/README/images/register-account.png)
Shoppers can register an account which will enable them access to further features such as profile details, order history and wishlist.
<details>
  <summary>Verify User's Email</summary>
  
  ![](documentation/README/images/registering-new-user.png)
</details>

#### Signing In:
![](documentation/README/images/account-sign-in.png)

#### Signing Out:
![](documentation/README/images/logout.png)

#### All Products:
![](documentation/README/images/all-products.png)
The all products page contains:
- All products page description.
- Products sort by and colour filter feature (as annotated). Sorts product by name (ascending, descending), users selected choice changes red when clicked. Filters products via product colour.
  - <details>
      <summary>Sort By Dropdown</summary>
  
    ![](documentation/README/images/sort-by.png)
    </details>
   - <details>
      <summary>Colour Dropdown</summary>
  
     ![](documentation/README/images/colour-filter.png)
     </details>
- Product count, total number of products available (as annotated).
- Back to top button, when user scrolls down page a 'BTT' button appears and when clicked take users back to top of page (as annotated).
- Wishlist button, for adding products to registered users wishlist, visible within the product card (see below).
- Edit product button, when signed in as Site Admin, super user, a edit product button is displayed within the product card.
   - <details>
      <summary>Product Card with Edit Button (for super user only) & Wishlist button</summary>
  
     ![](documentation/README/images/product-card.png)
     </details>

#### Product Detail:
![](documentation/README/images/product-detail.png)
The product detail page contains:
- product image (as annotated).
- Product name and category, which is also a link to the specified category page (as annotated).
- Product price (as annotated).
- Product colour (as annotated).
- Product description, a brief description of the product and it's features (as annotated).
- Size selector, where users/shoppers can select their desired size (as annotated).
- Add to Bag button, add product to users/shoppers shopping bag (as annotated).
  - <details>
      <summary>Add to bag alert</summary>
  
     ![](documentation/README/images/add-to-bag-alert.png)
     </details>
- Add to wishlist button, if users are registered they can add products to a wishlist (as annotated).
- Product reviews, can be viewed just underneath the product image.
- Review Product button, when users are signed in a 'Review Product' button is visible (see below).
  - <details>
      <summary>Review section</summary>
  
     ![](documentation/README/images/product-review.png)
     </details>
  - <details>
      <summary>Review section for registered users</summary>
  
     ![](documentation/README/images/product-review-signed-in.png)
     </details>
     
#### Add Product Review (For registered users):
![](documentation/README/images/add-review.png)
The add product review page contains:
- Name of product the users are reviewing.
- Review form, for users to add their comments and product rating.
- Add Review button, posts the users review to the reviewed product detail page.
- Cancel button, for when the users want to cancel the operation, returns back to homepage. 

#### Wishlist (For registered users):
![](documentation/README/images/wishlist.png)
The wishlist page contains:
- Product image, image of the wished product which is also a link to the product detail page.
- Product name.
- Product SKU.
- Product Price.
- Date added (d/m/y), the date the user added the wished item to their wishlist.
  - <details>
      <summary>Added to wishlist alert</summary>
  
     ![](documentation/README/images/added-to-wishlist-alert.png)
     </details>
- Remove button, removes the chosen wished item from users wishlist.
  - <details>
      <summary>Removed form wishlist alert</summary>
  
     ![](documentation/README/images/removed-from-wishlist.png)
     </details>
- Keep shopping link, positioned at the bottom of the wishlist page, takes users to all products page.

If users wishlist is empty.
![](documentation/README/images/empty-wishlist.png)

When non-registered users click on the 'add to wishlist' button, they are taken to the sign in page and are prompted by an alert to sign in or sign up.
![](documentation/README/images/not-authorised-wishlist.png)

#### Blog:
Blog page for users/shoppers:
![](documentation/README/images/blog-for-users.png)
The blog page for users/shoppers contains:
- Blog post featured image, also a link to the post detail page.
- Blog post title, also a link to the post detail page.
- Post created on date.

Blog page for super users:
![](documentation/README/images/blog-for-admin.png)
The blog page for super users additional features:
- Edit blog post button, allows admin to edit blog post (as annotated above).
- Add blog post button, allows admin to add new blog post (as annotated above).

#### Blog Post Detail:
![](documentation/README/images/blog-post-detail.png)
The blog post detail page contains:
- Blog post title.
- Blog post author, the admins username.
- Created on date, the date the post was created.
- Blog post featured image.
- Post content.

#### Add Blog Post (For super users only):
![](documentation/README/images/add-blog-post.png)
The add blog post page contains:
- Blog post form, for super users to populate with blog post details.
- Add blog post button, adds created blog post to blog page.
- Cancel button, cancels add blog post operation, returns user to blog page.

#### Edit Blog Post (For super users only):
![](documentation/README/images/edit-blog-post.png)
The edit blog post page contains:
- Pre-populated blog post form, form with current blog post details.
- Update blog post button, updates blog post details.
- Remove blog post button, removes chosen blog post.
- Cancel button, cancels the edit blog post operation, returns user back to blog page.

#### Users / Shoppers Shopping Bag:
![](documentation/README/images/bag-page.png)
The shopping bag page contains:
- Product info, includes product name, shoppers desired product size and sku.
- Product individual price.
- Product quantity, user can also update quantity from the shopping bag page using the minus and plus buttons.
- Order subtotal, the total price of one product.
- Remove from bag button, using [Font Awesome](https://fontawesome.com/) trash can icon, users can remove items from their bag when selected.
  - <details>
      <summary>Removed from shopping bag alert</summary>
  
     ![](documentation/README/images/removed-from-bag-alert.png)
     </details>
- Bag total, the total of the users/shoppers shopping bag, excluding delivery.
- Delivery info, delivery charge.
- Total, order grand total, including delivery.
- Secure checkout button, takes shoppers to the checkout page to continue with their purchase.
- Keep shopping link, takes users back to all products page.  

#### Checkout:
![](documentation/README/images/checkout-page.png)
The checkout page contains:
- Customer information form, includes shoppers details.
- Delivery details form, includes shoppers delivery information.
- A save info checkbox, users can save all details to make future checkout processes alot quicker.
- [Stripe](https://stripe.com/gb) payment input, for shoppers payment method.
- The shoppers bag, displayed to the right of the customer info form, includes the shoppers bag and it's contents details.
- Order subtotal and total, the amount the shopper will be charged.
- Complete payment button, completes the shoppers order process.

#### Successful Checkout:
![](documentation/README/images/successfull-checkout.png)
The successful checkout page contains:
- Thank you message from Flash Empire Apparel, assuring the shopper that their order has been received.
- Order no.
- Order date, the date of purchase.
- Order Details, includes delivery info and billing info.
- The shoppers purchases and product details.
- Keep shopping button, takes shoppers to all products page.
- Order successful alert (visible in the top right of the window), when the order has successfully been processed.

#### Add Product (For super users only):
![](documentation/README/images/add-new-product.png)
The add product page contains:
- Add product form, super users fill out this form with new product details.
- Select image button, allows admin users to upload new product image.
- Add product, adds the new product to the database and store.
- Cancel button, cancels the add new product operation, returns to homepage.

#### Edit Product (For super users only):
![](documentation/README/images/edit-product.png)
The edit product page contains:
- Pre-filled product form with current product details.
- Current product image, which can be removed via the remove checkbox.
- Select image button, allows admin users to upload new product image.
- Update product button, successfully updates products details.
- Remove product button, removes product from the store.
- Cancel button, cancels the edit product operation, returns back to homepage.
- Editing product info alert, when editing a product an alert is displayed in the top right corner telling the user what product they are editing.
  - <details>
      <summary>Editing product info alert</summary>
  
     ![](documentation/README/images/edit-product-alert.png)
     </details>
     
#### Footer:
![](documentation/README/images/footer.png)
The footer contains:
- Brand logo banner, which is also a homepage link.
- A brief company description.
- Shop links, links to individual product categories.
- Social section, links to Flash Empire's [Facebook](https://www.facebook.com/) and [Instagram](https://www.instagram.com/) pages.
- Community section, contains a link to the blog page.
- [Mail Chimp](https://mailchimp.com/en-gb/?currency=GBP) subscribe newsletter email input, allows users to subscribe to Flash Empire Apparel's newsletter.
  - <details>
      <summary>Subscription Email</summary>
  
     ![](documentation/README/images/newsletter.png)
     </details> 
- Copyright details.

#### Facebook Page:
[Flash Empire Apparel Facebook Page](https://www.facebook.com/people/Flash-Empire-Apparel/100090384290266/)
![](documentation/README/images/facebook.png)

#### Instagram Page:
[Flash Empire Apparel Instagram Pofile](https://www.instagram.com/flashempireapparel/)
![](documentation/README/images/instagram-profile.png)

#### My Profile Page (For registered users):
![](documentation/README/images/profile-page.png)
The my profile page contains:
- The user's saved delivery information.
- The user's order history, contains the order number, date of purchase, purchased items and order total.
- Update profile button, for when the user modifies their delivery information, when clicked will update their details.

## Testing
### HTML Validation
I used [W3C Markup Validation Service](https://validator.w3.org/) to test all HTML files.

| File | Result | Test Screenshot |
| ---- | ------ | ----------------|
| bag/templates/bag/bag.html | Pass | ![](documentation/html-validation/bag.png) |
| blog/templates/blog/blog.html | Pass | ![](documentation/html-validation/blog.png) |
| blog/templates/blog/blog-post-detail.html | Pass | ![](documentation/html-validation/blog-post-detail.png)|
| checkout/templates/checkout/checkout.html | Pass | ![](documentation/html-validation/checkout.png) |
| checkout/templates/checkout/checkout_success.html | Pass | ![](documentation/html-validation/successful-checkout.png) |
| home/templates/home/index.html | Pass | ![](documentation/html-validation/index.png) |
| templates/allauth/account/login.html | Pass | ![](documentation/html-validation/login.png) |
| templates/allauth/account/logout.html | Pass | ![](documentation/html-validation/logout.png) |
| templates/allauth/account/signup.html | Pass | ![](documentation/html-validation/register.png) |
| profiles/templates/profile/profile.html | Pass | ![](documentation/html-validation/profile.png) |
| products/templates/products/edit_product.html | Pass | ![](documentation/html-validation/edit-product.png) |
| products/templates/products/add_product.html | Pass | ![](documentation/html-validation/add-product.png) |
| products/templates/products/add_review.html | Pass | ![](documentation/html-validation/add-review.png) |
| products/templates/products/products.html | Pass | ![](documentation/html-validation/all-products.png) |
| products/templates/products/add_review.html | Pass | ![](documentation/html-validation/add-review.png) |
| wishlist/templates/wishlist/wishlist.html | Pass | ![](documentation/html-validation/wishlist.png) |

### CSS Validation
I used [W3C Markup Validation Service](https://validator.w3.org/) to test all CSS files via direct input.
| File | Result | Test Screenshot |
| ---- | ------ | --------------- |
| static/css/base.css | Pass<br>(8 Warnings) | ![](documentation/css-validation/base-css.png) |
| checkout/static/css/checkout.css | Pass<br>(1 Warning) | ![](documentation/css-validation/checkout-css.png) |
| profiles/static/css/profile.css | Pass | ![](documentation/css-validation/profiles-css.png) |

### JS Validation
I used [jshint](https://jshint.com/) to test all JS files via direct input.
| File | Result | Test Screenshot |
| ---- | ------ | --------------- |
| products/templates/products/products.html (Bottom of file) | No Errors | ![](documentation/js-validation/btt-btn-js.png) |
| profiles/static/js/countryfield.js | No Errors<br>(1 Warning) | ![](documentation/js-validation/countryfield-js.png) |
| products/templates/products/add_product.html (Bottom of file) | No Errors<br>(1 Warning) | ![](documentation/js-validation/new-img-file-js.png) |
| bag/templates/bag/includes/quantity-input-script.html | No Errors<br>(3 Warnings)| ![](documentation/js-validation/qty-input-js.png) |
| bag/templates/bag/bag.html (Bottom of file) | No Erros<br>(1 Warning) | ![](documentation/js-validation/update-qty-remove-js.png) |

### Python Validation
I used [Code Institute's Python Linter](https://pep8ci.herokuapp.com/) to lint my Python code.
| File | Result | Test Screenshot |
| ---- | ------ | --------------- |
| bag/apps.py | No Errors | ![](documentation/python-validation/bag-apps-py.png) |
| bag/templatetags/bag_tools.py | No Errors | ![](documentation/python-validation/bag-bagtools-py.png) |
| bag/contexts.py | No Errors | ![](documentation/python-validation/bag-contexts-py.png) | 
| bag/urls.py | No Errors | ![](documentation/python-validation/bag-urls-py.png) |
| bag/views.py | No Errors | ![](documentation/python-validation/bag-views-py.png) |
| blog/admin.py | No Errors | ![](documentation/python-validation/blog-admin-py.png) |
| blog/forms.py | No Errors | ![](documentation/python-validation/blog-forms-py.png) |
| blog/models.py | No Errors | ![](documentation/python-validation/blog-models-py.png) |
| blog/views.py | No Errors | ![](documentation/python-validation/blog-views-py.png) |
| checkout/forms.py | No Errors | ![](documentation/python-validation/checkout-forms-py.png) |
| checkout/models.py | 1 Error | ![](documentation/python-validation/checkout-models-py.png) |
| checkout/signals.py | No Errors | ![](documentation/python-validation/checkout-signals-py.png) |
| checkout/views.py | No Errors | ![](documentation/python-validation/checkout-views-py.png) |
| checkout/webhook_handler.py | 2 Errors | ![](documentation/python-validation/checkout-wh-handler-py.png) |
| checkout/webhooks.py | 1 Error | ![](documentation/python-validation/checkout-wh-py.png) |
| flash_empire_apparel/urls.py | No Errors | ![](documentation/python-validation/main-urls.png) |
| products/admin.py | No Errors | ![](documentation/python-validation/products-admin-py.png) |
| products/forms.py | No Errors | ![](documentation/python-validation/products-forms-py.png) |
| products/models.py | No Errors | ![](documentation/python-validation/products-models-py.png) |
| products/views.py | No Errors | ![](documentation/python-validation/products-views-py.png) |
| wishlist/models.py | No Errors | ![](documentation/python-validation/wishlist-models-py.png) |
| wishlist/views.py | No Errors | ![](documentation/python-validation/wishlist-views-py.png) |

### Lighthouse Reports
I used [Google Chrome DevTools Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/) was used to test performance, accessibility, best practises and SEO of selected pages.

#### Homepage Lighthouse Report:
   <details>
   <summary>Test Screenshot</summary>
  
   ![](documentation/README/images/homepage-lighthouse.png)
   </details>

#### All Products Lighthouse Report:
   <details>
   <summary>Test Screenshot</summary>
  
   ![](documentation/README/images/all-products-lighthouse.png)
   </details>

#### Product Detail Lighthouse Report:
   <details>
   <summary>Test Screenshot</summary>
  
   ![](documentation/README/images/product-detail-lighthouse.png)
   </details>
   
#### Add Product Lighthouse Report:
   <details>
   <summary>Test Screenshot</summary>
  
   ![](documentation/README/images/add-product-lighthouse.png)
   </details>
   
#### Edit Product Lighthouse Report:
   <details>
   <summary>Test Screenshot</summary>
  
   ![](documentation/README/images/edit-product-lighthouse.png)
   </details>

#### Blog Lighthouse Report:
   <details>
   <summary>Test Screenshot</summary>
  
   ![](documentation/README/images/blog-lighthouse.png)
   </details>
   
#### Blog Post Detail Lighthouse Report:
   <details>
   <summary>Test Screenshot</summary>
  
   ![](documentation/README/images/blog-detail-lighthouse.png)
   </details>

#### Bag Lighthouse Report:
   <details>
   <summary>Test Screenshot</summary>
  
   ![](documentation/README/images/bag-lighthouse.png)
   </details>
   
#### Profile Page Lighthouse Report:
   <details>
   <summary>Test Screenshot</summary>
  
   ![](documentation/README/images/profile-lighthouse.png)
   </details>
   
#### Wishlist Page Lighthouse Report:
   <details>
   <summary>Test Screenshot</summary>
  
   ![](documentation/README/images/wishlist-lighthouse.png)
   </details>
   
### Manual Testing:
Location | Element/Feature | Operation | Expected Result | Test Result |
| ------ | --------------- | --------- | --------------- | --------------- |
[Header](#header--navigation) | Brand Banner Home Link<br>![](documentation/README/images/brand-banner-home-link.png) | Click Element | Returns to homepage | Pass |
"" | Search Bar<br>![](documentation/README/images/search-bar.png) | Search for product | Displays desired search result, If nothing entered display error message | Pass |
"" | Account Dropdown Links<br>![](documentation/README/images/account-links.png) | Click Desired Element | Takes user to desired page links | Pass |
"" | Shopping Bag Link<br>![](documentation/README/images/shopping-bag-link.png) | Click Element | Takes user to their shopping bag page | Pass |
"" | All Products Nav Link<br>![](documentation/README/images/all-products-link.png) | Click Element | Takes user to all products page | Pass |
"" | Categories Nav Link<br>![](documentation/README/images/categories-link.png) | Click Element | Reveals dropdown of available product categories | Pass |
"" | Sale Nav Link<br>![](documentation/README/images/sale-link.png) | Click Element | Takes user to the sale page | Pass | 
[Home](#the-homepage) | Shop Now Btn<br>![](documentation/README/images/shop-now-btn.png) | Click Element | Takes user to all products page | Pass | 
[Footer](#footer) | Brand Banner Home Link<br>![](documentation/README/images/footer-brand-banner.png) | Click Element | Returns to homepage | Pass | 
"" | Shop Links<br>![](documentation/README/images/footer-shop-links.png) | Click Individual Elements | Takes user to desired product categories page | Pass | 
"" | Social Links<br>![](documentation/README/images/footer-social-links.png) | Click Individual Elements | Opens new tab to social pages | Pass |
"" | Blog Link<br>![](documentation/README/images/footer-blog-link.png) | Click Element | Takes user to blog page | Pass |
"" | Subscribe Element<br>![](documentation/README/images/footer-subscribe.png) | Enter email address, click subscribe btn | Adds user to subscription service, user receives [subscription email](#footer) | Pass |
[All Products](#all-products) | Sort By Dropdown<br>![](documentation/README/images/sort-by-dropdown.png) | Click Element, Select Choice | Sorts products in desired way | Pass | 
"" | Colour Filter Dropdown<br>![](documentation/README/images/colour-dropdown.png) | Click Element, Select Choice | Filters products via colour choice | Pass |
"" | Product Image Link<br>![](documentation/README/images/product-image-link.png) | Click Element | Takes user to product detail page | Pass |
"" | Category Link<br>![](documentation/README/images/category-link.png) | Click Element | Takes user to the product category page | Pass |
"" | Wishlist Btn<br>![](documentation/README/images/wishlist-btn.png) | Click Element | If signed in, add product to wishlist, if not registered display error take user to sign in page | Pass |
"" | Edit Product Btn (For Admin)<br>![](documentation/README/images/edit-product-btn.png) | Click Element | Takes super user to edit product page, displays info alert | Pass |
"" | Back To Top Btn<br>![](documentation/README/images/btt-btn-link.png) | Click Element | Returns user to top of page | Pass |
[Product Detail](#product-detail) | Category Link<br>![](documentation/README/images/category-link.png) | Click Element | Takes user to the product category page | Pass |
"" | Edit Product Btn (For Admin)<br>![](documentation/README/images/edit-product-btn.png) | Click Element | Takes super user to edit product page, displays info alert | Pass |
"" | Wishlist Btn<br>![](documentation/README/images/wishlist-btn.png) | Click Element | If signed in, add product to wishlist, if not registered display error take user to sign in page | Pass |
"" | Add To Bag Btn<br>![](documentation/README/images/add-to-bag-btn.png) | Click Element | Adds product to users/shoppers bag, displays shopping bag toast | Pass |
"" | Add Review Btn (For registered users)<br>![](documentation/README/images/add-review-btn.png) | Click Element | Takes user to add review form page | Pass |
"" | Keep Shopping Btn<br>![](documentation/README/images/keep-shopping-btn.png) | Click Element | Takes user to all products page | Pass |
[Add Product](#add-product-for-super-users-only) | Select Image Btn<br>![](documentation/README/images/select-img-btn.png) | Click Element | Allows super user to upload image file, if no image uploaded display product placeholder image | Pass |
"" | Add Product Btn<br>![](documentation/README/images/add-product-btn.png) | Click Element | Adds new product to store, displays successful alert, takes super user to new product detail page | Pass |
"" | Cancel Btn<br>![](documentation/README/images/cancel-btn.png) | Click Element | Cancels add product operation, returns super user back to homepage | Pass |
[Edit Product](#edit-product-for-super-users-only) | Remove Product Image<br>![](documentation/README/images/remove-img-box.png) | Click Element | Removes image when updated product | Pass |
"" | Update Product Btn<br>![](documentation/README/images/update-product-btn.png) | Click Element | Updated product detail, takes super user to product detail page, displays successfull update product alert | Pass |
"" | Remove Product Btn<br>![](documentation/README/images/remove-product-btn.png) | Click Element | Removes product from store, displays successfull remove product alert  | Pass |
[Blog](#blog) | Blog Post Links<br>![](documentation/README/images/blog-post-links.png) | Click blog post featured image or title element | Takes user to blog post detail page | Pass |
"" | Add Blog Post Btn (For Admin)<br>![](documentation/README/images/add-blog-post-btn.png) | Click Element | Takes super user to add blog post form page | Pass |
"" | Edit Blog Post Btn (For Admin)<br>![](documentation/README/images/edit-blog-post-btn.png) | Click Element | Takes super user to edit blog post form, displays info alert | Pass |
[Add Blog Post]() | Upload Feat. Image Btn<br>![](documentation/README/images/blog-ft-image-upload.png) | Click Element | Allows user to upload a featured image for blog post, if no image uploaded display placeholder featured image | Pass | 
"" | Add Blog Post Btn<br>![](documentation/README/images/blog-post-add-btn.png) | Click Element | Adds new blog post to blog page, displays successful alert | Pass |
"" | Cancel Btn<br>![](documentation/README/images/cancel-btn.png) | Click Element | Cancels add blog post operation, returns super user back to blog page | Pass |
[Edit Blog Post](#edit-blog-post-for-super-users-only) | Update Blog Post Btn<br>![](documentation/README/images/update-blog-post-btn.png) | Click Element | Updates blog post details, displays successfull blog post alert, returns super user back to blog post detail | Pass |
"" | Remove Blog Post Btn<br>![](documentation/README/images/remove-blog-post-btn.png) | Click Element | Removes blog post from blog, displays successfull remove blog post alert, returns super user to blog page | Pass | 
"" | Cancel Btn<br>![](documentation/README/images/cancel-btn.png) | Click Element | Cancels edit blog post operation, returns super user back to blog page | Pass |
[Wishlist](#wishlist-for-registered-users) | Wished Item Links<br>![](documentation/README/images/wished-item-links.png) | Click Element | Product img and name links takes user to product detail page | Pass |
"" | Remove From Wishlist Btn<br>![](documentation/README/images/remove-wished-item-btn.png) | Click Element | Removes wished item form users wishlist, displays successfull removed item from wishlist alert | Pass |
[Shopping Bag](#users--shoppers-shopping-bag) | Product Image<br>![](documentation/README/images/bag-product-img-link.png) | Click Element | Directs users to the product detail page | Pass |
"" | Item Quantity Btns<br>![](documentation/README/images/bag-qty-btns.png) | Click Element | Adjusts the quantity of items in users bag, displays shopping bag toast alerting updated item quantity | Pass |
"" | Remove From Bag Btn<br>![](documentation/README/images/remove-from-bag-btn.png) | Click Element | Removes desired item from bag, displays alert indicating removed product | Pass |
"" | Secure Checkout Btn<br>![](documentation/README/images/secure-checkout-btn.png) | Click Element | Directs user to checkout page | Pass |
"" | Keep Shopping Btn<br>![](documentation/README/images/keep-shopping-btn.png) | Click Element | Takes user to all products page | Pass |

### Device Testing:
Tested the application on several different devices, such as iPhone (11, SE), iPad air and Google nest hub (2nd gen).
No bugs or errors returned when testing on these devices. Only certain elements didn't respond that all well (see [Features for the Future](#features-for-the-future)).

### Browser Testing:
No bugs or errors occurred when testing on the following browsers:
- Google Chrome
- Firefox
- Safari

## Deployment
I developed this project on GitHub, using Git for version control. I then deployed to Heroku using the following steps:
- Log in to [Heroku](https://id.heroku.com/login) account.
- Click 'New' and create new app.
- I selected Europe as my region.
- Click 'Create App'.

I then created a database for my project for all project data to be stored:
- Log in to [ElephantSQL](https://customer.elephantsql.com/login) account.
- Select 'Create new instance'.
- Give database a name.
- Select plan (Tiny Turtle Free).
- Select region (europe-west2).
- Click 'Review'.
- Click 'Create Instance'.
- Redirected to ElephantSQL dashboard. 
- Select newly created database.
- Copy database URL link.
- Return to Heroku.
- Navigate to created app settings.
- Select 'Reveal config vars'.
- Add config var DATABASE_URL along with the value of the database URL from ElephantSQL.
- In Gitpod workspace console terminal, install dj-database_url and psycopg2 to connect to your database (pip3 install dj-database-url psycopg2).
- Freeze requirements.txt (pip3 freeze --local>requirements.txt).
- In project settings.py file, import dj_database_url.
- In the workspace terminal make migrations (python3 manage.py makemigrations).
- Then also in terminal, migrate changes (python3 manage.py migrate).
- In workspace terminal, create super user (python3 manage.py createsuperuser)
- Follow the steps to create super user (Name, email(optional), password x2)
- In the workspace terminal install gunicorn server (pip3 install gunicorn)
- Update requirements.txt file (pip3 freeze --local > requirements.txt).
- Create Procfile (touch Procfile).
- Go back to created app settings in Heroku.
- Add new config var DIASABLE_COLLECTSTATIC with a value of 1. 
- In Github workspace terminal, commit and push changes to Github.
- Back in Heroku created app, go to 'Deploy' and connect Github repository by searching for it and click connect.
- Selected 'Automatic Deploys', so whenever I push changes to Github it'll deploy in Heroku.
- Clicked deploy branch manually to deploy there and then.
- Once build is complete, click view to view deployed app.

## Features For The Future

- Add 'Delete Review' Button.
  - This feature would be for site users and superusers. If users want to remove their product review from the site, or if the superuser wants to remove them due to explicit content used by the site user.
- Product Image Carousel Feature.
  - This would be a good feature to have as you can add as many product images as you would like and allows the opportunity to show the users/shoppers more details of the product.
- Order Confirmation Email.
  - Already have the code for this but unfortunately does not work. This will give the shoppers/users assurance that their order has been processed.
- Better site responsiveness.
  - Although the site is responsive on many devices, there are certain elements that need to be modified manually in media queries, especially on XS/S screens.    

## Bugs & Errors:
- Adjust Product Quantity:
  - When editing shopping bag I noticed, when adjusting product quantity, you could only adjust the quantity of the  latest product added to the shopping bag. Think this maybe a Javascript glitch?
- Error in database:
  - I came upon errors involving the database and objects created but then didn't exist. This happened a couple of times and couldn't find any way around it other than to create a new database. I learned from the first time this happened and created a table of my [Site Data](documentation/PRO-5-DB-DATA.pdf) just in case it happened again, which it did. Having a copy of my site data made it that much quicker to import the data to the new database.
- Not receiving order confirmation email:
  - Whenever I tested the checkout order process I never received an order confirmation email. Think this might have something to do with my webhook in stripe as I followed the 'Boutique Ado' videos step by step for this feature but unfortunately I have had issues with it.
- Media files were not displaying when deployed to Heroku.
  - When deployed to Heroku static files were collected but not media files. I went back over the AWS videos in the 'Boutique Ado' walkthrough project to make sure I done everything correctly, which I did. I also looked at AWS' guide on how to link your bucket with projects but none of this helped the situation. Last resort was looking at YouTube videos on how to connect S3 bucket to Heroku projects. Whilst following one I noticed the 'Read' checkbox, for Everyone(Public Access) was not checked within the permission tab, under Access control list (ACL). Once I ticked this checkbox media files finally appeared on my deployed site.     

## Technologies Used:

### Languages Used:
- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/CSS)
- [Javascript](https://en.wikipedia.org/wiki/JavaScript)
- [Python](https://en.wikipedia.org/wiki/)


### Frameworks, Libraries and Programs Used:
- [Google Fonts](https://fonts.google.com/)
  - Google fonts was used to import the '' font.
- [FontAwesome](https://fontawesome.com/)
  - Fontawesome was used to add icons to several elements.
- [Git](https://git-scm.com/)
  - Git was used for version control and using the Gitpod terminal to commit and push to GitHub.
- [GitHub](https://github.com/)
  - GitHub is used to store the projects code after being pushed from Git.
- [Pixelmator](https://www.pixelmator.com/pro/)
  - I used Pixelmator to edit logo, homepage image and product images.
- [Bootstrap4](https://getbootstrap.com/docs/4.3/getting-started/introduction/)
  - Bootstrap framework is used for styling, structuring and reponsive development.
- [jQuery](https://en.wikipedia.org/wiki/JQuery)
  - jQuery is a fast, small, and feature-rich JavaScript library. It makes things like HTML document traversal and manipulation, event handling and       animation much simpler with an easy-to-use API that works across a multitude of browsers.
- [Django](https://www.djangoproject.com/)
  - Django framework was used to create the app/project.
- [Stripe](https://en.wikipedia.org/wiki/Stripe,_Inc.)
  - Stripe was used for the payment process integration.
- [Heroku](https://www.heroku.com/)
  - Heroku is used for creating my app.
- [AWS](https://aws.amazon.com/)
  - AWS is used for storing my static and media files.

## Credits:

### Code:
- The hover underline effect is from [30secondsofcode.org](https://www.30secondsofcode.org/css/s/hover-underline-animation/).
- The slanted div effect is from [html-css-js.com](https://html-css-js.com/css/generator/transform/).
- I generated my colour palette from [Coolors.co](https://coolors.co).
- I followed the [Code Institutes](https://codeinstitute.net/) walkthrough project 'Boutique Ado'. This project was a big help, especially with the stripe payment backend code.
- The colour filter code was from [Youtube](https://www.youtube.com/watch?v=exN6RdC_xbE).
- I occasionally referenced to [StackOverFlow](https://stackoverflow.com/) to overcome any issues.

### Media:
- The logo and branding are from [smashinglogo](https://smashinglogo.com/en/).
- The product graphic print designs are from [Vecteezy.com](https://www.vecteezy.com/).
- The clothing product images are from [VistaPrint](https://www.vistaprint.co.uk/) design template feature.
  - I used their upload design feature to add the my graphic print designs onto their apparel products, and print screened the resulting images.

## Acknowledgement & Support:
- My mentor Dario Carrasquel for supplying me with links for sitemaps, robots.txt, creating an ERD and using MailChimp. And for also giving advice on what to include for this README file.
