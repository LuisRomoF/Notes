<h1> HTML </h1>
HTML stands for Hyper Text Markup Languange.
At the top there always should be a Doctype declaration. It tells the browser which version of html the file was written in.
<!DOCTYPE html>

```html
<!DOCTYPE html>
this defines the language for the file.
<html lang="en">
    <head> 
    here goes important information about the file that is not going to be displayed to the user.
        <meta charset="UTF-8">
        <title> this is the title of the webpage </title>
    </head>

    <body>
        <h1> This is a header </h1>
        <h2> This is a smaller header </h2>
        <p> This is the content of the paragraph. </p>
    </body>
</html>
```

Void elements are elements that do not <br />
have anything inside of them.
<hr />

```html
horizontal rule element
<hr />
break element 
<br />
```
List Element
```html
Unordered list
<ul>
    <li>list element number 1</li>
    <li>list element number 2</li>
</ul>

Ordered list
<ol>
    <li>list element number 1</li>
    <li>list element number 2</li>
</ol>

Nested list
<ul>
    <li>list element number 1</li>
    <ul>
        <li> nested list element </li>
    </ul>
    <li>list element number 2</li>
</ul>
```
Anchor element
```html
<a href = url second_attribute = n draggable=true> content of the tag </a>
```
<a href = https://www.w3schools.com/tags/ second_attribute = n draggable=true> This will take you to W3 tag elements </a>

Image tag
<br>
<img src=url alt="alternative text description of the photo"/>

Adding CSS
There are 3 different ways to add CSS to your HTML file.
* **Inline** : it uses the attributes of the html files to assign a style value. This is useful when you only want to format a single element.
* **Internal**: it uses a special html tag called the style element.This is useful when you only want to format a single webpage.
* **External**: this is a separate file .css file that links up. This is the most common style
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
