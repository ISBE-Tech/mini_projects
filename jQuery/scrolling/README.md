# jQuery (more stuff)

We've covered some basics of jQuery including binding functions to elements, changing style, etc.

If we look at a quick snippet to refresh:

```
$('#element').click(function(event) {
	console.log('You clicked' + this);
})
```

We're binding a function, the `function() { console... }` to the item with the ID `#element`, so that any time it's clicked it logs into the console.

The `this` refers to the item that was clicked. `this` as a variable is always going to be set as the element the function was called on.

### Animations

jQuery is used for animation a lot.

A good example is:

```
$( "#element" ).click(function(event) {
  $( "#element2" ).animate({
    opacity: .25
  }, 1000, function() {
    console.log('animation complete');
  });
});
```

This code is again binding a function to `#element`—this time, the function is an animation.

The animation is called with $('#element').animate(properties [,duration ][, easing ][, complete ])

`properties` is, for example, `opacity: .25`. It's what you're going to be changing during the animation.

`duration` is the length in milliseconds the animation should take.

`complete` is a function that's called when the animation is finished.

Check out `example1.html` to see this in action.

### Scrolling with .animate()

We can implement animated scrolling with a property called `scrollTop`.

`scrollTop` is the position on the page of the top of the scroll-bar in the browser. 

By changing scrollTop for the `html` selector we can essentially scroll through the webpage.

Usually when we click an `<a href="..."></a>` tag it immediately takes us to the element. Using Javascript alone, we can stop this, using `event.preventDefault()`.

```
$('#anchor').click(function(event) {
	event.preventDefault();
})
```

Let's break a website!

Go to reddit.com and open console and copy the line:

`$('a').click(function(event) {event.preventDefault()})`

into the developer console.

This doesn't work for a lot of newer websites that already have the default behavior disabled. Reddit's front end is primitive, though, so we can break it.

When we're scrolling to an element we'll be setting the scrollTop: property of the page to the y position of the target.

We can grab this using:

```
$('#targetElement').offset().top
```

This should be all we need to perform the animation.


### The actual challenge

Create a basic webpage using `template.html` that:

* Has a number of elements spaced throughout it for scrolling to (<div>s, whatever)
* Has <a> tags that link to the elements
* Prevents the default action on <a> clicks
* Performs a jQuery scroll animation to the target element

To perform a scroll using .animate() we need to identify the arguments of the function we'll need.

As we've said, we want to change the `scrollTop` property of the entire webpage—essentially, $('html').

Write a function that performs an animation that scrolls to 



