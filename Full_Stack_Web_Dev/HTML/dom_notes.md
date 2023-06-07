# Document Object Model (DOM)
Objects inside the DOM have:
* Properties: they describe the object
* Methods: this list the actions the object can do. A method is associated with an object.

We can add js to a html document using the following methods:
* Inline js
* Internal js
* External js
```html
<!-- inline js -->
<body onload = "alert('Hello World!')">

<!-- internal js -->
<script type="text/javascript">
    alert("Hello");
</script>

<!-- external js -->
<script src="index.js" charset="utf-8"> </script>
```

```js
// here the first element of the document would be the html tag, then a heading which we saved on a variable and modified using the innerHTML function
var heading = document.firstElementChild.firstElementChild;
// Inner html will give everything inside the specified tags
heading.innerHTML = "Good Bye";
// this only changes the text inside the html
heading.textContent = "Good Bye";

// manipulating attributes
element.attributes;
element.getAttribute("href");
element.setAttribute("attribute","new attribute value")

// this line searches for the input element and performs the built in click method
document.querySelector("input").click();

//
document.querySelector("button").classList.toggle("invisible");
```