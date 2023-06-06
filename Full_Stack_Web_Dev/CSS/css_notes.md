# CSS

* CSS is the language we use to style a Web page.
* CSS stands for Cascading Style Sheets
* CSS describes how HTML elements are to be displayed on screen, paper, or in other media
* It can control the layout of multiple web pages all at once
* External stylesheets are stored in CSS files

Website to look for color combinations: colorhunt.co
<hr>

Adding CSS
There are 3 different ways to add CSS to your HTML file.
* **Inline** : it uses the attributes of the html files to assign a style value. This is useful when you only want to format a single element.
* **Internal**: it uses a special html tag called the style element.This is useful when you only want to format a single webpage.
* **External**: this is a separate file .css file that links up. This is the most common style

Cascade Hierarchy
1. First level of applying style comes from the external stylesheet
2. Then applies the internal style, so this would show over the external file

4 broad categories to determine the overall level of importance
 1. **Position:** the lower down the rule is located in the file, the more important it is.
 ```css
 li{
    color: red;
    color: blue; /*this is the one that would be apply since it comes last*/
 }
 ```
 2. **Specificity:** how specific a selector is in terms of applying the rule to
  ```css
 /*
 The following rules will all target but they have different specificity levels. They are ordered in specificity hierarchy where ID is the most specific.
 <li id="myId" class="myclass" draggable > */
 li{ color: blue;}
 .myclass {color:red;}
 li[draggable] {color:purple;}
 #myId {color:orange;}
 ```
 3. **Type**: this refers to the 3 different ways to add CSS to your html file
    1. External
    2. Internal
    3. Inline: since this is applied to an specific line element in the html, this is the most important

```html
Inline
<html style="background: blue">
</html>

Internal
<html>
    <head>
        <style>
            h1{
                color: red;
            }
        </style>
    </head>
</html>

External
<html>
    <head>
        <link
            rel = "stylesheet"
            href = "./styles.css"
        >
    </head>
</html>
```
 4. **Importance**: you can specify the importance of the rule. this ensure that the rule you specify is the most important rule for that element.
 ```css
 color:red;
 color:green !important;
 ```
<hr>

## CSS Selectors
* **Element selector:** it selects a particular html tag and applies the specified format to it
```css
In this example we format all the h1 headers in blue.
h1{
    color:blue
}
```
* **Class selector:** it applies the formatting to all the grouped elements in the specified class.
A class is an attribute we can add to any html element.
```css
<h2 class="name-of-the-class"> this is a header </h2>

In this example we format all the elements in the html code that are grouped in the specified class in blue.
.name-of-the-class{
    color:blue
}
```
* **ID selector:** it applies the formatting to all the grouped elements in the specified ID.
An ID should identify a unique element in a HTML file. 
```css
<h2 id = "name-of-the-id"> this is a header </h2>

In this example we format all the elements in the html code that are grouped in the specified class in blue.
#name-of-the-id{
    color:blue
}
```
* **Attribute selector:** it applies the formatting to all the grouped elements in the specified attributes.
```css
this applies the formatting to all the paragraph elements with the draggable attribute. 

p[draggable]{
    color:red
}
you can also specify the value of the attribute
p[draggable="false"]{
    color:red
}
```
* **Universal selector:** it applies the formatting to everything.
```css
this formats everything to red
*{
    color:red
}
```
## Font Properties
```css
h1{
    color: blue
    font-weight: bold
    font-size:20px
    font-family: sans-serif
    text-align: center
}
```
## Combining Selectors
```css
/*this would apply the style to all the h1 and h2 elements*/
h1,h2 {
    color: blue;
}
/*this would apply the style to the child paragraph inside the .box class*/
.box > p {
    color:blue;
}
/*Descendant selector */
.box li{
    color:blue;
}

/*Chaining Selectors: apply where all selector are true. It always starts with the element and the you add other selectors*/
li.myClass {
    color:blue;
}
```
## CSS Positioning
There are 4 different values for the positioning property.
1. **Static:** This is the default html positioning. 
2. **Relative:** Position relative to default position. The item is position relative to its default location.
3. **Absolute:** Position relative to nearest positioned ancestor or top left corner of webpage
4. **Fixed:** Position relative to top left corner of browser window

```css
.myclass {
    position:relative;
    top: 200px;
    left: 200px;
}
```
## CSS Display
The display property specifies the display behavior (the type of rendering box) of an element.

In HTML, the default display property value is taken from the HTML specifications or from the browser/user default style sheet. The default value in XML is inline, including SVG elements.
```css
h1 {display: none;}
h1 {display: inline;}
h1 {display: block;}
h1 {display: inline-block;}
```

## CSS Layout
* **Float**: The float property specifies how an element should float.
    - left - The element floats to the left of its container
    - right - The element floats to the right of its container
    - none - The element does not float (will be displayed just where it occurs in the text). This is default
    - inherit - The element inherits the float value of its parent
* **Clear**: The clear property specifies what elements can float beside the cleared element and on which side.
```css
img {
    float: left;
}
```
## Responsive Websites
1. Media Queries: this works as different rule sets depending on the window size and characteristics.
```css
@media (max-width: 600px) {
    /* CSS for screens below or equal to 600 px wide*/

@media (min-width: 600px) and (max-width: 900px){
    /* Styles for screens between 600px and 900px*/
}

}
```
2. CSS Grid
3. CSS Flexbox
4. External Frameworks